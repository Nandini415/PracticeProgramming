class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front=None
    self.rear=None
  def isEmpty(self):
    if self.front==None:
      return True
    return False
  def enqueue(self,data):
    if self.isEmpty():
      self.rear=self.front=Node(data)
    else:
      temp=Node(data)
      self.rear.next=temp
      self.rear=temp
  def dequeue(self):
    if self.isEmpty():
      return None
    elif self.front==self.rear:
      temp=self.front.data
      self.front=self.rear=None
    else:
      temp=self.front.data
      self.front=self.front.next
    return temp

  def display(self):
    if self.isEmpty():
      print("None")
    else:
      temp=self.front
      while temp!=None:
        print(temp.data)
        temp=temp.next


Q = Queue()
Q.enqueue(98)
Q.enqueue(32)
Q.enqueue(1)
Q.enqueue(23)
Q.enqueue(35)
Q.display()
print(Q.dequeue())
Q.display()