```
class queue
  def __init__(self):
    self.items = []
    
  def isEmpty():
    return not bool(self.items)
  
  def enqueue(self, item):
    self.items.insert(0, item)
  
  def dequeue(self):
    if self.isEmpty():
      return None:
    else:
      return self.items.pop()

  def size():
    return len(self.items())
  
  def peek():
    if self.isEmpty():
      return None:
    else:
      return self.items[-1]
    
```  
