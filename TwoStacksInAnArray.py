import math
class twoStacks:
  def __init__(self,n):
    self.size=n
    self.arr=[None]*n
    self.top1=math.floor(n/2)+1
    self.top2=math.floor(n/2)
  def push1(self,x):
    if self.top1>0:
      self.top1=self.top1-1
      self.arr[self.top1]=x
    else:
      print("Stack overflow")

  def push2(self,x):
    if self.top2 < self.size-1:
      self.top2=self.top2+1
      self.arr[self.top2]=x
    else:
      print("Stack2 overflow")

  def pop1(self):
    if self.top1<=self.size/2:
      y=self.arr[self.top1]
      self.top1=self.top1+1
      return y
    else:
      print("Stack underflow")
      return -1

  def pop2(self):
    if self.top2>=math.floor(self.size/2)+1:
      y=self.arr[self.top2]
      self.top2=self.top2+1
      return y
    else:
      print("Stack underflow")
      return -1

if __name__ == '__main__':
  s=twoStacks(7)
  s.push1(1)
  s.push2(2)
  s.push2(3)
  s.push2(6)
  s.push1(19)
  s.push1(3)
  s.push1(7)
  print(s.pop1())
  print(s.pop1())
  print(s.pop2())