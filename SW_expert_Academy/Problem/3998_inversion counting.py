class inversion:
    def __init__(self, num):
        self.node = num
        self.left = None
        self.right = None

    def add(self, num):
        if num > self.node: # 더 크면 오른쪽
            if self.right == None:
                self.right = inversion(num)
            else:
                next = self.right
                next.add(num)
        else:
            global ans
            ans += 1
            if self.left == None:
                self.left = inversion(num)
            else:
                next = self.left
                next.add(num)

T = int(input())
for testCase in range(1, T+1):
    N = int(input())
    inputList = list(map(int, input().split()))
    ans = 0
    Head = inversion(inputList[0])
    for n in inputList[1:]:
        Head.add(n)

    print("#%d %d" %(testCase, ans))
