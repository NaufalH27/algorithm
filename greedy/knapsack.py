knapsack_items = [
    {"item": "Laptop", "weight": 3, "value": 2000},
    {"item": "Headphones", "weight": 1, "value": 300},
    {"item": "Smartphone", "weight": 2, "value": 1500},
    {"item": "Camera", "weight": 4, "value": 2500},
    {"item": "Hard Drive", "weight": 2, "value": 800},
    {"item": "Book", "weight": 1, "value": 100},
    {"item": "Jacket", "weight": 2, "value": 500},
    {"item": "Shoes", "weight": 2, "value": 700},
    {"item": "Watch", "weight": 1, "value": 400},
    {"item": "Tablet", "weight": 3, "value": 1000},
    {"item": "Water Bottle", "weight": 1, "value": 50},
]

#can be applicable to schedule proft
def knapsack_greedy_method_all_or_nothing(items:list,max_weight):
    items.sort(key=lambda x:x["value"], reverse=True)
    
    results = []
    current_weight = 0
    for item in items:
        if item["weight"] + current_weight <= max_weight:
            results.append({item["item"] : 1})
            current_weight += item["weight"]
    return results
            
def knapsack_greedy_method_fraction(items:list, max_weight):
    items.sort(key=lambda x:x["value"]/x["weight"], reverse=True)
    
    results = []
    current_weight = 0
    for item in items:
        if item["weight"] + current_weight <= max_weight:
            results.append({item["item"] : 1})
            current_weight += item["weight"]
        else :
            results.append({ item["item"] : (max_weight - current_weight) / item["weight"]})
            break
        
    return results
        
print(knapsack_greedy_method_all_or_nothing(knapsack_items,10))
print(knapsack_greedy_method_fraction(knapsack_items,10))