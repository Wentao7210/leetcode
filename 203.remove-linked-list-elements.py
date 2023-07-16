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