namespace java com.xiu.recommender.monitor.thrift

struct StatusInfo {
    1: i32  id	  #ID
    2: string  ip  #�ͻ��˱���IP  
    3: double  cupRatio  #����CPU�ٷֱ�
    4: i64  memTotal    #�ܼ��ڴ�
    5: i64  memUsed	#�����ڴ�
    6: double  memRatio  #�����ڴ�ٷֱ�
    7: i64  diskTotal    #�ܼ��ڴ�
    8: i64  diskUsed	 #�����ڴ�
    9: double  diskRatio  #�����ڴ�ٷֱ�
    10: double  netDelay  #�����ӳٺ�����
  }
 service slaveStatusInfoService {  #�ͻ���״̬�ӿ�
    i32 reportStatusInfo(1:StatusInfo info) #�ϴ��ͻ��˵���״̬���ɹ�����1��ʧ�ܷ���0
 }