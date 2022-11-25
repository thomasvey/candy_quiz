import signal
import sys
import player as p
import result
import time
kids = [
            # Name      GPIO Pin
    p.player("Aleyna",   3),
    p.player("Aliya",    4),
    p.player("Amara",    17),
    p.player("Dalia",    13),
    p.player("Farah",    14),
    p.player("Maha",     15),
    p.player("Mayla",    16)
]

teacher = p.player("Hermann", 2, False)

# stop the Programm by Pressing CTRL+C
def signal_handler(sig, frame):
    sys.exit(0)
    
game_len = 10
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    while len(teacher.time_dots) < game_len:
        time.sleep(0.05)
    
    player = [teacher] + kids
    for p in player:
        p.disable_input()

    result.calculation(teacher, kids, delta=1)
    result.show(teacher, kids)