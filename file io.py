def game():
    return 1283

score=game()
with open("op.txt") as f:
        op=f.read()
if int(op) < score or op=='':
    with open("op.txt",'w') as f:
        f.write(str(score))        