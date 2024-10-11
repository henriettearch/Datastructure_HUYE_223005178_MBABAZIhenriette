from collections import deque

undo_stack = []

pending_shipments = deque()

inventory = []

def add_to_inventory(item):
    inventory.append(item)
    print(f"Added '{item}' to inventory. Current inventory: {inventory}")

def process_shipment(item):
    if item in inventory:
        inventory.remove(item)
        undo_stack.append(item)
        print(f"Shipped '{item}'. Inventory after shipment: {inventory}")
    else:
        print(f"Item '{item}' not found in inventory. Cannot ship.")

def undo_last_shipment():
    if undo_stack:
        last_shipped_item = undo_stack.pop()
        inventory.append(last_shipped_item)
        print(f"Undid shipment of '{last_shipped_item}'. Inventory: {inventory}")
    else:
        print("No shipments to undo.")

def add_pending_shipment(item):
    pending_shipments.append(item)
    print(f"Added '{item}' to pending shipments. Pending shipments: {list(pending_shipments)}")

def process_next_pending():
    if pending_shipments:
        next_item = pending_shipments.popleft()
        process_shipment(next_item)
        print(f"Processed next pending shipment of '{next_item}'. Pending shipments: {list(pending_shipments)}")
    else:
        print("No pending shipments to process.")

# Example usage:
add_to_inventory("Rice")
add_to_inventory("Maize flour")

process_shipment("Rice")
process_next_pending()


add_pending_shipment("Sugar")
add_pending_shipment("Salt")

process_next_pending()  
process_shipment("No existent Item") 


undo_last_shipment()
process_next_pending()