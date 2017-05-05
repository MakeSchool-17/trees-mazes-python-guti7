import maze
import random
# random.randint(0, self.totalCells-1)

# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # Implement create_dfs
    # Create a backtracking stack
    cell_stack = []
    # Choose random cell for start - currentCell
    random_int = random.randint(0, m.total_cells - 1)
    current_cell = (m.maze_array[random_int], 0)
    # update visitedCells + 1
    visited_cells = 1

    # while you haven't visited all cells (visitedCells < totalCells)
    while visited_cells < m.total_cells:
        # get all unvisited neighbors -> cell_neighbors
        neighbors = m.cell_neighbors(current_cell[0])
        # if found some neighbors:
        if len(neighbors) > 0:
            # choose random neighbor to be the new cell
            random_cell = random.randint(0, len(neighbors) - 1)
            new_cell = neighbors[random_cell]
            print(new_cell)
            # knock down walls between new cell and current cell -> connect_cells
            m.connect_cells(current_cell[0], new_cell[0], new_cell[1])
            # Push current cell to stack
            cell_stack.append(current_cell)
            # update current_cell to new_cell
            current_cell = new_cell
            # update visitedCells + 1
            visited_cells += 1
        else:
            # Pop from stack to "backtrack" to previous cell
            current_cell = cell_stack.pop()
        # Update the vizualization
        m.refresh_maze_view()
    # Update to 'solve'. Maze is created and ready to be solved
    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
