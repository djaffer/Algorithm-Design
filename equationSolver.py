import random
def evaluate2pass(exp):
  operator = []
  operand = []
  ops = ['+','-','/','*']
  i = 0
  n = len(exp)
  op = 0
  prev = 0
  while i < n:
    ch = exp[i]
    
    if ch == ' ' or ch =='\t':
      i += 1
      continue
    
    if ch in ops:
      op = ch
      operator.append(ch)
      i += 1
    else:
      num, i = getNumber(exp,i)
      operand.append(num)

      if op in ['*','/']:
        oper = operator.pop()
        y = operand.pop()
        x = operand.pop()
        operand.append(calculate(x,y,oper))
  
  if len(operand) == 1:
    return operand.pop()
  res = operand[0]

  j = 1
  
  for oper in operator:
    res = calculate(res,operand[j],oper)
    j += 1


 
  return res


def calculate(x,y,oper):

  if oper == "*":
    return x * y
  elif oper == '/':
    return x / y
  elif oper == '+':
    return x + y
  elif oper == '-':
    return x - y



def getNumber(exp,start):
  num = ""
  while start<len(exp):
    ch = exp[start]
    if exp[start] ==' ' or exp[start] == '/t':
      start += 1
      continue
    if (ch >= '0' and ch <='9') or ch==".":
      num += ch
    else:
      break
    start += 1
  
  return float(num),start


def evaluatePostfix(exp):
  postfix_eq= []
  operators = ['+','-','/','*']
  ops = []
  i = 0
  n = len(exp)
  while i < n:
    if exp[i] ==' ' or exp[i] == '/t':
      i += 1
      continue
    if (exp[i] in operators):
      while ops and preced(ops[-1],exp[i]):
        postfix_eq.append(ops.pop())
      ops.append(exp[i])
      op = exp[i]
      i += 1
    else:
      num,i = getNumber(exp,i)
      postfix_eq.append(num)

  while ops:
    postfix_eq.append(ops.pop())
  
  return postfixCalculate(postfix_eq)

def preced(op1, op2):
  if op1 == '*' or op1 == '/':
    return True

  if op1 == '+' or op1 == '-':
    if op2 == '+' or op2 == '-':
      return True

  return False

def postfixCalculate(exp):
  stack = []
  
  for e in exp:

    if e in ['+','-','/','*']:
      y = stack.pop()
      x = stack.pop()
      
      # print(x," ",y," ",e)
      res = calculate(float(x),float(y),e)
      stack.append(res)
    else:
      stack.append(e)
  return stack.pop()

def generate_expression(nOperators):
  ops = ['+', '/', '*', '-']
  d = random.random() * 100

  expression = []
  expression.append(d)
  for i in xrange(0, nOperators):
    c = ops[random.randint(0 , 3)]
    d = random.random() * 100
    if c == '/' and d == 0:
      d = d + 1
    expression.append(c)
    expression.append(d)

  return "".join(map(str, expression))

def test(expression):
  result_lib = eval(expression)
  result = evaluate2pass(expression)
  result_postfix = evaluatePostfix(expression)
  print("Correct Answer ", result_lib," 2 Pass:",result,"Post Fix",result_postfix)
  assert result_lib == result
  assert result_lib == result_postfix



test("5*2/2")

for i in xrange(1, 3000, 1000):
  expression = generate_expression(i)
  test(expression)
