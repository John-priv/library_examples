'''
Linked List (created using Standard Python)
'''


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_nodes(self, node_list):
        for node in node_list:
            self.add_node(node)

    def add_node(self, node_value):
        new_node = LinkedListNode(node_value)
        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.set_next(new_node)
        self.tail = new_node

    def remove_nodes(self, node_list):
        for node in node_list:
            self.remove_node(node)

    def remove_node(self, node_value):
        current_node = self.head
        if current_node is None:
            # print('Cannot remove {}: Empty linked list'.format(node_value))
            return
        else:
            if current_node.value == node_value:
                # print('Removing node {}: Head'.format(node_value))
                self.head = current_node.next   # Move head to next element
                current_node = None             # Delete original head
                return

        # Already checked head; now can check element n+1
        while current_node is not None:
            if current_node.next is not None:
                if current_node.next.value == node_value:
                    node_to_delete = current_node.next
                    current_node.next = node_to_delete.next
                    node_to_delete = None
                    # Move the tail
                    if current_node.next is None:
                        # print('Removing Node {}: Tail'.format(node_value))
                        self.tail = current_node
                    # else:
                    #     print('Removing Node {}: Body'.format(node_value))
                    return
            current_node = current_node.next
        # print('Cannot remove {}: Value not found in linked list'.format(node_value))

    def print_nodes(self):
        current_node = self.head
        node_count = 0
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next
            node_count += 1
        # print('\nThere are {} nodes in the linked list\n'.format(node_count))

    def generate_node_list(self):
        current_node = self.head
        node_list = []
        while current_node is not None:
            node_list.append(current_node.value)
            current_node = current_node.next
        return node_list


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next):
        self.next = next


def demo_linked_list():
    # Temporary section: Remove after linked list is functional
    linked_list = LinkedList()
    linked_list.add_nodes([1, 2, 3, 4, 5])
    linked_list.add_node(6)
    linked_list.print_nodes()

    linked_list.remove_nodes([1, 3, 6])
    linked_list.print_nodes()

    linked_list.add_nodes([1, 2, 3, 4, 5])
    linked_list.print_nodes()

    node_list = linked_list.generate_node_list()
    linked_list.remove_nodes(node_list)
    linked_list.print_nodes()

    linked_list.remove_node(1)
    linked_list.add_nodes([1, 2, 3, 4, 5])
    linked_list.remove_node(6)
    linked_list.print_nodes()


# Temporary section: Remove after linked list is functional
if __name__ == '__main__':
    demo_linked_list()
