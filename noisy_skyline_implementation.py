# -*- coding: utf-8 -*-
"""Noisy Skyline Implementation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WF8UXH8EeQFBPR5nhNmrQ0IBtdNSAmhZ
"""

import random
import math

def oracle(v1, v2, dim, deltaMain):
    # return v1[dim] >= v2[dim] with error probability deltaMain
    v1_comp = v1[dim]
    v2_comp = v2[dim]
    truthful = random.random()
    if v1_comp >= v2_comp:
        return True if truthful > deltaMain else False
    else:
        return False if truthful > deltaMain else True

def BoostProb(command, p, q, i, deltaMain, delta1, delta2):
    num_true = 0
    num_false = 0
    
    num_calls = 0
    while num_true - num_false < math.log(1/delta1) and num_false - num_true < math.log(1/delta2):
        if command == "dominates":
            query, calls = Dominates(p, q, deltaMain)
            num_calls += calls
        elif command == "oracle":
            query = not oracle(q, p, i, deltaMain)
            num_calls += 1
        else:
            return False, num_calls
        if query:
            num_true += 1
        else:
            num_false += 1
    if num_true - num_false >= math.log(1/delta1):
        return True, num_calls
    else:
        return False, num_calls

v1 = (1, 2)
v2 = (2, 1)
trials = 1000
num_correct = 0
p = 0.3
d1 = 0.01
d2 = 0.1
dim = 1
for _ in range(trials):
    output, calls = BoostProb("dominates", v1, v2, dim, p, d1, d2)
    if output == False:
        num_correct += 1
    # print([Dominates(v1, v2, p)[0] for _ in range(5)])
print(num_correct/trials, 1 - d2 if (v1[dim] >= v2[dim]) else 1 - d1)

v1 = (1, 2)
v2 = (2, 1)
trials = 10000
num_correct = 0
p = 0.3
d1 = 0.01
d2 = 0.1
dim = 1
for _ in range(trials):
    if BoostProb("oracle", v1, v2, dim, p, d1, d2) == (v1[dim] >= v2[dim]):
        num_correct += 1
print(num_correct/trials, 1 - d2 if (v1[dim] >= v2[dim]) else 1 - d1)

v1 = (1, 2)
v2 = (2, 1)
trials = 10000
num_correct = 0
p = 0.1
d1 = 0.01
d2 = 0.1
dim = 0
for _ in range(trials):
    if BoostProb("oracle", v1, v2, dim, p, d1, d2) == (v1[dim] >= v2[dim]):
        num_correct += 1
print(num_correct/trials, 1 - d2 if (v1[dim] >= v2[dim]) else 1 - d1)

v1 = (2, 1)
v2 = (1, 2)
trials = 10000
num_correct = 0
p = 0.1
d1 = 0.01
d2 = 0.1
dim = 0
for _ in range(trials):
    if BoostProb("oracle", v1, v2, dim, p, d1, d2) == (v1[dim] >= v2[dim]):
        num_correct += 1
print(num_correct/trials, 1 - d2 if (v1[dim] >= v2[dim]) else 1 - d1)

def Dominates(p,q, deltaMain):
    num_calls = 0
    for i in range(0,len(p)):
        cond, calls = BoostProb("oracle", q, p, i, deltaMain, 1/(16*len(p)), 1/16)
        num_calls += calls
        if cond:
            # print(q, p, i)
            return False, num_calls
    return True, num_calls

import numpy as np
v1 = (1, 1)
v2 = (1, 1)
print(np.all([v1[i] >= v2[i] for i in range(len(v2))]))
trials = 10000
num_correct = 0
p = 0.3
for _ in range(trials):
    output, calls = Dominates(v1, v2, p)
    # print(output)
    if output == np.all([v1[i] >= v2[i] for i in range(len(v2))]):
        num_correct += 1
print(1 - num_correct/trials, 1/16)

import numpy as np
v1 = (2, 1)
v2 = (3, 3)
print(np.all([v1[i] >= v2[i] for i in range(len(v2))]))
trials = 10000
num_correct = 0
p = 0.3
for _ in range(trials):
    output,calls = Dominates(v1, v2, p)
    # print(output)
    if output == np.all([v1[i] >= v2[i] for i in range(len(v2))]):
        num_correct += 1
print(1 - num_correct/trials, 1/16)

import numpy as np
v1 = (2, 2)
v2 = (1.5, 1.5)
print(np.all([v1[i] >= v2[i] for i in range(len(v2))]))
trials = 10
num_correct = 0
p = 0.3
for _ in range(trials):
    output, calls = Dominates(v1, v2, p)
    # print(output)
    if output == np.all([v1[i] >= v2[i] for i in range(len(v2))]):
        num_correct += 1
print(1 - num_correct/trials, 1/16)

import numpy as np
v1 = (1, 1)
v2 = (5, 3)
print(np.all([v1[i] >= v2[i] for i in range(len(v2))]))
trials = 100
num_correct = 0
p = 0.3
d1 = 0.1
d2 = 0.1
for _ in range(trials):
    output, calls = BoostProb("dominates", v1, v2, 0, p, d1, d2)
    # print(output)
    if output == np.all([v1[i] >= v2[i] for i in range(len(v2))]):
        num_correct += 1
print(1 - num_correct/trials, 1/16)

def SetDominates(S, q, delta1, delta2, deltaMain):
    num_calls = 0
    for i in range(len(S)):
        cond, calls = BoostProb("dominates", S[i], q, 0, deltaMain, delta1/len(S), delta2)
        num_calls += calls
        if cond:
            print(i, S[i], q)
            return True, num_calls
    return False, num_calls

s1 = [(1, 1)]
v2 = (5, 3)
trials = 1000
num_correct = 0
p = 0.1
d1 = 0.01
d2 = 0.1
for _ in range(trials):
    cond, calls = SetDominates(s2, v2, d1, d2, p)
    if not cond:
        num_correct += 1
print(num_correct/trials)

s1 = [(1, 1), (3,5)]
v2 = (5, 3)
trials = 10
num_correct = 0
p = 0.8
d1 = 0.01
d2 = 0.1
for _ in range(trials):
    if not SetDominates(s2, v2, d1, d2, p):
        num_correct += 1
print(num_correct/trials)

s1 = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (99, 1), (97, 5)]
v2 = (1, 99)
trials = 10
num_correct = 0
p = 0.8
d1 = 0.01
d2 = 0.1
for _ in range(trials):
    cond, calls =SetDominates(s2, v2, d1, d2, p)
    if not cond:
        num_correct += 1
print(num_correct/trials)

def Lex(p,q,deltaMain):
    num_calls = 0
    for i in range(0,len(p)):
        cond1, calls1 = BoostProb("oracle", p, q, i, deltaMain, 1/(32*len(p)), 1/32)
        num_calls += calls1
        if cond1:
            return True, num_calls
        else:
            cond2, calls2 = BoostProb("oracle", q, p, i, deltaMain, 1/(32*len(p)), 1/32)
            num_calls += calls2
            if cond2:
                return False, num_calls
    return True, num_calls

v1 = (1, 2)
v2 = (2, 1)
trials = 10000
num_correct = 0
p = 0.7
d1 = 0.4
d2 = 0.4
for _ in range(trials):
    if Lex(v2, v1, p):
        num_correct += 1
print(num_correct/trials)

def argmax_lex(a):
    return max(enumerate(a), key=lambda a:a[1])[0]
def argmax_rand(a):
    b = np.array(a)
    return np.random.choice(np.flatnonzero(b == b.max()))
def MaxLex(p, S, delta, deltaMain, use_argmax_lex = True, use_update = (1, 0.5, 1, -2), expected=None, use_cond = False):
    if len(S) == 1:
        return S[0], 0
    c = []
    for i in range(0,len(S)):
        c.append(math.log(1/delta))
    compl = False
    num_calls = 0
    if use_argmax_lex:
        argmax = lambda x: argmax_lex(x)
    else:
        argmax = lambda x: argmax_rand(x)
    rounds = 0
    if expected:
        ind = S.index(expected)
        prev = c[ind]
    num_increased = 0
    while not compl:
        q1Star = argmax(c)
        q1 = S[q1Star]
         
        cStar = c[:q1Star] + c[q1Star + 1:]
        q2Star = argmax(cStar)
        q2Star = q2Star + 1 if q2Star >= q1Star else q2Star
        q2 = S[q2Star]
        
        cond1, calls1 = Lex(q1,q2,delta)
        num_calls += calls1
        if cond1:
            x = q1
            xStar = q1Star
            y = q2Star
        else:
            x = q2
            xStar = q2Star
            y = q1Star
        
        c[y] = c[y] - use_update[0]
            
        cond2, calls2 = Dominates(x, p, deltaMain)
        num_calls += calls2
        if cond2:
            c[xStar] = c[xStar] + use_update[1]
        else:
            c[xStar] = c[xStar] - use_update[2]
        
        cond = (c[q2Star] <= use_update[3])
        if len(c) > 2 and use_cond:
            remaining = c[:min(q1Star, q2Star)] + c[min(q1Star, q2Star)+1:max(q1Star, q2Star)] + c[max(q1Star, q2Star)+1:]
            cond = cond and np.all([x <= -2 for x in remaining])
        if cond:
            compl = True
        rounds += 1
        if expected:
            curr = c[ind]
            if curr == prev + use_update[1]:
                num_increased += 1
            else:
                num_increased = num_increased
            prev = curr
    print(c, S)
    print(num_increased/rounds)
    return S[argmax(c)], num_calls

x = [(5,3), (3, 3), (5, 7), (6, 1)]
v1 = (3, 5)
expected = (5, 7)
lexexpected = (9,1)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, expected=expected)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(5,3), (3, 3), (5, 7), (6, 1)]
v1 = (3, 5)
expected = (5, 7)
lexexpected = (9,1)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, expected=expected, use_cond = False)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(7,3), (3, 3), (5, 7), (6, 1)]
v1 = (3, 5)
expected = (5, 7)
lexexpected = (6,1)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, expected=expected, use_cond = False)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(8,3), (3, 5), (5, 7), (9, 1)]
v1 = (3, 5)
expected = (5, 7)
lexexpected = (9,1)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, expected=expected)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(8,3), (3, 5), (5, 7), (9, 1)]
v1 = (3, 5)
expected = (5, 7)
lexexpected = (9,1)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, expected=expected, use_update = (1, 1, 1.1, -2))
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(8,3), (6,6), (3, 5), (5, 7)]
v1 = (3, 5)
expected = (6, 6)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, expected=expected)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set((8,3)):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(8,3), (3, 5), (1, 5), (5, 1)]
v1 = (3, 5)
expected = (3, 5)
lexcorrect = (8, 3)
trials = 1000
p = 0.
expected_p = 0.01
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, expected=expected, use_update = (1, 4, 1.1, -2))
    print(output)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexcorrect):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(8,3), (3, 5), (1, 5), (5, 1)]
v1 = (3, 5)
expected = (3, 5)
lexcorrect = (8, 3)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, expected=expected, use_update=(1, 1, 1, -2))
    print(output)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexcorrect):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(8,3), (7,7), (3, 5)]
v1 = (3, 5)
expected = (7, 7)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, expected=expected)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set((8,3)):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (1, 99), (99, 1), (97, 5)]
v1 = (1, 99)
expected = (1, 99)
lexexpected = (99, 1)
trials = 1000
p = 0.3
expected_p = 0.1
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, expected=expected, use_update = (1, 4, 3, -2), use_cond = True)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (1, 99), (99, 1), (97, 5)]
v1 = (1, 99)
expected = (1, 99)
lexexpected = (99, 1)
trials = 1000
p = 0.1
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, expected=expected, use_update = (1, 4, 1.1, -2), use_cond = True)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (1, 99), (99, 1), (97, 5)]
v1 = (97, 5)
expected = (97, 5)
lexexpected = (99, 1)
trials = 1000
p = 0.1
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, expected=expected, use_update = (1, 1, 1, -2), use_cond = True)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (1, 99), (99, 1), (97, 5)]
v1 = (97, 5)
expected = (97, 5)
lexexpected = (99, 1)
trials = 1000
p = 0.3
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, expected=expected, use_cond = True)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set(lexexpected):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (1, 99), (99, 1), (97, 5)]
v1 = (1, 99)
expected = (1, 99)
trials = 1000
p = 0.
expected_p = 0.05
wrong_answers = set([])
num_correct = 0
num_lexcorrect = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, expected=expected, use_cond = False)
    if set(output) == set(expected):
        num_correct += 1
    elif set(output) == set((99, 1)):
        num_lexcorrect += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
print(1 - num_lexcorrect/trials, expected_p)

x = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (1, 99), (99, 1), (97, 5)]
v1 = (1, 99)
expected = (1, 99)
trials = 1000
p = 0.2
expected_p = 0.1
wrong_answers = set([])
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True)
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False)
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, use_update = (1, 1, 1, -2))
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, use_update = (1, 1, 1, -2))
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)

x = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (1, 99), (99, 1), (97, 5)]
v1 = (1, 99)
expected = (1, 99)
trials = 500
values = []
for one in range(1, 11):
    for two in range(1, 21):
        for three in range(1, 31):
            p = 0.2
            expected_p = 0.1
            wrong_answers = set([])
            num_correct = 0
            for _ in range(trials):
                s = x.copy()
                random.shuffle(s)
                output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, use_update = (one, two, three, -2))
                if set(output) == set(expected):
                    num_correct += 1
                else:
                    wrong_answers.add(output)
            print("args;", one, two, three)
            print(wrong_answers)
            print(1 - num_correct/trials, expected_p)
            values.append((1 - num_correct/trials, expected_p, wrong_answers, one, two, three))

x = [(1, 1), (0.5, 0.5), (0.25, 0.25), (0.1, 0.1), (0.01, 0.01), (2, 2), (1, 99), (99, 1)]
v1 = (1, 99)
trials = 100
expected = (1, 99)
num_correct = 0
p = 0.1
expected_p = 0.1
wrong_answers = set([])
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True)
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False)
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, use_update = (1, 1, 1, -2))
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, use_update = (1, 1, 1, -2))
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)

s = [(1, 1), (2, 2), (1, 99), (99, 1)]
v1 = (1, 99)
expected = (1, 99)
trials = 1000
p = 0.2
expected_p = 0.1
wrong_answers = set([])
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True)
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False)
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True, use_update = (1, 1, 1, -2))
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)
num_correct = 0
for _ in range(trials):
    s = x.copy()
    random.shuffle(s)
    output, calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = False, use_update = (1, 1, 1, -2))
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)

s = [(1, 1), (3, 3), (5, 3), (3, 5)]
v1 = (3, 3)
trials = 1000
expected = (5,3)
num_correct = 0
p = 0.3
expected_p = 0.1
wrong_answers = set([])
for _ in range(trials):
    output, num_calls = MaxLex(v1, s, expected_p, p, use_argmax_lex = True)
    if set(output) == set(expected):
        num_correct += 1
    else:
        wrong_answers.add(output)
print(wrong_answers)
print(1 - num_correct/trials, expected_p)

s = [(1, 1), (2, 2), (3, 5), (5, 3), (7, 7), (1, 99), (99, 1), (97, 5)]
v1 = (1, 99)
trials = 10
num_correct = 0
p = 0.1
d1 = 0.4
d2 = 0.4
for _ in range(trials):
    output, calls = MaxLex(v1, s, 0.01, p, use_argmax_lex = False, )
    if output == (1, 99):
        num_correct += 1
    else:
        print(output)
print(num_correct/trials)

def SkylineHighDim(k, X, delta, deltaMain, use_argmax_lex = True, use_update = (1, 0.5, 1, -2)):
    S = []
    C = X.copy()
    num_calls = 0
    for i in range(1,k+1):
        #Finding a point p not dominated by current skyline points
        found = False
        while len(C) > 0 and not found:
            p = C[random.randint(0,len(C) -1)]
            cond1, calls1 = SetDominates(S, p, delta/(4*k), delta/(4*k*len(X)), deltaMain)
            num_calls += calls1
            if not cond1:
                print(p, S, "not dominated")
                found = True
            else:
                print(p, S, "dominated")
                C.remove(p)
                # print(C)
        if len(C) == 0:
            return S, num_calls
        else:
            #Finding a skyline point that dominates p
            pStar, calls2 = MaxLex(p, C, delta/(2*k), deltaMain, use_argmax_lex = use_argmax_lex, use_update = use_update)
            num_calls += calls2
            C.remove(pStar)
            print(pStar, C)
            S.append(pStar)
    return S, num_calls

s = [(1, 1), (3, 5), (5, 3)]
expected = s[-2:]
k = 4
delta = 0.1
deltaMain = 0.1
trials = 10
num_correct = 0
total_calls = []
wrong_answers = set()
for i in range(trials):
    X = s.copy()
    random.shuffle(X)
    # print("trial", i)
    output, num_calls = SkylineHighDim(k,X,delta, deltaMain, use_argmax_lex = True, use_update = (1, 0.5, 1, -2))
    total_calls.append(num_calls)
    # print(output)
    if set(expected) == set(output):
        num_correct += 1
    else:
        wrong_answers.add(tuple(output))
print(num_correct / (trials + 1), 1 - deltaMain, np.mean(total_calls), np.max(total_calls))
print(wrong_answers)
num_correct = 0
total_calls = []
wrong_answers = set()
for i in range(trials):
    X = s.copy()
    random.shuffle(X)
    # print("trial", i)
    output, num_calls = SkylineHighDim(k,X,delta, deltaMain, use_argmax_lex = False, use_update = (1, 0.5, 1, -2))
    total_calls.append(num_calls)
    # print(output)
    if set(expected) == set(output):
        num_correct += 1
    else:
        wrong_answers.add(tuple(output))
print(num_correct / (trials + 1), 1 - deltaMain, np.mean(total_calls), np.max(total_calls))
print(wrong_answers)
num_correct = 0
total_calls = []
wrong_answers = set()
for i in range(trials):
    X = s.copy()
    random.shuffle(X)
    # print("trial", i)
    output, num_calls = SkylineHighDim(k,X,delta, deltaMain, use_argmax_lex = True, use_update = (1, 1, 1, -2))
    total_calls.append(num_calls)
    # print(output)
    if set(expected) == set(output):
        num_correct += 1
    else:
        wrong_answers.add(tuple(output))
print(num_correct / (trials + 1), 1 - deltaMain, np.mean(total_calls), np.max(total_calls))
print(wrong_answers)
num_correct = 0
total_calls = []
wrong_answers = set()
for i in range(trials):
    X = s.copy()
    random.shuffle(X)
    # print("trial", i)
    output, num_calls = SkylineHighDim(k,X,delta, deltaMain, use_argmax_lex = False, use_update = (1, 0.5, 1, -2))
    total_calls.append(num_calls)
    # print(output)
    if set(expected) == set(output):
        num_correct += 1
    else:
        wrong_answers.add(tuple(output))
print(num_correct / (trials + 1), 1 - deltaMain, np.mean(total_calls), np.max(total_calls))
print(wrong_answers)

def is_dominated_noiseless(a, b):
    # a is dominated by b
    return np.all([a[i] <= b[i] for i in range(len(b))])
def brute_force_noiseless(s):
    n = len(s)
    dims = len(s[0])
    optimal = []
    sorted_i = []
    optimal = set([])
    for i in range(dims):
        s_i = msort2_noiseless(s, i)
        sorted_i.append(s_i)
        max_i = s_i[-1][i]
        optima_i = []
        compl = False
        curr = -1
        while not compl and len(s_i) > 0:
            if s_i[curr][i] == max_i:
                optima_i.append(s_i[curr])
                s_i.pop(-1)
            else:
                compl = True
        if i == 0:
            optimal = optima_i
        else:
            for marg in optima_i:
                if marg not in optimal:
                    optimal.append(marg)
    changed = True
    while changed:
        changed = False
        for i in range(dims):
            optima_i = []
            compl = False
            curr = -1
            while not compl and len(s_i) > 0:
                dominated = [is_dominated_noiseless(s_i[curr], x) for x in optimal]
                if not np.any(dominated):
                    optimal.append(s_i[curr])
                    changed = True
                    s_i.pop(-1)
                else:
                    compl = True
    
    # check internally:
    new_optimal = []
    for i in range(len(optimal)):
        sublist = optimal[:i] + optimal[i + 1:]
        if not np.any([is_dominated_noiseless(optimal[i], x) for x in sublist]):
            new_optimal.append(optimal[i])
    return new_optimal

def msort2_noiseless(x, dim):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = msort2_noiseless(x[:mid], dim)
    z = msort2_noiseless(x[mid:], dim)
    while (len(y) > 0) and (len(z) > 0):
        if y[0][dim] > z[0][dim]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result

X = [tuple(x) for x in [[1,1],[2,2],[3,5],[5,3],[7,7], [1,99], [99,1],[97,5]]]
expected = brute_force_noiseless(X)
print(expected)

X = [tuple(x) for x in [[1,1],[2,2],[3,5],[5,3],[7,7], [1,99], [99,1],[97,5]]]
expected = X[-4:]
# print(expected)
k = 8
delta = 0.1
deltaMain = 0.1
trials = 100
num_correct = 0
total_calls = []
hamming_dist = []
for i in range(trials):
    X = [tuple(x) for x in [[1,1],[2,2],[3,5],[5,3],[7,7], [1,99], [99,1],[97,5]]]
    expected = X[-4:]
    # print(X)
    # print(expected)
    # print("trial", i)
    output, num_calls = SkylineHighDim(k,X,delta, deltaMain)
    total_calls.append(num_calls)
    hamming_dist.append(len(set(output) ^ set(expected)))
    # print(output)
    if set(expected) == set(output):
        num_correct += 1
    else:
        print(output)

print(num_correct / (trials + 1), 1 - deltaMain, np.mean(total_calls), np.max(total_calls), np.mean(hamming_dist), np.max(hamming_dist))

import numpy as np
import random
import stats


def oracle_max(tup, dim, error):
    v1, v2 = tup
    v1_comp = v1[dim]
    v2_comp = v2[dim]
    truthful = random.random()
    if v1_comp <= v2_comp:
        return 0 if truthful < error else 1
    else:
        return 1 if truthful < error else 0

def Lex(p,q,deltaMain):
    num_calls = 0
    for i in range(0,len(p)):
        cond1, calls1 = BoostProb("oracle", p, q, i, deltaMain, 1/(32*len(p)), 1/32)
        num_calls += calls1
        if cond1:
            return True, num_calls
        else:
            cond2, calls2 = BoostProb("oracle", q, p, i, deltaMain, 1/(32*len(p)), 1/32)
            num_calls += calls2
            if cond2:
                return False, num_calls
    return True, num_calls

def max_4(s, dim, delta, error):
    num_checks = int(2 * len(s) - (1/6)/(error)+1)
    num_calls = 0
    if num_checks % 2 == 0:
        num_checks += 1
    if len(s) == 0:
        return None
    if len(s) == 1:
        return s[0]
    else:
        curr = s[0]
        for i in range(1, len(s)):
            temp, calls = Lex(curr, s[i], delta / 2)
            num_calls += calls
            if temp != 0:
                curr = s[i]
        return curr, num_calls

def find_max(s, dim, delta, error):
    s = list(s)
    size = len(s)
    if size == 0:
        return None, 0
    if size == 1:
        return s[0], 0
    # partition s into groups of at most 4
    s2 = []
    start = 0
    num_calls = 0
    while start + 4 < size:
        subset = s[start: start + 4]
        max_picked, calls = max_4(subset, dim, delta, error)
        s2.append(max_picked)
        num_calls += calls
        start += 4
    subset = s[start: size]
    max_picked, calls = max_4(subset, dim, delta, error)
    num_calls += calls
    s2.append(max_picked)
    mx, calls = find_max(s2, dim, delta / 2, error)
    return mx, num_calls + calls


def is_dominated(v, C, delta, error):
    dims = len(v)
    num_checks = int(np.log(1/delta) * 2)
    num_calls = 0
    if num_checks % 2 == 0:
        num_checks += 1
    for c in C:
        dominated = np.zeros(dims)
        comp = (v, c)
        for dim in range(dims):
            max_i = stats.mode([oracle_max(comp, dim, error) for _ in range(num_checks)])
            num_calls += num_checks
            dominated[dim] = max_i
        if np.all(dominated == 1):
            return True, num_calls
    return False, num_calls


def skysample(khat, s, delta, error, use_argmax_lex = None, use_update = None):
    assert len(s) > 0
    sky = []
    dims = len(s[0])
    remaining = set(s)
    num_calls = 0
    for i in range(khat):
        # find non-dominated points
        to_remove = []
        for r in remaining:
            comp, calls = is_dominated(r, sky, delta, error)
            num_calls += calls
            if comp:
                to_remove.append(r)
        for r in to_remove:
            remaining.remove(r)
        if len(remaining) > 0:
            remaining = list(remaining)
            z, calls = MaxLex(remaining[0], remaining, delta/2, error)
            num_calls += calls
            sky.append(z)
            remaining = set(remaining)
            remaining.remove(z)
    return sky, num_calls

def skyline_computation(s, delta, error, alg, use_argmax_lex = None, use_update = None):
    i = 1
    k = 4
    compl = False
    num_calls = 0
    while not compl:
        r, calls = alg(k, s, delta/(2** i), error, use_argmax_lex = use_argmax_lex, use_update = use_update)
        num_calls += calls
        if len(r) < k:
            compl = True
        else:
            i += 1
            k = k**2
    return r, num_calls

trials = 100
dims = 6
data_num = 6
X = [tuple(x) for x in [[1,1],[2,2],[3,5], [1,99]]]
expected = brute_force_noiseless(X)
print(expected)
# num_vec = 2
# len_vec = 10
# s = [tuple([1 for _ in range(num_vec)]) for _ in range(len_vec)] + [tuple([5 for _ in range(num_vec)])]
# expected = [tuple([5 for _ in range(num_vec)])]
calls = []
for p in [1/6]:
    num_correct = 0
    for i in range(trials):
        random.shuffle(X)
        output, num_calls = SkyLineHighDim(X, 0.01, p)
        calls.append(num_calls)
        # print(output)
        if set(output) == set(expected):
            num_correct += 1
    print(1 - num_correct/trials, p)
    print(np.mean(num_calls), np.max(num_calls))

trials = 100
dims = 6
data_num = 6
X = [tuple(x) for x in [[1,1],[2,2],[3,5], [1,99]]]
expected = brute_force_noiseless(X)
print(expected)
# num_vec = 2
# len_vec = 10
# s = [tuple([1 for _ in range(num_vec)]) for _ in range(len_vec)] + [tuple([5 for _ in range(num_vec)])]
# expected = [tuple([5 for _ in range(num_vec)])]
calls = []
for p in [1/6]:
    num_correct = 0
    for i in range(trials):
        random.shuffle(X)
        output, num_calls = skyline_computation(X, 0.01, p, skysample)
        calls.append(num_calls)
        # print(output)
        if set(output) == set(expected):
            num_correct += 1
    print(1 - num_correct/trials, p)
    print(np.mean(num_calls), np.max(num_calls))

trials = 100
dims = 6
data_num = 6
X = [tuple(x) for x in [[1,1],[2,2],[3,5], [1,99]]]
expected = brute_force_noiseless(X)
print(expected)
# num_vec = 2
# len_vec = 10
# s = [tuple([1 for _ in range(num_vec)]) for _ in range(len_vec)] + [tuple([5 for _ in range(num_vec)])]
# expected = [tuple([5 for _ in range(num_vec)])]
calls = []
for p in [1/6]:
    num_correct = 0
    for i in range(trials):
        random.shuffle(X)
        output, num_calls = skyline_computation(X, 0.01, p, SkylineHighDim, use_argmax_lex = True, use_update = (1, 1, 1, -2))
        calls.append(num_calls)
        if set(output) == set(expected):
            num_correct += 1
    print(1 - num_correct/trials, p)
    print(np.mean(num_calls), np.max(num_calls))

trials = 100
dims = 6
data_num = 6
X = [tuple(x) for x in [[1,1],[2,2],[3,5],[5,3],[7,7], [1,99], [99,1],[97,5]]]
expected = brute_force_noiseless(X)
print(expected)
# num_vec = 2
# len_vec = 10
# s = [tuple([1 for _ in range(num_vec)]) for _ in range(len_vec)] + [tuple([5 for _ in range(num_vec)])]
# expected = [tuple([5 for _ in range(num_vec)])]
for p in [1/9]:
    num_correct = 0
    for i in range(trials):
        random.shuffle(s)
        output = skyline_computation(X, 0.1, p)
        # print(output)
        if set(output) == set(expected):
            num_correct += 1
    print(1 - num_correct/trials, p)

def is_dominated(v, C, delta, error):
    dims = len(v)
    num_checks = int(np.log(1/delta) * 3)
    if num_checks % 2 == 0:
        num_checks += 1
    for c in C:
        dominated = np.zeros(dims)
        comp = (v, c)
        for dim in range(dims):
            max_i = stats.mode([oracle_max(comp, dim, error) for _ in range(num_checks)])
            dominated[dim] = max_i
        if np.all(dominated == 1):
            return True
        else: 
            num_checks = num_checks
            # print(c, dominated)
    return False

s1 = [(1, 1), (3,5), (7, 7)]
v2 = (5, 3)
trials = 1000
num_correct = 0
p = 0.05
d1 = 0.05

for _ in range(trials):
    if is_dominated(v2, s1, d1, p):
        num_correct += 1
print(1 - num_correct/trials, d1)

def max_4(s, dim, delta, error):
    num_checks = int(2 * len(s) - (1/6)/(error)+1)
    if num_checks % 2 == 0:
        num_checks += 1
    if len(s) == 0:
        return None
    if len(s) == 1:
        return s[0]
    else:
        curr = s[0]
        for i in range(1, len(s)):
            comp = (curr, s[i])
            temp = stats.mode([oracle_max(comp, dim, error) for _ in range(num_checks)])
            if temp != 0:
                curr = s[i]
        return curr
for num_vec in range(1, 4):
    s = [(1, 1) for _ in range(num_vec)] + [(5, 5)]
    random.shuffle(s)
    dim = 1
    expected = max(s)
    trials = 10000
    for p in [1/6, 1/9, 1/12, 1/18]:
        num_correct = 0
        for i in range(trials):
            random.shuffle(s)
            if max_4(s, dim, p/2, p) == expected:
                num_correct += 1
        print((1 - num_correct / trials)/p, 1 - num_correct / trials, delta, p, len(s))



