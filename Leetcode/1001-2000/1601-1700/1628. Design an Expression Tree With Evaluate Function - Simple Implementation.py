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


class ExpNode(Node):
    def __init__(self, val: str = '0', left: 'ExpNode' = None, right: 'ExpNode' = None) -> None:
        super().__init__()
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '/':
            return self.left.evaluate() // self.right.evaluate()
        else:
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
            if token in '+-*/':
                a = stack.pop()
                b = stack.pop()
                stack.append(ExpNode(token, b, a))
            else:
                stack.append(ExpNode(token))
        return stack[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
