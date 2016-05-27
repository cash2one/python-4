import time;
import copy
import random
import selenium.webdriver.support.events
from odo.convert import element_of
from selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from myCompany.UtilTaoBao import wait_for_page_load,get_element_parent
from myCompany.GlobalVar import  wait,driver
from myCompany.UtilTaoBao import load_jquery
def shopping():
    a = "https://detail.tmall.com/item.htm?id=525813607120&ali_refid=a3_430583_1006:1106206643:N:%E7%94%B7%E9%9E%8B:33e707fb36022fa72e7b0664eb6e05fc&ali_trackid=1_33e707fb36022fa72e7b0664eb6e05fc&spm=a230r.1.14.3.ABiMHf&skuId=3130359888126";
    with wait_for_page_load(driver):
        driver.get(a);
    # driver.maximize_window();
    load_jquery(driver)
    # time.sleep(5);
    # print(driver.page_source);
    # time.sleep(10);
    #颜色 与大小

    _select_color()

    _select_size()
    # _BuyNow()

    # time.sleep(2);

"""
*立即购买
"""
def _BuyNow():
    #加入购物车
    xpath = '//*[contains(text(),"加入购物车")]'
    wait.until(EC.element_to_be_clickable((By.XPATH,xpath)));
    element = driver.find_element_by_xpath(xpath)

    xpath = './/*[contains(text(),"立即购买")]'
    parent = get_element_parent(element);
    number = len(parent.find_elements_by_xpath(xpath))

    #flag 是用来判断往上走了多少层  因为立即购买一定与 加入购物车 有一个相同祖先  这个相同祖先一定不远
    flag = 5;
    while number == 0 and flag>=0:
        parent = get_element_parent(parent);
        number = len(parent.find_elements_by_xpath('.//*[contains(text(),"立即购买")]'))
        flag -=1;

    if(flag>=0):
        (parent.find_element_by_xpath('.//*[contains(text(),"立即购买")]')).click();
    else:
        raise CanotFindElement("加入购物车找不到")


def _select_color():
    liList = _getAllLiList("颜色","li");
    length = len(liList)
    flagList = checkClickable(liList);
    print(flagList)
    s = '//*[@id="J_BrandAttr"]/a/span'
    e = driver.find_element_by_xpath(s);
    print(e.location)
    print("*********************")
    selectOneLi(liList,flagList)




def _select_address():
    pass

def _select_size():
    liList = _getAllLiList("尺码","li");
    length = len(liList)
    flagList = checkClickable(liList);
    print(flagList)
    selectOneLi(liList,flagList)

def _select_amount():
    pass


def getElementShoppingCart():
    xpath = '//*[contains(text(),"加入购物车")]'
    wait.until(EC.element_to_be_clickable((By.XPATH,xpath)));
    element = driver.find_element_by_xpath(xpath)
    return element;


def submitAndBuy():

    # 去购物车结算
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="J_ResultSummary"]/div[4]/a[2]')));
    driver.find_element_by_xpath('//*[@id="J_ResultSummary"]/div[4]/a[2]').click();

    # 选择所有物品
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_SelectAll1"]')));
    driver.find_element_by_xpath('//*[@id="J_SelectAll1"]').click();

    # 去结算
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_Go"]')));
    driver.find_element_by_xpath('//*[@id="J_Go"]').click();

    #提交订单
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_Go"]')));
    driver.find_element_by_xpath('//*[@id="J_Go"]').click();


    # 点击其他付款方式
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J-rcChannels"]/div/div/a[1]')));
    driver.find_element_by_xpath('//*[@id="J-rcChannels"]/div/div/a[1]').click();

    # 添加银行卡
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J-rcChannels"]/div/div/a')));
    driver.find_element_by_xpath('//*[@id="J-rcChannels"]/div/div/a').click();




def find_goods():
    img_id = 'J_Itemlist_TLink_525569772774'

    xpath = '//*[@id="%s"]' % img_id;
    # print(xpath)
    # wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
    try:
        goods = driver.find_element_by_xpath(xpath);
        return (True,goods);
    except NoSuchElementException as e:
        return  (False,None);


"""
name 是名字  比如颜色 尺码 等
"""
def _getAllLiList(name,tagname):
    shoppingElement = getElementShoppingCart();

    parent = get_element_parent(shoppingElement);
    number = len(parent.find_elements_by_xpath(".//*[contains(text(),'"+name+"')]"));

    while number == 0:
        parent = get_element_parent(parent);
        number = len(parent.find_elements_by_xpath(".//*[contains(text(),'"+name+"')]"));

    parent = parent.find_element_by_xpath(".//*[contains(text(),'"+name+"')]")
    # print(parent.tag_name)
    #从这出来 parent的tag_name 应该是dt
    number = len(parent.find_elements_by_tag_name(tagname));
    while(number == 0 ):
        parent = get_element_parent(parent);
        number = len(parent.find_elements_by_tag_name(tagname));

    # parent 底下现在包括了li项目
    li_list = parent.find_elements_by_tag_name(tagname);
    return li_list;

def selectOneLi(liList,clickAble):
    length = len(liList);

    # print(length)
    def checkHaiYou(listvar):
        for i in listvar:
            if i == 1:
                return True
        return False


    randomNumber = random.randint(0,length-1);
    if(checkHaiYou(clickAble)):
        while(clickAble[randomNumber] == 0 ):
            randomNumber = random.randint(0,length-1);
    else:
        return False


    # print("random")
    # print(randomNumber)
    classAttr = str(liList[randomNumber].get_attribute("class"));
    if(classAttr.find("tb-selected")!=-1):
        return True
    else:
        while(checkHaiYou(clickAble)):
            element = liList[randomNumber].find_element_by_tag_name("a");
            element.click();
            classAttr = str(liList[randomNumber].get_attribute("class"));
            if(classAttr.find("tb-selected")!=-1):
                return True
            else:
                clickAble[randomNumber] = 0;
                #再次产生随机数  因为如果大家都在抢 那么虽然我一开始就获得可以点击的列表 但是这个短暂的时间内 有可能被抢了 所以在点击
                #的时候需要再次验证能否点击
                randomNumber = random.randint(0,length-1);
                if(checkHaiYou(clickAble)):
                    while(clickAble[randomNumber] == 0 ):
                        randomNumber = random.randint(0,length-1);
                else:
                    return False

def add_funtion_in_js(functionStr):
    """
    functionStr 格式如下 匿名函数
    function(canshu1,canshu2){

    }
    """
    js = """
                function addEvent_chen(obj, evType, fn) {
                    if (obj.addEventListener) {
                        obj.addEventListener(evType, fn, false);
                        return true;
                    } else if (obj.attachEvent) {
                        var r = obj.attachEvent("on" + evType, fn);
                        return r;
                    } else {

                    }
                }
                addEvent_chen(arguments[0],'click',%s);


            """ % (functionStr)
    driver.execute_script(js)

def checkClickable(liList):
    length = len(liList);
    clickAble = [1]*length;
    for i in range(length):
        element = liList[i].find_element_by_tag_name("a");
        print(element.tag_name)
        print(element)
        if(element.is_displayed()):

            js = """
                function addEvent_chen(obj, evType, fn) {
                    if (obj.addEventListener) {
                        obj.addEventListener(evType, fn, false);
                        return true;
                    } else if (obj.attachEvent) {
                        var r = obj.attachEvent("on" + evType, fn);
                        return r;
                    } else {

                    }
                }
                addEvent_chen(arguments[0],'click',function(evt){
                    alert(evt.screenX +"   "+evt.clientX + evt.screenY +"   "+evt.clientY)
                });

            """
            # alert(evt.screenX +"   "+evt.clientX + evt.screenY +"   "+evt.clientY)
            driver.execute_script(js,element);
            element.click();
            # time.sleep(30)
            # element.click();
            # load_jquery(driver)
            #这边直接用jquery 不能点击 但是可以设置属性

            # js = "arguments[0].click(); arguments[0].dispatchEvent(evt);"
            js = "arguments[0].click();"
            # js = """
            #     var evt = evt = new MouseEvent('click',
            #         {
            #         canBubble:true, // canBubble
            #         cancelable:true, // cancelable
            #         screenX:%d, // screenX
            #         screenY:%d, // screenY
            #         clientX:%d, // clientX
            #         clientY:%d, // clientY
            #         ctrlKey:false, // ctrlKey
            #         altKey:false, // altKey
            #         shiftKey:false, // shiftKey
            #         metaKey:false, // metaKey
            #         button:0, // button
            #         relatedTarget:null //relatedTarget
            #         }
            #      );
            #     arguments[0].dispatchEvent(evt);
            #
            #     """ % (0,0,0,0)
            # driver.execute_script(js,element);

            classAttr = str(liList[i].get_attribute("class"));
            #代表没有找到 说明不能点击
            if(classAttr.find("tb-selected")==-1):
                clickAble[i] = 0;
        else:
            clickAble[i] = 0;

    return  copy.deepcopy(clickAble)

def get_page_position(element):
   js = """
            var getAbsPosition = function(el){
            el = arguments[0]
            var el2 = el;
            var curtop = 0;
            var curleft = 0;
            if (document.getElementById || document.all) {
                do  {
                    curleft += el.offsetLeft-el.scrollLeft;
                    curtop += el.offsetTop-el.scrollTop;
                    el = el.offsetParent;
                    el2 = el2.parentNode;
                    while (el2 != el) {
                        curleft -= el2.scrollLeft;
                        curtop -= el2.scrollTop;
                        el2 = el2.parentNode;
                        }
                } while (el.offsetParent);

            } else if (document.layers) {
                curtop += el.y;
                curleft += el.x;
            }
        return [curtop, curleft];
        };
        return getAbsPosition(arguments[0])
    """
   print(driver.execute_script(js,element))
   # 上面是用js 获得的 跟下面得到的是一样的
   # print(element.location)


class CanotFindElement(Exception):
    def __init__(self, msg):
         self.value = msg;
    def __str__(self):
        return repr(self.value)

if(__name__=="__main__"):
    shopping()


"""
def shopping():
    a = "https://item.taobao.com/item.htm?spm=2013.1.0.0.R0JRyA&scm=1007.10010.18905.100200300000001&id=522792946786&pvid=d876dc94-0bf4-41cd-bf39-cac2b19b41fa";
    driver.get(a);
    # time.sleep(5);
    # print(driver.page_source);
    # time.sleep(10);
    #颜色 与大小
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_isku"]/div/dl[1]/dd/ul/li[1]')));
    driver.find_element_by_xpath('//*[@id="J_isku"]/div/dl[1]/dd/ul/li[1]').click();
    print("颜色")
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_isku"]/div/dl[2]/dd/ul/li[1]')));
    driver.find_element_by_xpath('//*[@id="J_isku"]/div/dl[2]/dd/ul/li[1]').click();

    #数量
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_IptAmount"]')));
    driver.find_element_by_xpath('//*[@id="J_IptAmount"]').clear();
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_IptAmount"]')));
    driver.find_element_by_xpath('//*[@id="J_IptAmount"]').send_keys(Keys.NUMPAD1);
    print("数量")
    #地址
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_WlAddressInfo"]')));
    driver.find_element_by_xpath('//*[@id="J_WlAddressInfo"]').click();
    time.sleep(0.1);
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J-AddressAllTitle-province"]')));
    driver.find_element_by_xpath('//*[@id="J-AddressAllTitle-province"]').click();
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J-AddressAllCon"]/ul/li[9]')));
    driver.find_element_by_xpath('//*[@id="J-AddressAllCon"]/ul/li[9]').click();
    print("数量'")

    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J-AddressAllCon"]/ul/li')));
    driver.find_element_by_xpath('//*[@id="J-AddressAllCon"]/ul/li').click();

    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J-AddressAllCon"]/ul/li[3]')));
    driver.find_element_by_xpath('//*[@id="J-AddressAllCon"]/ul/li[3]').click();


    # time.sleep(2);
    #加入购物车
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_juValid"]/div[2]/a')));
    driver.find_element_by_xpath('//*[@id="J_juValid"]/div[2]/a').click();

"""
