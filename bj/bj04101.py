def get_input():
    a, b = map(int, input().split(" "))

    if a != 0 and 0 != b:
        print("Yes" if a > b else "No ")
        get_input()


get_input()
