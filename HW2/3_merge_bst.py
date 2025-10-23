# Python3 code to implement the approach

# Class describing a node of tree
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

# Inorder Traversal
def print_inorder(root):
    if root:
        # Traverse left subtree
        print_inorder(root.left)
        
        # Visit node
        print(root.data,end=" ")
        
        # Traverse right subtree
        print_inorder(root.right)

# Inorder Traversal
def print_preorder(root):
    if root:
        # Visit node
        print(root.data,end=" ")

        # Traverse left subtree
        print_preorder(root.left)
        
        # Traverse right subtree
        print_preorder(root.right)

# Inorder collection of nodes
def collect_inorder(root, A, i):
    if root: # if not null
        (A, i) = collect_inorder(root.left, A, i)
        A[i] = root.data
        i += 1
        (A, i) = collect_inorder(root.right, A, i)
        print(A, ", ", i)
        # return (A, i)
    return (A, i)

# tester code: is a bst if left is less than, right is larger
def is_bst(root):
    if root:
        if root.left and root.left.data > root.data:
            return False
        if root.right and root.right.data < root.data:
            return False
        return is_bst(root.left) and is_bst(root.right)
    return True

# def inorder_merge(root, n, A, i):
#     print(i)
#     if root and i < n:
#       inorder_merge(root.left, n, A, i)
#       if (root and A[i] < root.data):
#         # insertion of new node
#         temp = root.left
#         new_node = Node(A[i])
#         root.left = new_node
#         if temp and temp.data > new_node.data:
#           new_node.right = temp
#         else:
#           new_node.left = temp
#         i += 1
#         while (i < n and A[i] < root.data):
#           if not new_node.right:
#             new_node.right = Node(A[i])
#             new_node = new_node.right
#           else:
#              #something
#              print("fuckup")
#           i += 1
#           # print(i)
#       i += 1
#       inorder_merge(root.right, n, A, i)

def merge(A, B):
    n = len(A)
    m = len(B)
    i = 0
    j = 0
    C = []

    while i < n and j < m:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        # elif A[i] > B[j]:
        else:
            C.append(B[j])
            j += 1
        # else: # they are equal, save one only, assume only distinct in bst
        #     C.append(A[i])
        #     i += 1
        #     j += 1

    while i < n:
        C.append(A[i])
        i += 1
    
    while j < m:
        C.append(B[j])
        j += 1
    return C

def create_BST(sorted_order, n):
    if n == 0: return None

    if n < 3: # special case for now
        if n == 2: # only 2 nodes
            BST_root = Node(sorted_order[0])
            BST_root.right = Node(sorted_order[1])
            return BST_root
        return Node(sorted_order[0])
    
    # if larger than 3
    # make a little subtree

    BST_root = Node(sorted_order[1])
    BST_root.left = Node(sorted_order[0])
    BST_root.right = Node(sorted_order[2])

    subtree = BST_root
    i = 3
    while (i < n):
        BST_root = Node(sorted_order[i])
        BST_root.left = subtree
        i += 1
        if i < n:
            BST_root.right = Node(sorted_order[i])
        subtree = BST_root
        i += 1

    return subtree

def better_create_BST(sorted_order, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    root = Node(sorted_order[mid])

    root.left = better_create_BST(sorted_order, start, mid - 1)
    root.right = better_create_BST(sorted_order, mid + 1, end)
    return root





if __name__ == "__main__":
    # Build the tree
    
    # BST 1
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
    BST2_root.right.right.left.left.right = Node(7) 
    
    # Function call
    # print("Inorder Traversal:",end="\n")
    # printInorder(BST1_root)
    # print()
    # printInorder(BST2_root)

    # run tester code on current bsts
    # print(is_bst(BST1_root))
    # print(is_bst(BST2_root))

    # get list of values in order
    A = [0] * 7
    (sortedBST1, _) = collect_inorder(BST1_root, A, 0)
    print(sortedBST1)

    B = [0] * 9
    (sortedBST2, _) = collect_inorder(BST2_root, B, 0)
    print(sortedBST2)

    mergedOrder = merge(sortedBST1, sortedBST2)
    print(mergedOrder)

    mergedBST = create_BST(mergedOrder, len(mergedOrder)) # OFFICIAL
    # mergedBST = create_BST([], 0) # fooling with edge cases
    print("INORDER")
    print_inorder(mergedBST)
    print()

    print("PREORDER")
    print_preorder(mergedBST)
    print()

    print(is_bst(mergedBST))

    mergedBST = better_create_BST(mergedOrder, 0, len(mergedOrder) - 1) # OFFICIAL
    # mergedBST = create_BST([], 0) # fooling with edge cases
    print("INORDER")
    print_inorder(mergedBST)
    print()

    print("PREORDER")
    print_preorder(mergedBST)
    print()

    print(is_bst(mergedBST))

    # # find correct subtree to append
    # i = 0
    # curr_node = BST2_root
    # while (curr_node and curr_node.right and sortedBST[0] > curr_node.data):
    #     curr_node = curr_node.right
    
    # print(curr_node.data)
    #  # TODO: go left as well
    # inorder_merge(curr_node, len(sortedBST), sortedBST, 0)
   
    # print_inorder(BST2_root)
