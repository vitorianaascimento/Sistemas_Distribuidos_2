import Pyro4

uri = input('Digite a URI do objeto: ')
#uri = "PYRO:obj_feca6a6d6ad64da2be55d0e41bbbf65d@localhost:56255"
math_service = Pyro4.Proxy(uri)
result1 = math_service.add(4, 5)
result2 = math_service.subtract(10, 6)
result3 = math_service.multiply(2, 8)
result4 = math_service.divide(10, 2)
print(result1, result2, result3, result4)
