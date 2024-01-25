import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph, node, pos=None, x=0, y=0, layer_height=1, layer_width=1):
    if pos is None:
        pos = {node: (x, y)}

    if node.children:
        dx = layer_width / len(node.children)
        next_x = x - layer_width / 2 + dx / 2

        for child in node.children:
            pos[child] = (next_x, y - layer_height)
            graph.add_edge(node, child)
            next_x += dx
            add_edges(graph, child, pos, next_x - dx / 2, y - layer_height, layer_height, layer_width)

def plot_tree(root):
    graph = nx.Graph()
    pos = {root: (0, 0)}
    add_edges(graph, root, pos)

    labels = {node: node.name for node in graph.nodes()}
    nx.draw(graph, pos, labels=labels, with_labels=True, node_size=700, node_color='cyan', font_size=8, font_color='black' , font_weight='bold', edge_color='gray',)
    plt.show()

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

from hash import sha256

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

def check_parent(m1 , m2):
    itr = m1
    while itr:
        if itr.name == m2.name:
            return 1
        itr = itr.parent
        
    itr = m2
    while itr:
        if itr.name == m1.name:
            return 1
        itr = itr.parent

    return 0

def find_common_parent(m1 , m2):
    m1_parrent_list = []
    itr = m1
    while itr:
        m1_parrent_list.append(itr.name)
        itr = itr.parent    
    
    m2_parrent_list = []
    itr = m2
    while itr:
        m2_parrent_list.append(itr.name)
        itr = itr.parent   
        
    last_common = m1_parrent_list[-1]

    
    while m1_parrent_list[-1] == m2_parrent_list[-1]:
        last_common =  m1_parrent_list[-1]
        

        m1_parrent_list.pop()
        m2_parrent_list.pop()
        

        
        if not m1_parrent_list or not m2_parrent_list:
            break
    
    return last_common

def find_node_with_longest_path(node):
    if not node.children:
        return 0 

    m = 0
    
    for c in node.children:
        m = max(m , 1 + find_node_with_longest_path(c))

    return m

def height(node):
    
    if node.children == []:
        return [1,[node.name]]
    
    ans =  max([height(child) for child in node.children], key=lambda x : x[0]) 
    
    ans[1].append(node.name)
    ans[0] = 1 + ans[0]
    
    return  ans

def diameter(root):
    if root.children == []:
        return [1 , [root.name]]

    heights = [height(child) for child in root.children]

    diameters = [diameter(child) for child in root.children]

    max_in_this_root_maxes = sorted(heights, reverse=True , key=lambda x : x[0])[:2]
    
    if len(heights) == 1:
        max_in_this_root = [max_in_this_root_maxes[0][0] + 1, max_in_this_root_maxes[0][1] + [root.name]]  
    else:     
        max_in_this_root = [max_in_this_root_maxes[0][0] + max_in_this_root_maxes[1][0] + 1, max_in_this_root_maxes[0][1] + [root.name] +max_in_this_root_maxes[1][1]]
    
    max_in_other_roots = max(diameters, key=lambda x : x[0])
    
    return max(max_in_this_root , max_in_other_roots , key=lambda x : x[0])

#################################################################################################################



selected_family = Node(sha256('chele'))

print('Hi , welcome to shajare name app! This app is designed by Sam and Mehrana \n Choose an option:')

opt = 1
while opt:
    print('    1) Add to the tree')
    print('    2) Delete from the tree')
    print('    3) check being parent')
    print('    4) check being siblings')
    print('    5) check being second-level family')
    print('    6) find nearest common parent')
    print('    7) find great greatest child')
    print('    8) find the diameter of the tree ')
    print('    9) Show tree')
    print('    0) Exit')
    
    opt = int(input())

    
    if opt == 1:

        
        print('choose a parent: ')
        show_family_members(selected_family)
        pname = input()
        pname = sha256(pname)
        selected_parent = find_family_member(selected_family , pname)

        if not selected_parent:
            print('! ! ! not found ! ! !')
            continue       
        
        print('Select a name for the child.')
        name = input()
        name = sha256(name)

        selected_parent.add_child(name)
        
        print('Created ! ! !')
        
    elif opt == 2:

        
        print('choose a member: ')
        show_family_members(selected_family)
        pname = input()
        pname = sha256(pname)
        selected_parent = find_family_member(selected_family , pname)

        if not selected_parent:
            print('! ! ! not found ! ! !')
            continue  
        
        perform_delete(selected_parent)
        
        print('Deleted ! ! !')
   

    elif opt == 3:
        
        print('choose members: ')
        show_family_members(selected_family)
        name1 = input()
        name2 = input()

        name1 = sha256(name1)
        name2 = sha256(name2)

        
        selected_member_1 = find_family_member(selected_family , name1)        
        selected_member_2 = find_family_member(selected_family , name2)        
        
        if not (selected_member_1 and selected_member_2):
            print('! ! ! not found ! ! !')
            continue  
                
        if check_parent(selected_member_1 , selected_member_2) : 
            print('YES')
        else:
            print('NO')           

    elif opt == 4:

        
        print('choose members: ')
        show_family_members(selected_family)
        name1 = input()
        name2 = input()
        
        name1 = sha256(name1)
        name2 = sha256(name2)

        
        selected_member_1 = find_family_member(selected_family , name1)        
        selected_member_2 = find_family_member(selected_family , name2)        
        
        if not (selected_member_1 and selected_member_2):
            print('! ! ! not found ! ! !')
            continue  

        if not (selected_member_1.parent.name and   selected_member_2.parent.name):
            print('! ! ! one of them is rais ! ! !')
            continue         

        if selected_member_1.parent.name ==   selected_member_2.parent.name: 
            print('YES')
        else:
            print('NO')   

    elif opt == 5:

        print('choose members: ')
        show_family_members(selected_family)
        name1 = input()
        name2 = input()

        name1 = sha256(name1)
        name2 = sha256(name2)

        
        selected_member_1 = find_family_member(selected_family , name1)        
        selected_member_2 = find_family_member(selected_family , name2)        
        
        if not (selected_member_1 and selected_member_2):
            print('! ! ! not found ! ! !')
            continue  
                
        if not check_parent(selected_member_2 ,selected_member_1) and not (selected_member_1.parent.name ==   selected_member_2.parent.name): 
            print('YES')
        else:
            print('NO') 

    elif opt == 6:
        
        print('choose members: ')
        show_family_members(selected_family)
        name1 = input()
        name2 = input()

        name1 = sha256(name1)
        name2 = sha256(name2)
        
        selected_member_1 = find_family_member(selected_family , name1)        
        selected_member_2 = find_family_member(selected_family , name2)        
        
        if not (selected_member_1 and selected_member_2):
            print('! ! ! not found ! ! !')
            continue  
                
        print(find_common_parent(selected_member_1 , selected_member_2))            
    
    elif opt == 7:
        name1 = input()
        name1 = sha256(name1)

        selected_member_1 = find_family_member(selected_family , name1)        

        
        if not selected_member_1:
            print('! ! ! not found ! ! !')
            continue
        
        print(find_node_with_longest_path(selected_member_1))

    elif opt == 8:    
        ans = diameter(selected_family)[1]  
        print(ans[0] , ans[-1])        
        
        
    elif opt == 9:
        plot_tree(selected_family)