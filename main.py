with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите данные: ")
        if line == "":
            break
        f1.write(line + '\n')


with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        if not any(char.isdigit() for char in line):
            f2.write(line)


with open('F2.txt', 'r') as f2:
    lines = f2.readlines()
    last_line = lines[-1].strip()
    count = len(last_line.split())
    print(count)