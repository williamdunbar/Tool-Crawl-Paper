from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai bao bien browser
browser  = webdriver.Chrome(executable_path="D:/11.My-job/2022_10_06 Uploadfile/chromedriver.exe")

# 2. Mở thử một trang web
browser.get("http://eprints.lqdtu.edu.vn/cgi/users/login?target=http%3A%2F%2Feprints.lqdtu.edu.vn%2Fcgi%2Fusers%2Fhome")

# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element_by_id("login_username")
txtUser.send_keys("editor") # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element_by_id("login_password")
txtPass.send_keys("editor")

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)


# 3. Dừng chương trình 5 giây
sleep(10)

# 4. Đóng trình duyệt
browser.close()