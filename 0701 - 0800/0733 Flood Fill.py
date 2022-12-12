class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        bfs = deque([[sr,sc]])
        visited = {(sr,sc)}
        replace_color = image[sr][sc]
        
        while bfs:
            y,x = bfs.popleft()
            image[y][x] = newColor
            
            for dy,dx in [[0,1],[1,0],[0,-1],[-1,0]]:
                y2,x2 = y+dy,x+dx
                
                if y2 >= 0 and y2 < len(image) and x2 >= 0 and x2 < len(image[0]) and image[y2][x2] == replace_color and (y2,x2) not in visited:
                    bfs.append([y2,x2])
                    visited.add((y2,x2))
                    
        return image
