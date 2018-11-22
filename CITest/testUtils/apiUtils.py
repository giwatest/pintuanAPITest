#coding=utf-8


#接口测试通用函数

import requests
import HTMLTestRunner

#接口请求函数
#参数: url 接口地址
#     form 接口参数,默认为空
#     method 接口请求方法, 值为"GET"或"POST", 默认"GET"
#返回值: json字符串
def url_request(url, form="", method="GET"):

    response = ""

    if method == "POST":
        response = requests.post(url, data=form)


    else:
        response = requests.get(url)

    print(response)

    return response.json()

#打印测试报告函数
#参数: suit 测试套件函数
#    filePath 测试报告文件路径!!需要先把文件夹建好!!
#    title 测试报告标题
#    descri 测试报告描述
def testReport(suit, filePath, title, descri):
    fp = open(filePath, "wb+")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description=descri)
    runner.run(suit)
    fp.close()




