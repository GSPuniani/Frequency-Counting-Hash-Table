from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self, item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:
      # if current.data == item: if item is not tuple of key and value
      if current.data == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1


  def update(self, item, index):
    """
    Pass in an item and its index to increment its value by 1.
    This method is only called if the item is known to already exist in the linked list.
    """

    # Iterate through linked list until index is reached
    current = self.head
    i = 0
    while i < index:
      current = current.next
      i += 1

    # Increment the value by 1 
    current.data[item] += 1


  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head

    for i in range(self.length()):
      print(f'{current.data}: {current.data}')
      current = current.next