with open('environment.yaml', 'r') as f:
    lines = f.readlines()

with open('newenv.yaml', 'w') as f:
    for line in lines:
        line = line.rsplit('=', 1)[0] + '\n'
        f.write(line)