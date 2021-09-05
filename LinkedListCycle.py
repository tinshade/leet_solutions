class Solution:
	def hasCycle(self, head):
		fast,slow = head,head
		while fast and slow and fast.next:
			fast = fast.next.next
			slow = slow.next
			if slow == fast:
				return True
		return False