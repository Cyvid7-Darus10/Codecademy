class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert(self, data):
    newNode = Node(data)
    if (self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def find(self, key) -> Node:
    current = self.head
    while (current):
      if (current.data[0] == key):
        return current
      current = current.next
    return None

class HashMap:
  def __init__(self, array_size: int):
    self.array_size = array_size
    self.array = [LinkedList() for item in range(array_size)]

  def hashFunc(self, key) -> int:
    hash_code = sum(key.encode())
    return hash_code % self.array_size

  def assign(self, key: 'any type' , value: 'any type'):
    array_index = self.hashFunc(key)
    check = self.array[array_index].find(key)
    if (check != None):
      print("Key is Already Taken")
      return
    self.array[array_index].insert([key, value])

  def retrieve(self, key) -> Node:
    array_index = self.hashFunc(key)
    Node = self.array[array_index].find(key)
    if (Node == None):
      return None
    return Node.data[1]

    
def main():
  blossom = HashMap(15)
  
  flower_definitions = [
    ['daisy', 'a wonderful flower'],
    ['sunflower', 'flower that is like a sun'],
    ['Water Lily', 'Flow on a pond']
   ]

  for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])
  
  print(blossom.retrieve('daisy'))

if __name__ == "__main__":
    main()
