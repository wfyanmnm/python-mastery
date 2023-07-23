total_cost = 0
with open('portfolio.dat', 'rt') as f:
    for line in f:
        parts = line.split()
        total_cost += int(parts[1]) * float(parts[2])
print('Total cost:', total_cost)
