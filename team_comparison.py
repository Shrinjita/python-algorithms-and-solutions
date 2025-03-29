n1 = int(input())
n2 = int(input())

if n1!= n2:
    print("Two teams are not equal")
else:
    team1 = [int(input()) for _ in range(n1)]
    team2 = [int(input()) for _ in range(n2)]

    if team1 == team2:
        print("Two teams Are Equal")
    else:
        print("Two teams Are Not equal")