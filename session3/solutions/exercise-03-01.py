TEXT_FILE = "les_miserables.txt"

def print_first_line():
    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        it = iter(file)
        print(next(it))

#print_first_line()

def find_first_JV():
    target = "Jean Valjean"
    found = None
    count = 0
    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            count += 1
            if target in line:
                found = count
                break
    print(f"{target} found in line {found}")

#find_first_JV()

def count_all_lines():
    count = 0
    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            count += 1
    print(f"Number of lines = {count}")

#count_all_lines()

def avg_line_lenght():
    total_length = 0
    count = 0

    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            count += 1
            total_length += len(line)

    average = total_length / count
    print(average)

#avg_line_lenght()

def print_100_lines():
    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print(lines[100])

#print_100_lines()

def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

# for line in non_empty_lines("les_miserables.txt"):
#     print(line)
#     break


# target = "Jean"           
# count = 0
# for line in non_empty_lines(TEXT_FILE):
#     if target in line:
#         count += 1

# print(count)