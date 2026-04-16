import os
import json
import time
from fileinput import filename

import matplotlib.pyplot as plt
from generators import *
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file:
        data = json.load(file)
    if field in data.keys():
        return data[field]
    else:
        print(f"Field {field} not exists")
        return None

def linear_search(sekvence, hledane_cislo):
    slov = {}
    index = []
    count = 0
    for i in range(len(sekvence)-1):
        if hledane_cislo == sekvence[i]:
            count += 1
            index.append(i)
    slov["positions"] = index
    slov["count"] = count
    return slov

def binary_search(sekvence, hledane_cislo):
    left = 0
    right = int(len(sekvence) - 1)
    while left <= right:
        idx_pul = int((left + right) / 2)
        if sekvence[idx_pul] == hledane_cislo:
            return idx_pul
        elif sekvence[idx_pul] < hledane_cislo:
            left = idx_pul+1
        elif sekvence[idx_pul] > hledane_cislo:
            right = idx_pul-1
    return None

def time_management(cisla1,cisla2):
    linear_times = []
    binary_times = []
    start1 = time.perf_counter()
    linear_search(cisla1,5)
    end1 = time.perf_counter()
    duration1 = end1 - start1
    linear_times.append(duration1)

    start2 = time.perf_counter()
    binary_search(cisla2, 2)
    end2 = time.perf_counter()
    duration2 = end2 - start2
    binary_times.append(duration2)
    return duration1,duration2

def main():
    filename = "sequential.json"
    data = read_data(filename, "unordered_numbers")
    print(data)

    search = linear_search(data, 5)
    print(search)

    data2 = read_data(filename, "ordered_numbers")
    b_search = binary_search(data2, 2)
    print(data2)
    print(b_search)

    seq1 = unordered_sequence(500)
    seq2 = unordered_sequence(1000)
    seq3 = ordered_sequence(1000)

    dur1, dur2 = time_management(seq1, seq3)
    print(f"První měření trvalo {dur1:.8f} s")
    print(f"Druhé měření trvalo {dur2:.8f} s")

    sizes = [500, 1000]
    times = [dur1,dur2]
    plt.plot(sizes,times)
    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Ukázkový graf měření")
    plt.show()



    pass


if __name__ == '__main__':
    main()
