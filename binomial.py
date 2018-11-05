import math
import argparse

'''
Module to calculate the binomial coefficient n!/k! (n-k)!
'''

# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="n number")
parser.add_argument("-k", type=int, help="k number")
parser.add_argument("-l", "--log", action="store_true", help="show it as a log")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

#Defining logfactorial function 
def logfactorial(n,k=0): 
  ''' 
  logfactorial calculates the log(n!)
  Example:
  >>> logfactorial(5,4)
  1.6094379124341005

  >>> logfactorial(5,5)
  0.0

  >>> logfactorial(5,6)
  0.0
  '''
  if k>n:
      results = math.log(1)
      return (results)

  sumlogsn = 0
  assert type(n)==int, "error message: n should be an integer";
  assert n >= 0, "error message: n should be greater or equal to 0";

  assert type(k)==int, "error message: k should be an integer";
  assert k >= 0, "error message: k be greater or equal to 0";

  for i in range(1, n+1):
   result = math.log(i)
   sumlogsn = sumlogsn + result

  sumlogsk = 0
  assert type(k)==int, "error message: here arg1 should be an integer";
  assert k >= 0, "error message: here arg1 should be greater or equal to 0";
  for y in range(1, k+1):
   result = math.log(y)
   sumlogsk = sumlogsk + result
   prefinal = sumlogsn - sumlogsk
  return prefinal


#Defining choose function 
def choose(n,k=0): 
  ''' 
  choose calculates n!/(k! (n-k)!)
  Example:

  >>> choose(10,4)
  210

  '''
  x = n-k 
  sumlogs = 0
  result = 1
  for i in range(1, x+1):
   result = (i*result)
   second = math.log(result)
   logfunction = (logfactorial(n,k) - second)
  binomialfinal = logfunction if args.log else int(math.exp(logfunction))
  return binomialfinal

#Defining runTest function to cheack the examples
def runTests():
    print("testing the module...")
    if args.n:
        print("ignoring n for testing purposes")
    if args.k:
        print("ignoring k for testing purposes")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print(choose(args.n,args.k))