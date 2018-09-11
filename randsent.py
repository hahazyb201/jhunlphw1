import random
import argparse


def gen_sen(pos,sdict):
    ran=int(random.random()*len(sdict[pos]))
    sen=sdict[pos][ran]
    words=sen.split()
    for i in range(len(words)):
        if words[i] in sdict:
            words[i]=gen_sen(words[i],sdict)
    sen=' '.join(words)
    return sen

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('repeat')

args = parser.parse_args()
fg=open(args.file,'r')
num_sen=int(args.repeat)

dic={}
for line in fg.readlines():
    if len(line)==0 or line[0]=='#' or line=='\n':
        continue
    n,l,r=line.split('\t',2)
    if l not in dic:
        dic[l]=[]
    r=r.split('#')[0].strip()
    dic[l].append(r)

fg.close()

for num in range(num_sen):
    sen=gen_sen('ROOT',dic)
    print(sen)