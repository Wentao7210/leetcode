#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeElements(self, head, val: int):       
        dummyhead = ListNode(next=head) 
        #head is the node of the input listnode
        #so dummnyhead.next is node of the input listnode
        current = dummyhead
        while current.next: #check current.next is None or not. if not, then execute while loop
            if current.next.val == val: #if the first node's value is the needed-delete value
                current.next = current.next.next 
            else:
                current = current.next
        return dummyhead.next

# @lc code=end
head = [1,2,6,3,4,5,6]

### chatgpt4 version of annotations explanation
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:       
        # Create a dummy node that acts as a pre-head node of the input list
        dummyhead = ListNode(next=head)

        # Initialize the current node as dummyhead
        current = dummyhead

        # Traverse through the linked list until reaching the end (None)
        while current.next: # While there's a next node in the list

            # If the next node's value equals the target value
            if current.next.val == val: 
                # Skip the next node, effectively removing it from the list
                # This works because Python's garbage collection will remove objects not referred to
                current.next = current.next.next 
            else:
                # Move to the next node in the list
                current = current.next

        # Return the head of the updated list, note that we skip the dummyhead
        return dummyhead.next
