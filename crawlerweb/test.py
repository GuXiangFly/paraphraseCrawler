from selenium import webdriver

class DriverFanyi:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.quit()

if __name__ == '__main__':
     driver = DriverFanyi()
