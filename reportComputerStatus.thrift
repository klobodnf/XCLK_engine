namespace java com.xiu.recommender.monitor.thrift

struct StatusInfo {
    1: i32  id	  #ID
    2: string  ip  #客户端本机IP  
    3: double  cupRatio  #空闲CPU百分比
    4: i64  memTotal    #总计内存
    5: i64  memUsed	#已用内存
    6: double  memRatio  #已用内存百分比
    7: i64  diskTotal    #总计内存
    8: i64  diskUsed	 #已用内存
    9: double  diskRatio  #已用内存百分比
    10: double  netDelay  #网络延迟毫秒数
    11: double  loadAvg  #15分钟机器负载
  }
 service SlaveStatusInfoService {  #客户端状态接口
    i32 reportStatusInfo(1:StatusInfo info) #上传客户端电脑状态，成功返回1，失败返回0
 }