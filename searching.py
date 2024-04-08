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

    with open("sequential.json","r") as f:
        allowed_key = json.load(f)

    if field not in allowed_key:
        return None

    with open(file_name,"r") as f:
        data = json.load(f)

    return data.get(field)

def linear_search(sequence, target):
    positions = []
    count = 0

    for i, num in enumerate(sequence):
        if num == target:
            positions.append(i+1)
            count += 1
    return {"positions": positions, "count": count}


def main():
    #pass
    sequential_data = read_data("sequential.json","unordered_numbers")
    print(sequential_data)


if __name__ == '__main__':
    main()