import time;

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from myCompany.downloadImg import  downjpg

driver  = webdriver.Chrome();
wait = WebDriverWait(driver,30);

def login():
    driver.get("https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fnekot%3DMTE5MzYxMDMyMnlhbmc%253D1447826354910");
    driver.maximize_window();
    # elem = driver.find_element_by_link_text("亲，请登录").click();
    # driver.implicitly_wait(5)
    wait.until(lambda driver:driver.find_element_by_id("TPL_username_1"));
    driver.find_element_by_id("TPL_username_1").send_keys("15957120592");
    wait.until(lambda driver:driver.find_element_by_id("TPL_password_1"));
    driver.find_element_by_id("TPL_password_1").send_keys("yanli194612");


    wait.until(lambda driver:driver.find_element_by_xpath('//*[@id="_scale_text"]'));
    kuang = driver.find_element_by_xpath('//*[@id="_scale_text"]');

    wait.until(lambda driver:driver.find_element_by_xpath('//*[@id="_n1z"]'));
    huakuai = driver.find_element_by_xpath('//*[@id="_n1z"]');

    wait.until(lambda driver:driver.find_element_by_xpath('//*[@id="_bg"]'));
    div = driver.find_element_by_xpath('//*[@id="_bg"]');

    ActionChains(driver).click_and_hold(huakuai).move_by_offset(xoffset=210,yoffset=0).release(huakuai).perform();
    # js = "document.getElementById(\"_bg\").style.width = \"210px\"; document.getElementById(\"_n1z\").style.left = \"215px\""
    # driver.execute_script(js);

    # driver.implicitly_wait(1);
    # img = driver.find_element_by_xpath('//*[@id="clickCaptcha"]/div[2]/img');
    # urllib.request.urlretrieve(img.get_attribute('src'), "d:\captcha.png")

    # print(img.get_attribute('src'));
    #下载图片
    # driver.get_screenshot_as_file("d:\ceshishiyong.jpg");

    # ActionChains(driver).drag_and_drop(kuang,huakuai);
    # driver.find_element_by_id("J_SubmitStatic").click();
    # print(elem.text);
    # print(elem.is_displayed());
    # elem.click();
    # time.sleep(10);
    # driver.get("http://www.baidu.com");
    # driver.maximize_window();
    # elem = driver.find_element_by_link_text("登录").click();
    # driver.implicitly_wait(30)
    # driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("1193610322@qq.com");
    # driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("chenyang");
    # driver.find_element_by_id("TANGRAM__PSP_8__submit").click();
    # print(elem.text);
    # print(elem.is_displayed());
    # # elem.click();
    # time.sleep(100);
    # assert "No results found." not in driver.page_source;
    # driver.close();
    print("滑动结束");


def shopping():
    a = "https://www.taobao.com/";
    driver.get(a);
    # time.sleep(5);
    # print(driver.page_source);
    # time.sleep(10);
    #颜色 与大小
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="J_Screen"]/div[2]/div[1]/div/dl/div/dd/div[1]/a[2]')));
    man = driver.find_element_by_xpath('//*[@id="J_Screen"]/div[2]/div[1]/div/dl/div/dd/div[1]/a[2]');

    ActionChains(driver).move_to_element(man).perform();


def loginagain():
    # 这个地方有可能会出现登录框  需要处理

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'mnl-ifr')));
    frame=driver.find_element_by_class_name(("mnl-ifr"));
    # frameInner = frame.find_element_by_tag_name("iframe");
    name = frame.get_attribute('id');
    print(name);
    driver.switch_to.frame(name)
    driver.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys("15957120592");
    driver.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys("yanli194612");
    # print(driver.find_element_by_xpath('//*[@id="nocaptcha"]'))

    # 等待滑块出现
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nocaptcha"]')));
    driver.find_element_by_xpath('//*[@id="nocaptcha"]');
    huakuai1 = driver.find_element_by_xpath('//*[@id="_n1z"]');
    ActionChains(driver).click_and_hold(huakuai1).move_by_offset(xoffset=210,yoffset=0).release(huakuai1).perform();

    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="clickCaptcha"]/div[2]/img')));
    img = driver.find_element_by_xpath('//*[@id="clickCaptcha"]/div[2]/img');
    wenzi = driver.find_element_by_xpath('//*[@id="clickCaptcha"]/div[4]/p');

    #wenzi.text是要点击的内容
    print(wenzi.text);

    url = img.get_attribute("src");
    print(url);
    downjpg(url);

    """
    ***这个代表在图片的那个位置点击
    """
    # 这个用于测试  点击login的关闭按钮 有效  测试过了
    # ActionChains(driver).move_to_element_with_offset(img1,263,-106).click().perform();
    print("切换过")

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


def bank():
    # time.sleep(5);
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div[2]/div[2]/iframe')));
    frame=driver.find_element_by_xpath(("/html/body/div[6]/div[2]/div[2]/iframe"));
    name = frame.get_attribute('name');
    print(name);

    driver.switch_to.frame(name)
    print("切换过")
    #银行卡交钱
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="card-num"]')));
    driver.find_element_by_xpath('//*[@id="card-num"]').send_keys('6222600170013444988');

    # 点击下一步
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submit"]')));
    driver.find_element_by_xpath('//*[@id="submit"]').click();

    # 选择快捷支付
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="DEBIT_EXPRESS-comm907"]')));
    driver.find_element_by_xpath('//*[@id="DEBIT_EXPRESS-comm907"]').click();

    # 点击下一步
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submitbtn"]')));
    driver.find_element_by_xpath('//*[@id="submitbtn"]').click();


    #输入手机号码
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mobileNo"]')));
    driver.find_element_by_xpath('//*[@id="mobileNo"]').send_keys('15957120592');

    # 点击获取验证码
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sms-validate-first"]')));
    driver.find_element_by_xpath('//*[@id="sms-validate-first"]').click();

if(__name__=="__main__"):
    # login();
    shopping();
    # loginagain();
    # submitAndBuy();
    # bank();