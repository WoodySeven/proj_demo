import unittest
import time
from selenium import webdriver


class Bugfree管理员登录退出(unittest.TestCase):
    """
    演示的是bugfree的登录和退出
    数据驱动，相同的逻辑使用不同的数据去运行。
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver

    def tearDown(self):
        pass

    def test_admin_login_success(self):
        """admin的登录正确用例"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)

    def test_admin_login_fail_with_invalid_username(self):
        """admin的登录失败，使用无效的用户名"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("invalid")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
