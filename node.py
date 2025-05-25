class Node:
    def __init__(self,key,value,bin_id=None):
        self.value=value
        self.left = None 
        self.right = None 
        self.height = 1
        self.key=key
        self.parent=None
        self.objects=None
        self.bin_id=bin_id
