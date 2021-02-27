from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    # Create an empty array
    arr = []
    
    # Iterate through list of numbers from 0 to size-1 and append a Linked List object to the array
    for i in range(size):
      arr.append(LinkedList())
    
    # Return array
    return arr
      


  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    '''
    Calculates the index for a word based on the number of consonants in that word
    '''
    index = 0
    vowels = ["a", "e", "i", "o", "u"]
    # Iterate through the key
    for char in key:
      # If the character is not a vowel, then increment the index by 1
      if char not in vowels:
        index += 1
      # If the character is the letter 'y' and it is third letter after two consonants, then it is probably not a consonant
      if index == 2 and char == 'y':
        index -= 1
    # Return the index modulo array length
    return index % self.arr.count


  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    new_data = (key, value)
    arr_index = self.hash_func(key)
    ll = self.arr[arr_index]

    ll_index = ll.find(key)
    # Only append if the word does not already exist in the table
    if ll_index == -1:
      ll.append(new_data)
    # If the word does exist in the table, then increment its value by 1
    else:
      # Call update() method on LinkedList

  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for ll in self.arr:
      ll.print_nodes()
    # Change print_nodes() method in LinkedList.py to be reformatted
    # Do not print anything if linked list is empty


