from charCount import CharCount
from bst import *

def main():
    """
    Create BSTs with TreeNodes that have CharCount elements
    """
    # a. First, create a Python list of 15 TreeNode objects
    #    each containing a CharCount object as its element 
    #    from this provided dictionary.
    #    You must use a loop to add these dictionary items 
    #    to a Python list. Print the list, so as to see the 
    #    order of the elements.

    char_dict = {'s': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 
                 'c': 3, 'a': 3, 'l': 3, 'i': 7, 'f': 1, 
                 'g': 1, 't': 1, 'x': 1, 'd': 1, 'o': 2}



    char_list = []

    for k, v in char_dict.items():

        temp = CharCount(k,v)

        char_list.append(temp)

    print("*** Character List ***")

    for node in char_list:

        print(node)

    # b. Insert these fifteen objects into a binary search tree, 
    #    manually. This means that you must link the nodes to 
    #    each other in the correct way so as to create a BST. 
     
    print()
    print("Manually created tree")

    root = TreeNode(char_list[0])
    root.right = TreeNode(char_list[1])
    root.left = TreeNode(char_list[2])
    root.left.left = TreeNode(char_list[3])
    root.left.right = TreeNode(char_list[4])
    root.left.left.left = TreeNode(char_list[5])
    root.left.left.left.left = TreeNode(char_list[6])
    root.left.left.right = TreeNode(char_list[7])
    root.left.left.right.left = TreeNode(char_list[8])
    root.left.left.right.left.left = TreeNode(char_list[9])
    root.left.left.right.left.left.right = TreeNode(char_list[10])
    root.right.left = TreeNode(char_list[11])
    root.right.right = TreeNode(char_list[12])
    root.left.left.left.right = TreeNode(char_list[13])
    root.left.left.right.right = TreeNode(char_list[14])
    ## Add your code here ##

    bst = BST(bst = root)

    # c. Use the BST you just created to construct a BST using 
    #    the BST class constructor.
    # d. Display this BST using each of the traversals:	
    #      in-order
    #      post_order
    #      pre-order

    # Mary: the traversals already do their own print
    print("*** IN_ORDER ***")
    #print(bst.inorder())
    bst.inorder()
    print()

    print("*** POST_ORDER ***")
    #print(bst.postorder())
    bst.postorder()
    print()

    print("*** PRE_ORDER***")
    #print(bst.preorder())
    bst.preorder()
    print()


    # e. Construct another BST by passing in the list of CharCount 
    #    objects to the BST constructor.
    # f. Display this BST using each of the traversals:	
    #      in-order
    #      post_order
    #      pre-order
    
    bstChar = BST(list_of_objects = char_list)

    print("*** BSTChar IN_ORDER ***")

    #print(bstChar.inorder())
    bst.inorder()
    print()
    
    print("*** BSTChar POST_ORDER ***")

    #print(bstChar.postorder())
    bst.postorder()
    print()
    
    print("*** BSTChar PRE_ORDER ***")

    #print(bstChar.preorder())
    bst.preorder()
    print()
    
    # h. Construct another BST by inserting each CharCount 
    #    object from the list created in Step a into the BST 
    # i. Display this BST using each of the traversals:	
    #      in-order
    #      post_order
    #      pre-order

    bst = BST()

    for item in char_list:

        bst.insert(item)
        
    print("Insert created tree")
    print("*** IN_ORDER ***")
    #print(bst.inorder())
    bst.inorder()
    print()
    
    print("*** POST_ORDER ***")
    #print(bst.postorder())
    bst.postorder()
    print()
    
    print("*** PRE_ORDER***")
    #print(bst.preorder())
    bst.preorder()
    print()


    # j. Use the BST iterator with the for each loop 
    #    to print each node

    print("Iterator displayed Tree")
    for node in bst:


        print(node)
        
        
main()
