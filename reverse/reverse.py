class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self):
        current = self.head #start with head node
        prev = None #previous when current changes
        while current:
            nxt = current.get_next() #find the next node to current
            current.set_next(prev) #set the next node to be the one previous of current.
            prev = current #set previous to be whatever the current node is, then move to next.
            current = nxt #repeat the process on the next node
        self.head = prev #set the head to be the last occurence

    def print_list(self):
        current = self.head
        lst = []
        while current:
            lst.append(current.value)
            current = current.next_node
        print('     ', lst)

test = LinkedList()
test.add_to_head('c')
test.add_to_head('b')
test.add_to_head('a')
print('        NON REVERSED')
test.print_list()
test.reverse_list()
print('          REVERSED')
test.print_list()
