# 피연산자면 무조건 출력
# ( 면 무조건 push
# ) 면 ( 나올떄까지 pop
# 연산자면 스택 top에 있는게 자신의 우선순위보다 같거나 낮으면 다 뽑아버리고 push
# +, - 의 경우 나보다 낮은 우선 순위가 없기 때문에 ( 가 나올때까치 출력한다.
# *, / 의 경우 자신의 우선 순위가 낮지 않으니까 같은 우선순위인 *, / 가 나올때 까지 pop 한다.

a = input()
stack = [] #스택
res='' #출력

for x in a:
    if x.isalpha(): #피연산자인지 아닌지 확인
        res+=x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x =='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res+=stack.pop()
            stack.pop()

#스택안에 남아있는 값들 pop
while stack:
    res += stack.pop()
print(res)