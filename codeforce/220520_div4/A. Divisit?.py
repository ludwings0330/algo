t = int(input())

while t:
    t -= 1
    rating = int(input())
    if 1900 <= rating:
        print("Division 1")
    elif 1600 <= rating < 1900:
        print("Division 2")
    elif 1400 <= rating < 1600:
        print("Division 3")
    else:
        print("Division 4")
