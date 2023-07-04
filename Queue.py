class Queue:
  def __init__(self):
    self.queue=[]
  def isEmpty(self):
    return self.queue==[]
  def enqueue(self,data):
    self.queue.append(data)
  def dequeue(self):
    x=None
    if not self.isEmpty():
      x=self.queue[0]
      self.queue=self.queue[1:]
    return x
  def __str__(self):
    return(str(self.queue))

q=Queue()
q.enqueue(9)
q.enqueue(87)
q.enqueue(56)
q.enqueue(768)
print(q)
print(q.dequeue())
print(q)