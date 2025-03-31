import dfa

def delta(state, letter):
    transitions = {
        (1, 'a'): 2,
        (1, 'b'): 4,
        (2, 'a'): 2,
        (2, 'b'): 3,
        (3, 'a'): 2,
        (3, 'b'): 2,
        (4, 'a'): 4,
        (4, 'b'): 4
    }
    return transitions[(state, letter)]

def delta2(state, letter):
    transitions = {
        (1, 'a'): 2,
        (1, 'b'): 1,
        (2, 'a'): 3,
        (2, 'b'): 1,
        (3, 'a'): 3,
        (3, 'b'): 1,
    }
    return transitions[(state, letter)]

def generate_words():
    words = []
    for a in ['a', 'b']:
        for b in ['a', 'b']:
            for c in ['a', 'b']:
                words.append(a + b + c)
    return words

def main():
    # Instantiate two DFAs using the provided transition functions.
    A1 = dfa.DFA([1, 2, 3, 4], ['a', 'b'], delta, 1, [3])
    A2 = dfa.DFA([1, 2, 3], ['a', 'b'], delta2, 1, [3])
    
    # Convert the DFAs to NFAs using our fixed to_NFA method.
    A1_nfa = A1.to_NFA() 
    A2_nfa = A2.to_NFA()
    
    words = generate_words()
    
    print("=== Testing Original DFAs ===")
    for automaton, name in [(A1, "DFA A1"), (A2, "DFA A2")]:
        print(f"\nResults for {name}:")
        for w in words:
            print(f"  {w}: {automaton.run(w)}")
    
    print("\n=== Testing Converted NFAs ===")
    for automaton, name in [(A1_nfa, "NFA A1"), (A2_nfa, "NFA A2")]:
        print(f"\nResults for {name}:")
        for w in words:
            automaton.accepted = False  # Reset the flag for each word
            print(f"  {w}: {automaton.run(w, automaton.q0)}")

if __name__ == "__main__":
    main()