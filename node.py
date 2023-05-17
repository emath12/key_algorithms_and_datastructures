class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return f"""
        {self.right}
        {self.left}
        {self.value}
        """