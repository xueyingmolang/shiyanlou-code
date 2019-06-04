for i in range(1,101):
    if str(i)[0] == "7" or str(i)[-1] == "7" or i % 7 == 0:
        continue
    print(i)
