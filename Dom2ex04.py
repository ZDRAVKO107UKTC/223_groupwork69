clothes_on_pallet = list(map(int, input().split()))  # Дрехи на палета
shelf_capacity = int(input())  # Капацитет на стелажа

shelves_count = 0
current_shelf_load = 0

while clothes_on_pallet:
    current_cloth = clothes_on_pallet[0]

    if current_shelf_load + current_cloth <= shelf_capacity:
        current_shelf_load += current_cloth
        clothes_on_pallet.pop(0)
    else:
        shelves_count += 1
        current_shelf_load = 0

# Проверяваме за останали дрехи, които не са се вместили на последния стелаж
if current_shelf_load > 0:
    shelves_count += 1

print(shelves_count)
