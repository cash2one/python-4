
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time;
import lxml;


import  urllib.request;
driver = webdriver.Chrome();


for x in range(0,1):
    driver.get("https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fnekot%3DMTE5MzYxMDMyMnlhbmc%253D1447826354910");
    driver.maximize_window();
    # elem = driver.find_element_by_link_text("亲，请登录").click();
    driver.implicitly_wait(5)
    driver.find_element_by_id("TPL_username_1").send_keys("15957120592");
    driver.find_element_by_id("TPL_password_1").send_keys("yanli194612");
    kuang = driver.find_element_by_xpath('//*[@id="_scale_text"]');
    huakuai = driver.find_element_by_xpath('//*[@id="_n1z"]');
    div = driver.find_element_by_xpath('//*[@id="_bg"]');

    ActionChains(driver).click_and_hold(huakuai).move_by_offset(xoffset=210,yoffset=0).release(huakuai).perform();
    # js = "document.getElementById(\"_bg\").style.width = \"210px\"; document.getElementById(\"_n1z\").style.left = \"215px\""
    # driver.execute_script(js);

    driver.implicitly_wait(1);
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
    time.sleep(10);
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
    assert "No results found." not in driver.page_source;
    # driver.close();
    a = "https://item.taobao.com/item.htm?spm=a219r.lm895.14.17.kjFS3Y&id=522976276956&ns=1&abbucket=20&sku=1627207:1038916854#detail";
    driver.get(a);
    time.sleep(5);
    # print(driver.page_source);
    time.sleep(10);
    #颜色 与大小
    driver.find_element_by_xpath('//*[@id="J_isku"]/div/dl[1]/dd/ul/li[1]').click();
    driver.find_element_by_xpath('//*[@id="J_isku"]/div/dl[2]/dd/ul/li[1]').click();
    #数量
    driver.find_element_by_xpath('//*[@id="J_IptAmount"]').clear();
    driver.find_element_by_xpath('//*[@id="J_IptAmount"]').send_keys(Keys.NUMPAD1);

    #地址
    driver.find_element_by_xpath('//*[@id="J_WlAddressInfo"]').click();
    time.sleep(0.1);
    driver.find_element_by_xpath('//*[@id="J-AddressAllTitle-province"]').click();
    driver.find_element_by_xpath('//*[@id="J-AddressAllCon"]/ul/li[9]').click();

    driver.find_element_by_xpath('//*[@id="J-AddressAllCon"]/ul/li').click();

    driver.find_element_by_xpath('//*[@id="J-AddressAllCon"]/ul/li[3]').click();


    time.sleep(2);
    #加入购物车
    driver.find_element_by_xpath('//*[@id="J_juValid"]/div[2]/a').click();
    time.sleep(2);
    driver.find_element_by_xpath('//*[@id="J_ResultSummary"]/div[4]/a[2]').click();

    time.sleep(2);

    driver.find_element_by_xpath('//*[@id="J_SelectAll1"]').click();
    time.sleep(1);
    driver.find_element_by_xpath('//*[@id="J_Go"]').click();
    time.sleep(3);

    driver.find_element_by_xpath('//*[@id="J_Go"]').click();

    time.sleep(5);

    driver.find_element_by_xpath('//*[@id="J-rcChannels"]/div/div/a[1]').click();

    time.sleep(3);

    driver.find_element_by_xpath('//*[@id="J-rcChannels"]/div/div/a').click();

    time.sleep(5);

    driver.find_element_by_xpath('//*[@id="card-num"]').send_keys('6222600170013444988');

    time.sleep(3);

    driver.find_element_by_xpath('//*[@id="submitbtn"]').click();

    time.sleep(2);

    driver.find_element_by_xpath('//*[@id="mobileNo"]').send_keys('15957120592');

