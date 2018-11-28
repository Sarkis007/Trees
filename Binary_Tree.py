class node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None

class binary_search_tree:
    def __init__(self):
        self.root=None

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root,0)

    def _get_height(self,temp_node,temp_height):
        if temp_node==None:
            return temp_height
        lh=self._get_height(temp_node.left,temp_height+1)
        rh=self._get_height(temp_node.right,temp_height+1)
        return max(lh,rh)

    def print_tree(self):
        y = 20
        x = " "
        temp = self.root

        while temp.left is not None and temp.right is not None:
            if temp == self.root:
                print y*x, temp.value
            y = y/2
            print y*x, str(temp.right.value), y*x, str(temp.left.value)
            temp = temp.right






def main():
    bt = binary_search_tree()
    n = node(1)
    n.left = node(2)
    n.right = node(2)
    n.right.right = node(3)
    n.right.left = node(3)
    n.left.left = node(4)
    n.left.right = node(4)
    bt.root = n
    bt.print_tree()
    print "height", bt.get_height()
main()