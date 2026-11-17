# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        level_queue=deque()
        level_queue.append(root)
        level_queue.append(None)
        avg_list=[]
        while level_queue[0] is not None:
            level_sum=0.0
            nodes=0
            while level_queue[0] is not None:
                node=level_queue.popleft()
                level_sum+=node.val
                nodes+=1
                if node.left is not None:
                    level_queue.append(node.left)
                if node.right is not None:
                    level_queue.append(node.right)
            level_queue.append(level_queue.popleft())
            avg_list.append(level_sum/nodes)
        return avg_list
        