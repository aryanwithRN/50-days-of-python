class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, new_data):
        c = 0
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    
    def insert_at_pos(self,new_data,pos):
        new_node = Node(new_data)
        if pos < 1:
            print("Invalid position")
        elif self.head is None:
            print("Empty link list")
        else:
            new_node = Node(new_data)
            current = self.head
            C = 1
            while current.next is not None:
                if C == pos - 1:
                    new_node.next = current.next
                    current.next = new_node
                    # break
                C +=1
                current = current.next
    
    
    # Delete Node
    # def deleteNode(self,pos):
    #     if self.head is None:
    #         print("The single linked list does not exist ! ")
    #     else:
    #         if pos == 0:
    #             if self.head == self.tail:
    #                 self.head = None
    #                 self.tail = None

    #             else:
    #                 self.head = self.head.next

    #         elif pos == 1:
    #             if self.head == self.tail:
    #                 self.head = None
    #                 self.tail = None
    #             else:
    #                 node = self.head
    #                 while node is not None:
    #                     if node.next == self.tail:
    #                         break
    #                     node = node.next
    #                 node.next = None
    #                 self.tail = node
    #         else:
    #             tempNode = self.head
    #             index = 0  
    #             while index < pos -1 :
    #                 tempNode = tempNode.next
    #                 index +=1
    #             nextNode = tempNode.next
    #             tempNode = nextNode.next



#  delete Node
    def deleteNode(self,del_data):
        current = self.head
        if current.data == del_data:
            self.head = current.next
            current.next=None
        else:
            prev_node = None
            while current and current.data != del_data:
                prev_node = current
                current = current.next
            prev_node.next = current.next
            current.next = None


    def delete_at_pos(self,pos):
        current = self.head
        prev_node = None
        c =1
        while current and c!=pos:
            prev_node = current
            current = current.next
            c+=1
        prev_node.next = current.next
        current.next= None

    def display(self):
        current = self.head
        if current is None:
            print("None")
            return
        print(current.data, end="->")
        while current.next is not None:
            current = current.next
            print(current.data, end="->")
        print("None")
       
# main

L1 = LinkedList()
L1.insert(1)
L1.insert(2)
L1.insert(3)
L1.insert(4)
L1.insert(5)
L1.display()
L1.insert_at_pos(6,3)
L1.display()

L1.deleteNode(3)
# print("here")
L1.display()

# del at positon
L1.delete_at_pos(3)
L1.display()

