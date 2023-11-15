class Binary_search_tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:     # Since duplicates aare not allowed hence retun if already exist
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_search_tree_node(data)  # adding value using class by creating node

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_search_tree_node(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def search(self, val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_min(self):
        if self.left == None:
            return self.data
        else:
            return self.left.find_min()
    def find_max(self):
        if self.right == None:
            return self.data
        else:
            return self.right.find_max()
    def calculate_sum(self):
        if self.left:
            left_sum = self.left.calculate_sum()
        else:
            left_sum = 0
        if self.right:
            right_sum = self.right.calculate_sum()
        else:
            right_sum = 0

        return left_sum + right_sum + self.data


def build_tree(elements):
    root = Binary_search_tree_node(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [12,13,7,3,20,35,19,29]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())   # will retun in sorted order, will ignore duplicates if any
    # print(number_tree.search(20))
    # print(number_tree.find_max())
    # print(number_tree.find_min())
    print(number_tree.calculate_sum())
    # countries = ["uk", "usa", "china", "india", "france"]
    # country_tree = build_tree(countries)
    # print(country_tree.in_order_traversal())
    # print("Uk is in the list?",country_tree.search("uk"))
    # print("germany is in the list?", country_tree.search("germany"))
