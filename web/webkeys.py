# coding = utf8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time,os,traceback
from common.logger import logger

class WEB:
    """
    打开并操作浏览器的类
    """
    def __init__(self,w):
        self.driver = None
        self.writer = w

    def openbrower(self,b='chrome',d='chromedriver'):

        if b == 'chrome' or b=="":
            if d=="":
                d='chromedriver'
            op = Options()
            # 去除提示
            op.add_argument('--disable-infobars')
            try:
                userdir = os.environ['USERPROFILE'] + '\\AppData\\Local\\Google\\Chrome\\User Data'
            except Exception as e:
                userdir = 'C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data'
            # 添加用户文件
            op.add_argument('--user-data-dir=' + userdir)
            self.driver = webdriver.Chrome(executable_path=d, options=op)
            self.driver.implicitly_wait(30)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1)


    def geturl(self,url):
        try:
            self.driver.get(url)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(url))
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def click(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "点击成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))


    def input(self,xpath,text):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(text)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "输入成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def iniframe(self,xpath):
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(xpath))
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "进入iframe成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))



    def outiframe(self,xpath):
        try:
            self.driver.switch_to.default_content()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "退出iframe成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))


    def switchwindow(self,index):
        try:
            self.driver.switch_to.window(self.driver.window_handles[int(index)])
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "切换窗口成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))

    def moveto(self,xpath):
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.driver.find_element_by_xpath(xpath)).perform()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "移动滚动条成功")
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))



    def excutejs(self,js):
        """
        封装了默认执行js的方法
        :param js: 需要执行的标准js语句
        :return: 无
        """
        try:
            self.driver.execute_script(js)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "执行js成功")
            return  True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False


    def closebrower(self):
        self.driver.quit()
