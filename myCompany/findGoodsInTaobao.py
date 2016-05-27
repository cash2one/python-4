import time;
import  re
from myCompany.GlobalVar import  wait,driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from myCompany.UtilTaoBao import *

def taobao_serach(name):
    url = "https://www.taobao.com";
    with wait_for_page_load(driver):
        driver.get(url);

    xpath = '//*[@id="q"]';
    wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
    driver.find_element_by_xpath(xpath).send_keys(name);

    xpath = '//*[@id="J_TSearchForm"]/div[1]/button';
    wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
    with wait_for_page_load(driver):
        driver.find_element_by_xpath(xpath).click();


def get_current_pageNumber():
    return get_current_page_number(0)[0]

def goto_number_page(pagenumber):
    xpath = '//*[text()="下一页"]';
    wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
    element = driver.find_element_by_xpath(xpath);

    #查找输入框
    parent = get_element_parent(element);
    number = len(parent.find_elements_by_xpath('.//input'));
    while(number == 0):
        parent = get_element_parent(parent);
        number = len(parent.find_elements_by_xpath('.//input'));

    parent = parent.find_element_by_xpath('.//input')
    parent.clear();
    parent.send_keys(pagenumber)

    #查找确定按钮
    parent = get_element_parent(element);
    number = len(parent.find_elements_by_xpath(".//*[contains(text(),'确定')]"));
    while(number == 0):
        parent = get_element_parent(parent);
        number = len(parent.find_elements_by_xpath(".//*[contains(text(),'确定')]"));

    parent = parent.find_element_by_xpath(".//*[contains(text(),'确定')]");
    print("goto")
    with wait_for_ajax_load_taobao(driver):
        parent.click();





def get_element_parent(obj):
    xpath = '..'
    # wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
    parent = obj.find_element_by_xpath(xpath);
    return parent


def go_next_page():
    xpath = '//*[text()="下一页"]';
    wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
    next_page = driver.find_element_by_xpath(xpath);

    parent = next_page.find_element_by_xpath("..");
    # print("asdfasdf")
    print(parent.tag_name)
    # 如果可以点击的话 那么下一页的父节点是a标签
    if(parent.tag_name == 'a'):

        with  wait_for_ajax_load_taobao(driver):
            next_page.click();
        #刷单时间长了 淘宝在点击到下一页的时候会跳出登录框
        # time.sleep(2);
        # driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        # xpath = '//*[@id="TPL_username_1"]';
        # driver.find_element_by_xpath(xpath).send_keys("15957120592");
        #
        # xpath = '//*[@id="TPL_password_1"]';
        # driver.find_element_by_xpath(xpath).send_keys("yanli194612");
        # wait_for_ajax();


        return True;
    else:
        return False


def get_total_page():
    xpath = '//*[text()="下一页"]';
    wait.until(EC.visibility_of_element_located((By.XPATH,xpath)));
    next_page = driver.find_element_by_xpath(xpath);

    parent = next_page.find_element_by_xpath("..");
    number = len(parent.find_elements_by_xpath(".//*[contains(text(),'共')]"))
    while number == 0:
        parent = parent.find_element_by_xpath("..");
        number = len(parent.find_elements_by_xpath(".//*[contains(text(),'共')]"))
    total = parent.find_element_by_xpath(".//*[contains(text(),'共')]")
    text = total.text;
    res = re.findall(r"\d{1,}",text);
    print("total")
    print(res);
    return int(res[0]);

