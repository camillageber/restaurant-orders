import csv
from collections import defaultdict


def csv_importer(path_to_file: str):
    with open(path_to_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        return data


def get_orders(orders):
    return [{"client": item[0], "order": item[1],
             "day": item[2]} for item in orders]


def count_orders(orders, client):
    counter = defaultdict(int)
    for order in orders:
        if order["client"] == client:
            counter[order["order"]] += 1
    return dict(counter)


def marias_most_ordered_dish(orders: dict):
    max_dish = None
    max_count = -1
    for dish, count in orders.items():
        if count > max_count:
            max_dish = dish
            max_count = count
    return max_dish


def what_joao_never_did(orders, client):
    all_orders_days = set(data["day"] for data in orders)
    client_days = set(data["day"] for data in orders
                      if data["client"] == client)
    set_no_days = set()
    for day in all_orders_days:
        if day not in client_days:
            set_no_days.add(day)
    all_orders = set(order["order"] for order in orders)
    client_orders = set(order["order"] for order in orders
                        if order["client"] == client)
    set_no_dishes = set()
    for dish in all_orders:
        if dish not in client_orders:
            set_no_dishes.add(dish)
    return set_no_dishes, set_no_days


def analyze_log(path_to_file):

    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        csv_importer(path_to_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    csv_file = csv_importer(path_to_file)
    all_orders = get_orders(csv_file)
    orders_counter = count_orders(all_orders, "maria")
    most_ordered_dish = marias_most_ordered_dish(orders_counter)
    how_many_hamburgers = count_orders(
        all_orders, "arnaldo")['hamburguer']
    joao_no_day, joao_no_dish = what_joao_never_did(all_orders, "joao")

    result = [
        f'{most_ordered_dish}\n',
        f'{how_many_hamburgers}\n',
        f'{joao_no_day}\n',
        f'{joao_no_dish}\n'
    ]
    with open('data/mkt_campaign.txt', mode="w") as file:
        file.write(''.join(result))
