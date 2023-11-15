class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None    # We are not passing an argument instead we are defining

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node     # impportant since node is now a box of a list (node) so head should point to this node
    def print_list(self):
        if self.head is None:
            print('Linkedlist is empty')
            return
        itr = self.head
        lllist = ''
        while itr:
            lllist += str(itr.data) + '-->'
            itr = itr.next
        print(lllist)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):  # creating a new linked list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def calculate_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.calculate_length():
            raise Exception("invalid index")
        if index==0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.calculate_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = linkedlist()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(10)
    # ll.print_list()
    # ll.insert_at_end(25)
    ll.insert_values(["apple", "banana", "mango"])
    ll.print_list()
    print('Length of linked list is:', ll.calculate_length())
    #ll.remove_at(1)
    ll.insert_at(1,"guava")
    ll.print_list()
