# https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next


class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        ptr1 = poly1
        ptr2 = poly2
        result = PolyNode()
        ptr = result
        while ptr1 is not None and ptr2 is not None:
            if ptr1.power > ptr2.power:
                newNode = PolyNode(x=ptr1.coefficient, y=ptr1.power)
                ptr.next = newNode
                ptr = ptr.next
                ptr1 = ptr1.next
            elif ptr1.power < ptr2.power:
                newNode = PolyNode(x=ptr2.coefficient, y=ptr2.power)
                ptr.next = newNode
                ptr = ptr.next
                ptr2 = ptr2.next
            else:
                if ptr1.coefficient + ptr2.coefficient != 0:
                    newNode = PolyNode(x=ptr1.coefficient + ptr2.coefficient, y=ptr1.power)
                    ptr.next = newNode
                    ptr = ptr.next
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        while ptr1 is not None:
            newNode = PolyNode(x=ptr1.coefficient, y=ptr1.power)
            ptr.next = newNode
            ptr = ptr.next
            ptr1 = ptr1.next
        while ptr2 is not None:
            newNode = PolyNode(x=ptr2.coefficient, y=ptr2.power)
            ptr.next = newNode
            ptr = ptr.next
            ptr2 = ptr2.next
        return result.next