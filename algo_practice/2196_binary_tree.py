from dataclasses import dataclass
from collections import deque
from typing import Optional 

@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

def createBinaryTree(descriptions: list[list[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from descriptions and returns its root."""
    if not descriptions:
        return None

    nodes: dict[int, TreeNode] = {}
    children: set[int] = set()
    
    for parent_val, child_val, is_left in descriptions:
        # Create nodes if they don't exist
        if parent_val not in nodes:
            nodes[parent_val] = TreeNode(parent_val)
        if child_val not in nodes:
            nodes[child_val] = TreeNode(child_val)
        
        # Link the nodes
        parent_node = nodes[parent_val]
        child_node = nodes[child_val]
        
        if is_left == 1:
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        
        children.add(child_val)
        
    # Find the root
    root_node = None
    for node_val in nodes:
        if node_val not in children:
            root_node = nodes[node_val]
            break
            
    return root_node

def levelOrderTraversal(root: Optional[TreeNode]) -> list[int]:
    """Performs a level order traversal of the tree."""
    if not root:
        return []

    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

def main():
    descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    
    # 1. Build the tree
    root = createBinaryTree(descriptions)
    
    # 2. Perform Level Order Traversal
    if root:
        traversal_result = levelOrderTraversal(root)
        print(f"Input: descriptions = {descriptions}")
        print(f"Output: {traversal_result}")
        print("Expected: [50, 20, 80, 15, 17, 19]")
    else:
        print("Could not build a valid tree.")

if __name__ == "__main__":
    main()
