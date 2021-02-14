# CS 170 Project
# 	8-puzzle Solver using search methods
# Problems: game driver code working
# 	uc uses incorrect heuristic function
# 	manhattan distance not fully written
# 	astar misplaced written, but not working
# Solutions: replace my queue implementation
# 	with priority queue python built in
# 	finish manhattan distance

import copy, time
from enum import Enum 
from queue import PriorityQueue 

# Game Engine
class game:

	# Initialize
	def __init__(self, init_state=['1', '2', '3', '4', '5', '6', '7', '8', ' '], algorithm='uniform'):


		self.board = init_state
		if isinstance(self.board, str):
			self.board = list(self.board)
		self.correct = '12345678 '
		self.empty_index = 8
		for x in range(0, len(self.board)):
			if self.board[x] == ' ':
				self.empty_index = x

		# AI Variables
		self.algorithm = algorithm
		self.cost = 0
		self.f_n = 0

	# Operators
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

	# Utility Functions
	# Verification
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

	# Testing
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

	# Display
	def print(self):

		print('\n')
		print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
		print('-+-+-')
		print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
		print('-+-+-')
		print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
		print('\n')

	# Compare
	def __lt__(self, other):
		if self.algorithm == 'uniform':
			# print(str(self.cost) + " <= " + str(other.cost))
			# exit()
			return self.cost <= other.cost

		elif self.algorithm == 'astar':
			return self.f_n < other.f_n
# AI Search Algorithms
class ai:

	# Initialize
	def __init__(self, board=None):
		self.my_game = game(board)
		self.my_game.print()
		self.nodes = PriorityQueue()
		self.visited = list()

	# Utility
	def visited_check(self, node):

		for i in self.visited:

			if i.get_current_result() == node.get_current_result():

				return False

		return True

	# Expansion
	def expand(self, node):
		
		if self.nodes is None:

			self.nodes = PriorityQueue()


		tempGame = copy.deepcopy(node)

		if tempGame.move_up():


			if self.visited_check(tempGame):
				self.nodes.put((tempGame.cost, tempGame))
				tempGame.cost += 1
			tempGame = copy.deepcopy(node)


		if tempGame.move_down():

			if self.visited_check(tempGame):
				self.nodes.put((tempGame.cost, tempGame))
				tempGame.cost += 1
			tempGame = copy.deepcopy(node)


		if tempGame.move_left():

			if self.visited_check(tempGame):
				self.nodes.put((tempGame.cost, tempGame))
				tempGame.cost += 1
			tempGame = copy.deepcopy(node)

		if tempGame.move_right():

			if self.visited_check(tempGame):
				self.nodes.put((tempGame.cost, tempGame))
				tempGame.cost += 1
			tempGame = copy.deepcopy(node)
	def expand_a_star(self, node):
		
		if self.nodes is None:

			self.nodes = PriorityQueue()


		tempGame = copy.deepcopy(node)

		if tempGame.move_up():

			self.nodes.put((self.a_star_cost(tempGame), tempGame))
			tempGame.cost += 1
			tempGame = copy.deepcopy(node)


		if tempGame.move_down():

			self.nodes.put((self.a_star_cost(tempGame), tempGame))
			tempGame.cost += 1
			tempGame = copy.deepcopy(node)


		if tempGame.move_left():

			self.nodes.put((self.a_star_cost(tempGame), tempGame))
			tempGame.cost += 1
			tempGame = copy.deepcopy(node)

		if tempGame.move_right():

			self.nodes.put((self.a_star_cost(tempGame), tempGame))
			tempGame.cost += 1
			tempGame = copy.deepcopy(node)

	# Heuristic Calculator
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
			x_position = int(x.index(y[a]))
			y_position = a
			h = abs(x_position - y_position)
		return h
	def a_star_cost(self, node, mode='misplaced'):

		g = self.heuristic_mis(node) + node.cost

		if mode == 'manhattan':
			g = self.heuristic_man(node) + node.cost

		return g
	def cost(self, node):

		g = node.cost
		return g

	# Search Algorithms
	def uniform_cost(self, my_game=None):

		if my_game is None:

			my_game = self.my_game

		# Initialize Variables
		self.nodes.put((my_game.cost, my_game))
		min_index = 0
		level_count = 0

		print("Starting Search...")
		# Start Search
		while True:

			if self.nodes.qsize() == 0:
				print("Failure. Impossible to solve...")
				return False

			# Pop Smallest from Nodes, Append to Visited
			_, node = self.nodes.get()
			self.visited.append(node) # maybe replace with hash

			# Check if Game Over
			if my_game.game_over(my_game.get_current_result(node.board)):
				print("Found Game Winning Node. Took " + str(level_count) + " Levels...")
				return True
			
			# Expand Popped Node
			self.expand(node)
			node.print()
			print("Cost: " + str(node.cost))
			print("iter: " + str(level_count))
			level_count += 1
	def a_star_mis(self, my_game=None):

		if my_game is None:

			my_game = self.my_game

		# Initialize Variables
		self.nodes.put(my_game)
		min_index = 0
		level_count = 0

		print("Starting Search...")

		# Start Search
		while True:

			if self.nodes.qsize() == 0:
				print("Failure. Impossible to solve...")
				return False

			# Pop Smallest from Nodes, Append to Visited
			_, node = self.nodes.get()

			# Check if Game Over
			if my_game.game_over(my_game.get_current_result(node.board)):
				print("Found Game Winning Node. Took " + str(level_count) + " Levels...")
				return True

			# Expand Popped Node
			self.expand(node)
			level_count += 1
	def a_star_man(self, my_game=None):
		if my_game is None:

			my_game = self.my_game

		# Initialize Variables
		self.nodes.put(my_game)
		min_index = 0
		level_count = 0

		print("Starting Search...")

		# Start Search
		while True:

			if self.nodes.qsize() == 0:
				return False

			# Pop Smallest from Nodes, Append to Visited
			_, node = self.nodes.get()

			# Check if Game Over
			if my_game.game_over(my_game.get_current_result(node.board)):
				print("Found Game Winning Node. Took " + str(level_count) + " Levels...")
				return True

			# Expand Popped Node
			self.expand(node)
			level_count += 1

# Utility Testing
def game_testing():


    print("Starting Game!\n\n")

    # Initialize Game
    print("Initializing Game Engine...")
    my_game = game()
    my_game.print()


    # Test Game Operators
    print("Testing Basic Operations...")
    my_game.move_up()
    my_game.print()

    my_game.move_down()
    my_game.print()

    my_game.move_left()
    my_game.print()

    my_game.move_right()
    my_game.print()


    # Rapid Test
    print("Rapid Testing...")

    print("Testing Up...")
    for i in range(0, 10):
    	my_game.move_up()
    	my_game.print()


    print("Testing Down...")
    for i in range(0, 10):
    	my_game.move_down()
    	my_game.print()


    print("Testing Left...")
    for i in range(0, 10):
    	my_game.move_left()
    	my_game.print()


    print("Testing Right...")
    for i in range(0, 10):
    	my_game.move_right()
    	my_game.print()
def shuffling_testing():

	my_game = game()
	my_game.shuffling()
	return my_game.get_current_result(my_game.board)
def start_game():
	print('Starting w/ Sequence: ')
	new_game = game(shuffling_testing())
	return new_game


# Main 
def main():

	print('Main...')

	# Sequences to Test
	x = '856314 27'
	# x = '671345 82'

	# Test Uniform Cost Search
	my_ai = ai(x)
	my_ai.uniform_cost()


	# Test A Star Misplaced Search
	# x = shuffling_testing()
	# my_ai = ai(x)
	# my_ai.a_star_mis()


if __name__ == "__main__":
    main()







