# Problem solutions
    - array - easy problems
    - linked lists - easy problems
    - hash table - esay problems
# Linked lists
- ## Compared to array
    | Data Structure | Insertion/Deletion (Time Complexity) | Query (Time Complexity) | Suitable Use Cases                            |
    | -------------- | ----------------------------------- | ---------------------- | --------------------------------------------- |
    | Array          | O(n)                                | O(1)                   | Fixed data size, frequent queries, few changes |
    | Linked List    | O(1)                                | O(n)                   | Variable data size, frequent changes, few queries |
    
    - The length of the array is fixed when it is defined, and if you want to change the length of the array, you need to redefine a new array.
    - The length of the linked list can be variable, and can be dynamically added and deleted, suitable for data volume is not fixed, frequent addition and deletion, less query scenarios.
- ## Define a linked list
    Python:
    ```
    class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next
    ```