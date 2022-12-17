class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        calculated_vals = dict()

        for (var1,var2),og_val in zip(equations,values):
            for top,bot,val in [[var1,var2,og_val], [var2,var1,1/og_val]]:
                if not isclose(val, calculated_vals.get((top,bot),val), abs_tol = 10**-5): return True
                
                calculated_vals[top,bot] = val

                for (top2,bot2),val2 in list(calculated_vals.items()):
                    if bot == top2:
                        val3 = val*val2
                        
                        if not isclose(val3, calculated_vals.get((top,bot2),val3), abs_tol = 10**-5): return True

                        calculated_vals[top,bot2] = val3

        return False
