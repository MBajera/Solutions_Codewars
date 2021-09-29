class Calculator(object):

    @staticmethod
    def small_eval(string):
        actions = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }
        array = string.split(" ")
        while any([a for a in array if a in "*/"]):
            for i, operator in enumerate(array):
                if operator in "*/":
                    score = actions[operator](float(array[i - 1]), float(array[i + 1]))
                    array[i - 1] = str(score)
                    array.pop(i)
                    array.pop(i)
                    break
        while any([a for a in array if a in "+-"]):
            for i, operator in enumerate(array):
                if operator in "+-":
                    score = actions[operator](float(array[i - 1]), float(array[i + 1]))
                    array[i - 1] = str(score)
                    array.pop(i)
                    array.pop(i)
                    break
        value = float(array[0])
        return value

    def evaluate(self, string):
        while any([a for a in string if a in "()"]):
            x,y = 0, 0
            for i,dig in enumerate(string):
                if dig == "(":
                    x = i
                elif dig == ")":
                    y = i
                if x and y:
                    score = self.small_eval(string[x+2:y-1])
                    break
            string = string[:x] + str(score) + string[y+1:]
        value = self.small_eval(string)
        return value

