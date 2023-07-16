class linkedlist:
    def __init__(self):
        self.head = None
    

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

    def __repr__(self):
        return self.data

list1 = linkedlist()
first_node = Node('a')
list1.head = first_node
second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
