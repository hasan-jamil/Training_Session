class LinkedList:
	def __init__(self, value):
		self.value = value 
		self.next = None 


def removeDuplicatesFromLinkedList(linkedlist):      # O(n) time | O(1) space 
	currentNode = linkedlist
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
			nextDistinctNode = nextDistinctNode.next

		currentNode.next = nextDistinctNode
		currentNode = nextDistinctNode

	return linkedlist