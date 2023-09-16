class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Llist:
    def __init__(self):
        self.head=None
    
    def addLast(self,val):
        nw=Node(val)
        if self.head is None:
            self.head = nw
            return
        else:
            start=self.head
            while start.next:
                start=start.next
            start.next = nw

    def delLast(self):
        temp=start=self.head
        if self.head==None:
            return
        else:
            while start.next:
                temp=start
                start=start.next
        temp.next=None
        start=None

    def printList(self):
        start=self.head
        while start:
            print(start.val, end=" ")
            start=start.next
        print()

root = Llist()
while True:
    ch=int(input("Enter 1: add last 2: delele last -"))
    if ch == 1:
        n=int(input("Enter a number:"))
        root.addLast(n)
    elif ch == 2:
        root.delLast()
    else:
        print("Invalid Case")
    root.printList()
    ans=input("Continue(Y/N)?")
    if ans in 'Yy':
        continue
    else:
        break