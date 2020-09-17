from file_creator import task_force
from random import choice, randint
import os
import sqlite3
from itertools import permutations, combinations

gen_list = [[0, 0, 0, 0], [0, 0, 0, 0,], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
loc_trail = [0, 1, 2] #for the previous year players as delhi, haryana, up
empty_slots = [] #For empty slots left after the creation of template
done_slot = []

if not os.path.isfile("layer1.txt"):
    task_force()


# To pick the last year teams
def picker_0():
    with open("layer1.txt", "r") as f:
        a = randint(1, 40320)
        for i, line in enumerate(f):
            if i == a:
                k, c = len(line), 0
                for i in line[1:(k-1)].split():
                    gen_list[c][0] = int(i[0:len(i)-1])
                    if gen_list[c][0] == 11:
                        loc_trail[0] =  (c, 0)
                    elif gen_list[c][0] == 21:
                        loc_trail[1] = (c, 0)
                    elif gen_list[c][0] == 41:
                        loc_trail[2] = (c, 0)
                    c += 1
                break


# To fill the other templates
def editor(fil, key_ptt = None, max_val = None, sector = None):
    with open(fil, "r") as k:
        locus = True
        val = randint(1, max_val)
        for i, line in enumerate(k):
            if i == val:
                z = []
                for i in line[1:len(line)-1].split():
                    z.append(int(i[0:len(i)-1]))
                if str(gen_list[key_ptt][0])[0] != str(z[key_ptt])[0]:
                    for i in range(0,8):
                        gen_list[i][sector] = z[i]
                    return gen_list

        val = randint(1, max_val)
        return editor(fil, key_ptt, max_val, sector)

def final_touch(done, emp, li):
    k = li
    z= done[0:5]
    for i in combinations(emp, 5):
        for j in permutations(z):
            if final_touch2(j, i, k):
                for (m, n) in zip(done, emp):
                    k[n[0]][n[1]] = m
                return k

def final_touch2(per, em, k):
    for (i, j) in zip(per, em):
        if i == 58:
            if 57 in k[j[0]]:
                return False
        if i == 57:
            if 58 in k[j[0]]:
                return False
        if i == 62:
            if 61 in k[j[0]]:
                return False
        if i == 61:
            if 62 in k[j[0]]:
                return False
        if i == 69:
            if 68 in k[j[0]]:
                return False
        if i == 68:
            if 69 in k[j[0]]:
                return False
        if i == 81:
            if 82 in k[j[0]]:
                return False
        if i == 82:
            if 81 in k[j[0]]:
                return False
    return True




picker_0()
editor("delh.txt", loc_trail[0][0], 1680, 1)
editor("hary.txt", loc_trail[1][0], 336, 2)
editor("up.txt", loc_trail[2][0], 336, 3)

a, b = len(gen_list), len(gen_list[0])
for x in range(a):
    for y in range(b):
        if gen_list[x][y] == 0:
            empty_slots.append((x, y))
        else:
            done_slot.append(gen_list[x][y])

mydb = sqlite3.connect('Assign')
c = mydb.cursor()
c.execute("SELECT code FROM Data")
a = c.fetchall()
a.pop()
b = []

for i in a:
    b.append(i[0])

a = []
for i in done_slot:
    b.remove(i)

done_slot = b
b = []

gen_list = final_touch(done_slot, empty_slots, gen_list)
print(gen_list)

for i in range(0, len(gen_list)):
    for j in range(0, 4):
        sql_select_query = c.execute("SELECT  Name FROM Data where code = (?)",((gen_list[i][j], )))
        o = str(sql_select_query.fetchone())
        gen_list[i][j] = o[3:len(o)-3]


print(gen_list)
y = 65
li = gen_list
for i in range(0, len(li)):
    # sql_select_query = c.execute("INSERT INTO Result VALUES (?, ?, ?, ?, ?)",((, )))
    oo = chr(y)
    v1, v2, v3, v4 = li[i][0], li[i][0], li[i][0], li[i][0]
    c.execute("INSERT INTO Result VALUES (?, ?, ?, ?, ?)",(oo, v1, v2, v3, v4))
    y += 1

print("Thank you for looking at the work")
mydb.commit()
mydb.close()
# motiv = input("Enter (a) for write into db and display, (b) for only display ")
# print(motiv)
# if motiv == 'a':
#     print("hello")
#
# else:
#     print('BYE')
    # print(gen_list)

