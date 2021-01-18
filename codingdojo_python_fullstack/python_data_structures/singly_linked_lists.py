class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node # SET the list's head TO the node we created in the last step
        return self                # return self to allow for chaining

    def print_values(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
   
    def add_to_back(self, val):
        if self.head == None: # if the list is empty
            self.add_to_front(val) # run the add_to_front method
            return self # let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = new_node # increment the runner to the next node in the list
        return self                 # return self to allow for chaining

    def remove_from_front(self):
        if self.head != None:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
            return self
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None
        return self

    def remove_val(self, val):
        if self.head == None:
            return self
        elif self.head.value == val: # when head node has our value
            self.head = self.head.next
            return self
        else:
            current = self.head
            while current.next != None and current.next.value != val:
                current = current.next
            if current.next == None: # We hit the end of the list and didn't find the value in the list
                return self
            else: # We hit the value in a node in front of us and need to make sure we reassign the current node's next to go around
                current.next = current.next.next
                return self
           

class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

sll = SList()
sll.add_to_front("B").add_to_front("A").add_to_back("C").remove_from_front().print_values()
sll2 = SList()
sll2.add_to_back("Z").add_to_back("Y").remove_from_back().remove_from_back().remove_from_back().remove_from_back().print_values()
sll3 = SList()
sll3.add_to_back("A").add_to_back("B").add_to_back("C").add_to_back("D").remove_val("A").print_values()
# sll3.add_to_back("A").add_to_back("B").add_to_back("C").add_to_back("D").remove_val("B").print_values()
# sll3.add_to_back("A").add_to_back("B").add_to_back("C").add_to_back("D").remove_val("C").print_values()
# sll3.add_to_back("A").add_to_back("B").add_to_back("C").add_to_back("D").remove_val("D").print_values()
