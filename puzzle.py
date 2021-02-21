"""
CS 170 Project
Alec Asatoorian, 862026505
8-puzzle Solver using search algorithms
	Uniform Cost Search, A* Misplaced Tile Search,
	A* Manhattan Distance Search
"""
import copy, time
from enum import Enum  

# game engine class for 8-Puzzle
class game:

	# initialize a game board
	def __init__(self, init_state=['1', '2', '3', '4', '5', '6', '7', '8', ' ']):


		self.board = init_state
		if isinstance(self.board, str):
			self.board = list(self.board)
		self.correct = '12345678 '
		self.empty_index = 8
		for x in range(0, len(self.board)):
			if self.board[x] == ' ':
				self.empty_index = x

		# AI Variables
		self.cost = 0

	# game operators
	def move_down(self):

		empty_index = self.empty_index

		if ((empty_index + 1) < 4):

			# print("Invalid. Can't Move Down...")

			return False

		else:

			# print("Moving Down...")

			self.board[empty_index], self.board[empty_index - 3] = self.board[empty_index - 3], self.board[empty_index] 
			self.empty_index = empty_index - 3

			return True
	def move_up(self):

		empty_index = self.empty_index

		if ((empty_index + 1) > 6):

			# print("Invalid. Can't Move Up...")

			return False

		else:

			# print("Moving Up...")

			self.board[empty_index], self.board[empty_index + 3] = self.board[empty_index + 3], self.board[empty_index] 
			self.empty_index = empty_index + 3

			return True
	def move_left(self):

		empty_index = self.empty_index


		if((empty_index + 1) % 3 != 0):

			# print("Moving Left...")

			self.board[empty_index], self.board[empty_index + 1] = self.board[empty_index + 1], self.board[empty_index] 
			self.empty_index = empty_index + 1

			return True

		else:

			# print("Invalid. Can't Move Left...")

			return False
	def move_right(self):

		empty_index = self.empty_index

		if((empty_index + 1) % 3 != 1):

			# print("Moving Right...")

			self.board[empty_index], self.board[empty_index - 1] = self.board[empty_index - 1], self.board[empty_index] 
			self.empty_index = empty_index - 1
			return True

		else:

			# print("Invalid. Can't Move Right...")

			return False

	# utility functions
	def get_current_result(self, my_board=None):

		if(my_board == None):
			my_board = self.board

		str_sum = ''

		# print(my_board)
		for x in range(0, len(my_board)):

			str_sum += my_board[x]

		return str_sum
	def game_over(self, str_sum):


		if(str_sum == self.correct):

			return True

		else:
			return False

	# testing functions
	def operator_test(self, new_board):

		result = get_current_result()
		correct = get_current_result(new_board)


		assert result == correct, "Result should be" + correct + "but was " + result
	def shuffling(self):

		operators = Enum('Operators', 'up down left right')
		previousMove = None
		board = self.board

		for i in range(0, 5):

			if self.move_up() and previousMove != operators.down:
				previousMove = operators.up
			if self.move_down() and previousMove != operators.up:
				previousMove = operators.down
			if self.move_right() and previousMove != operators.left:
				previousMove = operators.right
			if self.move_left() and previousMove != operators.right:
				previousMove = operators.left
		for i in range(0, 10):
			self.move_right()
			self.move_down()
			self.move_down()
			self.move_right()
			self.move_up()
			self.move_right()
			self.move_down()
			self.move_up()
			self.move_left()
			self.move_left()
			self.move_right()
			self.move_down()
			self.move_left()
			self.move_up()
			self.move_right()
			self.move_right()
			self.move_down()
			self.move_down()
		
		# self.print()
		return board

	# display game board 
	def print(self):

		print('\n')
		print('\t\t' + self.board[0] + '|' + self.board[1] + '|' + self.board[2])
		print('\t\t' + '-+-+-')
		print('\t\t' + self.board[3] + '|' + self.board[4] + '|' + self.board[5])
		print('\t\t' + '-+-+-')
		print('\t\t' + self.board[6] + '|' + self.board[7] + '|' + self.board[8])
		print('\n')

# search algorithm class
class ai:

	# initialize the ai class
	def __init__(self, board=None):
		self.my_game = game(board)
		self.nodes = list()
		self.visited = list()
		self.expanded_nodes = 0
		self.max_nodes = 0

	# utility functions
	def visited_check(self, node):

		for i in self.visited:

			if i.get_current_result() == node.get_current_result():

				return False

		return True
	def reset(self, board):
		self.my_game = game(board)
		self.nodes = list()
		self.visited = list()
		self.max_nodes = 0

	# search algorithm expansion functions
	def expand(self, node):
		
		if self.nodes is None:

			self.nodes = list()


		tempGame = copy.deepcopy(node)

		if tempGame.move_up():


			if self.visited_check(tempGame):
				self.nodes.append(tempGame)
				tempGame.cost += 1
				self.expanded_nodes += 1
			tempGame = copy.deepcopy(node)


		if tempGame.move_down():

			if self.visited_check(tempGame):
				self.nodes.append(tempGame)
				tempGame.cost += 1
				self.expanded_nodes += 1
			tempGame = copy.deepcopy(node)


		if tempGame.move_left():

			if self.visited_check(tempGame):
				self.nodes.append(tempGame)
				tempGame.cost += 1
				self.expanded_nodes += 1
			tempGame = copy.deepcopy(node)

		if tempGame.move_right():

			if self.visited_check(tempGame):
				self.nodes.append(tempGame)
				tempGame.cost += 1
				self.expanded_nodes += 1
			tempGame = copy.deepcopy(node)
	def expand_a_star(self, node):
		
		if self.nodes is None:

			self.nodes = list()


		tempGame = copy.deepcopy(node)

		if tempGame.move_up():

			self.nodes.append(tempGame)
			tempGame.cost += 1
			self.expanded_nodes += 1
			tempGame = copy.deepcopy(node)


		if tempGame.move_down():

			self.nodes.append(tempGame)
			tempGame.cost += 1
			self.expanded_nodes += 1
			tempGame = copy.deepcopy(node)


		if tempGame.move_left():


			self.nodes.append(tempGame)
			tempGame.cost += 1
			self.expanded_nodes += 1
			tempGame = copy.deepcopy(node)

		if tempGame.move_right():


			self.nodes.append(tempGame)
			tempGame.cost += 1
			self.expanded_nodes += 1
			tempGame = copy.deepcopy(node)

	# heuristic calculations
	def heuristic_mis(self, node):

		h = 0

		x = node.get_current_result(node.board)
		y = "12345678 "

		for a in range(0, 9):
				if x[a] != y[a]:
					h += 1

		return h
	def heuristic_man(self, node):

		h = 0

		x = node.get_current_result(node.board)
		y = "12345678 "

		for a in range(0, 9):

			if x[a] == " ":
				x_position = 9
			else:
				x_position = int(x[a])
			y_position = a
			h += abs(x_position - y_position)

		return h
	def g_cost(self, node, mode='misplaced'):

		g = self.heuristic_mis(node) + node.cost

		if mode == 'manhattan':
			g = self.heuristic_man(node) + node.cost

		return g
	def cost(self, node):

		g = node.cost
		return g

	# search algorithm implementation
	def uniform_cost(self, my_game=None):

		if my_game is None:

			my_game = self.my_game

		# my_game.print()

		# Initialize Variables
		self.expanded_nodes = 0
		self.nodes.append(my_game)
		min_index = 0
		level_count = 0

		# print("Starting Search...")
		# Start Search
		while True:

			if len(self.nodes) == 0:
				print("\tFailure. Impossible to solve...")
				return None


			if len(self.nodes) > self.max_nodes:
				self.max_nodes = len(self.nodes)

			# Pop Smallest from Nodes, Append to Visited
			min_index, _  = min(enumerate(self.nodes), key=lambda x : self.cost(x[1]))
			node = self.nodes.pop(min_index)
			self.visited.append(node)

			# Check if Game Over
			if node.game_over(node.get_current_result(node.board)):
				# node.print()				
				print("\t\tGame Over. Found Game Winning Node...")
				print("\t\tTook " + str(node.cost) + " Levels...")
				print("\t\tExpanded " + str(self.expanded_nodes) + " Nodes...")
				print("\t\tMax number of nodes in list: " + str(self.max_nodes))
				return node
			
			# Expand Popped Node
			self.expand(node)
			# print('Num Levels: ' + str(self.cost(node)))
			# print(level_count)
			print('\t\tThe best state to expand with a g(n) = ' + str(self.cost(node)))
			node.print()
			level_count += 1
	def a_star_mis(self, my_game=None):

		if my_game is None:

			my_game = self.my_game

		# my_game.print()

		# Initialize Variables
		self.expanded_nodes = 0
		self.nodes.append(my_game)
		min_index = 0
		level_count = 0

		# print("Starting Search...")

		# Start Search
		while True:

			if len(self.nodes) == 0:
				print("Failure. Impossible to solve...")
				return None

			if len(self.nodes) > self.max_nodes:
				self.max_nodes = len(self.nodes)

			# Pop Smallest from Nodes, Append to Visited
			min_index, _  = min(enumerate(self.nodes), key=lambda x : self.g_cost(x[1]))
			node = self.nodes.pop(min_index)
			self.visited.append(node)

			# Check if Game Over
			if node.game_over(node.get_current_result(node.board)):
				# node.print()				
				print("\t\tGame Over. Found Game Winning Node...")
				print("\t\tTook " + str(node.cost) + " Levels...")
				print("\t\tExpanded " + str(self.expanded_nodes) + " Nodes...")
				print("\t\tMax number of nodes in list: " + str(self.max_nodes))
				return node

			# Expand Popped Node
			self.expand(node)
			# node.print()
			# print('Node Level: ' + str(node.cost))
			# print('Heuristic: ' + str(self.heuristic_mis(node)))
			# print(level_count)
			print('\t\tThe best state to expand with a g(n) = ' + str(self.cost(node)) + ' and h(n) = ' + str(self.heuristic_mis(node)))
			# node.print()
			level_count += 1
	def a_star_man(self, my_game=None):

		if my_game is None:

			my_game = self.my_game

		# my_game.print()

		# Initialize Variables
		self.expanded_nodes = 0
		self.nodes.append(my_game)
		min_index = 0
		level_count = 0

		# print("Starting Search...")

		# Start Search
		while True:

			if len(self.nodes) == 0:
				return None

			if len(self.nodes) > self.max_nodes:
				self.max_nodes = len(self.nodes)

			# Pop Smallest from Nodes, Append to Visited
			min_index, _  = min(enumerate(self.nodes), key=lambda x : self.g_cost(x[1], 'manhattan'))
			node = self.nodes.pop(min_index)
			self.visited.append(node)

			# Check if Game Over
			if node.game_over(node.get_current_result(node.board)):
				# node.print()				
				print("\t\tGame Over. Found Game Winning Node...")
				print("\t\tTook " + str(node.cost) + " Levels...")
				print("\t\tExpanded " + str(self.expanded_nodes) + " Nodes...")
				print("\t\tMax number of nodes in list: " + str(self.max_nodes))

				return node

			# Expand Popped Node
			self.expand(node)
			# print('Heuristic: ' + str(self.g_cost(node, 'manhattan')))
			# print(len(self.nodes))
			print('\t\tThe best state to expand with a g(n) = ' + str(self.cost(node)) + ' and h(n) = ' + str(self.heuristic_mis(node)))
			# node.print()
			level_count += 1

# evaluates search algorithms performance 
def evaluate_ai(sequence, depth):

	my_ai = ai(sequence)


	print("\nTesting " + str(depth) + "-Level Sequence:")
	game(sequence).print()

	print("\n\tUniform Cost:\n")
	start = time.time()
	assert (my_ai.uniform_cost()).cost == depth, "*** Depths Not Equal! Incorrect! ***"
	end = time.time()
	print("\t\tElapsed Time: " + str(end - start))

	print("\n\tA* Misplaced:\n")
	my_ai.reset(sequence)
	start = time.time()
	assert (my_ai.a_star_mis()).cost == depth, "*** Depths Not Equal! Incorrect! ***"
	end = time.time()
	print("\t\tElapsed Time: " + str(end - start))

	print("\n\tA* Manhattan:\n")
	my_ai.reset(sequence)
	start = time.time()
	assert (my_ai.a_star_man()).cost == depth, "*** Depths Not Equal! Incorrect! ***"
	end = time.time()
	print("\t\tElapsed Time: " + str(end - start))

# main 
def main():

	print('Main...')
	print('Starting Test...')

	""" 
		evaluate all three search algorithms
		for each game board with known
		solution depths
	"""
	evaluate_ai('12345678 ', 0)
	evaluate_ai('123456 78', 2)
	evaluate_ai('1235 6478', 4)
	evaluate_ai('1365 2478', 8)
	evaluate_ai('1365 7482', 12)
	evaluate_ai('1675 3482', 16)
	evaluate_ai('71248563 ', 20)


	print('Testing Over...')

if __name__ == "__main__":
    main()







