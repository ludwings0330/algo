import sys

if __name__ == "__main__":
    M = int(input())

    S = set()

    for i in range(M):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == 'add':
            S.add(int(command[1]))
        elif command[0] == 'remove':
            if int(command[1]) in S:
                S.remove(int(command[1]))
            pass
        elif command[0] == 'check':
            if int(command[1]) in S:
                print(1)
            else:
                print(0)
            pass
        elif command[0] == 'toggle':
            if int(command[1]) in S:
                S.remove(int(command[1]))
            else:
                S.add(int(command[1]))
        elif command[0] == 'all':
            S = {i for i in range(1, 21)}
            pass
        elif command[0] == 'empty':
            S = set()
            pass