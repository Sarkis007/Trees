class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class binary_tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(data)

            else:
                self._insert(data, cur_node.right)
        else:
            print "Value already in tree!"

    def Inorder(self):
        print"\n"
        print "Inorder Binary Tree Traverse is: "
        if self.root != None:
            self._Inorder(self.root)

    def _Inorder(self, root):
        if root != None:
            self._Inorder(root.left)
            print str(root.data),
            self._Inorder(root.right)

    def Preorder(self):
        print"\n"
        print "Preorder Binary Tree Traverse is: "
        if self.root != None:
            self._Preorder(self.root)

    def _Preorder(self, root):
        if root != None:
            print str(root.data),
            self._Preorder(root.left)
            self._Preorder(root.right)

    def Postorder(self):
        print"\n"
        print "Postorder Binary Tree Traverse is: "
        if self.root != None:
            self._Postorder(self.root)

    def _Postorder(self, root):
        if root != None:
            self._Postorder(root.left)
            self._Postorder(root.right)
            print str(root.data),


def main():
    tree = binary_tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.Inorder()
    tree.Postorder()
    tree.Preorder()
main()

# insert function in main2 is from video you provided
def main2():
    tree = binary_tree()

    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)

    tree.Inorder()
    tree.Postorder()
    tree.Preorder()



