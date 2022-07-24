
def count_up_loop(num, start=0):
    if num == start:
        print(start)
        print('-----count up-----')
        return num
    else:
        print(start)
        return count_up_loop(num, start+1)

count_up_loop(5,)
def count_down_loop(num):
    if num == 0:
        print(num)
        print('----count down----')
        return num
    else:
        print(num)
        return count_down_loop(num - 1)
        

count_down_loop(5)