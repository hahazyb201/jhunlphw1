import random
import argparse
 
M = 500


def get_random_branch(pos, sdict):
    sum = 0.0
    for poss in sdict[pos]:
        sum += poss[1]
    ran = random.random() * sum
    lab = 0.0
    for poss in sdict[pos]:
        if lab <= ran < lab + poss[1]:
            return poss[0]
        lab += poss[1]


def gen_sen(pos, sdict):
    global M
    if M == 0:
        return "..."
    M -= 1
    words = get_random_branch(pos, sdict).split()
    for i in range(len(words)):
        if words[i] in sdict:
            words[i] = gen_sen(words[i], sdict)
    return ' '.join(words)


def gen_tree(pos, sdict):
    global M
    if M == 0:
        return "..."
    M -= 1
    words = get_random_branch(pos, sdict).split()
    tree = "(" + pos + " "
    for i in range(len(words)):
        if words[i] in sdict:
            tree += gen_tree(words[i], sdict)
        else:
            tree += words[i] + " "
    tree = tree.strip() + ")"
    return tree


parser = argparse.ArgumentParser()
parser.add_argument("-t", action="store_true")
parser.add_argument("file")
parser.add_argument("repeat")

args = parser.parse_args()
fg = open(args.file, 'r')
num_sen = int(args.repeat)

dic = {}
for line in fg.readlines():
    if len(line) == 0 or line[0] == '#' or line == '\n':
        continue
    n, l, r = line.split('\t', 2)
    if l not in dic:
        dic[l] = []
    r = r.split('#')[0].strip()
    dic[l].append((r, float(n)))

fg.close()

for num in range(num_sen):
    M = 500
    if args.t:
        tree = gen_tree("ROOT", dic)
        print (tree)
    else:
        sen = gen_sen('ROOT', dic)
        print(sen)
