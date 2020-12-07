class HashMap:
  def __init__(self, array_size: int):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hashFunc(self, key, count_collisions: int = 0) -> int
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return (hash_code + count_collisions) % self.array_size

  def assign(self, key: 'any type' , value: 'any type'):
    array_index = self.hashFunc(key)
    current_array_value = self.array[array_index]

    number_collisions = 0

    while(current_array_value != None and current_array_value[0] != key):
      if number_collisions > self.array_size: #All array values are travelled
        print("Array is Full")
        return
      number_collisions += 1
      array_index = self.hashFunc(key, number_collisions)
      current_array_value = self.array[array_index]

    self.array[array_index] = [key, value]

  def retrieve(self, key):
    array_index = self.hashFunc(key)
    possible_return_value = self.array[array_index]

    if possible_return_value == None:
      return None
      
    retrieval_collisions = 0

    while (possible_return_value[0] != key):
      if retrieval_collisions > self.array_size: #All array values are travelled
        return None
      retrieval_collisions += 1
      retrieving_array_index = self.hashFunc(key, retrieval_collisions)
      possible_return_value = self.array[retrieving_array_index]

    return possible_return_value[1]

def main():
  hash_map = HashMap(15)

  hash_map.assign("gabbro", "igneous")
  hash_map.assign("sandstone", "sedimentary")
  hash_map.assign("gneiss", "metamorphic")
  hash_map.assign("2gabbra", "2igneous")
  hash_map.assign("2sandsone", "2sedimentary")
  hash_map.assign("2gneis", "2metamorphic")
  hash_map.assign("1gabro", "1igneous")
  hash_map.assign("1sadstone", "1sedimentary")
  hash_map.assign("1geiss", "1metamorphic")

  print (hash_map.retrieve("gabbro"))
  print (hash_map.retrieve("sandstone"))
  print (hash_map.retrieve("2gneis"))

if __name__ == "__main__":
    main()