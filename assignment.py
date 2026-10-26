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
    # Write your code here
    pass

# Exercise 4
def find_score(filename, name):
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
