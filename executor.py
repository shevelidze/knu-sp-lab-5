class Executor:
    def __init__(self, ast):
        self.ast = ast
        self.binary_operations_semantics = {
            '+': lambda a, b: ('number', a[1] + b[1]),
            '-': lambda a, b: ('number', a[1] - b[1]),
            '*': lambda a, b: ('number', a[1] * b[1]),
            '/': lambda a, b: ('number', a[1] / b[1]),
        }

        self.unary_operations_semantics = {
            '-': lambda a: ('number', -a[1]),
            '+': lambda a: ('number', a[1])
        }

    def execute(self):
        return self.__execute_operation(self.ast)

    def __execute_operation(self, operation):
        operation_type = operation[0];

        if operation_type == 'grouped':
            return self.__execute_operation(operation[1]);
        elif operation_type == 'number':
            return operation
        elif operation_type == 'binop':
            operator = operation[1]

            if operator in self.binary_operations_semantics:
                return self.binary_operations_semantics[operator](
                    self.__execute_operation(operation[2]),
                    self.__execute_operation(operation[3]),
                )
            else:
                raise RuntimeError(f'Unknown binary operator {operator}')
        elif operation_type == 'unary':
            operator = operation[1]

            if operator in self.unary_operations_semantics:
                return self.unary_operations_semantics[operator](
                    self.__execute_operation(operation[2])
                )
            else:
                raise RuntimeError(f'Unknown unary operation {factor}')
        else:
            raise RuntimeError(f'Unknown operation type {operation_type}')
 
