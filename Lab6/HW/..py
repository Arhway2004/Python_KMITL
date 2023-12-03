import curses

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking input

    # Set up initial positions
    paddle1_y = paddle2_y = 0
    ball_y, ball_x = curses.LINES // 2, curses.COLS // 2
    ball_dy, ball_dx = 1, 1

    score1 = score2 = 0

    while True:
        stdscr.clear()

        # Draw paddles
        stdscr.addch(paddle1_y, 0, '|')
        stdscr.addch(paddle2_y, curses.COLS - 1, '|')

        # Draw ball
        stdscr.addch(ball_y, ball_x, 'o')

        # Display scores
        stdscr.addstr(0, curses.COLS // 2 - 5, f"Player 1: {score1} | Player 2: {score2}")

        # Get user input
        key = stdscr.getch()

        # Update paddle positions
        if key == ord('w') and paddle1_y > 0:
            paddle1_y -= 1
        elif key == ord('s') and paddle1_y < curses.LINES - 1:
            paddle1_y += 1
        elif key == curses.KEY_UP and paddle2_y > 0:
            paddle2_y -= 1
        elif key == curses.KEY_DOWN and paddle2_y < curses.LINES - 1:
            paddle2_y += 1

        # Update ball position
        ball_y += ball_dy
        ball_x += ball_dx

        # Ball collision with walls
        if ball_y == 0 or ball_y == curses.LINES - 1:
            ball_dy *= -1

        # Ball collision with paddles
        if ball_x == 1 and paddle1_y <= ball_y < paddle1_y + 3:
            ball_dx *= -1
        elif ball_x == curses.COLS - 2 and paddle2_y <= ball_y < paddle2_y + 3:
            ball_dx *= -1

        # Ball out of bounds
        if ball_x == 0:
            score2 += 1
            ball_y, ball_x = curses.LINES // 2, curses.COLS // 2
        elif ball_x == curses.COLS - 1:
            score1 += 1
            ball_y, ball_x = curses.LINES // 2, curses.COLS // 2

        stdscr.refresh()

        # Break the loop if a player wins
        if score1 >= 5 or score2 >= 5:
            break

curses.wrapper(main)
