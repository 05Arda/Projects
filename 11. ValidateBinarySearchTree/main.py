class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ValidateTree:
    def isValidBST(self, root):
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, tree, min_val, max_val):
        # Base case
        if tree is None:
            return True
        if tree.value < min_val or tree.value >= max_val:
            return False
        # Recursive
        return self.validate(tree.left, min_val, tree.value) and self.validate(tree.right, tree.value, max_val)

if __name__ == '__main__':
    tree = BinaryTree(2)
    tree.left = BinaryTree(1)
    tree.right = BinaryTree(3)
    print(ValidateTree().isValidBST(tree)) # True

    tree = BinaryTree(5)
    tree.left = BinaryTree(1)
    tree.right = BinaryTree(4)
    tree.right.left = BinaryTree(3)
    tree.right.right = BinaryTree(6)
    print(ValidateTree().isValidBST(tree)) # False