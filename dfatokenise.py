class DFA:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.accept_states = {'q1'}
        self.transition = {
            'q0': {'letter': 'q1'},
            'q1': {'letter': 'q1', 'digit': 'q1'}
        }
        self.current_state = 'q0'


    def transition_function(self, symbol):
        if symbol.isalpha():
            return 'letter'
        elif symbol.isdigit():
            return 'digit'
        else:
            return None


    def is_accept_state(self):
        return self.current_state in self.accept_states


    def reset(self):
        self.current_state = 'q0'


    def tokenize(self, input_string):
        tokens = []
        current_token = ''
        for symbol in input_string:
            transition_key = self.transition_function(symbol)
            if transition_key is None:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
            else:
                next_state = self.transition[self.current_state][transition_key]
                self.current_state = next_state
                current_token += symbol
        if current_token:
            tokens.append(current_token)
        return tokens


def main():
    dfa = DFA()
    input_string = "var1 = 10 + var2"
    tokens = dfa.tokenize(input_string)
    print("Input String:", input_string)
    print("Tokens:", tokens)


if __name__ == "__main__":
    main()
