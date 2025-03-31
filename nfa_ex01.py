import nfa

# generate words for testing
def generate_words():
    words = []
    sigma = ["0", "1"]
    for first in sigma:
        for second in sigma:
            for third in sigma:
                for fourth in sigma:
                    words.append(first + second + third + fourth)
    return words

def __main__() :
    
    # Instantiate NFA A1
    A1dict = {("q0", "0"):["q0","q1"],
              ("q0", "1"):[],
              ("q1", "0"):[],
              ("q1", "1"):["q0"]}
    A1 = nfa.NFA(set(["q0","q1"]), set([0, 1]), A1dict, "q0", set(["q1"]), False)

    # Instantiate NFA A2
    A2dict = {("q0", "0"):["q0","q1"],
              ("q0", "1"):["q0"],
              ("q1", "0"):[],
              ("q1", "1"):["q2"],
              ("q2", "0"):["q2"],
              ("q2", "1"):["q2"]}
    A2 = nfa.NFA(set(["q0","q1","q2"]), set([0, 1]), A2dict, "q0", set(["q2"]), False)
    
    # Instantiate NFA A3
    A3dict = {("q0", "0"):["q0","q1"],
              ("q0", "1"):["q0"],
              ("q1", "0"):[],
              ("q1", "1"):["q2"],
              ("q2", "0"):["q2"],
              ("q2", "1"):["q2"]}
    A3 = nfa.NFA(set(["q0","q1","q2"]), set([0, 1]), A3dict, "q0", set(["q0","q1"]), False)
    
    # Instantiate NFA A4
    A4dict = {("q0", "0"):["q0"],
              ("q0", "1"):["q0","q1"],
              ("q1", "0"):["q2"],
              ("q1", "1"):["q2"],
              ("q2", "0"):["q3"],
              ("q2", "1"):["q3"],
              ("q3", "0"):["q4"],
              ("q3", "1"):["q4"],
              ("q4", "0"):["q4"],
              ("q4", "1"):["q4"],}
    A4 = nfa.NFA(set(["q0","q1","q2","q3","q4"]), set([0, 1]), A4dict, "q0", set(["q4"]), False)
    
    
    words = generate_words()
    automatas = [A1,A2,A3,A4]

    # automatas = [A3]
    
    # test words on automata
    for X in automatas:
        #  print(f"{X.__repr__()}")
         for w in words:
            # X.run(w, "q0")
            X.accepted = False
            print(f"{w}: {X.run(w, 'q0')}")

         print("\n")


__main__()