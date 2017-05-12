import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    # TODO: Implement solve_dfs
    # Create stack for backtrack
    backtrack_stack = []
    # Set current_cell = 0
    current_cell = (0, 0)
    # Set visited cells = 0
    visited_cells = 0
    print(current_cell)
    # while current cell is not goal
    while current_cell[0] != m.total_cells - 1:  # <
        # get unvisited neighbors using cell_neighbors
        neighbors = m.cell_neighbors(current_cell[0])
        # if neighbors > 0
        print("initial: {}".format(neighbors))
        if len(neighbors) > 0:
            # choose random neighbor
            random_neighbor = random.randint(0, len(neighbors) - 1)
            # visit the new neighbor using visit_cell
            # new_cell = m.maze_array[random_neighbor]
            new_cell = neighbors[random_neighbor]

            m.visit_cell(current_cell[0], new_cell[0], new_cell[1])
            # push current cell to stack
            backtrack_stack.append(current_cell)
            # update current to new neighbor
            current_cell = new_cell
            # update visited cells
            visited_cells += 1
        # else
        else:
            # backtrack current cell using backtrack method
            m.backtrack(current_cell[0])
            # pop from the stack to current cell
            if len(backtrack_stack) > 0:
                current_cell = backtrack_stack.pop()
        # refresh_maze_view to update visualization
        m.refresh_maze_view()

    # update state to 'idle'
    m.state = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    pass


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
