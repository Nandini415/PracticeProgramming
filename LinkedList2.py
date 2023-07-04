class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def isempty(self):
    if self.head == None: 
      return True
    else:
      return False
  def append(self,data):
    if self.isempty():
      self.head=Node(data)
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      temp.next = Node(data)
  def delete(self,v):
    if self.isempty() == True:
      return 'List is empty'
    elif self.head.next == None:
      if self.head.data == v: 
                self.head = None
      else:
         return 'Not exist'
    else:
      temp = self.head
      temp1 = self.head
      while temp.next!= None and temp.data != v: 
        temp1 = temp
        temp = temp.next
      if temp.data == v and temp == self.head: 
        self.head = temp.next
      elif temp.data == v: 
        temp1.next= temp.next
      else:
        return 'Not exist'
  def display(self):
    if self.isempty()==True:
      print('None')
    else:
      temp = self.head
      while temp!=None:
       print(temp.data,end="  ")
       temp = temp.next

L = LinkedList()
L.append(30)
L.append(40)
L.append(50)
L.display()
L.delete(30)
L.display()