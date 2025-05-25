from avl import AVLTree,comp_id
class Bin:
    def __init__(self, id, capacity):
        self.id=id
        self.capacity=capacity
        self.objects= AVLTree()
        pass

    def add_object(self, object):

        self.objects.insert_value(object.id,object)
        

        self.capacity = self.capacity-object.capacity
        # Implement logic to add an object to this bin
        pass

    def remove_object(self, object_id):
        self.objects.remove(object)
        self.capacity_left += object.size
        # Implement logic to remove an object by ID
        pass
