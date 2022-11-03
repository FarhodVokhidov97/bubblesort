from random import randint
import timeit


def bubbleSort(list):
    list_len = len(list)
    for i in range(list_len):
        for k in range(list_len-i-1):
            if list[k]>list[k+1]:
                list[k],list[k+1] = list[k+1],list[k]
                print(list)       


if __name__ == '__main__':
    list = [randint(0,10)for i in range(10)]
    bubbleSort(list)