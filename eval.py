def calculator(str):
    exp = []
    for x in expr:
        try: 
            int(x)
            exp.append(x)
        except ValueError:
            continue
    print(exp)
  
expr = "(2+(4+2)-1)-(5+8)"
calculator(expr)

def final(expr):
    x=j=0
    value = 0
    for x in range(len(expr)):
        j=x+1
        while j < len(expr):
            try:
                int(x), int(j)
                value = x
                j+=1
            except ValueError:
                j+=1
                continue
    return value
