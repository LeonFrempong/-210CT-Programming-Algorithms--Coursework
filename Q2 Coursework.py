class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

    englishNodes_file = open(r"EnglishNodes.txt", "r") # file used for th binary search
    print(englishNodes_file.read())

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
"""
pre_order function outputs the items by following the left tree, then right tree 
"""
def pre_order(tree):
    print(tree.value)
    if tree.left != None:
        pre_order(tree.left)
    if tree.right != None:
        pre_order(tree.right)
    
if __name__ == '__main__':
   
  t=tree_insert(None,'My');
  tree_insert(t,'name')
  tree_insert(t,'is')
  tree_insert(t,'Leon')
  tree_insert(t,'Frempong')
  tree_insert(t,'and')
  tree_insert(t,'i')
  tree_insert(t,'am')
  tree_insert(t,'nineteen')
  tree_insert(t,'years')
  tree_insert(t,'old')
  #in_order(t)
  pre_order(t)
