class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data)
def Preorder(root):
    if root:
        print(root.data)
        Preorder(root.left)
        Preorder(root.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print "Preorder Binary Tree Traverse is: "
    Preorder(root)

    print "Inorder Binary Tree Traverse is: "
    Inorder(root)

    print "Postorder Binary Tree Traverse is: "
    Postorder(root)
main()