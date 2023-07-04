class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Stack:
  def __init__(self):
    self.top=None
  def isEmpty(self):
    if self.top==None:
      return True
    return False
  def push(self, data):
    temp=Node(data)
    temp.next=self.top
    self.top=temp
  def pop(self):
    if self.isEmpty():
      return None
    temp=self.top.data
    self.top=self.top.next
    return temp
  def display(self):
    if self.isEmpty():
      return None
    temp=self.top
    while(temp!=None):
      print(temp.data,end=' ')
      temp=temp.next
    print()

s=Stack()
print(s.display())
print(s.pop())
s.push(67)
s.push(55)
s.push(87)
s.push(123)
s.display()
print(s.pop())
print(s.pop())
s.display()