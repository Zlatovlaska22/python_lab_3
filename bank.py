with open(r"d:\сяп 1 сем\task2\bankclients.txt", 'r', encoding="utf-8") as file:
    content = file.readlines()
    print("Список всех клиентов: ")
    for line in content:
        print(line.strip())

if not line:
    print("Файл пуст.")
else:
    name = []
    cost = []
    date = []

for line in content:
    parts = line.split()
    if len(parts) == 3:
        client_name = parts[0]
        client_cost = float(parts[1])
        client_date = parts[2]
        name.append(client_name)
        cost.append(client_cost)
        date.append(client_date)

print("\nКлиенты с нулевым балансом: ")
for i in range(len(name)):
    if cost[i] == 0:
        print(f"{name[i]} - {cost[i]}")


all_price = sum(cost)
print(f"Общий баланс: {all_price}")