# creating a simple script to test idea of stack as bst
#
# idea is to push to the bst and the keys are the order added
# always keep most recent as 1, when pushing, increment all other keys
# when popping, always remove 1 and decrement all keys.

# class encapsulating a bst
class Bst:
    def __init__(self, root):
        self.root = root

    # Inorder Traversal
    def inorder(self, root):
      if root:
        # Traverse left subtree
        self.inorder(root.left)
        
        # Visit node
        print("(", root.data, ",", root.order, ")", end=" ")
      
        
        # Traverse right subtree
        self.inorder(root.right)

    # tester code: is a bst if left is less than, right is larger
    def is_bst(self, root):
      if root:

        if root.left and root.left.order > root.order:
          return False
        if root.right and root.right.order < root.order:
          return False
        
        return self.is_bst(root.left) and self.is_bst(root.right)
      
      return True
  

    def insert(self, node):
      if not node: return
      if not self.root: 
        self.root = node
        return
      
      curr = self.root
      # parent = curr

      # you could order this way at risk of long skinny tree
      while curr:
        parent = curr
        if node.order > curr.order: 
          curr = curr.right
        elif node.order < curr.order:
          curr = curr.left

      if node.order < parent.order:
        parent.left = node
      else:
        parent.right = node

    # Get inorder successor (smallest in right subtree)
    def get_successor(self, curr):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

    # Delete a node with value x from BST
    def delete(self, root, o):
        if not root:
            return root

        if root.order > o:
            root.left = self.delete(root.left, o)
        elif root.order < o:
            root.right = self.delete(root.right, o)
        else: # found node to delete
            
            # node with 0 or 1  children
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            #  Node with 2 children
            succ = self.get_successor(root)
            root.data = succ.data
            root.order = succ.order
            root.right = self.delete(root.right, succ.order)

        return root


    # def delete(self, o):
    #   if not self.root: return
    #   print("what")

    #   curr = self.root
    #   parent = curr

    #   while o != curr.order:
    #     parent = curr
    #     if o < curr.order:
    #       curr = curr.left
    #     else:
    #       curr = curr.right

    #   if curr == self.root:
    #     self.root = None
    #   else:
    #     parent.left = None # this is a key part


    def push(self, node):
      self.increment_order(self.root)
      self.insert(node)
      
      
    
    def increment_order(self, root):
      if root:
        # Traverse left subtree
        self.increment_order(root.left)
        
        root.order = root.order + 1
        
        # Traverse right subtree
        self.increment_order(root.right)       
    
    def pop(self):
      self.root = self.delete(self.root, 1)
      self.decrement_order(self.root)

    def decrement_order(self, root):
      if root:
        # Traverse left subtree
        self.decrement_order(root.left)
        
        # Visit node
        root.order = root.order - 1
        
        # Traverse right subtree
        self.decrement_order(root.right)
    


    

# a node for the bst
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.order = 1 # note, always 1 to avoid problems








# Driver code

if __name__ == "__main__":
    # Build the tree
    
    bst = Bst(None)
    bst.inorder(bst.root) 
    print()

    bst.push(Node(27))
    bst.inorder(bst.root)
    print()

    bst.push(Node(32))
    bst.inorder(bst.root)
    print()

    bst.push(Node(34))
    bst.inorder(bst.root)
    print()

    bst.push(Node(4))
    bst.inorder(bst.root)
    print()


    bst.pop()
    bst.inorder(bst.root)
    print()

    bst.pop()
    bst.inorder(bst.root)
    print()

    bst.push(Node(-1))
    bst.inorder(bst.root)
    print()

    bst.pop()
    bst.inorder(bst.root)
    print()

    bst.pop()
    bst.inorder(bst.root)
    print()

    bst.pop()
    bst.inorder(bst.root)
    print()

    bst.pop()
    bst.inorder(bst.root)
    print()

    bst.push(Node(5))
    bst.inorder(bst.root)
    print()

    bst.push(Node(2))
    bst.inorder(bst.root)
    print()

    bst.pop()
    bst.inorder(bst.root)
    print()

    bst.push(Node(5))
    bst.inorder(bst.root)
    print()

    bst.pop()
    bst.inorder(bst.root)
    print()


    
   
    # 
    print(bst.is_bst(bst.root))