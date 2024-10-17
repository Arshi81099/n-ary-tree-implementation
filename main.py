from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def createTree(self, values):
        """Create an N-ary tree from a list of values."""
        if not values or values[0] is None:
            return None

        root = Node(values[0])
        queue = [root]
        i = 1 if values[1] is not None else 2  # Start index for children

        while i < len(values):
            node = queue.pop(0)

            # Add children to the current node
            while i < len(values) and values[i] is not None:
                child = Node(values[i])
                node.children.append(child)
                queue.append(child)
                i += 1

            # Skip None values
            if i < len(values) and values[i] is None:
                i += 1

        return root

    def print_tree(self, root, level=0):
        """Print the tree in a structured format."""
        if not root:
            return
        print("  " * level + str(root.val))
        for child in root.children:
            self.print_tree(child, level + 1)

    def levelOrder(self, root):
        """Return the level order traversal of the tree as a list of lists."""
        levels = defaultdict(list)

        def dfs(node, depth):
            levels[depth].append(node.val)
            for child in node.children:
                dfs(child, depth + 1)

        if root:
            dfs(root, 0)

        return [levels[i] for i in sorted(levels.keys())]

    def postorder(self, root):
        """Return the postorder traversal of the tree as a list."""
        if not root:
            return []

        res = []

        def dfs(node):
            for child in node.children:
                dfs(child)
            res.append(node.val)

        dfs(root)
        return res

if __name__ == "__main__":
    solution = Solution()
    values = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
    root = solution.createTree(values)
    print("Tree structure:")
    solution.print_tree(root)
    print("\nPostorder traversal:", solution.postorder(root))
    print("Level order traversal:", solution.levelOrder(root))
