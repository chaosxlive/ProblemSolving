# https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

import abc
from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    """
    This is the interface for the expression tree Node.
    You should not remove it, and you can define some classes to implement it.
    """
    @abstractmethod
    def evaluate(self) -> int:
        pass


class ExpNode(Node, ABC):
    def __init__(self, val: str = '0', left: 'ExpNode' = None, right: 'ExpNode' = None) -> None:
        super().__init__()
        self.val = val
        self.left = left
        self.right = right


class AddNode(ExpNode):
    def __init__(self, left: 'ExpNode' = None, right: 'ExpNode' = None) -> None:
        super().__init__('', left, right)

    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()


class SubNode(ExpNode):
    def __init__(self, left: 'ExpNode' = None, right: 'ExpNode' = None) -> None:
        super().__init__('', left, right)

    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()


class MulNode(ExpNode):
    def __init__(self, left: 'ExpNode' = None, right: 'ExpNode' = None) -> None:
        super().__init__('', left, right)

    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()


class DivNode(ExpNode):
    def __init__(self, left: 'ExpNode' = None, right: 'ExpNode' = None) -> None:
        super().__init__('', left, right)

    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()


class NumNode(ExpNode):
    def __init__(self, val: str = '') -> None:
        super().__init__(val)

    def evaluate(self) -> int:
        return int(self.val)


class TreeBuilder(object):
    """    
    This is the TreeBuilder class.
    You can treat it as the driver code that takes the postinfix input
    and returns the expression tree represnting it as a Node.
    """

    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for token in postfix:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(AddNode(b, a))
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(SubNode(b, a))
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(MulNode(b, a))
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(DivNode(b, a))
            else:
                stack.append(NumNode(token))
        return stack[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
