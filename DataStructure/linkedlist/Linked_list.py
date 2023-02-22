# why use linkedlist --> list is dynamic array (add double size of space to insert new value)
#additional capacity = capacity = size *2
# linkedd_list individual values in different memory by storing the link through memory address, list store contiguous memory
#ll --> change the address of the link --> insert i e
#insert at begin --> 0(1) at end --> 0(n)
#single linked_list
#----> Insert is easier and don't need to prelocate space
#Traverse --> 0(n)
#access --> 0(n)
#Double linked_list
#implement from scratch

class Node:
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self , data):

        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(23)
    ll.insert_at_begining(45)
    ll.insert_at_begining(65)
    ll.insert_at_begining(55)
    ll.insert_at_end(546)
    ll.insert_at_end(234)
    ll.print()