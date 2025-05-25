from bin import Bin
from avl import AVLTree,comp_default,comp_id,comp_greater_id,comp_smaller_id
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self,id=None,capacity=None):
        #self.bins_cap_avl_tree = AVLTree(comp_cap)
        self.objects_avl_tree = AVLTree(comp_default)
        self.bins_id_avl_tree=AVLTree(comp_default)
        self.bins_cap_larger_id=AVLTree(comp_greater_id)
        self.bins_cap_smaller_id=AVLTree(comp_smaller_id)
        

    def add_bin(self, id, capacity):
        self.bins_cap_larger_id.insert_value(capacity,id)
        self.bins_cap_smaller_id.insert_value(capacity,id)
        #bin=Bin(id,capacity)
        self.bins_id_avl_tree.insert_value(id,Bin(id,capacity))
        #self.bins_cap_larger_id.printInorder(self.bins_cap_larger_id.root)
    def add_object(self,object_id,size,color):
        if color==Color.BLUE:
            bin_found=self.bins_cap_smaller_id.find_blue_yellow(self.bins_cap_smaller_id.root,size)
        
            self.objects_avl_tree.insert_value(object_id,size,bin_found)
            Bin=self.bins_id_avl_tree.find_norm(bin_found)
            if Bin:
                old_capacity=Bin.capacity
                Bin.add_object(Object(object_id,size,color,bin_found))
                new_capacity=Bin.capacity
            #a=self.objects_avl_tree.find_value(object_id,size)
            #a.bin_id=bin_found.value
            
                self.bins_cap_smaller_id.delete_value(old_capacity,bin_found)
                self.bins_cap_smaller_id.insert_value(new_capacity,bin_found)
                self.bins_cap_larger_id.delete_value(old_capacity,bin_found)
                self.bins_cap_larger_id.insert_value(new_capacity,bin_found)
            
            '''bin_found=self.bins_cap_smaller_id.find_blue_yellow(self.bins_cap_smaller_id.root,size)
            self.objects_avl_tree.insert_value(object_id,size)
            print("this is checkpoint")
            a=self.objects_avl_tree.find_value(object_id,size)
            a.bin_id=bin_found.value
            self.bins_cap_smaller_id.delete_value(bin_found.key,bin_found.value)
            self.bins_cap_smaller_id.insert_value(bin_found.key-size,bin_found.value)
            self.bins_cap_larger_id.delete_value(bin_found.key,bin_found.value)
            self.bins_cap_larger_id.insert_value(bin_found.key-size,bin_found.value)
            self.bins_id_avl_tree.delete_value(bin_found.value,bin_found.key)
            self.bins_id_avl_tree.insert_value(bin_found.value,bin_found.key-size)
            node=self.bins_id_avl_tree.find_id(self.bins_id_avl_tree.root,bin_found.value)
            if node.objects==None:
                node.objects=AVLTree(comp_default)
            node.objects.insert_value(object_id,size)'''
        if color==Color.YELLOW:
            bin_found=self.bins_cap_larger_id.find_blue_yellow(self.bins_cap_larger_id.root,size)
        
            self.objects_avl_tree.insert_value(object_id,size,bin_found)
            Bin=self.bins_id_avl_tree.find_norm(bin_found)
            if Bin:
                old_capacity=Bin.capacity
                Bin.add_object(Object(object_id,size,color,bin_found))
                new_capacity=Bin.capacity
                #a=self.objects_avl_tree.find_value(object_id,size)
                #a.bin_id=bin_found.value
                
                self.bins_cap_smaller_id.delete_value(old_capacity,bin_found)
                self.bins_cap_smaller_id.insert_value(new_capacity,bin_found)
                self.bins_cap_larger_id.delete_value(old_capacity,bin_found)
                self.bins_cap_larger_id.insert_value(new_capacity,bin_found)

            '''bin_found=self.bins_cap_larger_id.find_blue_yellow(self.bins_cap_larger_id.root,size)
        
            self.objects_avl_tree.insert_value(object_id,size)
            x=self.objects_avl_tree.find_value(object_id,size)
            x.bin_id=bin_found
            Bin=self.bins_id_avl_tree.find_norm(bin_found)
            old_capacity=Bin.capacity
            Bin.add_object(Object(object_id,size,color,bin_found))
            new_capacity=Bin.capacity
            #a=self.objects_avl_tree.find_value(object_id,size)'''
           

            
            
        if color==Color.RED:#largest fit least id
            bin_found=self.bins_cap_smaller_id.find_red_green(size)
            
            self.objects_avl_tree.insert_value(object_id,size,bin_found)
            Bin = self.bins_id_avl_tree.find_norm(bin_found)
            if Bin:
                old_capacity=Bin.capacity
                Bin.add_object(Object(object_id,size,color,bin_found))
                new_capacity=Bin.capacity
                self.bins_cap_smaller_id.delete_value(old_capacity,bin_found)
                self.bins_cap_smaller_id.insert_value(new_capacity,bin_found)
                self.bins_cap_larger_id.delete_value(old_capacity,bin_found)
                self.bins_cap_larger_id.insert_value(new_capacity,bin_found)
            
        if color==Color.GREEN:
            bin_found=self.bins_cap_larger_id.find_red_green(size)
            #the problem is when they have the same size but different ids
            self.objects_avl_tree.insert_value(object_id,size,bin_found)
            
            Bin = self.bins_id_avl_tree.find_norm(bin_found)
            if Bin:
                old_capacity=Bin.capacity
                Bin.add_object(Object(object_id,size,color,bin_found))
                new_capacity=Bin.capacity
            
                self.bins_cap_smaller_id.delete_value(old_capacity,bin_found)
                self.bins_cap_smaller_id.insert_value(new_capacity,bin_found)
                self.bins_cap_larger_id.delete_value(old_capacity,bin_found)
                self.bins_cap_larger_id.insert_value(new_capacity,bin_found)
            
            
            

    def delete_object(self,object_id):
        node=self.objects_avl_tree.find_gay(self.objects_avl_tree.root,object_id)

        #node gives the object data:its id and its size
        if node:
            node_1=self.bins_id_avl_tree.find_id(self.bins_id_avl_tree.root,node.bin_id)
        #print(type(node_1)) #node
        #print(type(node_1.capacity))#bin
        #ye checks are made to avoid none type stuff

            node_2=self.bins_cap_larger_id.find_gay(self.bins_cap_larger_id.root,node_1.capacity)
        #by capacity
            node_3=self.bins_cap_smaller_id.find_gay(self.bins_cap_smaller_id.root,node_1.capacity)
            
            self.objects_avl_tree.delete_value(node.key,node.value)
            if node_1.objects:
                node_4=node_1.objects.find_value(object_id,node.value)
                if node_4:
                    node_1.objects.delete_value(node_4.key,node_4.value)
                if node_1:
                    node_1.capacity+=node.value
            #node_1.capacity+=node.value

            if node_2:    
                temp=Node(node_2.key,node_2.value+node.value)
        
                self.bins_cap_larger_id.delete_value(node_2.key,node_2.value)
                self.bins_cap_larger_id.insert_value(temp.key,temp.value)
            #node_1.capacity+=node.value
            if node_3:
                temp1=Node(node_3.key,node_3.value+node.value)
                self.bins_cap_smaller_id.delete_value(node_3.key,node_3.value)
                self.bins_cap_smaller_id.insert_value(temp1.key,temp1.value)

    def bin_info(self, id):
        bin_found = self.bins_id_avl_tree.find_id(self.bins_id_avl_tree.root,id)
        if bin_found.objects:
            return bin_found.capacity,bin_found.objects.inorder_traversal(bin_found.objects.root)
        else:
            raise Exception("Bin info not found")
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        pass
    
    def object_info(self, object_id):
        object_found=self.objects_avl_tree.find_gay(self.objects_avl_tree.root,object_id)
        if object_found:
            bin=object_found.bin_id
        return bin
