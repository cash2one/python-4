from splinter.browser import Browser
b = Browser(driver_name="chrome")
b.visit("http://www.qq.com")
b.find_by_value(u"百度一下")