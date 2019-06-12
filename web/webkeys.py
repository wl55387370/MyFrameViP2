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
        # 保存参数
        self.params = {}

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
            self.writer.write(self.writer.row, self.writer.clo + 1,"打开浏览器成功")


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

    def uploadfile(self, xpath, filepath):
        """
        根据xpath，找到元素
        使用send_keys上传文件
        :param xpath: 元素的xpath
        :param filepath: 需要上传文件的全路径
        :return: 无
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            # 定位失败，则直接返回
            return False
        try:
            ele.send_keys(filepath)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, "上传成功")
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

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

    def hover(self, xpath):
        """
        根据xpath，找到元素，并将鼠标悬停到元素
        该关键字自动化过程中，如果认为移动了鼠标可能导致悬停失败
        该关键字也可以用于页面滚动，但不一定都能滚动成功
        :param xpath: 元素的xpath
        :return:
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            # 定位失败，则直接返回
            return False
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(ele).perform()
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, "悬停成功")
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            # 定位失败，则直接返回
            return False

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

    # 强制等待
    def sleep(self, t):
        try:
            t = int(t)
        except:
            t = 1
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))

        time.sleep(t)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, "强制等待成功")

        return True

    def gettitle(self):
        """
        获取当前窗口的title，并在系统中保存一个名叫title的变量
        在支持关联的关键字中，可以使用{title}，来调用它的值
        :return: 无
        """
        title = self.driver.title
        self.params['title'] = title
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        return True

    def gettext(self, xpath):
        """
        获取当前xpath定位元素的文本，并在系统中保存一个名叫text的变量
        在支持关联的关键字中，可以使用{text}，来调用它的值
        :param xpath: 元素的xpath
        :return: 无
        """
        self.params['text'] = ''
        try:
            text = self.driver.find_element_by_xpath(xpath).text
            self.params['text'] = text
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            return True
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(traceback.format_exc()))
            return False

    def assertequals(self, param, value):
        """
        定义断言相等的关键字，用来判断前后的值是否一致
        :param param: 需要校验的参数
        :param value: 需要校验的值
        :return: 无
        """
        param = self.__getparams(param)
        value = self.__getparams(value)
        if str(param) == str(value):
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(param))
            return True
        else:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(param))
            return False

        # 获取参数里面的值

    def __getparams(self, s):
        logger.info(self.params)
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s


    def closebrower(self):
        try:
            self.driver.quit()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            self.writer.write(self.writer.row, self.writer.clo + 1, "关闭浏览器成功")

        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))
