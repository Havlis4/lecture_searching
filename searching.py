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

def pattern_search(sequence, pattern):
    positions = set()
    pattern_length = len(pattern)
    sequence_length = len(sequence)
    i = 0

    while i <= sequence_length - pattern_length:
        j = 0
        while j < pattern_length and sequence[i+j] == pattern[j]:
            j += 1
            if j == pattern_length:
                positions.add(i)
                i += pattern_length
            elif j == 0:
                i += 1
            else:
                i += j
                
    return positions



def main():
    #pass
    sequential_data = read_data("sequential.json","unordered_numbers")
    print(sequential_data)


if __name__ == '__main__':
    main()