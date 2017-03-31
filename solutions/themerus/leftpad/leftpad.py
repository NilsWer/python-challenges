def leftpad(value, length):
    solution = ""
    for i in range(len(str(value))-1, len(str(value)) - length -1, -1):
        if i == -1:
            break
        solution = str(value)[i] + solution
    if length - len(str(value)) > 0:
        for i in range(length - len(str(value))):
            solution = "0" + solution
    return solution


#leftpad(1234, 5)



