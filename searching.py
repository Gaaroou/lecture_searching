import os
import json

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

def main():
    pass


if __name__ == '__main__':
    main()
    filename = "sequential.json"
    data = read_data(filename, "unordered_numbers")
    print(data)

    search = linear_search(data,5)
    print(search)
