# .Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking 
# for n-queens problem
print("Enter the number of queens : ")
N = int(input())
board =[[0]*N for _ in range(N)]

def attack(i, j):
    for k in range(0, N):
        if(board[i][k]==1 or board[k][j]==1):
            return True
    for k in range(0, N):
        for l in range(0, N):
            if((k+l == i+j) or (k-l==i-j)):
                if board[k][l] == 1:
                    return True
            
    return False
    
def nqueen(n):
    for i in board:
        print(i)
    print('/n')
    if n==0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if(not(attack(i, j)) and board[i][j]!=1):
                board[i][j] = 1
                if nqueen(n-1) == True:
                    return True
                board[i][j] = 0
        
    return False

nqueen(N)

for i in board:
    print(i)

## time complexity is N^N. 


# print("Enter the number of queens : ")
# N = int(input())  # Input the number of queens
# board =[[0]*N for _ in range(N)]  # Create an empty chessboard of size N x N

# def attack(i, j):
#     # Check if there's any queen in the same row or column
#     for k in range(0, N):
#         if(board[i][k]==1 or board[k][j]==1):
#             return True
#     # Check if there's any queen diagonally attacking
#     for k in range(0, N):
#         for l in range(0, N):
#             if((k+l == i+j) or (k-l==i-j)):
#                 if board[k][l] == 1:
#                     return True
#     return False

# def nqueen(n):
#     for i in board:  # Print the board
#         print(i)
#     print('/n')
#     if n==0:  # If all queens are placed
#         return True
#     for i in range(0, N):  # Iterate through each row
#         for j in range(0, N):  # Iterate through each column
#             # If it's safe to place a queen in this cell
#             if(not(attack(i, j)) and board[i][j]!=1):
#                 board[i][j] = 1  # Place the queen
#                 # Recursively place remaining queens
#                 if nqueen(n-1) == True:
#                     return True
#                 board[i][j] = 0  # Backtrack if placement leads to failure
#     return False

# nqueen(N)  # Start the N-Queen problem solving

# for i in board:  # Print the final board configuration
#     print(i)
