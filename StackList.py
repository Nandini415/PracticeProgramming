class Stack:
  def __init__(self):
    self.stack=[]
  def isEmpty(self):
    return self.stack==[]
  def push(self,a):
    self.stack.append(a)
  def pop(self):
    x=None
    if not self.isEmpty():
      x=self.stack.pop()
    return x
  def __str__(self):
    return(str(self.stack))

s=Stack()
s.push(1)
s.push(5)
s.push(4)
s.push(4)
print(s)
print(s.pop())
print(s)