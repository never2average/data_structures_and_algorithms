class node:
    def __init__(self,value=None):
            self.value=value
            self.left_child=None
            self.right_child=None
            self.parent=None

class binary_search_tree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root==None:
                self.root=node(value)
        else:
                self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value<cur_node.value:
                if cur_node.left_child==None:
                        cur_node.left_child=node(value)
                        cur_node.left_child.parent=cur_node # set parent
                else:
                        self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
                if cur_node.right_child==None:
                        cur_node.right_child=node(value)
                        cur_node.right_child.parent=cur_node # set parent
                else:
                        self._insert(value,cur_node.right_child)

    def print_tree(self):
        if self.root!=None:
                self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
                self._print_tree(cur_node.left_child)
                print (str(cur_node.value))
                self._print_tree(cur_node.right_child)

    def height(self):
        if self.root!=None:
                return self._height(self.root,0)
        else:
                    return 0

    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

tree=binary_search_tree()
arr_size = int(input())
arr = list(map(int, input().rstrip().split()))
for i in arr:
    tree.insert(i)

tree.print_tree()
print(tree.height()-1)
