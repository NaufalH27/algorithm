activities = [
    {"start": 1, "finish": 4},
    {"start": 3, "finish": 5},
    {"start": 0, "finish": 6},
    {"start": 5, "finish": 7},
    {"start": 3, "finish": 8},
    {"start": 5, "finish": 9},
    {"start": 6, "finish": 10},
    {"start": 8, "finish": 11},
    {"start": 8, "finish": 12},
    {"start": 2, "finish": 13},
    {"start": 12, "finish": 14}
]


def activity_greedy_method(activities : list):
    activities.sort(key=lambda x:x["finish"])
    
    results = []
    for activity in activities:
        if len(results) == 0 or activity["start"] >= results[-1]["finish"]:
            results.append(activity); 
            
    return results

print(activity_greedy_method(activities))