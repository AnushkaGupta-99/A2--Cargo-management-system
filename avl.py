from node import Node
from exceptions import NoBinFoundException

def comp_greater_id(node_1, node_2):
    if node_1.key > node_2.key:
        return 1
    elif node_2.key > node_1.key:
        return -1
    else:
        if node_1.value > node_2.value:
            return 1
        elif node_1.value<node_2.value:

            return -1
        else:
            return 0
        

def comp_smaller_id(node_1, node_2):
    if node_1.key > node_2.key:
        return 1
    elif node_2.key > node_1.key:
        return -1
    else:
        if node_1.value > node_2.value:
            return -1
        elif node_1.value<node_2.value:
            return 1
        else:
            return 0

def comp_default(node_1, node_2):
    if node_1.key is None:
        return -1
    elif node_2.key is None:
        return 1
    elif node_1.key < node_2.key:
        return -1
    elif node_1.key > node_2.key:
        return 1
    else:
        return 0

def comp_id(node_1, node_2):
    if node_1 is None:
        return -1
    elif node_2 is None:
        return 1
    if node_1.id < node_2.id:
        return -1
    elif node_1.id > node_2.id:
        return 1
    else:
        return 0

def normal_comparison(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

class AVLTree:
    def __init__(self, compare_function=comp_default):
        self.root = None
        self.size = 0
        self.compare_function = compare_function

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _rotate_right(self, z):
        temp = z.left
        T3 = temp.right

        temp.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))

        return temp

    def _rotate_left(self, z):
        temp = z.right
        T2 = temp.left

        temp.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))

        return temp

    def balance(self, node):
        balance_factor = self.get_balance(node)
        if balance_factor > 1:
            if self.get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance_factor < -1:
            if self.get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _insert(self, root, node):
        if root is None:
            self.size += 1
            return node
        if self.compare_function(node, root) < 0:
            root.left = self._insert(root.left, node)
            root.left.parent = root
        else:
            root.right = self._insert(root.right, node)
            root.right.parent = root

        self.update_height(root)
        return self.balance(root)

    def insert_value(self, key, value,bin_id=None):
        node = Node(key, value,bin_id)
        if self.root is None:
            self.root = node
        else:
            self.root = self._insert(self.root, node)

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def _delete(self, root, node):
        if root is None:
            return root
        if self.compare_function(node, root) < 0:
            root.left = self._delete(root.left, node)
        elif self.compare_function(node, root) > 0:
            root.right = self._delete(root.right, node)
        else:
            if root.left== None:
                return root.right
            elif root.right== None:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self._delete(root.right, temp)

        self.update_height(root)
        return self.balance(root)

    def _min_value_node(self, root):
        a = root
        while a.left != None:
            a = a.left
        return a
    #this returns the leftmost node

    def delete_value(self, key, value):
        node = Node(key, value)
        self.root = self._delete(self.root, node)

    def find_id(self, root, id):
        if root is None:
            return root
        if root.key == id:
            return root.value
        if root.key > id:
            return self.find_id(root.left, id)
        return self.find_id(root.right, id)
    
    def find_gay(self, root, id):
        if root is None:
            return None
        if root.key == id:
            return root
        if root.key > id:
            return self.find_gay(root.left, id)
        else:
            return self.find_gay(root.right, id)
    
    def find_norm(self, id, value=None):
        node = Node(id, value)
        if self._find_norm(self.root, node):
            return self._find_norm(self.root, node).value
        
    def _find_norm(self, root, node):
        if root is None:
            return None
        if self.compare_function(node, root) == 0:
            return root
        if self.compare_function(node, root) < 0:
            return self._find_norm(root.left, node)
        return self._find_norm(root.right, node)
    
    def find_value(self, key, value):
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None
    
    def find_blue_yellow(self, root, size, greatest_id=False):
        best_fit = None
        
        while root != None:
            if root.key >= size:
    
                if best_fit is None or root.key < best_fit.key or (root.key == best_fit.key and (greatest_id and root.value > best_fit.value) or (not greatest_id and root.value < best_fit.value)):
                    best_fit = root

                root = root.left
            else:
    
                root = root.right
        if best_fit:
            return best_fit.value
        else:
            return None
        



    '''def find_blue_yellow(self, root, size):
        root = self.root
        while root.key >= size and root.left is not None:
            root = root.left
        foundsize = root.key
        while root.key == foundsize and root.right is not None:
            root = root.right
        return root.value'''
    
    def inorder_traversal(root):
        result = []
    
        def travel(node):
            if node:
                travel(node.left)  # this goes through left subtree
                result.append(node.value)  # this will visit node
                travel(node.right)  # this goes through right subtree
    
        travel(root)
        return result

    def find_red_green(self,size):
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        if p.key>=size:    
            return p.value
        
        
    def inorder_traversal(self, root):
        if root is None:
            return []
        result = []
        if root.left is not None:
            result.extend(self.inorder_traversal(root.left))
        result.append(root.key)
        if root.right is not None:
            result.extend(self.inorder_traversal(root.right))
        return result    
    