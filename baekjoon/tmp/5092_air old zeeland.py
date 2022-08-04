import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    N = int(input())
    products = dict()

    if N == 0:
        break
    for _ in range(N):
        name, point, delay = input().split()
        products[name] = [int(point), int(delay)]

    C = int(input())
    ans = []
    n_discontented = 0
    for _ in range(C):
        customer_no, p, m = map(int, input().split())
        total = 0
        discontented = False
        for _ in range(int(p)):
            product_name = input()

            if products[product_name][1] > m:
                discontented = True
            else:
                total += products[product_name][0]
        if discontented:
            n_discontented += 1
        ans.append([customer_no, total, '*' if discontented else ''])

    for a in ans:
        print(*a)
    print("Number of discontented customers is:", n_discontented)