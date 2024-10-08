from typing import Optional
# Main. This is where you test the solution class that was generated by calling on it.
def main():
    print("Hello World!")
    root_list = [1,None,2,None,3]
    root = build_tree(root_list)
    print_tree(root)
    p = TreeNode(2)
    q = TreeNode(8)
    solution_obj = Solution
    retVal = solution_obj.isBalanced(solution_obj, root)
    print(retVal)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            print(node.val, end=' ')
            queue.append(node.left)
            queue.append(node.right)
        else:
            print(None, end=' ')

def build_tree(root_list):
    if not root_list:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in root_list]
    root = nodes[0]
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        node = queue.pop(0)

        if node:
            node.left = nodes[i]
            i += 1
            queue.append(node.left)

            if i < len(nodes):
                node.right = nodes[i]
                i += 1
                queue.append(node.right)

    return root

# TODO: change the name of the defined method "something" to the problem name
# TODO: Write out the solution for the problem, writing out the class and method
# TODO: ensure the return value and parameters match the problem

# Wacky definition. So for each node, the left and right subtree differ by at most one.
# Easy solution I can think of: go left until full depth, go right until full depth?
# return (lenLeft - lenRight <= 1) or (lenRight - lenLeft <=1) (too lazy to do math.abs)
# Okay good idea, wrong problem. The issue here is that ^ that definition has to apply to ALL
# nodes. Aka: recursion...
# Writing out idea...

# Pseudo code:
# Issue with previous algo: taking height of entire left subtree and right subtree of the root node doesnt work
# because there are 12 edge cases where you can have the overall root have a balanced tree but each node doesnt.
# THUS, we repackage the recursive height counting method to be used now for ALL node. And then we go through
# each node of the tree within the while loop 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root == None):
            return True
        
        stack = []
        stack.append(root)

        def lengthoftree(root: Optional[TreeNode], length) -> bool:
            if (root == None):
                return length-1
            else:
                sizeLeft = lengthoftree(root.left, length+1)
                sizeRight = lengthoftree(root.right, length+1)

                if (sizeLeft > sizeRight):
                    return sizeLeft
                else:
                    return sizeRight
            
            return length
        
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            

        lenLeft = lengthoftree(traverserleft, 1)
        lenRight = lengthoftree(traverserright, 1)
        print("TEST")
        print(lenLeft)
        print(lenRight)
        
        diff = lenLeft - lenRight
        if (diff < 0):
            diff = diff * -1
        return diff <= 1


# If this is the file that is running "__name__ == __main__",
# run the main() function
if __name__ == "__main__":
    main()

# Problem description:
# Given a binary tree, determine if it is
# height-balanced
# .

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:

# Input: root = []
# Output: true

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 5000].
#     -104 <= Node.val <= 104


