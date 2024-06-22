import pulp

# Initializing the model
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Defining variables
L = pulp.LpVariable('L', lowBound=0, cat='Integer') # Quantity of Lemonade
FJ = pulp.LpVariable('FJ', lowBound=0, upBound=10, cat='Integer') # Quantity of Fruit juice

# Objective function (Profit maximization)
model += 1 * L + 1 * FJ, "Profit"

# Adding constraints
model += 2 * L + 1 * FJ <= 100 # Constraint for Water
model += 1 * L + 0 * FJ <= 50 # Constraint for Sugar
model += 1 * L + 0 * FJ <= 30 # Constraint for Lemon juice
model += 0 * L + 2 * FJ <= 40 # Constraint for Fruit puree

# Solving the model
model.solve()

# Displaying the results
print("Produce Lemonade:", L.varValue)
print("Produce Fruit Juice:", FJ.varValue)