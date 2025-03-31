import dfa
# a class for NFAs
# modify as needed
class NFA :

    # init the NFA
    def __init__(self, Q, Sigma, delta, q0, F, accepted) : 
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # non-deterministic transition function
        self.q0 = q0 # initial state
        self.F = F # final states
        self.accepted = accepted
   
   # print the data of the NFA
    def __repr__(self) :
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the NFA on the word w
    # return if the word is accepted or not
    # modify as needed
    def run(self, w, startState) :
        if self.accepted:
            return "Accepted"

        if len(w) != 0:
            value = self.delta[(startState, w[0])]
            if not value:

                return "Rejected"
            else:
                for state in self.delta[(startState, w[0])]:
                    if self.accepted:
                        return "Accepted"
                    if (state != startState):

                        w1 = w[1:]
                        result = self.run(w1, state)
                        if result == "Accepted":
                            return "Accepted"

                    else:

                        w1 = w[1:]
                        result = self.run(w1, startState)
                        if result == "Accepted":
                            return "Accepted"
            return "Rejected"
        else :
            for accepting in self.F:
                if(startState == accepting):

                    self.accepted = True
                    return "Accepted"

        

    def to_DFA(self):
        newQ = []
        newF = []
        newDelta = {}
        start_node = [self.q0]
        nodes_to_visit = [start_node]
        visited_nodes = [start_node]
        newQ.append(tuple(start_node))
        
        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)

            for trans in self.Sigma:
                trans = str(trans)
                new_node = []
                
                for state in current_node:
                    if (state, trans) in self.delta:
                        new_node.extend(self.delta[(state, trans)])
                new_node = sorted(set(new_node))
                if new_node:
                    current_key = tuple(current_node)
                    new_key = tuple(new_node)
                    newDelta[(current_key, trans)] = new_key
                    
                    if new_node not in visited_nodes:
                        visited_nodes.append(new_node)
                        nodes_to_visit.append(new_node)
                        newQ.append(new_key)
                        accepting = any(state in self.F for state in new_node)

                        if accepting:
                            newF.append(new_key)
        return dfa.DFA(newQ, self.Sigma, newDelta, (self.q0,), newF)

