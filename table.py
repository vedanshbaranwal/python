for i in range(1,20):
    with open(f"New folder/table{i}.txt",'w') as f:
        for v in range(1,11):
            f.write (f"{i}x{v}={i*v}\n")
            