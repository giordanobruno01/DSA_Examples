class stackClass:

    def __init__(self) -> None:
        self.max = 1000
        self.top = -1
        self.stack = []
        self.message = ""
        self.line = 0

    def processor(self, codeLine, line):
        self.line = line
        brackets = ["[", "]","{","}","(",")"]
        for i in codeLine:
            if i in brackets:
                self.operation(i, codeLine)
        
        
    def operation(self, brack, codeLine):
        
        openingBrackets =["[", "{", "("]
        brackets = {"[":"]" , "{":"}" , "(":")"}
        if brack in openingBrackets:
            self.stack.append(brack)
            self.top +=1
        else:
            # top = {
            # brack = }
            if (brack == brackets[self.stack[self.top]]):
                self.stack.pop()
                self.top -=1
            else:
                self.message = f"Error at line number {self.line} \n {codeLine}"
                

        

    def display(self):
        return self.message



