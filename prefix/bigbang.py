# Import library
from d3graph import d3graph, vec2adjmat

# Source node names
source = ['Penny', 'Penny', 'Amy', 'Bernadette', 'Bernadette', 'Sheldon', 'Sheldon', 'Sheldon', 'Rajesh']
# Target node names
target = ['Leonard', 'Amy', 'Bernadette', 'Rajesh', 'Howard', 'Howard', 'Leonard', 'Amy', 'Penny']
# Edge Weights
weight = [5, 3, 2, 2, 5, 2, 3, 5, 2]

# Convert the vector into a adjacency matrix
adjmat = vec2adjmat(source, target, weight=weight)

# Initialize
d3 = d3graph()
d3.graph(adjmat)
d3.show()
