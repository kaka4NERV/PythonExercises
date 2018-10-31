# 输出指定格式的日期。
import time
tick = time.time()
print('当前时间戳为：', tick)
localtime = time.localtime()
print('时间元祖为：', localtime)
localtime = time.asctime(localtime)
print('时间格式为：', localtime)
time.sleep(3)
print('格式化时间为：', time.strftime('%Y %m %d %H %M %S', time.localtime()))
print('格式化时间为：', time.strftime('%Y/%m/%d/%H/%M/%S', time.localtime()))
print('格式化时间为：', time.strftime('%H:%M:%S %m/%d %Y', time.localtime()))
print('格式化初始时间为：', time.strftime('%H:%M:%S %m/%d %Y', time.localtime(tick)))