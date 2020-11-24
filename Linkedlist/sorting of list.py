class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist():
    def __init__(self):
        self.head=None
    def print(self,s):
        if self.head==None:
            print("linkedlist is empty")
            return
        itr=self.head
        lstr=''
        count=1
        while itr:
            if count==s:
                lstr+=str(itr.data)
            else:
                lstr+=str(itr.data)+" "
            itr=itr.next
            count+=1
        print(lstr)
    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_end(data)
l=Linkedlist()
a=int(input())
b=[int(i) for i in input().split()]
l.insert_values(sorted(b))
l.print(a)
