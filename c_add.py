import time
from ctypes import *
def main():
    num = int(input("请输入整数值:"))
    result = 0
    start_time = time.time()
    result = cdll.LoadLibrary("./c_dll.so")
    result.my_add(num)

    end_time = time.time()
    print("总共用时%s"%(end_time-start_time))

# def print_str():
#     s = str(input("请输入字串:"))
#     print("py print "+s)
#     start_time = time.time()
#     result = cdll.LoadLibrary("./c_dll.so")
#     result.print_str("print")

#     end_time = time.time()
#     print("总共用时%s"%(end_time-start_time))



if __name__ == "__main__":
    main()
    # print("======")
    # print_str()

