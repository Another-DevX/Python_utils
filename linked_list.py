from node import Node
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __append__(self,value):
        node = Node(value)
        if self.size == 0:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        self.size += 1

    def __str__(self):
        string = "["
        current = self.head
        if self.size > 0:
            while current.next != None:
                string += str(current.value)
                string += ", "
                current = current.next
            string += str(current.value)
            string += "]"
            return string
        else:
            return False 
    
    def __len__(self):
        return self.size
    
    def delete(self, value):
        current =  self.head
        if self.size == 0:
            return False 
        else:
            try:
                while current.next.value != value:
                    current = current.next
                removed_node = current.next
                current.next = removed_node.next
                self.size -= 1
            except AttributeError:
                return False

        
    
    def search_by_value (self, value):
        current = self.head
        if self.size == 0:
            return False
        else:
            while current.next != None:
                if current.value == value:
                    return f"The value {value} is in the linked list"
                else:
                    current = current.next
            if current.value == value:
                return f"The value {value} is in the linked list"
            return f"The value {value} is not in the linked list"
    
    def search_by_position(self, position):
        if position > self.size or position < 0:
            raise ValueError(f'Index out of range {position}, size {self.size}')
        else:
            current = self.head
            if position == 0:
                return current.value
            else:
                for i in range(position):
                    current = current.next
                return current.value
                
    def search_position_by_value(self,value):
        current = self.head
        position = 0
        if self.size == 0:
            return False
        else:
            while current.next != None:
                position += 1
                if current.value == value:
                    return position - 1
                else:
                    current = current.next
            if current.value == value:
                return position
            return False
    
    def replace(self,value,replaced):
        current = self.head
        if self.size == 0:
            return False
        else:
            while current.next != None:
                if current.value == value:
                    current.value = replaced
                else:
                    current = current.next
            if current.value == value:
                current.value = replaced
            return False
        
    def insert(self,value,index):
        if index > self.size or index < 0:
            raise ValueError(f'Index out of range {index}, size {self.size}')
        else:
            node = Node(value)
            current = self.head
            if index == 0:
                node.next = current
                self.head = node
            else:
                for i in range(index-1):
                    current = current.next
                node.next = current.next
                current.next = node
                
            
    
    def clear(self):
        self.head = None
        self.size = 0
            
if __name__ == '__main__':
    linkList = LinkedList()
    for value in range(1,5):
        linkList.__append__(value)
    print(linkList.search_by_value(4))
    print(linkList.search_by_value(10))
    print(linkList)
    linkList.delete(2)
    print(len(linkList))
    linkList.replace(1, 10)
    print(linkList)
    print(linkList.search_by_position(2))
    print(linkList.search_position_by_value(4))
    linkList.insert(20,0)
    print(linkList)