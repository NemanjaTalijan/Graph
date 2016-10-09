import sys

list = [[False for i in range(0,25)] for j in range(0,25)]

print("Please enter the connected nods:")
nodes = sys.stdin.readline()

while (nodes != "END\n"):
    list[ord(nodes[0]) - 65][ord(nodes[1]) - 65] = True
    list[ord(nodes[1]) - 65][ord(nodes[0]) - 65] = True
    nodes = sys.stdin.readline()
else:
 print("Please enter the node link check:")
 nodes = sys.stdin.readline()
 print(list[ord(nodes[0]) - 65][ord(nodes[1]) - 65])