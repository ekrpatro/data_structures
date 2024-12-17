class Node:
    def __init__(self, data):
        # Initialize node with data and next pointer
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize an empty LinkedList
        self.head = None

    def add_node(self, data):
        """Add a node to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        """Delete a node by value."""
        temp = self.head
        
        # If the head node itself is the target node
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        # Search for the node to delete
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        # If key was not found
        if temp is None:
            print(f"Node with value {key} not found.")
            return
        
        # Unlink the node
        prev.next = temp.next
        temp = None

    def display(self):
        """Display the linked list."""
        if self.head is None:
            print("The linked list is empty.")
            return
        
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage
if __name__ == "__main__":
    ll = LinkedList()
    
    # Adding nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    
    print("Linked List after adding nodes:")
    ll.display()
    
    # Deleting a node
    ll.delete_node(20)
    print("Linked List after deleting 20:")
    ll.display()
    
    # Deleting a node that does not exist
    ll.delete_node(100)
    print("Linked List after attempting to delete 100:")
    ll.display()
