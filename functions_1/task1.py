import random

catalog = [
{"item":101,"name": "Notebook", "category": "Paper", "price": 3.99},
{"item":102, "name": "Pen", "category": "Writing", "price": 1.50},
{"item":103,"name": "Pencil", "category": "Writing", "price": 0.75},
{"item":104,"name": "Eraser", "category": "Correction", "price":
0.99},
{"item":105,"name": "Sharpener", "category": "Accessories", "price":
1.25},
{"item":106, "name": "Ruler", "category": "Measuring", "price":
2.50},
{"item":107, "name": "Glue Stick", "category": "Adhesive", "price":
1.99},
{"item":108, "name": "Scissors", "category": "Cutting", "price":
4.99},
{"item":109, "name": "Highlighter", "category": "Writing", "price":
2.75},
{"item":110, "name": "Marker", "category": "Writing", "price": 3.49},
{"item":111, "name": "Stapler", "category": "Office Supplies",
"price": 5.99},
{"item":112, "name": "Staples", "category": "Office Supplies",
"price": 1.50},
{"item":113, "name": "Paper Clips", "category": "Office Supplies",
"price": 2.00},
{"item":114, "name": "Binder", "category": "Organizing", "price":
6.50},
{"item":115, "name": "Sticky Notes", "category": "Paper", "price":
3.25},
{"item":116,"name": "Index Cards", "category": "Paper", "price":
2.99},
{"item":117, "name": "Whiteboard Marker", "category": "Writing",
"price": 3.75},
{"item":118,"name": "File Folder", "category": "Organizing", "price":
4.50},
{"item":119,"name": "Calculator", "category": "Electronics", "price":
12.99},
{"item":120,"name": "Tape Dispenser", "category": "Adhesive",
"price": 5.49}
]

def find_price(item_number):
    for product in catalog:
        if product["item"] == item_number:
            return{
                "name":product["name"],
                "category":product["category"],
                "price":product["price"]
            }
        return "Item was not found."
        
def find_extreme(category, extreme="Highest"):
    selected_item = None
    
    for product in catalog:
        if product["category"] == category:
            if selected_item is None:
                selected_item = product
                
            elif extreme.lower() == "highest":
                if product["price"] > selected_item["price"]:
                    selected_item = product
                    
    if selected_item is None:
        return "Category not found."
    return{
        selected_item["item"]: {
            "name": selected_item["name"],
            "category": selected_item["category"],
            "price": selected_item["price"]
        }
    }

