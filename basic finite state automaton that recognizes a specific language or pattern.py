class FiniteStateAutomaton:
    def __init__(self):
        # Define states
        self.states = {'q0', 'q1', 'q2'}
        # Define alphabet
        self.alphabet = {'a', 'b'}
        # Define transitions
        self.transitions = {
            'q0': {'a': 'q0', 'b': 'q1'},
            'q1': {'a': 'q2', 'b': 'q1'},
            'q2': {'a': 'q2', 'b': 'q1'}
        }
        # Define initial state
        self.current_state = 'q0'
        # Define accepting state
        self.accepting_state = 'q2'

    def process_input(self, input_string):
        for char in input_string:
            if char not in self.alphabet:
                # Ignore invalid characters
                continue
            
            if self.current_state not in self.transitions:
                raise ValueError(f"Invalid state '{self.current_state}' in the transition table.")
            
            self.current_state = self.transitions[self.current_state][char]

        return self.current_state == self.accepting_state


# Example usage
def main():
    automaton = FiniteStateAutomaton()

    # Test strings
    test_strings = ['aab', 'abb', 'abc', 'ab', 'baab']

    for test_string in test_strings:
        automaton.current_state = 'q0'  # Reset the current state to the initial state before processing each string
        result = automaton.process_input(test_string)
        print(f"String '{test_string}' is {'accepted' if result else 'rejected'}.")


if __name__ == "__main__":
    main()
