import operator as op

x = int(input())
operations = (op.gt, op.lt, op.ge, op.le, op.ne, op.eq)
for action in operations:
    print(action(x, 0))
