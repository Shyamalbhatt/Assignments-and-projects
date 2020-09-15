class Node:
   def __init__(self, data, next = None, prev = None):
      self.data = data
      self.next = next
      self.prev = prev

class doubly_linked_list:

   def __init__(self):
      self.head = None

# Adding data elements		
   def push(self, n):
      New_n = Node(n)
      New_n.next = self.head
      if self.head is not None:
         self.head.prev = New_n
      self.head = New_n

# Print the Doubly Linked list		
   def listprint(self, node):
      while (node is not None):
         print(node.data)
         last = node
         node = node.next

d = doubly_linked_list()
d.push(12)
d.push(8)
d.push(62)
d.listprint(d.head)
