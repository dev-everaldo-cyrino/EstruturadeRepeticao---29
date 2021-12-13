n = int(input('digite um numero: '))
n1=1
n2=1
total=0
num = ['1/1']
while n1 < n:
    n1 += 1
    n2 += 2
    num.append('+ {}/{}'.format(n1,n2))
    total += n1/n2
print('''
a sequencia de numeros é
{}
e sua soma é = {:.2f}'''.format(num,total))