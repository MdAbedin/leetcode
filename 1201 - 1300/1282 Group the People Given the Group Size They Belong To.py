class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        IDs = defaultdict(list)
        for ID,size in enumerate(groupSizes): IDs[size].append(ID)
        return [IDs_list[i:i+size] for size,IDs_list in IDs.items() for i in range(0,len(IDs_list),size)]
