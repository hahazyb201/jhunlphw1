import random
import argparse


M = 450


def get_random_branch(pos, sdict):            
    suma = 0.0
    for poss in sdict[pos]:
        suma += poss[1]
    ran = random.random() * suma
    lab = 0.0
    for poss in sdict[pos]:
        if lab <= ran < lab + poss[1]:
            return poss[0]
        lab += poss[1]



def gen_sen(pos, sdict):                         #generate the sentence
    global M
    if M == 0:
        return "..."
    M -= 1
    words = get_random_branch(pos, sdict).split()
    for i in range(len(words)):
        if words[i] in sdict:
            words[i] = gen_sen(words[i], sdict)
    return ' '.join(words)



def gen_tree(pos, sdict):                         #generate the tree as well as the sentence
    global M
    if M == 0:
        return "..."
    M -= 1
    words = get_random_branch(pos, sdict).split()
    tree = ["(" + pos]
    for i in range(len(words)):
        if words[i] in sdict:
            tree.append(gen_tree(words[i], sdict))
        else:
            tree.append(words[i])
    tree[len(tree) - 1] += ")"
    return " ".join(tree)


parser = argparse.ArgumentParser()
parser.add_argument("-t", action="store_true")
parser.add_argument("file",nargs='?', default="grammar.gr")
parser.add_argument("repeat", nargs='?', type=int, default=1)

args = parser.parse_args()
fg = open(args.file, 'r')
num_sen = int(args.repeat)

dic = {}
for line in fg.readlines():                                                #build a dictionary to store grammars
    if len(line) == 0 or line[0] == '#' or line == '\n':
        continue
    n, l, r = line.split('\t', 2)
    if l not in dic:
        dic[l] = []
    r = r.split('#')[0].strip()
    dic[l].append((r, float(n)))

fg.close()

for num in range(num_sen):
    M = 450
    if args.t:
        tree = gen_tree("ROOT", dic)
        print(tree)
    else:
        sen = gen_sen('ROOT', dic)
        print(sen)
