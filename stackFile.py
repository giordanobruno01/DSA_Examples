class stackClass:

    def __init__(self) -> None:
        self.max = 1000
        self.top = -1
        self.stack = []
        self.message = "No error found"
        self.line = 0
        self.closingBrack = []

    def processor(self, codeLine, line):
       
        self.line = line
        brackets = ["[", "]","{","}","(",")"]
        for i in codeLine:
            if i in brackets:
                self.operation(i, codeLine, line)
        
        
    def operation(self, brack, codeLine,lineNumber):
        
        openingBrackets =["[", "{", "("]
        brackets = {"[":"]" , "{":"}" , "(":")"}
        if brack in openingBrackets:
            l = [brack,codeLine, lineNumber]
            self.stack.append(l)
            self.top +=1
        else:
            topBracket = self.stack[self.top]
            if (brack == brackets[topBracket[0]]): #]
                self.stack.pop()
                self.top -=1
            else:
                self.message = f"This bracket '{topBracket[0]}' at line {topBracket[2]} with the code  '{topBracket[1]}' is not being closed correctly at line number {lineNumber}"#
        

    def display(self):
        return self.message



