import random
from heapq import heappush, heappop
from typing import List, Tuple, Dict, Set

# 보드 크기
BOARD_SIZE = 16

# 방향 정의
DIRECTIONS = {
   'U': (-1, 0),
   'D': (1, 0),
   'L': (0, -1),
   'R': (0, 1)
}

# 보드 생성
def create_empty_board(size: int) -> List[List[Dict[str, bool]]]:
   return [[{'U': False, 'D': False, 'L': False, 'R': False} for _ in range(size)] for _ in range(size)]

# 벽 추가 함수
def add_wall(board, x, y, direction):
   board[x][y][direction] = True
   dx, dy = DIRECTIONS[direction]
   nx, ny = x + dx, y + dy
   if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
      opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}[direction]
      board[nx][ny][opposite] = True

# 보드에 랜덤 벽 추가
def add_random_walls(board, num_walls: int):
   for _ in range(num_walls):
      x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
      direction = random.choice(list(DIRECTIONS.keys()))
      add_wall(board, x, y, direction)

# 리코셰 이동
def ricochet_move(board, robots, robot_idx, direction):
   x, y = robots[robot_idx]
   dx, dy = DIRECTIONS[direction]
   while True:
      nx, ny = x + dx, y + dy
      if not (0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE):
         break
      if board[x][y][direction]:
         break
      if (nx, ny) in robots:
         break
      x, y = nx, ny
   new_positions = list(robots)
   new_positions[robot_idx] = (x, y)
   return tuple(new_positions)

# 휴리스틱 함수 (맨해튼 거리)
def heuristic(pos1, pos2):
   return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# A* 기반 최단 경로 탐색
def astar_path(board, start_robots, goal, goal_robot_idx):
   visited: Set[Tuple[Tuple[int, int], ...]] = set()
   heap = []
   heappush(heap, (0, 0, start_robots, []))  # (우선순위, 이동수, 상태, 경로)

   while heap:
      priority, cost, robots, path = heappop(heap)
      if robots[goal_robot_idx] == goal:
         return cost, path
      if robots in visited:
         continue
      visited.add(robots)

      for i in range(len(robots)):
         for dir_key in DIRECTIONS:
               new_state = ricochet_move(board, robots, i, dir_key)
               if new_state != robots:
                  new_cost = cost + 1
                  est_total = new_cost + heuristic(new_state[goal_robot_idx], goal)
                  heappush(heap, (est_total, new_cost, new_state, path + [(i, dir_key, new_state[i])]))
   return -1, []

# 전체 시뮬레이션: 여러 목표 순차 해결
def solve_multiple_goals(board, start_robots, goals: List[Tuple[int, Tuple[int, int]]]):
   total_moves = 0
   full_path = []
   robots = start_robots

   for goal_robot_idx, goal_pos in goals:
      moves, path = astar_path(board, robots, goal_pos, goal_robot_idx)
      if moves == -1:
         return -1, []
      total_moves += moves
      full_path.extend(path)
      robots = list(robots)
      robots[goal_robot_idx] = goal_pos
      robots = tuple(robots)
   return total_moves, full_path

# 보드 생성 및 랜덤 벽 추가
board = create_empty_board(BOARD_SIZE)
add_random_walls(board, num_walls=50)

# 로봇 초기 위치 (4개)
robots = tuple((random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)) for _ in range(4))

# 무작위 목표 위치 3개 (로봇 번호, 목표 좌표)
goals = [(random.randint(0, 3), (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))) for _ in range(3)]

# 실행
total_moves, full_path = solve_multiple_goals(board, robots, goals)

print("총 이동 횟수:", total_moves)
print("목표들:", goals)
print("경로 중 첫 10단계:")
for step in full_path[:10]:
   print(f"  로봇 {step[0]} → {step[1]} → {step[2]}")