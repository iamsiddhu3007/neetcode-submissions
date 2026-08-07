class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None
    
class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}
    self.head = Node(None, None)
    self.tail = Node(None, None)
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def insert(self, node):
    last = self.tail.prev

    last.next = node
    node.prev = last

    self.tail.prev = node
    node.next = self.tail 
  
  def remove(self, node):
    prevNode = node.prev
    nextNode = node.next

    prevNode.next = nextNode
    nextNode.prev = prevNode
  
  def get(self, key):
    if key in self.cache:
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].value
    return -1
  
  def put(self, key, value):
    if key in self.cache:
      self.remove(self.cache[key])
    self.cache[key] = Node(key, value)
    self.insert(self.cache[key])
    if len(self.cache)>self.capacity:
      first = self.head.next
      self.remove(first)
      del self.cache[first.key]
