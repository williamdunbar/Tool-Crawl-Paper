from logging import exception
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from string import ascii_lowercase, ascii_uppercase

try:
    browser = webdriver.Chrome(executable_path="D:/11.My-job/2022_10_06 Uploadfile/chromedriver.exe")


    browser.get("http://eprints.lqdtu.edu.vn/cgi/users/login?target=http%3A%2F%2Feprints.lqdtu.edu.vn%2Fcgi%2Fusers%2Fhome")

    txtUser = browser.find_element_by_id("login_username")
    txtUser.send_keys("editor") # <---  Điền username thật của các bạn vào đây

    txtPass = browser.find_element_by_id("login_password")
    txtPass.send_keys("editor")

    txtPass.send_keys(Keys.ENTER)

    time = [2014, 2015, 2016 ]
    with open('paper_title.txt', 'w') as f:
        for i in time:
            url = str("http://eprints.lqdtu.edu.vn/view/year/scopus/"+str(i)+".html")
            f.write(str(i)+'\n')
            browser.get(url)
            article_titles = browser.find_elements_by_xpath("//em")
            for article_title in article_titles:
                f.write(article_title.text+'\n')

    browser.close()

except(exception):
# sleep(5)
# 6. Đóng browser
    print(exception)
    browser.close()
