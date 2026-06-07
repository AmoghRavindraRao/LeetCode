from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def bfs_dictionary(self, graph, start_node):
        nodes = {}
        nodes[start_node] = TreeNode(start_node)

        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()

            left_child, right_child = graph.get(current_node, [None, None])

            if left_child is not None:
                nodes[left_child] = TreeNode(left_child)
                nodes[current_node].left = nodes[left_child]
                queue.append(left_child)

            if right_child is not None:
                nodes[right_child] = TreeNode(right_child)
                nodes[current_node].right = nodes[right_child]
                queue.append(right_child)

        return nodes[start_node]

    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        data = {}
        keys = set()
        values = set()

        for parent, child, is_left in descriptions:
            if parent not in data:
                data[parent] = [None, None]

            keys.add(parent)
            values.add(child)

            if is_left == 1:
                data[parent][0] = child
            else:
                data[parent][1] = child

        start = list(keys - values)[0]

        return self.bfs_dictionary(data, start)