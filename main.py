import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def heart_animation(message, repeat=5, delay=0.1):
    msg_chars = list(message)
    msg_len = len(msg_chars)

    for _ in range(repeat):
        idx = 0
        heart_lines = []

        for y in range(15, -15, -1):
            line = ""
            for x in range(-40, 40):  # Wider X range
                # Adjust scaling: make x "stretch" more
                if ((x * 0.04)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.04)**2 * (y * 0.1)**3 <= 0:
                    line += msg_chars[idx % msg_len]
                    idx += 1
                else:
                    line += " "
            heart_lines.append(line)

        clear_console()
        for line in heart_lines:
            print(line)

        time.sleep(delay)

# Try it with your message
heart_animation("I love you Te Amo ", repeat=20, delay=0.2)