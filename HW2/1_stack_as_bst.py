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
        print(root.data,end=" ")
        
        # Traverse right subtree
        self.inorder(root.right)

    # tester code: is a bst if left is less than, right is larger
    def is_bst(self, root):
      if root:

        if root.left and root.left.data > root.data:
          return False
        if root.right and root.right.data < root.data:
          return False
        
        return self.is_bst(root.left) and self.is_bst(root.right)
      
      return True
  
    def insert(self, node):
      if not node: return
      if not self.root: 
        self.root = node
        return
      
      curr = self.root
      parent = curr

      # you could order this way at risk of long skinny tree
      while curr:
        parent = curr
        if node.order >= curr.order: # allowing for equivalence
          curr = curr.right
        elif node.order < curr.order:
          curr = curr.left

      if node.order < parent.order:
        parent.left = node
      else:
        parent.right = node

      # while curr:
      #   parent = curr
      #   if node.data >= curr.data: # allowing for equivalence
      #     curr = curr.right
      #   elif node.data < curr.data:
      #     curr = curr.left

      # if node.data < parent.data:
      #   parent.left = node
      # else:
      #   parent.right = node

    def delete(self, o):
      if not self.root: return

      curr = self.root
      parent = curr

      while o != curr.order:
        parent = curr
        if o < curr.order:
          curr = curr.left
        else:
          curr = curr.right

      curr = self.smallest_in_right(curr, parent)
      
    def smallest_in_right(self, to_delete, parent):
      replace = to_delete.right
      
      # if a non null to right of node to delete
      if replace: 
        # find smallest non null in left side or until fall off tree
        while replace.left:
          replace = replace.left
        return replace
      
      # no node to the right, so see if theres a left child
      replace = to_delete.left
      if replace:
        if parent.left == to_delete:
          parent.left = replace
        else:
          parent.right = replace
        return replace

      return None


    def push(self, node):
      self.insert(node)
      self.increment_order(node, self.root)
    
    def increment_order(self, node, root):
      if root:
        # Traverse left subtree
        self.increment_order(node, root.left)
        
        # Visit node
        if root != node:
          print(root.data,end=" ")
          root.order = root.order + 1
        
        # Traverse right subtree
        self.increment_order(node, root.right)       
    
    def pop(self):
      self.delete(1)
      self.decrement_order(self, self.root)

    def decrement_order(self, root):
      if root:
        # Traverse left subtree
        self.decrement_order(root.left)
        
        # Visit node
        root.order -= 1
        print(root.data,end=" ")
        
        # Traverse right subtree
        self.decrement_order(root.right)
    


    

# Class describing a node of tree
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v
        self.order = 1 # note, always 1 to avoid problems








# Driver code

if __name__ == "__main__":
    # Build the tree
    
    bst = Bst(None)
    bst.push(Node(27))
    bst.push(Node(32))
    bst.push(Node(34))

    
   
    bst.inorder(bst.root)
    print(bst.is_bst(bst.root))