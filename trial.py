import sys
import traceback

def func():
    print("running func!")
    print(a)


try:
    func()
except:
    error_type, error_value, error_trace = sys.exc_info()  # 错误类型、错误内容、traceback对象

print(error_type)

print(error_value)

with open('error.txt', 'a') as f:
    traceback.print_tb(error_trace)
    traceback.print_tb(error_trace, file=f)  # 将信息存入文件