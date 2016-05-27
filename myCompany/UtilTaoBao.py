import time;

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from myCompany.GlobalVar import  wait,driver


def get_element_parent(obj):
    xpath = '..'
    # wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
    parent = obj.find_element_by_xpath(xpath);
    return parent

def get_current_page_number(digui_number):
    try:
        xpath = '//*[text()="下一页"]';
        wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
        next_page = driver.find_element_by_xpath(xpath);

        parent = get_element_parent(next_page);

        while parent.tag_name!='li':
            parent = get_element_parent(parent);

        parent = get_element_parent(parent);
        # print(parent.tag_name);
        xpath = './/*[contains(@class,"active")]/span';
        current_number = parent.find_element_by_xpath(xpath).text;
        # print("current_number");
        # print(current_number);
        return (current_number,digui_number);
    except StaleElementReferenceException as e:
        print("again");
        return get_current_page_number(digui_number+1);

def wait_for(condition_function,time_jiange,zong_shijian):
    start_time = time.time()
    while time.time() < start_time + zong_shijian:
        if condition_function():
            return True
        else:
            time.sleep(time_jiange)
    raise Exception(
        'Timeout waiting for {0}'.format(condition_function.__name__)
    )

# 只能等待 标签会转圈的url  如果点击后标签不会转圈 那么就相当于ajax一样  会抛出异常 也就是说html节点 没有重新创建 只是重新加载了数据
class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        print("__enter__")
        self.old_page = self.browser.find_element_by_xpath('//html')

        print("out __enter__")
        return self

    def page_has_loaded(self):

        print("page_has_loaded");

        # print(len(driver.find_elements_by_xpath('//html')))
        new_page = self.browser.find_element_by_xpath('//html')
        # print(self.old_page.id);
        # print(new_page.id)
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        time.sleep(0.5);
        print("in __exit__");
        # WebDriverWait(self.browser, 20).until(staleness_of(self.old_page))
        wait_for(self.page_has_loaded,0.5,30)

        #这个只有page 加载的时候才能用
        s = "return document.readyState";
        wait_for(lambda :driver.execute_script(s)=="complete",0.2,60);
        print("__exit__");

def wait_wrong_taobao():
    xpath = '//*[@id="srp-error"]'
    element = driver.find_element_by_xpath(xpath)
    s = element.value_of_css_property("display");
    print(s)
    return s == "none";


"""
    *这个等待ajax加载完有限制  只能用于淘宝上的
"""


# = 0 代表正常 =1 代表出错了
global_ajax_flag_taobao = 0;
class wait_for_ajax_load_taobao(object):

    def __init__(self, browser):
        self.flag = 0;
        global global_ajax_flag_taobao;
        self.browser = browser
        global_ajax_flag_taobao = 0;

    def __enter__(self):
        #self.page_number = get_current_page_number(0)[0]
        return self

    def ajax_has_loaded(self):
        global global_ajax_flag_taobao;
        xpath = '//html'
        print("begin")
        element = driver.find_element_by_xpath(xpath)
        s = str(element.get_attribute("class"));
        # print(s)

        #如果有这个 代表还没有加载结束 否则代表加载结束  看看有没有出错
        if( s.find("nprogress-busy") != -1 ):
            print("正在加载")

            self.flag = 1;
            return False
        elif(self.flag == 1):
            xpath = '//*[@id="srp-error"]'
            element = driver.find_element_by_xpath(xpath)
            child_number = len(element.find_elements_by_xpath(".//*[contains(text(),'请刷新或重新点击尝试')]"))
            s = element.value_of_css_property("display");
            print(s);
            print(child_number);
            #if里面是出现错误的条件
            if child_number!=0 and s == 'block':
                #等待错误消失  因为出现错误到消失还要一点时间 他是一个动画
                wait_for(wait_wrong_taobao,0.2,30)
                #代表点击出错了 没有到下一页  而是出现 请刷新或重新点击尝试
                global_ajax_flag_taobao = 1;

            #进入else 代表一定加载结束了
            return True
        else:
            return False;
    def __exit__(self, *_):

        # WebDriverWait(self.browser, 20).until(staleness_of(self.old_page))
        wait_for(self.ajax_has_loaded,0.3,30)



def load_jquery(mydriver):
     # 加载juery.js
    flag = mydriver.execute_script("return typeof jQuery =='undefined'");
    # print(flag)

    if (flag):
        with open('E:\jquery\jquery-1.11.3.min.js') as f:
            s = f.read()
        # s = "var jq =document.createElement('script');"+ " jq.type ='text/javascript'; "\
        #                     + r" jq.src ='https://lib.sinaapp.com/js/jquery/1.9.1/jquery-1.9.1.min.js';"\
        #                     +" document.getElementsByTagName('head')[0].appendChild(jq);"
        # print(s)
        mydriver.execute_script(s);
        wait_for(lambda : mydriver.execute_script("return typeof jQuery !='undefined'"),0.5,30);
        f.close();

    flag = mydriver.execute_script("return typeof jQuery =='undefined'");
    print(flag)

def test_jquery():
    js = '$("body").css("background","red");'
    driver.execute_script(js);
"""
# 老版本
class wait_for_ajax_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('script')

    def page_has_loaded(self):

        new_page = self.browser.find_element_by_tag_name('script')
        # print(self.old_page.id);
        # print(new_page.id);
        if(new_page.id != self.old_page.id):
            self.old_page = new_page;

            print(new_page.get_attribute("src"))
            return False
        # print("%%%%%%%%%%%%")
        # print(self.browser.find_element_by_tag_name('html').id)
        # print(new_page.id)
        return True

    def __exit__(self, *_):

        # WebDriverWait(self.browser, 20).until(staleness_of(self.old_page))
        __wait_for(self.page_has_loaded,0.5)
"""
"""
def load_jquery(mydriver):
     # 加载juery.js  这个加载用于淘宝有事加载失败  所以抛弃
    flag =mydriver.execute_script("return typeof jQuery =='undefined'");
    # print(flag)

    if (flag):
        s = "var jq =document.createElement('script');"+ " jq.type ='text/javascript'; "\
                            + r" jq.src ='https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js';"\
                            +" document.getElementsByTagName('head')[0].appendChild(jq);"
        mydriver.execute_script(s);

        time.sleep(3);

    flag =mydriver.execute_script("return typeof jQuery =='undefined'");
    print(flag)

    page_state = mydriver.execute_script('return $.active == 0');
    print(page_state)
"""
# def wait_for_ajax():
#     def neibu():
#         page_state = driver.execute_script('return document.readyState');
#         print(page_state)
#         return page_state == 'complete'
#     # wait.until(EC.presence_of_all_elements_located(By.ID));
#     __wait_for(neibu)
#     # pass;

"""
# = 0 代表正常 =1 代表出错了
global_ajax_flag_taobao = 0;
class wait_for_ajax_load_taobao(object):

    def __init__(self, browser):
        global global_ajax_flag_taobao;
        self.browser = browser
        global_ajax_flag_taobao = 0;

    def __enter__(self):
        self.page_number = get_current_page_number(0)[0]
        return self

    def page_has_loaded(self):
        global global_ajax_flag_taobao;
        (new_page_number,digui_number )= get_current_page_number(0)
        print("&&&&&&&&&&&&")
        # if len(driver.find_elements_by_xpath('//*[not(contains(@style,"none") and @id="srp-error"]'))==1:
        #     print(driver.find_elements_by_xpath('//*[not(contains(@style,"none") and @id="srp-error"]')[0].text)
        #     print(driver.find_elements_by_xpath('//*[not(contains(@style,"none") and @id="srp-error"]')[0].tag_name)
        print(self.page_number);
        print(new_page_number);
        print("%%%%%%%%%%%%%%")
        if( new_page_number == self.page_number):
            # 这个xpath是  出错啦，请刷新或重新点击尝试！的id
            xpath = '//*[@id="srp-error"]'
            element = driver.find_element_by_xpath(xpath)
            child_number = len(element.find_elements_by_xpath(".//*[contains(text(),'请刷新或重新点击尝试')]"))
            s = element.value_of_css_property("display");
            print(s);
            print(child_number);

            #if里面是出现错误的条件
            if child_number!=0 and s == 'block':
                #等待错误消失  因为出现错误到消失还要一点时间 他是一个动画
                wait_for(wait_wrong_taobao,0.2,30)
                #代表点击出错了 没有到下一页  而是出现 请刷新或重新点击尝试
                global_ajax_flag_taobao = 1;
                return True;
            else:
                return False;

        # print("%%%%%%%%%%%%")
        # print(self.browser.find_element_by_tag_name('html').id)
        # print(new_page.id)
        return True

    def __exit__(self, *_):

        # WebDriverWait(self.browser, 20).until(staleness_of(self.old_page))
        wait_for(self.page_has_loaded,0.3,30)
"""

