from Node import *


class LinkedList:
    def __init__(self):
        self.head = None
        self.current_size = 0

    def add(self, index, data):
        if index < 0 or index > self.current_size:
            raise Exception("The index should be between 0 and linked list size. ")
        if index == 0:
            self.add_first(data)
            return
        new_node = Node(data)
        tmp_pointer = self.head
        for count_move in range(1, index):
            tmp_pointer = tmp_pointer.next
        new_node.next = tmp_pointer.next
        tmp_pointer.next = new_node
        self.current_size = self.current_size + 1

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.current_size = self.current_size + 1

    def add_last(self, data):
        if self.head is None:
            self.add_first(data)
            return
        new_node = Node(data)
        tmp_pointer = self.head
        for count_move in range(1, self.current_size):
            tmp_pointer = tmp_pointer.next
        tmp_pointer.next = new_node
        new_node.next = None
        self.current_size = self.current_size + 1

    def contains(self, data):
        if self.head is None:
            return False
        tmp_pointer = self.head
        # Traverse to null
        while tmp_pointer is not None:
            if tmp_pointer.data == data:
                return True
            tmp_pointer = tmp_pointer.next
        return False

    def get(self, index):
        if index < 0 or index > self.current_size:
            raise Exception("The index should be between 0 and linked list size. ")
        tmp_pointer = self.head
        for count_move in range(1, index + 1):
            tmp_pointer = tmp_pointer.next
        return tmp_pointer.data

    def get_first(self):
        return self.head.data
        # return self.get(0)

    def get_last(self):
        tmp_pointer = self.head
        # Traverse to last node
        while tmp_pointer.next is not None:
            tmp_pointer = tmp_pointer.next
        return tmp_pointer.data
        # return self.get(self.current_size - 1)

    def get_size(self):
        return self.current_size

    def is_empty(self):
        return self.head is None

    def remove_node(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            return self.remove_first()
        tmp_pointer = self.head
        prev_pointer = None
        while tmp_pointer is not None:
            if tmp_pointer.data == data:
                prev_pointer.next = tmp_pointer.next
                self.current_size = self.current_size - 1
                return data
            prev_pointer = tmp_pointer
            tmp_pointer = tmp_pointer.next
        return None

    def remove(self, index):
        if self.head is None:
            return None
        if index < 0 or index > self.current_size:
            raise Exception("The index should be between 0 and linked list size. ")
        if index == 0:
            return self.remove_first()
        tmp_pointer = self.head
        for count_move in range(1, index):
            tmp_pointer = tmp_pointer.next
        removed_data = tmp_pointer.next.data
        tmp_pointer.next = tmp_pointer.next.next
        self.current_size = self.current_size - 1
        return removed_data

    def remove_first(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        tmp_pointer = self.head
        tmp_pointer = tmp_pointer.next
        self.head = tmp_pointer
        self.current_size = self.current_size - 1
        return removed_data

    def remove_last(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.remove_first()
        tmp_pointer = self.head
        # Traverse to second last node
        for count_move in range(1, self.current_size - 1):
            tmp_pointer = tmp_pointer.next
        removed_data = tmp_pointer.next.data
        tmp_pointer.next = None
        self.current_size = self.current_size - 1
        return removed_data

    def set(self, index, data):
        if self.head is None:
            return
        if index < 0 or index > self.current_size - 1:
            raise Exception("The index should be between 0 and linked list size. ")
        if index == 0:
            self.head.data = data
        tmp_pointer = self.head
        for count_move in range(1, index + 1):
            tmp_pointer = tmp_pointer.next
        tmp_pointer.data = data

    def show(self):
        tmp_pointer = self.head
        for i in range(0, self.current_size):
            print("[ " + str(tmp_pointer.data) + " ] -> ", end='')
            tmp_pointer = tmp_pointer.next
        print(" null ")


ll = LinkedList()
ll.add_first(100)
ll.add_first(200)
ll.add_last(500)
ll.add(3, 600)
ll.show()
print(ll.contains(600))
print(ll.get(0))
print(ll.get_first())
print(ll.get_last())
print(ll.get_size())
print(ll.is_empty())
print(ll.remove_first())
print(ll.remove_last())
print(ll.remove(0))
ll.show()
ll.set(0, 800)
ll.add_first(500)
ll.show()
print(ll.remove_node(500))
ll.show()                





