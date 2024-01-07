class Node:
    def __init__(self , name :str , parent = None): # creating a node is from O(1)
        self.name = name
        self.children = []
        self.parent = parent
    
    def add_child(self , node): # adding a child is from O(1)
        if isinstance(node , Node):
            self.children.append(node)
            return 1
        
        return 0

def create_tree(name): # O(1)
    root = Node(name)
    return root

# list of families
families = []


opt = 1
while opt:
    print('Hi , welcome to shajare name app! This app is designed by Sam and Mehrana \n Choose an option:')
    print('    1) Create a new tree')
    print('    2) Add to a existing tree')
    print('    0) Exit')
    
    otp = int(input())
    
    if opt == 1:
        fname , rname = input('give family name and owner by order and seperated by ,').split()
        root = create_tree(rname)
        families.append((fname , root))
        print('Family created ! ! !')
    
    print(families)