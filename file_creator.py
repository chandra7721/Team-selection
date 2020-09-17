from threading import Thread
from itertools import permutations, combinations
from random import choice

main_list = [11, 21, 33, 41, 68, 57, 71, 61]
matrix = [0, 1, 2, 3, 4, 5, 6, 7]
delh_list = []
up_list = []
hary_list = []

def writer(block, header = None, leng = None):
    if leng == None:
        leng = len(block)
    with open(header, "w") as task:
        for i in permutations(block, leng):
            task.write(str(list(i)))
            task.write("\n")

def worker(block, header = None):
    karry = [0,0,0,0,0,0,0,0]
    with open(header, "w") as task_1:
        x = len(block)
        for i in combinations(matrix, x):
            for j in permutations(block):
                for n in range(0, x):
                    karry[i[n]] = j[n]
                task_1.write(str(karry))
                task_1.write("\n")
                karry = [0,0,0,0,0,0,0,0]

def task_force():
    layer1 = Thread(target = writer(main_list, "layer1.txt"))
    delh = Thread(target = worker([12, 13, 14, 15], "delh.txt"))
    up = Thread(target = worker([42, 43, 44], "up.txt"))
    hary = Thread(target = worker([22, 23, 24], "hary.txt"))
    layer1.start()
    delh.start()
    up.start()
    hary.start()
    layer1.join()
    delh.join()
    up.join()
    hary.join()
