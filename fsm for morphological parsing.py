class PluralFiniteStateMachine:
    def __init__(self):
        # Define states
        self.states = {'vowel', 'consonant_y', 'consonant_f', 'regular'}

        # Define transitions
        self.transitions = {
            'vowel': 'regular',
            'consonant_y': 'regular',
            'consonant_f': 'regular',  # Handle 'f' -> 'ves'
            'regular': 'regular'
        }

        # Set initial state
        self.current_state = 'regular'

    def pluralize_noun(self, noun):
        if noun[-1].lower() in {'a', 'e', 'i', 'o', 'u'}:
            self.current_state = 'vowel'
        elif noun[-1].lower() == 'y':
            self.current_state = 'consonant_y'
        elif noun[-1].lower() == 'f':
            self.current_state = 'consonant_f'

        return self.current_state == 'regular'

# Example usage
def main():
    plural_fsm = PluralFiniteStateMachine()

    # Test nouns
    test_nouns = ['cat', 'dog', 'city', 'baby', 'knife', 'leaf']

    for noun in test_nouns:
        result = plural_fsm.pluralize_noun(noun)
        if result:
            plural_form = noun + 's'
        elif noun.endswith('f'):
            plural_form = noun[:-1] + 'ves'
        else:
            plural_form = noun + ' (irregular plural)'
        print(f"The plural form of '{noun}' is '{plural_form}'.")

if __name__ == "__main__":
    main()
