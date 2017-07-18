from sets import Set
from collections import deque
import heapq

# A class that wraps the heapq functionality
# into a convenient min heap container
# which always maintains the smallest element of
# a set of data, with O(log(n)) insertion and removal
# This heap does not support node cost updating, so just
# insert duplicate nodes with different path costs if necessary
class MinHeap:
	def __init__(self):
		self.container = []
	
	def push(self, obj):
		heapq.heappush(self.container, obj)

	# If obj is not in heap, push it into the heap
	# If obj is already in heap, but with a higher cost,
	# 	update the heap so that obj has the lower cost. Otherwise,
	# 	do nothing.
	def push_or_update(self, obj):
		if obj in self.container:
			index = self.container.index(obj)
			if obj.totalcost < self.container[index].totalcost:
				self.container[index] = self.container[-1]
				self.container.pop()
				heapq.heapify(self.container)
				heapq.heappush(self.container, obj)
		else:
			heapq.heappush(self.container, obj)

	def pop(self):
		return heapq.heappop(self.container)

	def top(self):
		return self.container[0]
	
	# So that you can call the python len() function on this object
	def __len__(self):
		return len(self.container)

# An implementation of the node class
# You may re-implement this if you wish
# But then be sure to re-implement the extract_path function
class node:
	node_count = 0
	def __init__(self, parent, position, pathcost=0, heuristic=0):
		self.idnum = node.node_count
		node.node_count += 1
		self.position = position
		self.pathcost = pathcost
		self.heuristic = heuristic
		self.totalcost = pathcost+heuristic
		self.parent = parent
		if parent is None:
			self.depth = 0
		else:
			self.depth = parent.depth+1

	# Less-than implemented so nodes can be put in MinHeap
	def __lt__(self, other):
		return self.totalcost < other.totalcost

	# Equality implemented so you can test whether nodes
	# are in a Set()
	# Nodes are equivalent if their positions are equal
	def __eq__(self, other):
		return (self.position == other.position)

	# Hash implemented so nodes can be put in Set()
	def __hash__(self):
		return hash(self.position)

# A dummy heuristic function that always returns 0
# Useful for searches that don't have a heuristic
def zero_heuristic(curpos, endpos):
	return 0

# Manhattan distance between curpos and endpos (tuples)
def manhattan(curpos, endpos):
	return abs(endpos[0]-curpos[0])+abs(endpos[1]-curpos[1])

# Euclidean distance between curpos and endpos (tuples)
def euclidean(curpos, endpos):
	return ((curpos[0]-endpos[0])**2+(curpos[1]-endpos[1])**2)**(0.5)

# A function that takes the current node, the grid,
# The goal position (endpos), and possibly the heuristic function, and returns a list of successors
def get_successors(curnode, grid, endpos, heuristic=zero_heuristic):
	# Fill in this function
	# You may want to create several versions of this function
	# Insert successors in the order north, east, south, west

	successors = []
	##### Your code here ######

	return successors

# A function that tests whether a node is a goal node
def goal_test(curnode, endpos):
	return (curnode.position == endpos)

# extract_path takes a goal node and returns a path
# (a list of tuples) from the initial state to the goal.
# If you change the node class, re-implement this function
def extract_path(curnode):
	path = []
	while curnode is not None:
		path.append(curnode.position)
		curnode = curnode.parent
	return path[::-1]

# For all of the following search functions,
# "grid" is a python list of lists of integers describing the board
# Index the grid via grid[rowindex][columnindex]
# startpos is a tuple of the agent's starting position
# endpos is the location of the batter
# Do not change the arguments or return values of these functions

def get_successors_dfs(curnode, grid, endpos, heuristic=zero_heuristic):
	# Fill in this function
	# You may want to create several versions of this function
	# Insert successors in the order north, east, south, west
	x = curnode[0]
	y = curnode[1]
	
	successors = []
	print(curnode[0])

	return successors

def depth_first_search(grid, startpos, endpos):
	# Perform depth-first search
	# Goal test at generation
		
	# Return all of the following, in order
	return #goalnode, total_nodes_generated, max_nodes_stored, num_iters, depth_of_goal, total_cost_of_goal

def iterative_deepening_search(grid, startpos, endpos):
	# Perform iterative deepening search
	# Goal test at generation

	# Return all of the following
	return #goalnode, total_nodes_generated, max_nodes_stored, num_iters, depth_of_goal, total_cost_of_goal

#size [x,y]
#curnode [x,y]
#def checkEdge(curnode, size):
	#return FALSE

def get_successors_bfs(curnode, grid, endpos, visits):
	# Fill in this function
	# You may want to create several versions of this function
	# Insert successors in the order north, east, south, west
	rows = len(grid)
	cols = len(grid[0])
	suc = deque()
	res = 0
	y = curnode[0]
	x = curnode[1]
	#N
	if(y > 0):	
		cd = [curnode[0] - 1, curnode[1]]
		if (visits[cd[0]][cd[1]] == 0):
			visits[cd[0]][cd[1]] == 1
			suc.extendleft([cd])
			res = res + 1
	#E
	if(x < (cols - 1)):
		cd = [curnode[0], curnode[1] + 1]
		if visits[cd[0]][cd[1]] == 0:
			visits[cd[0]][cd[1]] == 1
			suc.extendleft([cd])
			res = res + 1
	#S
	if(y < rows - 1):
		cd = [curnode[0] + 1, curnode[1]]
		if visits[cd[0]][cd[1]] == 0:
			visits[cd[0]][cd[1]] == 1
			suc.extendleft([cd])
			res = res + 1
	#W
	if(x > 0):
		cd = [(curnode[0]), curnode[1] - 1]
		if visits[cd[0]][cd[1]] == 0:
			suc.extendleft([cd])
			res = res + 1
	return suc, res

def breadth_first_search(grid, startpos, endpos):
	# Perform breadth-first search
	# Goal test at generation
	#def get_successors(curnode, grid, endpos, heuristic=zero_heuristic):
	#FIFO extend left, removeright
	
	aNode = node(None, startpos)
	othernode = aNoe
	nodePath = deque()
	nodePath.extendleft(aNode)
	
	total_nodes_generated = max_nodes_stored = 0
	num_iters = depth_of_goal = dequeSize = 0;
	if startpos == endpos:
		return startpos, total_nodes_generated, max_nodes_stored, num_iters, depth_of_goal, total_cost_of_goal
		
	d = deque()
	d.extendleft([startpos])
	dequeSize += 1
	if(dequeSize > max_nodes_stored):
		max_nodes_stored = dequeSize
	
	
	rows = len(grid)
	cols = len(grid[0])
	print grid[1][0]
	
	visits = [[0]*cols for _ in range(rows)]
	
	while(dequeSize > 0):
		curnode = d.pop()
		othernode.pos = curnode
		othernode.parent = aNode
		total_nodes_generated += 1
		dequeSize -= 1
		visits[curnode[0]][curnode[1]] = 1
		
		res = deque()
		res = get_successors_bfs(curnode, grid, endpos, visits)
		
		for num in range(0, res[1]):
			cd = res[0].pop()
			visits[cd[0]][cd[1]] = 1
			d.extendleft([cd])
			dequeSize += 1
			aNode.pos = cd
			aNode.parent = othernode
			nodePath.extendleft(aNode)
		if(dequeSize > max_nodes_stored):
			max_nodes_stored = dequeSize	
		
		if(curnode[0] == endpos[0] and curnode[1] == endpos[1]):
			print ('Found goal:')
			print curnode
			break
	
	
	
	# Return all of the following
	return #goalnode, total_nodes_generated, max_nodes_stored, num_iters, depth_of_goal, total_cost_of_goal

def uniform_cost_search(grid, startpos, endpos):
	# Perform uniform cost search
	# Goal test at expansion


	# Return all of the following
	return #goalnode, total_nodes_generated, max_nodes_stored, num_iters, depth_of_goal, total_cost_of_goal
	
def a_star_search(grid, startpos, endpos, heuristic=manhattan):
	# Perform A* search
	# Goal test at expansion

	# Return all of the following
	return #goalnode, total_nodes_generated, max_nodes_stored, num_iters, depth_of_goal, total_cost_of_goal


