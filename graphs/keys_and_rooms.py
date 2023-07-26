def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    visited = 0
    keys = [0]
    while len(keys) > 0 and visited < len(rooms):
        uk = keys.pop()
        if rooms[uk] != 'visited':
            keys.extend(rooms[uk])
            rooms[uk] = 'visited'
            visited+=1
    
    return visited == len(rooms)

if __name__ == '__main__':
    print('tests')
    print(canVisitAllRooms([[1],[2],[3],[]]) == True)
    print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False)