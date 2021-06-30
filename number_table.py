import time as t


h = int(input("Enter number to get table: "))


def tables_num(num):
    t1 = t.perf_counter()
    for i in range(2, 21):
        a = i * num
        print('%d x %d = %d' % (num, i, a))
    t2 = t.perf_counter()
    print('\nTime of Execution:', t2 - t1, 'milliseconds')


tables_num(h)
