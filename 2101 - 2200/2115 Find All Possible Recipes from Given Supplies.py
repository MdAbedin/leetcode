class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredients_left = {food: set(ingredients_list) for food,ingredients_list in zip(recipes,ingredients)}
        foods = defaultdict(list)

        for food,ingredients_list in zip(recipes,ingredients):
            for ingredient in ingredients_list: foods[ingredient].append(food)

        bfs = supplies
        ans = []

        for item in bfs:
            for food in foods[item]:
                ingredients_left[food].remove(item)
                if not ingredients_left[food]: bfs.append(food)

        return list(set(recipes) & set(bfs))
