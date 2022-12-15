import config
import time
import utils

class KTM:
    # initialize the KTM with the given tapes, and corresponding parameters (e.g., k, Gamma, delta, etc.)
    def __init__(self):
        self.name = config.name
        self.num_tapes = config.k
        self.state = config.q0
        self.tapes = config.tapes
        length = 0
        for index, tape in enumerate(self.tapes):
            length = (100 - len(tape)) // 2
            self.tapes[index] = ['#'] * length + tape + ['#'] * (100 - len(tape) - length)
        self.transition_function = config.delta
        self.final_states = config.F
        self.tape_symbols = config.Gamma
        self.pointers = [length for _ in range(self.num_tapes)]
        #print(self.pointers)
        pass

    # run the KTM with the given tapes until it halts
    def run(self):
        while self.state not in config.F:
            import os
            os.system('cls')
            self.visualize()
            time.sleep(0.8)
            self.step()
        print('Accept!')

    # run the KTM with the given tapes in one step, i.e., perform the transition function delta
    def step(self):
        tuple_tapes = tuple([tape[self.pointers[idx]] for idx, tape in enumerate(self.tapes)])
        try:
            next_state, next_symbols, next_directions = self.transition_function[(self.state, tuple_tapes)]
        except KeyError:
            print('Invalid direction: ', (self.state, tuple_tapes))
            print('KTM halted.')
            exit(1)
        self.state = next_state
        for idx, tape in enumerate(self.tapes):
            if next_symbols[idx] != '*':
                tape[self.pointers[idx]] = next_symbols[idx]
            if next_directions[idx] == 'L':
                self.pointers[idx] -= 1
            elif next_directions[idx] == 'R':
                self.pointers[idx] += 1
            elif next_directions[idx] == 'N':
                pass
            else:
                print('Invalid direction: ', next_directions[idx])
                print('KTM halted.')
                exit(1)

    # visualize the steps counter, current state, pointers, tapes of the KTM
    # TODO: learn how to perform dynamic printing
    def visualize(self):
        print('function: ', self.name)
        print('number of tapes: ', self.num_tapes)
        print('input tapes: ', config.tapes_origin[0])
        print('current state: ', self.state)
        tape_str = [''.join(tape) for tape in self.tapes]
        pointer_str = [''.join([' ' for _ in range(self.pointers[idx])] + ['^'] + [' '] * (99 - self.pointers[idx])) for
                       idx, tape in enumerate(self.tapes)]
        final_str = ''
        for i in range(len(tape_str)):
            final_str += tape_str[i] + '\n' + pointer_str[i] + '\n'
        print('\r{}'.format(final_str), end='', flush=True)

    # * in transition_function is a wildcard, add all possibilities corresponding to * to transition_function
    def add_wildcard(self):
        temp_dict = {}
        for state, idx_tuple in ktm.transition_function:
            for idx, i in enumerate(idx_tuple):
                if i == '*':
                    for j in config.Gamma:
                        new_tuple = list(idx_tuple)
                        new_tuple[idx] = j
                        new_tuple = tuple(new_tuple)
                        temp_dict[(state, new_tuple)] = ktm.transition_function[(state, idx_tuple)]
        ktm.transition_function.update(temp_dict)


if __name__ == '__main__':
    utils.check_validity()
    ktm = KTM()
    ktm.add_wildcard()
    ktm.run()



