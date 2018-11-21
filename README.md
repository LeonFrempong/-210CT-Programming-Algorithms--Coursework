# 210CT-Coursework
class BinTreeNode(object):
 
    def __init__(self, value, parent=None):
        self.value=value
        self.left=None
        self.right=None
        self.parent=parent
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item, tree)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item, tree)
            else:
                tree_insert(tree.left,item, )
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item, tree)
            else:
                tree_insert(tree.right,item, )
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)

def BIN_TREE_FIND(tree,target):
    if tree.value==target or tree == None:
        return tree
    elif(tree.value>target):
            return BIN_TREE_FIND(tree.left,target)
    else:
        return BIN_TREE_FIND(tree.right,target)
    return 0

def COUNT_CHILDREN(n):
    count=None
    if n.left != None:
        count = count + 1
    if n.right != None:
        count = count + 1
    return count

def REMOVE_NODE(tree, value):


    node=BIN_TREE_FIND(tree, value)
    children=COUNT_CHILDREN(node)

    if children == 0: #if the node has no children, then we clear the data
        print(node.value)
        del(node)

    """
    if the node has only one child, we set the child's parent variable to the node
    above the node to be completed
    """
   #elif children == 1:








        #find a value with no children python binary

if __name__ == '__main__':
   #finds out if the value has no children
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
  REMOVE_NODE(t, 4 )
  in_order(t)


