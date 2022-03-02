##Implementation of Doubly linked list

class node:
    def __init__(self ,data):
        self.data = data
        self.prev = None
        self.next = None

class linked_list:
    def __init__(self):
        self.HEAD = None

def forward_print_linked_list(link_list):

    while link_list != None:
        print(link_list.data )
        link_list = link_list.next


if __name__ == '__main__':

    one = node(0)
    scnd = node(1)
    third = node(2)

    one.prev = None
    one.next = scnd

    scnd.prev = one
    scnd.next = third

    third.prev = scnd
    third.next = None

    link_list = linked_list()
    link_list.HEAD = one

    forward_print_linked_list(link_list.HEAD)
