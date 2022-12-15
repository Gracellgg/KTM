import random
import config


# random generate k tapes with non-empty length n with Sigma
def random_generate_tapes(n):
    tapes = []
    for i in range(config.k):
        tape = []
        for j in range(n):
            tape.append(random.choice(config.Sigma))
        tapes.append(tape)
    return tapes


# random generate a delta function based on the given Q, Gamma, F and number of tape k
def random_generate_delta():
    delta = {}
    for q in config.Q:
        if q not in config.F:
            for index in range(0, len(config.Gamma) ** config.k):
                read = []
                for i in range(config.k):
                    read.insert(0, config.Gamma[index % len(config.Gamma)])
                    index = index // len(config.Gamma)
                read = tuple(read)
                q1 = random.choice(config.Q)
                write = []
                for i in range(config.k):
                    write.append(random.choice(config.Gamma))
                write = tuple(write)
                move = []
                for i in range(config.k):
                    move.append(random.choice(['L', 'R']))
                move = tuple(move)
                delta[(q, read)] = (q1, write, move)
    return delta

def check_validity():
    # check whether the transition function is complete and not including invalid symbols
    # check whether the initial tapes are valid, i.e., only contain symbols in Sigma
    for key in config.delta:
        if key[0] not in config.Q or (key[1][0] or key[1][1]) not in config.Gamma:
            print('Invalid transition function: ', key)
            exit(1)
    for tape in config.tapes:
        for symbol in tape:
            if symbol not in config.Sigma:
                print('Invalid tape symbol: ', symbol)
                exit(1)
    return True

if __name__ == '__main__':
    # print(random_generate_tapes(10))
    print(random_generate_delta())
