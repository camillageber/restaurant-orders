from collections import Counter


class TrackOrders:

    def __init__(self):
        self._orders = []

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        new_order = (customer, order, day)
        self._orders.append(new_order)

    def track_data_from_orders(self, i, customer=None):
        data_orders = [
            order[i]
            for order in self._orders
            if not customer or order[0] == customer
        ]
        return data_orders

    def get_most_ordered_dish_per_customer(self, customer):
        ordered_dishes = self.track_data_from_orders(1, customer)

        if not ordered_dishes:
            return None

        dish_counts = {}
        for dish in ordered_dishes:
            dish_counts[dish] = dish_counts.get(dish, 0) + 1

        most_ordered_dish = max(dish_counts, key=dish_counts.get)
        return most_ordered_dish

    def get_never_ordered_per_customer(self, customer):
        all_dishes = set(self.track_data_from_orders(1))
        customer_dishes = set(self.track_data_from_orders(1, customer))
        never_ordered = all_dishes - customer_dishes
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        all_days = set(self.track_data_from_orders(2))
        customer_days = set(self.track_data_from_orders(2, customer))
        never_visited = all_days - customer_days
        return never_visited

    def get_busiest_day(self):
        all_days = self.track_data_from_orders(2)
        max_days = Counter(all_days).most_common()
        max_day = max_days[0][0]
        return max_day

    def get_least_busy_day(self):
        all_days = self.track_data_from_orders(2)
        max_days = Counter(all_days).most_common()
        min_day = max_days[-1][0]
        return min_day
