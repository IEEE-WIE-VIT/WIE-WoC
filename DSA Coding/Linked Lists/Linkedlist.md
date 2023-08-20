# Linked List

Linked List can be defined as collection of objects 
called **nodes** that are randomly stored in the memory.

A node contains two fields i.e. data stored at that 
particular address and the pointer which contains the address of the next node in the memory.

The last node of the list contains pointer to the null.

```py

LinkedList:object
Node:object
    
# Start with the empty list
llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

'''
Three nodes have been created.
We have references to these three blocks as head,
second and third

    llist.head        second              third
        |                |                  |
        |                |                  |
+----+------+     +----+------+     +----+------+
| 1  | None |     | 2  | None |     |  3 | None |
+----+------+     +----+------+     +----+------+
'''

llist.head.next = second; # Link first node with second

'''
Now next of first Node refers to second.  So they
both are linked.

    llist.head        second              third
        |                |                  |
        |                |                  |
+----+------+     +----+------+     +----+------+
| 1  |  o-------->| 2  | null |     |  3 | null |
+----+------+     +----+------+     +----+------+
'''

second.next = third; # Link second node with the third node

'''
Now next of second Node refers to third.  So all three
nodes are linked.

    llist.head        second              third
        |                |                  |
        |                |                  |
+----+------+     +----+------+     +----+------+
| 1  |  o-------->| 2  |  o-------->|  3 | null |
+----+------+     +----+------+     +----+------+
'''
```



#### Advantages of Linked Lists

1. Dynamic size
2. Ease of insertion/deletion

#### Drawbacks of Linked Lists

1. Random access is not allowed (Since elements aren't indexed)
2. Extra memory required for the pointer/reference to next node
3. takes a lot of time in traversing and changing the pointers


### Linked List operations

- Insertion
    - [Inserting a node](https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/)

- Delete a node
    - algorithm i used:
    ```md
    1. find the node to be deleted
    2. link the nodes before and after the deleted node
    3. check if the head is shifted (if deleted node is first one)
    ```

    - [delete the first occurrence of data](https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/)
    - [Delete a Linked List node at a given position](https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/)
