TT_NUMBER = 'NUMBER'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREM = 'RPAREN'
TT_EOF = 'EOF'

class Token:
    def __init__(self, type, valor = None):
        self.type = type
        self.valor = valor

    def __repr__(self):
        if(self.valor is not None):
            return f'{self.type}:{self.valor}'
        return f'{self.type}' 
    
class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = -1
        self.atual = None
        self.avancar()

    def avancar(self):
        self.position += 1
        if(self.position < len(self.text)):
            self.atual = self.text[self.position]
        else:
            self.atual = None

    def makeToken(self):
        tokens = []
        
        while(self.atual != None):
            if(self.atual.isspace()):
                self.avancar()
            elif(self.atual == '+'):
                tokens.append(Token(TT_PLUS))
                self.avancar()
            elif(self.atual == '-'):
                tokens.append(Token(TT_MINUS))
                self.avancar()
            elif(self.atual == '*'):
                tokens.append(Token(TT_MUL))
                self.avancar()
            elif(self.atual == '/'):
                tokens.append(Token(TT_DIV))
                self.avancar()
            elif(self.atual == '('):
                tokens.append(Token(TT_LPAREN))
                self.avancar()
            elif(self.atual == ')'):
                tokens.append(Token(TT_RPAREM))
                self.avancar()
            elif(self.atual.isdigit()):
                tokens.append(Token(TT_NUMBER))
                self.avancar()        
        tokens.append(Token(TT_EOF))
        return tokens

def run(text):
        lexer = Lexer(text)
        tokens = lexer.makeToken()
        return tokens      
