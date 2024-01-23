class Node:
    def __init__(self , name :str , parent = None): # creating a node is from O(1)
        self.name = name
        self.children = []
        self.parent = parent
    
    def add_child(self , node): # adding a child is from O(1)
            child = Node(node , self)
            self.children.append(child)

    def __str__(self) -> str:
        return self.name

                
                
def create_tree(name): # O(1)
    root = Node(name)
    return root

def show_families(f):
    for x in f:
        print(x[0])
        
def find_family(families , fname):
    for x in families:
        if x[0] == fname:
            return x[1]
    
    return None

def show_family_members(family):
    visited = set()
    queue = [family]
    c = 1
    while queue:
        current_node = queue.pop(0)
        print(f'{c}) {current_node.name}') 
        c += 1 
        visited.add(current_node)

        for child in current_node.children:
            if child not in visited and child not in queue:
                queue.append(child)


def find_family_member(family  ,fname):
    
    visited = set()
    queue = [family]

    while queue:
        current_node = queue.pop(0)

        if current_node.name == fname:
            return current_node
        
        visited.add(current_node)

        for child in current_node.children:
            if child not in visited and child not in queue:
                queue.append(child)

    return None

def perform_delete(node):
    parent = node.parent
    
    if not parent:
        print('Cant delete sahab hamatoon')
        return None

    parent.children.remove(node)

    del node


#################################################################################################################



families = []

print('Hi , welcome to shajare name app! This app is designed by Sam and Mehrana \n Choose an option:')

opt = 1
while opt:
    print('    1) Create a new tree')
    print('    2) Add to a existing tree')
    print('    3) Delete from a tree')

    print('    0) Exit')
    
    opt = int(input())
    
    if opt == 1:
        fname , rname = input('give family name and owner by order and seperated by ,').split()
        root = create_tree(rname)
        families.append((fname , root))
        print('Family created ! ! !')
    
    elif opt == 2:
        print('choose a family: ')
        show_families(families)
        fname = input()
        selected_family = find_family(families  ,fname)
        
        if not selected_family:
            print('! ! ! not found ! ! !')
            continue
        
        print('choose a parent: ')
        show_family_members(selected_family)
        pname = input()
        selected_parent = find_family_member(selected_family , pname)

        if not selected_parent:
            print('! ! ! not found ! ! !')
            continue       
        
        print('Select a name for the child.')
        name = input()
        selected_parent.add_child(name)
        
        print('Created ! ! !')
        
    elif opt == 3:
        print('choose a family: ')
        show_families(families)
        fname = input()
        selected_family = find_family(families  ,fname)
        
        if not selected_family:
            print('! ! ! not found ! ! !')
            continue
        
        print('choose a member: ')
        show_family_members(selected_family)
        pname = input()
        selected_parent = find_family_member(selected_family , pname)

        if not selected_parent:
            print('! ! ! not found ! ! !')
            continue  
        
        perform_delete(selected_parent)
        
        print('Deleted ! ! !')
   

    print(families)