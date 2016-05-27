from myCompany.GlobalVar import  wait,driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
    driver.find_elements_by_xpath()