from find_route import find_route

def lambda_handler(event, context): 
    
    origin = event["origin"] # 출발지
    destination = event["destination"] # 도착지
    
    path = find_route(origin, destination)
    print(path)
    
    return path