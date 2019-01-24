def pyramid(rows):
    sp_len = rows - 1
    for i in range(0, rows):
        for j in range(0, sp_len):
            print(end=" ")
        for k in range(0, i + 1):
            l = k + 1
            print(l,"", end="")
        sp_len = sp_len - 1
        print("\r")

pyramid(5)