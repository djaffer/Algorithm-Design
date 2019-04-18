import random
def evaluate(exp):
  exp = exp.replace(' ','')
  vals = []
  v = ""
  operators = ['+','-','/','*']
  for i in range(len(exp)):
    n = exp[i]
    if n in operators:
      vals.append(v)
      vals.append(n)
      v = ""
    else:
      v += exp[i]
  
  vals.append(v)
  while "*" in vals or "/" in vals:
    
    res = pimdas(vals,"*/")
    i = 0
    a = ""
    b = "" 
    c = ""
    if res["*"]:
      i = res["*"]
      b = vals.pop(i)
      a = vals.pop(i-1)
      c = vals.pop(i-1)
      
    elif res["/"]:
      i = res["/"]
      b = vals.pop(i)
      a = vals.pop(i-1)
      c = vals.pop(i-1)
      
    
    vals.insert(i-1,calculate(a,b,c))
    
  while "+" in vals or "-" in vals:
    
    res = pimdas(vals,"+-")
    i = 0
    a = ""
    b = "" 
    c = ""

    if res["+"]:
      i = res["+"]
      b = vals.pop(i)
      a = vals.pop(i-1)
      c = vals.pop(i-1)
    elif res["-"]:
      i = res["-"]
      b = vals.pop(i)
      a = vals.pop(i-1)
      c = vals.pop(i-1)
    vals.insert(i-1,calculate(a,b,c))
  return float(vals.pop())
def pimdas(arr,oper):
  count = 0
  res = {"+":None,"-":None,"/":None,"*":None}
  for i in range(len(arr)):
    
    if not res["*"] and arr[i] == "*":
      res["*"] = i
      count += 1
    elif not res["/"] and arr[i] == "/":
      res["/"] = i
      count += 1
    elif not res["+"] and arr[i] == "+":
      res["+"] = i
      count += 1
    elif not res["-"] and arr[i] == "-":
      res["-"] = i
      count += 1
      
    if oper=="*/" and (res['*'] or res['/']):
      break
    
    if oper=="+-" and (res['+'] or res['-']):
      break
  return res


def calculate(x,y,z):
  x = float(x)
  z = float(z)
  if y == "+":
    return x + z
  elif y == "-":
    return x - z
  elif y == "/":
    return x / z
  elif y == "*":
    return x * z
  return -1
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
  result = evaluate(expression)
  print(result_lib," ",result)
  assert result_lib == result



test("5*2/2")
for i in xrange(1, 3000, 1000):
  expression = generate_expression(i)
  test(expression)

