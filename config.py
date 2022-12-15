# TODO:
#  1. include N/S transitions
#  2. add dead state when input not in transition function
#  3. process finite tapes question
# configuration of the KTM

# k = 2  # number of tapes
# Q = ['q0', 'q1', 'q2', 'qf']  # set of states
# Sigma = ['a', 'b', '#']  # set of input symbols
# Gamma = ['a', 'b', '#', 'c']  # set of tape symbols
# q0 = 'q0'  # initial state
# F = ['qf']  # set of final states
# # transition function
# name = ' recognize language L = {wcw | w ∈ {a, b}∗}.'
# delta = {('q0', ('a', '#')): ('q0', ('a', 'a'), ('R', 'R')), ('q0', ('b', '#')): ('q0', ('b', 'b'), ('R', 'R')),
#          ('q0', ('c', '#')): ('q1', ('c', '#'), ('N', 'L')),
#          ('q1', ('c', 'a')): ('q1', ('c', 'a'), ('N', 'L')), ('q1', ('c', 'b')): ('q1', ('c', 'b'), ('N', 'L')),
#          ('q1', ('c', '#')): ('q2', ('c', '#'), ('R', 'R')),
#          ('q2', ('a', 'a')): ('q2', ('a', 'a'), ('R', 'R')), ('q2', ('b', 'b')): ('q2', ('b', 'b'), ('R', 'R')),
#          ('q2', ('#', '#')): ('qf', ('#', '#'), ('N', 'N'))}
# # initial tapes for the KTM, each tape is a list of symbols
# tapes = [['a', 'b', 'b', 'b', 'c', 'a', 'b', 'b', 'a'], ['#', '#', '#', '#', '#', '#', '#', '#', '#']]

name = ' recognize language L = {ww^R | w ∈ {a, b}∗}.'
k = 2  # number of tapes
Q = ['q0', 'q1', 'q2', 'q3', 'qf']  # set of states
Sigma = ['a', 'b', '#']  # set of input symbols
Gamma = ['a', 'b', '#']  # set of tape symbols
q0 = 'q0'  # initial state
F = ['qf']  # set of final states
# transition function
delta = {('q0', ('#', '#')): ('q1', ('#', '#'), ('R', 'R')),
         ('q1', ('a', '#')): ('q1', ('a', 'a'), ('R', 'R')), ('q1', ('b', '#')): ('q1', ('b', 'b'), ('R', 'R')),
         ('q1', ('#', '#')): ('q2', ('#', '#'), ('L', 'L')),
         ('q2', ('a', '*')): ('q2', ('a', '*'), ('L', 'N')), ('q2', ('b', '*')): ('q2', ('b', '*'), ('L', 'N')),
         ('q2', ('#', '*')): ('q3', ('#', '*'), ('R', 'N')),
         ('q3', ('a', 'a')): ('q3', ('a', 'a'), ('R', 'L')), ('q3', ('b', 'b')): ('q3', ('b', 'b'), ('R', 'L')),
         ('q3', ('#', '#')): ('qf', ('#', '#'), ('L', 'R'))}

# initial tapes for the KTM, each tape is a list of symbols
tapes = [['#', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'a'], ['#', '#', '#', '#', '#', '#', '#', '#', '#']]
tapes_origin = tapes.copy()




