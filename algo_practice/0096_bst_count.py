def numTrees(n: int) -> int:
    """
    Calculates the number of structurally unique Binary Search Trees (BSTs)
    that can be formed using n nodes with values from 1 to n.

    This problem is a classic application of Dynamic Programming and the Catalan numbers.

    Args:
        n: The number of nodes (from 1 to n).

    Returns:
        The total number of unique BSTs.
    """
    
    # dp[i] will store the number of unique BSTs with i nodes.
    # Initialize dp array with size n + 1, all zeros.
    dp = [0] * (n + 1)
    
    # Base cases:
    # There is 1 way to form an empty tree (0 nodes).
    dp[0] = 1 
    
    # There is 1 way to form a single-node tree (1 node).
    # This line should only execute if n is at least 1, to prevent IndexError for n=0.
    if n >= 1: 
        dp[1] = 1 
    
    # Fill the dp array using the Catalan number recurrence relation.
    # For i nodes, we iterate through all possible roots (j from 1 to i).
    # If j is the root:
    #   - The left subtree will have (j - 1) nodes.
    #   - The right subtree will have (i - j) nodes.
    # The number of ways to form BSTs with j as root is dp[j-1] * dp[i-j].
    # We sum these possibilities for all possible roots j.
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
            
    # The result for n nodes is stored at dp[n].
    return dp[n]

# Example Usage (for testing purposes)
def main():
    print(f"Number of unique BSTs for n = 0: {numTrees(0)}") # Expected: 1
    print(f"Number of unique BSTs for n = 1: {numTrees(1)}") # Expected: 1
    print(f"Number of unique BSTs for n = 2: {numTrees(2)}") # Expected: 2
    print(f"Number of unique BSTs for n = 3: {numTrees(3)}") # Expected: 5
    print(f"Number of unique BSTs for n = 4: {numTrees(4)}") # Expected: 14
    print(f"Number of unique BSTs for n = 5: {numTrees(5)}") # Expected: 42

if __name__ == "__main__":
    main()
