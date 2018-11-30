"""
Title:Binary Search Tree
Author: Hintea, D
Date: 2018
Availability: http://moodle.coventry.ac.uk 
"""
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

def pre_order(tree): # this function first outputs the item, follows the left then the right tree
    print(tree.value) # prints the head node
    if (tree.left != None):
        pre_order(tree.left)#constantly goes left side when there are values 
    if (tree.right != None):
        pre_order(tree.right)#constantly goes right where are values 


def FileOpen(): # this function opens and reads the file
    openf = open("EnglishNodes.txt" ,"r") 
    openf = openf.read().upper().split() #opens the file with capital letter and splits the words
    return openf

Openfile = FileOpen()

t = tree_insert(None,Openfile[0])
for i in range(len(Openfile)):#finds the lengths of the file
      tree_insert(t,Openfile[i])#calls the function 
pre_order(t) # prints in pre_order 


    

