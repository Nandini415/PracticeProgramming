class Node:
  def __init__(self, v = None):
    self.value = v
    self.next = None
  def isempty(self):
    if self.value == None:
      return(True)
    return(False)

  def append(self,x):
    if self.isempty():
      self.value=x
    elif self.next==None:
      self.next=Node(x)
    else:
      self.next.append(x)
    return

  def appendi(self,x):
    if self.isempty():
      self.value=x
      return
    temp=self
    while temp.next!=None:
      temp=temp.next
    temp.next=Node(x)
    return

  def insert(self,v):
    if self.isempty():
      self.value=v
      return
    newnode=Node(v)
    (self.value,newnode.value)=(newnode.value,self.value)
    (self.next,newnode.next)=(newnode,self.next)
    return
  def delete(self,v):
    if self.isempty():
      return 
    if self.value==v:
      self.value=None
      if self.next!=None:
        self.value=self.next.value
        self.next=self.next.next
    else:
      if self.next != None:
        self.next.delete(v)
        if self.next.value == None:
          self.next = None
    return
  def display(self):
    if self.isempty()==True:
      print('None')
    else:
      temp = self
      while temp!=None:
        print(temp.value,end="  ")
        temp = temp.next
      print()
head = Node(10)
head.append(20)
head.append(30)
head.appendi(40)
head.display()
head.appendi(50)
head.insert(67)
head.display()
head.delete(30)
head.display()
head.insert(67)
head.display()