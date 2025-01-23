def function_with_uncommon_error(a, b):
    try:
        if isinstance(b, (int, float)) and b !=0:
            result = a / b
            return result
        else:
            print("Error: Invalid operand for division")
            return None
    except TypeError:
        print("Error: Unsupported operand type(s) for /'")
        return None

#Example usage
result = function_with_uncommon_error(10, 2)
print(result)
result = function_with_uncommon_error(10, 0)
print(result)
result = function_with_uncommon_error(10, 'abc')
print(result) 