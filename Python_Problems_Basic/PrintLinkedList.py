#You are given the head of a singly linked list. Return an array containing the values of the nodes.


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def printList(self, head):
        # code here
        res = []
        curr = head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res


# ---- TESTING ----
# Create linked list: 1 -> 4 -> 3
head = Node(1)
head.next = Node(4)
head.next.next = Node(3)

sol = Solution()
print(sol.printList(head))