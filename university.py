with open(r"d:\сяп\task3\university.txt", 'r', encoding="utf-8") as file:
    lines = file.readlines()
    print("\nДанные о занятиях: ")
    for line in lines:
        print(line.strip())


classes_dict = {}

for line in lines:
    parts = line.strip().split(':')
    subject = parts[0].strip()
    details = parts[1].strip().split()

    lectures = 0
    practicals = 0
    lab = 0

    for detail in details:
        if detail.endswith('(л)'):
            lectures += int(detail[:-3])
        elif detail.endswith('(пр)'):
            practicals += int(detail[:-4])
        elif detail.endswith('(лаб)'):
            lab += int(detail[:-5])
    all = lectures + practicals + lab

    classes_dict[subject] = all
print(f"Общее количество: {classes_dict}")