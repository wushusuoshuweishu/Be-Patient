import sys

from selenium.webdriver import Chrome
from pywinauto import Desktop
import time
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.action_chains import ActionChains
import os

web = Chrome()
options = web.create_options()
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
web = Chrome(chrome_options=options)
web.get("http://localhost:8080")
time.sleep(2)


def test_wrong_login():
    # 测试错误信息登录
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/section/form/div[2]/div/div/div/div/div/input').send_keys("123")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/section/form/div[3]/div/div/div/div/div/input').send_keys("123")
    time.sleep(2)
    web.find_element_by_xpath('/html/body/div/div/section/section/main/section/form/div[7]/button').click()
    time.sleep(2)


def test_right_login():
    # 测试正确信息登录
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/section/form/div[2]/div/div/div/div/div/input').clear()
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/section/form/div[2]/div/div/div/div/div/input').send_keys("test")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/section/form/div[3]/div/div/div/div/div/input').clear()
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/section/form/div[3]/div/div/div/div/div/input').send_keys("test")
    time.sleep(2)
    web.find_element_by_xpath('/html/body/div/div/section/section/main/section/form/div[7]/button').click()
    time.sleep(2)


def test_post_blog():
    # 测试发帖
    web.find_element_by_xpath('//*[@id="commitBlog"]').click()
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div/section/form/div[1]/div/div/input').send_keys(
        "test_title")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div/section/form/div[2]/div/div/input').send_keys(
        "test_summary")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div/section/form/div[3]/div/div/input').send_keys(
        "tag1 tag2")
    time.sleep(2)
    content = "What is it about?\nTyping and handwriting are two different forms of written production as they allow different sensorimotor programming and execution of gestures. In the present study, we aimed at understanding if and how the differences in typing and handwriting gestures allow for different processing of the linguistic properties of words during the motor execution of these gestures. Basically, we verified how the linguistic properties interact with different chronometric measures collected during typing and handwriting dictation tasks. We analyzed the latency in starting to write/type a dictated word, the time intervals between consecutive letters, and the time necessary to write/type the whole dictated word. Thanks to the analysis of these measures we were able to detect patterns of acceleration or deceleration during motor execution of the two written production modalities depending on the different linguistic proprieties of words (i.e., lexicality, orthographic complexity, and length)."
    web.find_element_by_xpath('//*[@id="cert"]').send_keys(content)
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div[1]/section/form/div[5]/div/button[1]').click()
    time.sleep(2)


def test_set_star():
    # 测试帖子加精
    web.find_element_by_xpath('/html/body/div[1]/div/section/section/main/div/main/div[1]/div').click()
    time.sleep(2)
    web.find_element_by_xpath('/html/body/div[1]/div/section/section/main/div/section/header/button[3]').click()
    time.sleep(2)


def test_post_comment():
    # 测试发表评论
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/footer/form/div[1]/div/div/input').send_keys("comment")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/footer/form/div[2]/div/button').click()
    time.sleep(2)


def test_delete_comment():
    # 测试删除评论
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/main/div[2]/div/div/div[2]/button').click()
    time.sleep(2)


def test_delete_blog():
    # 测试删除帖子
    web.find_element_by_xpath('/html/body/div/div/section/section/main/div/section/header/button[2]').click()
    time.sleep(2)
    web.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
    time.sleep(2)


def test_set_person_info():
    # 测试设置个人资料
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div/section/aside/div/div[1]/div[3]/div[6]/button[2]').click()
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div/section/main/form/div[2]/div/div/input').send_keys(
        "13637373737")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div/section/main/form/div[3]/div/div/input').send_keys("student")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div/section/main/form/div[4]/div/div/input').send_keys("America")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div/section/main/form/div[5]/div/div/input').send_keys(
        "One apple per day, doctor stays away.")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div[1]/div/section/section/main/div[1]/section/main/form/div[6]/div/div/div/div').click()

    some = Desktop()
    dialog = some['打开']
    dialog["Edit"].click()
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = file_path + r'\pics\avatar.png'
    print(file_path)

    time.sleep(2)
    send_keys(file_path)  # 在输入框中输入值
    time.sleep(1)
    send_keys("{VK_RETURN}")
    time.sleep(1)
    web.find_element_by_xpath(
        '//*[@id="commit_bt"]').click()
    time.sleep(2)


def test_upload_checklist():
    web.get("http://localhost:8080/HealthAid")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/aside/div/div[2]/div[2]/form/div[1]/div/div/input').send_keys(
        'test_name')
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/aside/div/div[2]/div[2]/form/div[2]/div/div/div/div').click()
    time.sleep(2)

    some = Desktop()
    dialog = some['打开']
    dialog["Edit"].click()
    file_path = os.path.dirname(os.path.abspath(__file__))
    file_path = file_path + r'\pics\avatar.png'
    print(file_path)

    time.sleep(2)
    send_keys(file_path)  # 在输入框中输入值
    time.sleep(1)
    send_keys("{VK_RETURN}")
    time.sleep(1)

    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/aside/div/div[2]/div[2]/form/div[3]/div/button').click()
    time.sleep(2)


def test_download_checklist():
    web.find_element_by_xpath('//*[@id="tab-first"]').click()
    time.sleep(2)
    web.find_element_by_xpath('//*[@id="dld"]').click()
    time.sleep(2)


def test_delete_checklist():
    web.find_element_by_xpath('//*[@id="btn"]').click()
    time.sleep(2)


def test_daily_health():
    web.get("http://localhost:8080/HealthAid")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/main/form/div[1]/div/div/input').send_keys(
        'test_title'
    )
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/main/form/div[2]/div/div/input').send_keys(
        'test_summary'
    )
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/main/form/div[3]/div/list/div[1]/div/div/input').send_keys(
        '100'
    )
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/main/form/div[3]/div/list/div[2]/div/div/input').send_keys(
        '10'
    )
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/main/form/div[3]/div/list/div[3]/div/div/input').send_keys(
        '100'
    )
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/main/form/div[3]/div/list/div[4]/div/div/input').send_keys(
        '100'
    )
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section/section/main/form/div[4]/div/div/textarea').send_keys(
        'I feel good these days. But my blood pressure is still abnormal sometimes.'
    )
    time.sleep(2)
    web.find_element_by_xpath(
        '//*[@id="mainContainer"]/div/section/section/main/form/div[5]/div/button').click()
    time.sleep(2)
    web.find_element_by_xpath(
        '//*[@id="person_info"]/div[1]/div[3]/div[6]/button[3]').click()
    time.sleep(2)


def test_search():
    web.get("http://localhost:8080/SearchInfo")
    time.sleep(2)
    web.find_element_by_xpath(
        '//*[@id="searchInput"]').send_keys("白血病")
    time.sleep(2)
    web.find_element_by_xpath(
        '/html/body/div/div/section/section/main/div/section[1]/button').click()
    time.sleep(2)


test_wrong_login()
test_right_login()
test_post_blog()
test_set_star()
test_post_comment()
test_delete_comment()
test_delete_blog()
test_set_person_info()
test_upload_checklist()
test_download_checklist()
test_delete_checklist()
test_daily_health()
test_search()
print("测试全部完成！")
