import socket

m, n = 10, 12 # m x n grid
charOccupied, charNonoccupied = '.', 'O'

def display_board():
    print('\n')
    for row in board:
        print()
        for col in row:
            print(col, end=' ')
    print('\n')

def move_player(deltax, deltay):
    global x, y
    board[y][x] = charNonoccupied

    x = (x + deltax) % n
    y = (y + deltay) % m
    board[y][x] = charOccupied

board, x, y = [], 0, 0
for i in range(m):
    board.append([])
    for j in range(n):
        board[i].append(charNonoccupied)
board[y][x] = charOccupied

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen()

play_time = 0

while True:
    display_board()

    client, addr = server.accept()
    if play_time == 0:
        client.send(f"Server Connected on address {addr}".encode())
    message = client.recv(1024).decode()

    if message == "Terminate":
        break

    deltaxstr, deltaystr = message.split(' ')
    deltax, deltay = int(deltaxstr), int(deltaystr)

    move_player(deltax, deltay)
    client.send(f"Player now at ({x}, {y})".encode())

    play_time += 1

client.send("Connection ended.".encode())
server.close()
