#internal implementation of set is BST

# insertion and access elemrn in 0(n)
#BFS
#DFS --> Inorder -> (left, root, right) , preorder --> root, left, right, post order--> left, right, root

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)
    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements +=self.right.inorder_traversal()
        return elements
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    numbers = [17,3,5,2,89,23,32,3]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(2))
    print(numbers_tree.search(23))
    print(numbers_tree.search(233))

    print(numbers_tree.inorder_traversal()) # sort
