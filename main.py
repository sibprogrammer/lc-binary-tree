class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def traverse(root: TreeNode, level: int) -> str:
            if not root:
                return ''
            prefix = '  ' * level
            return f'{prefix}({root.val})\n' + traverse(root.left, level + 1) + traverse(root.right, level + 1)
        return str.rstrip(traverse(self, 0))


def build_complete_tree(arr: list[int], i: int, n: int) -> TreeNode | None:
    """
    >>> arr = [1, 2, 3]
    >>> build_complete_tree(arr, 0, len(arr))
    (1)
      (2)
      (3)
    """
    root = None
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_complete_tree(arr, 2 * i + 1, n)
        root.right = build_complete_tree(arr, 2 * i + 2, n)
    return root


def build_tree(arr: list[int]) -> TreeNode | None:
    """
    >>> arr = [1, 2, 3, None, 4, None, None, 5, 6, None, 7]
    >>> build_tree(arr)
    (1)
      (2)
        (4)
          (5)
            (7)
          (6)
      (3)
    """
    if len(arr) == 0:
        return None

    nodes = []

    val = arr.pop(0)
    root = TreeNode(val)
    nodes.append(root)

    while len(arr) > 0:
        curr = nodes.pop(0)

        left_val = arr.pop(0)
        if left_val is not None:
            curr.left = TreeNode(left_val)
            nodes.append(curr.left)

        if len(arr) > 0:
            right_val = arr.pop(0)
            if right_val is not None:
                curr.right = TreeNode(right_val)
                nodes.append(curr.right)

    return root


if __name__ == '__main__':
    import doctest
    doctest.testmod()
