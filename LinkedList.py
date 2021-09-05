class Node:
	def __init__(self,data=None):
		'''
			Singly Node class
		'''
		self.data=data
		self.next=None


class LinkedList:
	def __init__(self):
		self.head = Node() #Not indexed, placeholder for the first element

	def append(self, data):
		'''
			Appends data to the end of the list
		'''
		new_node = Node(data)
		curr = self.head
		#Looking for the last element by traversing through the list
		while curr.next != None:
			curr = curr.next
		curr.next = new_node #curr is now the last and curr.next is empty, so we fill it with new_node

	def length(self):
		'''
			Returns the length of the list
		'''
		curr = self.head
		total = 0
		while curr.next != None:
			total +=1
			curr = curr.next
		return total

	def display(self):
		'''
			Returns the current contents in the list
		'''
		data = []
		curr_node = self.head
		while curr_node.next != None:
			curr_node = curr_node.next
			data.append(curr_node.data)
		return data

	def get(self,index):
		'''
			Returns element at a given index
		'''
		if index >=self.length():
			return "Index of Out Of Range"
		curr_index,curr_node = 0, self.head
		while True:
			curr_node=curr_node.next
			if curr_index==index:
				return curr_node.data
			curr_index+=1

	def erase(self,index):
		'''
			Deletes an element at a given index
		'''
		if index >=self.length():
			return "Index Out Of Range"
		curr_index, curr_node = 0, self.head
		while True:
			last_node = curr_node #Book keeping for deleting middle elements
			curr_node = curr_node.next
			if curr_index == index:
				last_node.next = curr_node.next
				return
			curr_index+=1

	def pop(self,index):
		'''
			Pops an element at a given index
		'''
		if index >=self.length():
			return "Index Out Of Range"
		curr_index, curr_node = 0, self.head
		while True:
			last_node = curr_node #Book keeping for deleting middle elements
			curr_node = curr_node.next
			if curr_index == index:
				last_node.next = curr_node.next
				return curr_node.data
			curr_index+=1


linkedList = LinkedList()
print(linkedList.display()) #[]
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
print(linkedList.display()) #[1,2,3]
print(linkedList.get(10)) #Error
print(linkedList.get(1)) #2
linkedList.erase(1)
print(linkedList.display())
print(linkedList.pop(1))


