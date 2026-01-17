import pulp #used python 3.13 and pupl to it

model = pulp.LpProblem("Model Name", pulp.LpMaximize)  
A = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
B = pulp.LpVariable('Fruit_juice', lowBound=0, cat='Integer')
C = pulp.LpVariable('Water', lowBound=0, upBound=100, cat='Integer')
D = pulp.LpVariable('Sugar', lowBound=0, upBound=50, cat='Integer')
E = pulp.LpVariable('Lemon_juice', lowBound=0, upBound=30, cat='Integer')
F = pulp.LpVariable('Fruit_puree', lowBound=0, upBound=40, cat='Integer')
model += A + B, "Problem"
model += C == A + B, "Water_balance"
model += D == A, "Sugar_balance"
model += E == A, "Lemon_juice_balance"
model += F == B, "Fruit_puree_balance"
model.solve()
print("Виробляти Лимоннаду:", A.varValue)
print("Виробляти Фруктовий сік:", B.varValue)
