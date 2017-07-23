# coding:utf8
from selenium import webdriver
import pdb
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def query_cse(key):
    print key
    t0 = time.time()
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
        "(KHTML, like Gecko) Chrome/15.0.87"
    )
    dcap["phantomjs.page.settings.loadImages"] = False
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    # driver = webdriver.Chrome()

    # pdb.set_trace()

    driver.get("https://cse.google.com/cse/publicurl?cx=013188831728452306869:s3tgav2ld94")

    e1 = driver.find_element_by_xpath('//*[@id="gsc-i-id1"]')
    e1.send_keys(key)

    e2 = driver.find_element_by_xpath('//*[@id="___gcse_0"]/div/div/form/table[1]/tbody/tr/td[2]/input')
    e2.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="resInfo-0"]'))
    )

    fh = open('imgs/%s.png' % key, 'w')
    fh.write(driver.get_screenshot_as_png())
    fh.close()

    driver.quit()

    print time.time() - t0


def query_cse_page_tuning(driver, key):
    print key
    t0 = time.time()
    cur_page = 1

    while True:
        try:
            if cur_page == 1:
                driver.get("https://cse.google.com/cse/publicurl?cx=013188831728452306869:s3tgav2ld94")
                # wait
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="gsc-i-id1"]'))
                )
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="___gcse_0"]/div/div/form/table[1]/tbody/tr/td[2]/input'))
                )

                e1 = driver.find_element_by_xpath('//*[@id="gsc-i-id1"]')
                e1.send_keys(key)

                e2 = driver.find_element_by_xpath('//*[@id="___gcse_0"]/div/div/form/table[1]/tbody/tr/td[2]/input')
                e2.click()

                # wait
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="resInfo-0"]'))
                )
            else:
                # wait
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@class="gsc-cursor"]/div[%s]' % cur_page))
                )

                next_page = driver.find_element_by_xpath('//div[@class="gsc-cursor"]/div[%s]' % cur_page)
                next_page.click()

                # wait
                WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element(
                        (By.XPATH, '//div[@class="gsc-cursor-page gsc-cursor-current-page"]'), str(cur_page))
                )

            fh = open('imgs_new/%s_%i.png' % (key, cur_page), 'w')
            fh.write(driver.get_screenshot_as_png())
            fh.close()

            # 

            # 判断是否翻页
            page_nodes = driver.find_elements_by_xpath('//div[@class="gsc-cursor"]/div')
            if cur_page >= len(page_nodes):
                break

            cur_page += 1
        except Exception as e:
            print 'key:%s,page:%s,error:%s' % (key, cur_page, str(e))

    print time.time() - t0


def test_cse_page_tuning():
    fh = open('keywords', 'r')
    # pdb.set_trace()

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
        "(KHTML, like Gecko) Chrome/15.0.87")
    dcap["phantomjs.page.settings.loadImages"] = False

    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    # driver = webdriver.Chrome()
    driver.implicitly_wait(0.1)

    for line in fh.readlines():
        line = line.strip().decode('utf8')
        while True:
            try:
                query_cse_page_tuning(driver, line)
                driver.delete_all_cookies()
                break
            except Exception as e:
                print 'aaa:' + str(e)

    driver.quit()


def test_use_time():
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
        "(KHTML, like Gecko) Chrome/15.0.87")
    dcap["phantomjs.page.settings.loadImages"] = False

    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.set_page_load_timeout(20)
    # from selenium.webdriver.chrome.options import Options
    # chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.implicitly_wait(0.1)

    t0 = time.time()

    driver.get("https://www.baidu.com")
    # WebDriverWait(driver, 5).until(EC.title_contains(u'百度'))
    print len(driver.page_source)
    with open('html111.html', 'w') as f:
        f.write(driver.page_source.encode('utf8'))
    # driver.save_screenshot('screenshot111.png')
    print time.time() - t0

    sites = ['http://www.renren.com',
             'http://www.weibo.com',
             'http://www.jianshu.com',
             'http://www.aliyun.com',
             'http://www.qq.com',
             'http://www.126.com',
             'http://www.163.com',
             'http://www.hao123.com',
             'http://www.zhihu.com',
             'http://www.v2ex.com',
             ]
    # sites = ['https://www.zhihu.com']*10
    for i in xrange(len(sites)):
        t0 = time.time()
        driver.get(sites[i])
        # driver.get("https://www.zhihu.com")
        # WebDriverWait(driver, 3).until(EC.title_contains(u'知乎'))
        print len(driver.page_source)
        with open('html_%s.html' % i, 'w') as f:
            f.write(driver.page_source.encode('utf8'))
        # driver.save_screenshot('screenshot%s.png'%i)
        print time.time() - t0

    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    # test_cse()
    # test_cse_page_tuning()
    test_use_time()
