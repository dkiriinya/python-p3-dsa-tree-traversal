class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Helper function for depth-first traversal
        def dfs(node):
            # Check if the current node matches the given id
            if node and node.get('id') == id:
                return node

            # Recursively search children
            for child in node.get('children', []):
                result = dfs(child)
                if result:
                    return result

            return None

        # Start the traversal from the root
        return dfs(self.root)
