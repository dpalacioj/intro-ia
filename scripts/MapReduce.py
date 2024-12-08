from collections import defaultdict

data = [
    ("New York", 5),
    ("Buenos Aires", 2),
    ("New York", 3),
    ("Buenos Aires", 4),
    ("Medellín", 1),
]

# Fase Map

mapped_data = []
for city, count in data:
    mapped_data.append((city, count))

# Fase Reduce

reduced_data = defaultdict(int)
for city, count in mapped_data:
    reduced_data[city] += count

# Resultados

for city, total in reduced_data.items():
    print(f"{city}:{total}")