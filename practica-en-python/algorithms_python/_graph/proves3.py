from GraphPro import GraphPro as g
import os

os.system('clear')
print("<--------Test Create------->\n")

weights = [1, 2, 3]
graph = g.creategraph(100, .05, weights)
graph.print_r()

print("-------Incremental-----")
data = graph.dynamic_incremental_random_vertex(weights)
graph.print_r()

graph.draw()
print()
print("------------------------")