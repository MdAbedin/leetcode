def get_id_list(string):
    maps = dict()
    counter = 0
    id_list = []

    for char in string:
        if char not in maps:
            maps[char] = counter
            counter += 1

        id_list.append(maps[char])

    return id_list

class Solution:        
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_id_list = get_id_list(pattern)
        
        return filter(lambda x: get_id_list(x) == pattern_id_list, words)
