# Python3 code to implement the approach

# Class describing a node of tree
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

# Inorder Traversal
def printInorder(root):
    if root:
        # Traverse left subtree
        printInorder(root.left)
        
        # Visit node
        print(root.data,end=" ")
        
        # Traverse right subtree
        printInorder(root.right)

# Inorder collection of nodes
def collect_inorder(root, A):
    if root: # if not null
        collect_inorder(root.left, A)
        A.append(root.data)
        collect_inorder(root.right, A)
        return A

# tester code: is a bst if left is less than, right is larger
def is_bst(root):
    if root:
        if root.left and root.left.data > root.data:
            return False
        if root.right and root.right.data < root.data:
            return False
        return is_bst(root.left) and is_bst(root.right)
    return True

def inorder_merge(root, n, A, i):
    print(i)
    if root and i < n:
      inorder_merge(root.left, n, A, i)

    
      if (root and A[i] < root.data):
        # insertion of new node
        temp = root.left
        new_node = Node(A[i])
        root.left = new_node
        if temp and temp.data > new_node.data:
          new_node.right = temp
        else:
          new_node.left = temp
        i += 1
        while (i < n and A[i] < root.data):
          if not new_node.right:
            new_node.right = Node(A[i])
            new_node = new_node.right
          else:
             #something
             print("fuckup")
          i += 1
          # print(i)

      i += 1
          
      

      inorder_merge(root.right, n, A, i)

# Driver code

if __name__ == "__main__":
    # Build the tree
    
    # BST 2
    BST1_root = Node(6)
    BST1_root.left = Node(4)
    BST1_root.left.right = Node(5)
    BST1_root.right = Node(8)
    BST1_root.right.left = Node(7)
    BST1_root.right.right = Node(10)
    BST1_root.right.right.left = Node(9)
    
    # BST 2
    BST2_root = Node(1)
    BST2_root.left = Node(0)
    BST2_root.right = Node(6)
    BST2_root.right.right = Node(11)
    BST2_root.right.left = Node(5)
    BST2_root.right.left.left = Node(4)
    BST2_root.right.right.left = Node(9)
    BST2_root.right.right.left.left = Node(7) 
    
    # Function call
    # print("Inorder Traversal:",end="\n")
    # printInorder(BST1_root)
    # print()
    # printInorder(BST2_root)

    # run tester code on current bsts
    # print(is_bst(BST1_root))
    # print(is_bst(BST2_root))

    # get list of values in order
    sortedBST = collect_inorder(BST1_root, [])
    print(sortedBST)

    # find correct subtree to append
    i = 0
    curr_node = BST2_root
    while (curr_node and curr_node.right and sortedBST[0] > curr_node.data):
        curr_node = curr_node.right
    
    print(curr_node.data)
     # TODO: go left as well
    inorder_merge(curr_node, len(sortedBST), sortedBST, 0)
   
    printInorder(BST2_root)


    # This code is contributed by ajaymakvana.