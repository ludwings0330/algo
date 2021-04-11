if __name__ == "__main__":
    X, Y = map(int, input().split())

    def Rev(n):
        n = str(n)
        n = n[::-1]
        return int(n)
    print(Rev(Rev(X)+ Rev(Y)))