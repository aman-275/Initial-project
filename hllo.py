class Node:

    def __init__(self,value):

        self.value=value
        self.next=None


class linkedlist:

    def __init__(self):

        self.head=None


    def add(self,element):

        node=Node(element)

        if self.head is None:

            self.head=node

        else:

            cur=self.head
            while cur.next:
                cur=cur.next

            cur.next=node


    def printlinklist(self):

        cur=self.head
        while cur:

            print(cur.value)
            cur=cur.next


    
    def deletelinklist(self,element):

        cur=self.head

        while cur and cur.value==element:

            cur=cur.next
            self.head=cur

        assert(cur!=None),'nothing to delete add more elements'


        cur=self.head
        prev=None

        while cur:


            if cur.value==element:
                prev.next=cur.next
                cur=prev.next




            else:

                prev=cur
                cur=cur.next









l=linkedlist()

l.add(2)
l.add(2)
l.add(2)
l.add(3)
l.printlinklist()
l.deletelinklist(2)
print('='*8)
l.printlinklist()
