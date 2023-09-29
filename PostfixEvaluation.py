class Evaluate:

  def __init__(self, n):
    self.top = -1
    self.n = n
    self.arr = []

  def pop(self):
    if self.top != -1:
      p = self.arr[-1]
      self.top -= 1
      return self.arr.pop()

  def push(self, x):
    self.top += 1
    self.arr.append(x)

  def evaluatePostfix(self, exp):
    for i in exp:
      if i.isdigit():
        self.push(i)
      else:
        val1 = self.pop()
        val2 = self.pop()
        self.push(str(eval(val2 + i + val1)))
    return int(self.pop())


if __name__ == '__main__':
  exp = "231*+9-"
  obj = Evaluate(len(exp))
  s = obj.evaluatePostfix(exp)
  print("value:", s)
