# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None #initializes class

    def push(self, value): #creates node for new value and puts it at top of stack
        newnode = Node(value)
        newnode.next = self.top
        self.top = newnode

    def pop(self): #removes top value from the stack
        if not self.top: #makes sure that there is something at the top of the stack
            return None
        removednode = self.top
        self.top = self.top.next #removes node by replacing it with the next
        return removednode.value
    
    def peek(self):
        if self.top: #makes sure stack has something in it
            return self.top.value #returns first value
        else:
            return None
    
    def print_stack(self):
        firstnode = self.top
        if not firstnode: #makes sure stack isn't empty
            print("Stack is empty")
            return
        while firstnode:
            print(f"{firstnode.value}")
            firstnode = firstnode.next #sets the firstnode variable to the next value in stack


def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack() 
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack()

            print(f"Action performed: {action}")

        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            if undo_stack.top == None: #makes sure that there is an action that can be undone
                print("No actions to undo")
            else:
                redo_stack.push(undo_stack.top.value)#adds value to redo_stack before removing from undo_stack
                undo_stack.pop()

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            if not redo_stack.top:
                print("No actions to redo")
            else:
                undo_stack.push(redo_stack.top.value) #adds value to undo_stack before removing from redo_stack
                redo_stack.pop()

        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            
        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()