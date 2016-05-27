import time;

from myCompany.selectWhichKindOfGood import find_goods
from myCompany.findGoodsInTaobao import get_total_page,go_next_page,taobao_serach,goto_number_page


if(__name__=="__main__"):
    # login();
    # shopping();
    # img_href = '//detail.tmall.com/item.htm?spm=a230r.1.14.10.HTLM5y&id=520377909602&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=5';
    # xpath = '//*[@href="%s"]' % img_href;
    # print(xpath)

    print("begin")

    taobao_serach("男鞋")
        # print("asdjlkajs");
        # for i in range(4):
        #     print(driver.execute_script('return document.readyState'));
        #     time.sleep(0.5)

    # print(driver.execute_script('return document.readyState'));

    print("end");

    time.sleep(5)

    print(get_total_page())

    print(find_goods());
    for i in range(10):
        goto_number_page(i+2);
        print(str(i)+"   test")
        find_goods();

        time.sleep(2)
    # loginagain();
    # submitAndBuy();
    # bank();