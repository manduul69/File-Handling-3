# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    if line_number <= 0:
        return ""
    else:
        file = open(filename, 'r')
        for current_line in range(1, line_number + 1):
            line = file.readline()
            if current_line == line_number:
                return line.rstrip('\n')
            if not line:
                return ""
    file.close()
filename = "Days.txt"
line_number = 3
print(read_line(filename,line_number))

# Exercise 2
def reverse_lines(source, destination):
    file = open(source, 'r')
    lines = file.readlines()
    file.close()
    reversed_lines = []
    for i in range(len(lines) - 1, -1, -1):
        cleaned_line = lines[i].strip() + "\n"
        reversed_lines.append(cleaned_line)
    file = open(destination, 'w')
    for line in reversed_lines:
        file.write(line)
    file.close()
    return len(reversed_lines)
source = "Days.txt"
destination = "destination.txt"
print(reverse_lines(source,destination))

# Exercise 3
def merge_files(first, second, destination):
    def merge_files(first, second, destination):
    file_1 = open(first, "r")
    lines_1 = file_1.readlines()
    file_1.close()
    file_2 = open(second, "r")
    lines_2 = file_2.readlines()
    file_2.close()
    file_3 = open(destination, "w")
    count = 0
    for line in lines_1:
        file_3.write(line.strip() + "\n")
        count += 1
    for line in lines_2:
        file_3.write(line.strip() + "\n")
        count += 1
    file_3.close()
    return count
    
# Exercise 4
def find_score(filename, name):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == name:
            return int(parts[1])
    return -1

# Exercise 5
def update_score(filename, name, new_score):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    found = False
    for i in range(len(lines)):
        parts = lines[i].strip().split(",")
        if parts[0] == name:
            lines[i] = parts[0] + "," + str(new_score) + "\n"
            found = True
            break
    if found == False:
        return False
    file = open(filename, "w")
    for line in lines:
        file.write(line)
    file.close()
    return True
