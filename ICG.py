def to_postfix(expression, precedence):
	postfix,stack = '',[]
	for i in expression:
		if i.isalpha():
			postfix += i
		else:
			if not stack:
				stack.append(i)
			elif (precedence[i] > precedence[stack[-1]]) or (i == stack[-1] and i == '^'):
				stack.append(i)
			else:
				while stack and precedence[i] <= precedence[stack[-1]]:
					postfix += stack.pop()
				stack.append(i)
	while stack:
		postfix += stack.pop()
	return postfix
def assignment(expr):
	precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
	res, expr = expr[0], expr[2:]
	three_ac, temp, count = [], [], 0
	for ch in to_postfix(expr, precedence):
		if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
			temp.append(ch)
		else:
			count += 1
			tname = 't' + str(count)
			op = tname + '='
			op2, op1 = temp.pop(), temp.pop()
			op += op1 + ch + op2
			three_ac.append(op)
			temp.append(tname)
	assg = res + '=t' + str(count)
	three_ac.append(assg)
	return three_ac
def arithmetic(expr):
	expr="k+"+expr
	three_ac = assignment(expr)
	return three_ac[:-1]
def relational(expr):
	total,index=0,100
	expr1=expr[0:4]
	count=[0,0,0,0,0]
	while "&&" in expr or "||" in expr:
		op=expr[3:5]
		if op == "&&":
			count[total]=1
		total=total+1
		expr=expr[5:len(expr)+1]
		index=getIndex(index,expr,total)	
	total=total+1
	index=getIndex(index,expr1,total)
	Conditions=total-1
	for i in range(0,Conditions):
		total=total+1
		if count[i] is 1:
			print(str(index)+":t"+str(total)+" =t"+str(total-1)+" and t"+str(i+2))
		else:
			print(str(index)+":t"+str(total)+" =t"+str(total-1)+" or  t"+str(i+2))	
		index=index+1
	return 
def getIndex(index,equation,total):
	Condition=equation[0:3]
	print(str(index)+":if "+str(Condition)+" go to "+str(index+3))
	index=index+1
	print(str(index)+":t"+str(total)+"=0")
	index=index+1
	print(str(index)+":go to "+str(index+2))
	index=index+1
	print(str(index)+":t"+str(total)+"=1")
	index=index+1
	return index
while True:
	choice = int(input('1.Assignment  2. Arithmetic  3.Relational: '))	
	if choice == 1:
		expr = input('Enter the expression: ')
		three_ac = assignment(expr)
		print('\n'.join(three_ac))
	elif choice == 2:
		expr = input('Enter the expression: ')
		al=arithmetic(expr)
		print('\n'.join(al))
	elif choice == 3:
		expr=input('Enter the expression: ')
		relational(expr)
	else:
		break
"""Input should be without brackets for all 3 ---AQID KHATKHATAY
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_8$ python3 ICG.py 
1.Assignment  2. Arithmetic  3.Relational: 3
Enter the expression: a>b&&c>d
100:if c>d go to 103
101:t1=0
102:go to 104
103:t1=1
104:if a>b go to 107
105:t2=0
106:go to 108
107:t2=1
108:t3 =t2 and t2
1.Assignment  2. Arithmetic  3.Relational: 1
Enter the expression: k=a*b-c^d/e
t1=a*b
t2=c^d
t3=t2/e
t4=t1-t3
k=t4
1.Assignment  2. Arithmetic  3.Relational: 2
Enter the expression: a*b-c^d/e
t1=a*b
t2=c^d
t3=t2/e
t4=t1-t3
1.Assignment  2. Arithmetic  3.Relational: 4
aqid98@aqid98-VPCEB34EN:~/Desktop/Practical_Exam/SPCC/Exp_8$ 
"""
