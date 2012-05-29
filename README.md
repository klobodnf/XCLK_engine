XCLK_engine
===========
这个是XCLK推荐引擎的项目文件

出现异常NameError: global name 'TApplicationException' is not defined
必须手动改slaveStatusInfService.py文件、在包导入from thrift.Thrift import TType, TMessageType, TException后添加
TApplicationException