def solution(bridge_length, weight, truck_weights):
    bridge = []
    count = 0
    truck_index = 0
    now_weight = 0
        
    while True:
        if truck_index == len(truck_weights):
            break
            
        if count >= bridge_length:
            now_weight -= bridge[count - bridge_length]
        
        if weight >= truck_weights[truck_index] + now_weight:
            bridge.append(truck_weights[truck_index])
            now_weight += truck_weights[truck_index]
            truck_index += 1
        else:
            bridge.append(0)
            
        count += 1
        
    return count + bridge_length