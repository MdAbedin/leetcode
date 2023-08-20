class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        items = defaultdict(list)
        next_group = m

        for i in range(len(group)):
            if group[i] == -1:
                group[i] = next_group
                next_group += 1
            
            items[group[i]].append(i)

        groups = next_group
        before_items,after_items = defaultdict(set),defaultdict(set)
        before_groups,after_groups = defaultdict(set),defaultdict(set)

        for i,before_items_list in enumerate(beforeItems):
            for before_item in before_items_list:
                before_items[i].add(before_item)
                after_items[before_item].add(i)

                if group[i] != group[before_item]:
                    before_groups[group[i]].add(group[before_item])
                    after_groups[group[before_item]].add(group[i])

        tsort = deque(group_i for group_i in range(groups) if not before_groups[group_i])
        group_order = []

        while tsort:
            group_i = tsort.popleft()
            group_order.append(group_i)

            for group_i2 in after_groups[group_i]:
                before_groups[group_i2].remove(group_i)
                if not before_groups[group_i2]: tsort.append(group_i2)

        if len(group_order) != groups: return []

        ans = []

        for group_i in group_order:
            tsort = deque(i for i in items[group_i] if not before_items[i])
            item_order = []

            while tsort:
                i = tsort.popleft()
                item_order.append(i)

                for i2 in after_items[i]:
                    before_items[i2].remove(i)
                    if not before_items[i2] and group[i2] == group_i: tsort.append(i2)

            if len(item_order) != len(items[group_i]): return []
            
            ans.extend(item_order)

        return ans
