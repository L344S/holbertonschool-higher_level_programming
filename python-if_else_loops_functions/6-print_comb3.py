#!/usr/bin/python3
for i in range(0, 10):  # count from 0 to 9
    for j in range(i + 1, 10):  # count from i + 1 to 9
        if i == 8:  # if i is not 8 (last two digits combination)
            print(f"{i}{j}")  # print each two unique digits combination
        else:
            print(f"{i}{j}", end=", ")  # print each two unique digits comb
