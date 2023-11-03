class Inventory:

    def __init__(self, __capacity: int) :
        self.__capacity = __capacity
        self.items = []

    def add_items(self, item: str):
        if self.__capacity > 0:
            self.__capacity -= 1
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}. \nCapacity left: {self.__capacity}"


inventory = Inventory(2)
inventory.add_items("potion")
inventory.add_items("sword")
print(inventory.add_items("bottle"))
print(inventory.get_capacity())
print(inventory)