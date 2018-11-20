#coding=utf-8
import unittest
#import HTMLTestRunner
import sys
sys.path.append("..")
#print('\n The python path', sys.path)
import testUtils.apiUtils as apiUtils
import globalVar


#测试端口:/Home/Login/getUid
#参数: [openId] 微信登录openId
#     [methods] url请求方法,默认为POST,支持持POST请求,GET请求不通过
#返回: [uid] 用户uid
#     [ERRORCODE] 错误码 0001(登录成功) 0002(输入不能为空) 0003(输入有误) 0004(用户不存在) 0008(请求错误)
class loginTest(unittest.TestCase):

    def setUp(self):
        self.url = globalVar.HOST_SERVER + "/Home/Login" + "/getUid"

    #def tearDown(self):


    #测试:微信登录
    #输入:正确用户openID
    #输出:错误码ERRORCODE=0001,登录成功
    def testLogin1(self):
        method = "POST"
        form = {"openId": globalVar.TEST_OPENID}
        r = apiUtils.url_request(self.url, form, method)
        print(r)
        self.assertEqual(r['ERRORCODE'], "0001")


    def testLogin2(self):
        method = "POST"
        form = {"openId": ""}
        r = apiUtils.url_request(self.url, form, method)
        print(r)
        self.assertEqual(r['ERRORCODE'], "0003")


    def testLogin3(self):
        method = "POST"
        form = {"NoOpenId": "test"}
        r = apiUtils.url_request(self.url, form, method)
        print(r)
        self.assertEqual(r['ERRORCODE'], "0003")

    def testLogin4(self):
        method = "POST"
        form = {"openId": "I am an error openID"}
        r = apiUtils.url_request(self.url, form, method)
        print(r)
        self.assertEqual(r['ERRORCODE'], "0004")





#测试套件
def suite():
    print("**********suite***********")
    loginTestCase = unittest.makeSuite(loginTest, "test")

    return loginTestCase



if __name__ == '__main__':

    print("**********__main__***********")
    file_path = "../report/test_report.html"
    apiUtils.testReport(suite(), file_path, "测试报告", "详情")#打印测试报告







