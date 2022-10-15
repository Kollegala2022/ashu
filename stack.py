class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=N1one
    def push(self,data):
        n=node(data)
        if self.head is None:
            self.head=n
        else:
            n.next=self.head
            self.head=n

    def pop(self):
        if self.head is None:
            print("Stack is empty")
        else:
            temp=self.head
            self.head.next=self.head

    def display(self):
        if self.head is None:
            print("Stack is empty")
        else:
            temp=self.head
            while temp:

                print(temp.data)
                temp = temp.next
s=stack()
while True:
    print('''\nstack operation:
    1.Push
    2.Pop
    3.Display the stack
    4.Exit''')
    c=int(input("enter the Choice:"))
    if c==1:
        a=int(input("enter the elemenet:"))
        s.push(a)
    elif c==2:
        s.pop()
    elif c==3:
        a=s.display()
        for i in reversed(a):
            print(i)
    elif c==4:
        print("exit")
        break
    else:
        print("invaild input")