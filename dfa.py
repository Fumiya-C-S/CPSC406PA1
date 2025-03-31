# a class for DFAs
# modify as needed
import nfa
class DFA :

    # init the DFA
    def __init__(self, Q, Sigma, delta, q0, F) : 
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function
        self.q0 = q0 # initial state
        self.F = F # final states
   
   # print the data of the DFA
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the DFA on the word w
    # return if the word is accepted or not
    # modify as needed
    def run(self, w):
        curState = self.q0
        for letter in w:
            if callable(self.delta):
                curState = self.delta(curState, letter)
            else:
                if (curState, letter) not in self.delta:
                    return "Rejected"
                curState = self.delta[(curState, letter)]
        return "Accepted" if curState in self.F else "Rejected"

    def refuse(self) :
        newFinalStates = self.Q - self.F
        return DFA(self.Q, self.Sigma, self.delta, self.q0, newFinalStates)


    def to_NFA(self):
        newdelta = {}
        for q in self.Q:
            for s in self.Sigma:
                newdelta[(q, s)] = [self.delta(q, s)]
        return nfa.NFA(self.Q, self.Sigma, newdelta, self.q0, self.F, False)

