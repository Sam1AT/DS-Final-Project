class Node:
    def __init__(self , name , parent): # creating a node is from O(1)
        self.name = name
        self.children = []
        self.parent = parent
    
    def add_child(self , node): # adding a child is from O(1)
        if isinstance(node , Node):
            self.children.append(node)
            return 1
        
        return 0

   
