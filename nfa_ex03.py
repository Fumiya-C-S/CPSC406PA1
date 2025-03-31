import nfa
import dfa

def generate_words(alphabet, max_length=3):
    """
    Generate all words over the given alphabet from length 0 to max_length.
    """
    words = []
    def helper(prefix, length):
        if length == 0:
            words.append(prefix)
        else:
            for symbol in alphabet:
                helper(prefix + symbol, length - 1)
    for l in range(max_length + 1):
        helper("", l)
    return words

def main():
    # --- Define NFAs ---
    # NFA A1
    A1dict = {
        ("q0", "0"): ["q0", "q1"],
        ("q0", "1"): [],
        ("q1", "0"): [],
        ("q1", "1"): ["q0"]
    }
    A1 = nfa.NFA(set(["q0", "q1"]), set(["0", "1"]), A1dict, "q0", set(["q1"]), False)

    # NFA A2
    A2dict = {
        ("q0", "0"): ["q0", "q1"],
        ("q0", "1"): ["q0"],
        ("q1", "0"): [],
        ("q1", "1"): ["q2"],
        ("q2", "0"): ["q2"],
        ("q2", "1"): ["q2"]
    }
    A2 = nfa.NFA(set(["q0", "q1", "q2"]), set(["0", "1"]), A2dict, "q0", set(["q2"]), False)

    # NFA A3
    A3dict = {
        ("q0", "0"): ["q0", "q1"],
        ("q0", "1"): ["q0"],
        ("q1", "0"): [],
        ("q1", "1"): ["q2"],
        ("q2", "0"): ["q2"],
        ("q2", "1"): ["q2"]
    }
    A3 = nfa.NFA(set(["q0", "q1", "q2"]), set(["0", "1"]), A3dict, "q0", set(["q0", "q1"]), False)

    # NFA A4
    A4dict = {
        ("q0", "0"): ["q0"],
        ("q0", "1"): ["q0", "q1"],
        ("q1", "0"): ["q2"],
        ("q1", "1"): ["q2"],
        ("q2", "0"): ["q3"],
        ("q2", "1"): ["q3"],
        ("q3", "0"): ["q4"],
        ("q3", "1"): ["q4"],
        ("q4", "0"): ["q4"],
        ("q4", "1"): ["q4"]
    }
    A4 = nfa.NFA(set(["q0", "q1", "q2", "q3", "q4"]), set(["0", "1"]), A4dict, "q0", set(["q4"]), False)

    # New NFA (A5) with a different alphabet.
    A5dict = {
        ("p", "a"): ["p", "q"],
        ("p", "b"): ["r"],
        ("q", "a"): ["r"],
        ("q", "b"): ["p"],
        ("r", "a"): [],
        ("r", "b"): ["r"]
    }
    A5 = nfa.NFA(set(["p", "q", "r"]), set(["a", "b"]), A5dict, "p", set(["r"]), False)

    # List of NFAs to test.
    automata = [
        ("NFA A1", A1),
        ("NFA A2", A2),
        ("NFA A3", A3),
        ("NFA A4", A4),
        ("NFA A5", A5)
    ]

    # For each NFA, convert it to a DFA, run test words on both versions, and compare.
    for name, automaton in automata:
        print("\n=== Testing {} ===".format(name))
        # Convert the NFA to a DFA.
        dfa_converted = automaton.to_DFA()

        print("Comparison of results on test words:")
        
        # Generate test words using the automaton's alphabet.
        alphabet = list(automaton.Sigma)
        words = generate_words(alphabet, max_length=3)
        
        for w in words:
            # Use 'ε' to denote the empty word.
            display_word = w if w != "" else "ε"
            # Reset the accepted flag before running the original NFA.
            automaton.accepted = False
            nfa_result = automaton.run(w, automaton.q0)
            dfa_result = dfa_converted.run(w)
            print("Word '{}' -> Original NFA: {} | Converted DFA: {}".format(display_word, nfa_result, dfa_result))
        print("--------------------------------------")

if __name__ == "__main__":
    main()
