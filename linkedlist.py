class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node()
    
    def addElement(self,data):
        new_node=Node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
    
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    
    def display(self):
        cur_node=self.head
        print("Elements are:",end=" ")
        while cur_node!=None:
            cur_node=cur_node.next
            if cur_node!=None:
                print(cur_node.data,end=" ")
        print()

    def addElementAtPosition(self,data,index):
        new_node=Node(data)
        if index>=self.length() or index<0:
            self.addElement(data)
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            if cur_idx==index:
                new_node.next=cur_node.next
                cur_node.next=new_node
                return
            cur_node=cur_node.next
            cur_idx+=1
    
    def addElementAtHead(self,data):
        new_node=Node(data)
        if self.head.next==None:
            self.head.next=new_node
        else:
            new_node.next=self.head.next
            self.head.next=new_node
    
    def addElementAtTail(self,data):
        self.addElement(data)
    
    def removeElementAtTail(self):
        cur_node=self.head
        while True:
            if cur_node.next.next==None:
                cur_node.next=None
                break
            cur_node=cur_node.next
    
    def removeElementAtHead(self):
        self.head.next=self.head.next.next
    
    def removeElementAtIndex(self,index):
        if index>=self.length():
            self.removeElementAtTail()
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1
    
    def get(self,index):
        if index>=self.length():
            print("ERROR:'get' index out of range")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index:
                return cur_node.data
            cur_idx+=1
    
    def search(self,data):
        cur_node=self.head
        cur_idx=0
        while cur_node!=None:
            cur_node=cur_node.next
            if cur_node!=None:
                if cur_node.data==data:
                    return "Found at Index: "+str(cur_idx)
            cur_idx+=1
        return "Element Not Found"
    
    def selectionSort(self):
        currentpre=self.head
        current=currentpre.next

        while current!=None:
            minimum=current
            nextprev=current
            beforesort=nextprev
            nextinner=current.next

            while nextinner!=None:

                if minimum.data>nextinner.data:
                    beforesort=nextprev
                    minimum=nextinner
                nextprev=nextinner
                nextinner=nextinner.next


            if current.next==minimum :
                minimumNext=minimum.next
                currentpre.next=minimum
                minimum.next=current
                current.next=minimumNext
                current=minimum

            elif current.next!=minimum and current!=minimum:
                    currentNext=current.next
                    minimumNext=minimum.next
                    currentpre.next=minimum
                    minimum.next=currentNext
                    beforesort.next=current
                    current.next=minimumNext
                    current=minimum
            currentpre=current
            current=current.next
    
    def bubbleSort(self):
        numElements=self.length()-1
        while numElements>0:
            curr_idx=0
            curr_node=self.head.next
            while curr_idx<numElements:
                if curr_node.data>curr_node.next.data:
                    curr_node.data,curr_node.next.data=curr_node.next.data,curr_node.data
                curr_node=curr_node.next
                curr_idx+=1
            numElements-=1

    def insertionSort(self):
        numElements=self.length()
        curr_prev=self.head
        curr_node=curr_prev.next



ll=LinkedList()
ll.addElement(21)
ll.addElement(2)
ll.addElement(1)
ll.addElement(11)
# ll.display()
ll.addElementAtPosition(21,2)
# ll.display()
ll.removeElementAtHead()
ll.removeElementAtTail()
# ll.display()
ll.addElementAtHead(12)
ll.addElementAtTail(212)
# ll.display()
ll.removeElementAtIndex(0)
ll.display()
print(ll.get(2))
print(ll.search(215))
ll.insertionSort()
ll.display()