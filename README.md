XCLK_engine
===========
这个是XCLK推荐引擎的项目文件

使用xclk必须先安装thrift库、可以先来到这里参看一下thrift的py库安装
http://192.168.3.51/bbs/viewthread.php?tid=16&extra=page%3D1

P.S.：示例文件出现异常NameError: global name 'TApplicationException' is not defined
必须手动改slaveStatusInfService.py文件、在包导入from thrift.Thrift import TType, TMessageType, TException后添加
TApplicationException

