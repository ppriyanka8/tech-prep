import random

levels = ["INFO", "DEBUG", "WARNING", "ERROR"]

with open("server.log", "w")  as f:
    for i in range(100):
        level = random.choice(levels)
        f.write(f"{level}: message number {i}\n")
