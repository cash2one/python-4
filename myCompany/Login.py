from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from myCompany.GlobalVar import  wait,driver
from myCompany.downloadImg import  downjpg


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

    # 得到父节点 很重要
    print("huakuai parent")
    parent = huakuai.find_element_by_xpath("..");
    # print(parent.tag_name);
    # print(parent.get_attribute("id"));

    width = parent.value_of_css_property("width");
    width = str(width)[0:str(width).find("px")];
    print(width)

    # print(driver.current_url)
    # driver.title 返回的是html中title 使用查看网页源代码就可以看得到
    # print(driver.title)

    # 获得parent 下的所有节点  必须使用".//*" 而不是//*
    # elems = parent.find_elements_by_xpath('.//*')
    # for i in elems:
    #     print(i.get_attribute("id"))

    #
    # parent = parent.find_element_by_xpath("..");
    # print(parent.tag_name);
    # print(parent.get_attribute("id"));

    # wait.until(lambda driver:driver.find_element_by_xpath('//*[@id="_bg"]'));
    # div = driver.find_element_by_xpath('//*[@id="_bg"]');

    ActionChains(driver).click_and_hold(huakuai).move_by_offset(xoffset=width,yoffset=0).release(huakuai).perform();
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

     # 得到父节点 很重要
    print("huakuai parent")
    parent = huakuai1.find_element_by_xpath("..");
    # print(parent.tag_name);
    # print(parent.get_attribute("id"));

    # 得到宽度
    width = parent.value_of_css_property("width");
    # 上面会得到298px  下面就是去掉px这个字母
    width = str(width)[0:str(width).find("px")];
    print(width)

    ActionChains(driver).click_and_hold(huakuai1).move_by_offset(xoffset=width,yoffset=0).release(huakuai1).perform();

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

if __name__ == "__main__":
    login();