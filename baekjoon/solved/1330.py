if __name__ =="__main__":
    A, B = map(int, input().split())
    st = '=='
    if A>B:
        st = '>'
    elif A<B:
        st = '<'
    print(st)
