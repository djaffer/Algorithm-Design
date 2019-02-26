
rowcol = input().strip() #take out leading/ending space
numofcell = rowcol.split(' ')

        
row = int(numofcell[1])
col = int(numofcell[0])
cells = []
for i in range(row):
    new_col = []
    for j in range(col):
        user_in = input().strip()
        new_col.append(user_in)
    cells.append(new_col)

result = dict()


def evaluate():
    count = 0
    total = row*col
    solved = False 
    while count < total **2 and not solved:# worst case within n^2 times run loops to solve all dependent expressions
      for i in range(row):
          for j in range(col):
              if not isFloat(cells[i][j]): # if expression 
                  val = process_cell(cells[i][j])
                  if (val):
                      cells[i][j] = val
                      result[str(i) + "-" + str(j)] = val
              count += 1
              if len(result) == row*col: #optimization if all solved break loop
                solved = True
                break

          if solved:
            break
def process_cell(exp):
    stack = []
    expression = exp.split(' ')
    for e in expression:
        if (any(x in e for x in ['+', '-', '/', '*'])):
            a = stack.pop()
            b = stack.pop()
            val = calculate(e, float(b), float(a))
            stack.append(val)
        elif e.isnumeric():
            stack.append(float(e))
        elif " " not in e:
            x, y = convToIndex(e)
            if str(x) + "-" + str(y) in result:
                val = result[str(x) + "-" + str(y)]
                if val:
                    stack.append(float(val))
            else:
                return None
    return stack.pop()


def convToIndex(rc):
    row = int(ord(rc[0]) - ord('A'))
    col = int(rc[1:]) - 1

    return (row, col)


def calculate(op, x, y):
    if op == "*":
        return x * y
    elif op == '-':
        return x - y
    elif op == '+':
        return x + y
    elif op == '/':
        return x / y
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

for i in range(row):
    for j in range(col):
        
        if not isFloat(cells[i][j]):
            val = process_cell(cells[i][j]) 
            if val:
                result[str(i) + "-" + str(j)] = val
                cells[i][j] = val
        else:
            cells[i][j] = float(cells[i][j]) #cell already numerical
            result[str(i) + "-" + str(j)] = cells[i][j]
print(rowcol)
evaluate()
for i in range(row):
    for j in range(col):
        if isFloat(cells[i][j]):
          print("{:.5f}".format(cells[i][j]))
        else:
          print("Cyclic Dependency Error")