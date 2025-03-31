from Node import Node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def len(self):
        return self.length

    def __add_new_node(self, actual_node, new_node):
        if not actual_node.next:
            actual_node.next = new_node
            return

        self.__add_new_node(actual_node.next, new_node)

    def append(self, value):
        new_node = Node(value)

        if self.head:
            self.__add_new_node(self.head, new_node)
        else:
            self.head = new_node

        self.length += 1

    """def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node

        else:
            actual_node = self.head
            while actual_node.next:
                actual_node = actual_node.next

            actual_node.next = new_node

        self.length += 1"""


    def __str__(self):
        pass