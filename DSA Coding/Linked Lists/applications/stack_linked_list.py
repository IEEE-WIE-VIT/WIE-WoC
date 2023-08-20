class node:
    def __init__(self ,data ,link):
        self.data = data 
        self.link = link

class linked_list:
    def __init__(self ):
        self.head = None

    def create_node(self ,data ,link):
        new_node = node(data ,link)

        return new_node

    def insert_node(self ,data ):
        if self.head == None:
           self.head = self.create_node(data ,None)
        
        else:
            tmp =self.head
            while tmp.link != None:
                tmp = tmp.link
            
            tmp.link  = self.create_node(data ,None)
        
        return self.head
    def delete_node(self):
        if self.head == None:
            return "EMPTY-STACK"
        
        tmp =self.head
        while tmp.link.link != None:
            tmp = tmp.link
        tmp.link = None

    
    def print_list(self):
        tmp = self.head
        while tmp.link != None:
            print("> %d"%tmp.data)
            tmp =tmp.link 



linklist = linked_list()
linklist.head = node(0 ,None)
linklist.print_list()

head = linklist.insert_node(1)
head = linklist.insert_node(2 )
head = linklist.insert_node(3 )
head = linklist.insert_node(4 )
head = linklist.insert_node(5 )
head = linklist.insert_node(6 )

linklist.print_list()



linklist.delete_node()

linklist.print_list()
        
linklist.delete_node()
linklist.delete_node()


linklist.print_list()
