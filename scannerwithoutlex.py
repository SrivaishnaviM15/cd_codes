class Scanner:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.current_pos = 0
        self.keywords = {'int', 'float', 'if', 'else', 'return', 'printf', 'main'}  # Define keywords here

    def scan(self):
        while self.current_pos < len(self.text):
            if self.text[self.current_pos].isspace():
                self.current_pos += 1
                continue
            if self.text[self.current_pos].isdigit():
                token = self.scan_number()
                token_type = 'Number'
            elif self.text[self.current_pos].isalpha():
                token = self.scan_identifier()
                token_type = 'Identifier' if token not in self.keywords else 'Keyword'
            elif self.text[self.current_pos] == '"':
                token = self.scan_string()
                token_type = 'String'
            else:
                token = self.text[self.current_pos]
                token_type = 'Symbol'
                self.current_pos += 1
            self.tokens.append((token_type, token))

    def scan_number(self):
        num = ''
        while self.current_pos < len(self.text) and (self.text[self.current_pos].isdigit() or self.text[self.current_pos] == '.'):
            num += self.text[self.current_pos]
            self.current_pos += 1
        return float(num) if '.' in num else int(num)

    def scan_identifier(self):
        identifier = ''
        while self.current_pos < len(self.text) and (self.text[self.current_pos].isalnum() or self.text[self.current_pos] == '_'):
            identifier += self.text[self.current_pos]
            self.current_pos += 1
        return identifier
    
    def scan_string(self):
        string = ''
        self.current_pos += 1  # Skip the opening double quote
        while self.current_pos < len(self.text) and self.text[self.current_pos] != '"':
            string += self.text[self.current_pos]
            self.current_pos += 1
        self.current_pos += 1  # Skip the closing double quote
        return string

    def get_tokens(self):
        return self.tokens

# Test Case

text = """
int main() {
    int a = 10;
    float b = 3.14;
    if (a < b) {
        printf("a is less than b");
    } else {
        printf("a is greater than or equal to b");
    }
    return 0;
}
"""

scanner = Scanner(text)
scanner.scan()
tokens = scanner.get_tokens()
for token in tokens:
    print(f"{token[0]}: {token[1]}")
