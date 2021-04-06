class Caculate:
    def addition(self, a, b):
        result = a+b
        if isinstance(result,float):
            result = round(result,2)
        return result
    def subtraction(self, a,b):
        result = a-b
        if isinstance(result,float):
            result = round(result,2)
        return result
    def multiplication(self, a, b):
        result = a*b
        if isinstance(result, float):
            result = round(result, 4)
        return result
    def division(self, a, b):
        try:
            result = a/b
        except ZeroDivisionError:
            print("除数为0,无法计算")
        else:
            if isinstance(result, float):
                result = round(result, 2)
            return result

