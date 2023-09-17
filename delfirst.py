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

    def delFirst(self):
        start=self.head
        if self.head==None:
            return
        else:
            self.head=start.next
            start=None

    def delAny(self, pos):
        temp=start=self.head
        if self.head==None:
            return
        else:
            for i in range(1,pos):
                temp=start
                if start:
                    start=start.next
            if i==pos and start==None:
                temp.next=None
                start=None
            elif i==pos-1 and start!=None:
                temp.next=start.next
                start=None
            else:
                print("Invalid Position")

    def insAny(self, val, pos):
        nw=Node(val)
        if self.head==None:
            self.head=nw
        else:
            temp=start=self.head
            for i in range(1,pos):
                temp=start
                if start:
                    start=start.next
            if i==pos and start==None:
                start.next=nw
            elif i==pos-1 and start!=None:
                temp.next=nw
                nw.next=start
            else:
                print("Invalid Position")

    def printList(self):
        start=self.head
        while start:
            print(start.val, end=" ")
            start=start.next
        print()

root = Llist()
while True:
    ch=int(input("Enter 1: add last 2: delele last 3: delete first 4: delete anywhere 5: insert anywhere -"))
    if ch == 1:
        n=int(input("Enter a number:"))
        root.addLast(n)
    elif ch == 2:
        root.delLast()
    elif ch == 3:
        root.delFirst()
    elif ch==4:
        pos=int(input("Enter a position:"))
        root.delAny(pos)
    elif ch==5:
        pos=int(input("Enter a position:"))
        val=int(input("Enter a value:"))
        root.insAny(val, pos)
    else:
        print("Invalid Case")
    root.printList()
    ans=input("Continue(Y/N)?")
    if ans in 'Yy':
        continue
    else:
        break
