food_quantity = int(input())  # Количеството на наличната храна
orders = list(map(int, input().split()))  # Списък с поръчките

largest_order = max(orders)  # Намираме най-голямата поръчка

while orders:
    current_order = orders[0]

    if food_quantity >= current_order:
        food_quantity -= current_order
        orders.pop(0)
    else:
        break

if not orders:
    print(largest_order)  # Най-голямата поръчка
    print("Orders complete")
else:
    print(largest_order)  # Най-голямата поръчка
    remaining_orders = ', '.join(map(str, orders))
    print(f"Orders left: {remaining_orders}")
