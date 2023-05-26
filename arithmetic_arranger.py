#import to use regex
import re


def arithmetic_arranger(problems, solve=False):

  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""

  if (len(problems) >= 6):
    return "Error: Too many problems."

  for problem in problems:
    if (re.search("[^\s0-9.+-]", problem)):
      if (re.search("[/]", problem) or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    firstNumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]

    if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
      return "Error: Numbers cannot be more than four digits."
    #Calculations done if solve=True 
    sum = ""
    if (operator == "+"):
      sum = str(int(firstNumber) + int(secondNumber))
    elif (operator == "-"):
      sum = str(int(firstNumber) - int(secondNumber))
    #Numbers right-aligned and put in top/bottom position
    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = operator + str(secondNumber).rjust(length - 1)
    line = ""
    res = str(sum).rjust(length)
    #dashes run along the entire length of each problem individually.
    for s in range(length):
      line += "-"
    #Four spaces between each problem
    if problem != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      second += bottom
      lines += line
      sumx += res

  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + second + "\n" + lines
  return string
