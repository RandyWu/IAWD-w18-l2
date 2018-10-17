import random

v={
'1':'a',
'2':'e',
'3':'i',
'4':'o',
'5':'u',
'6':'y',
}

d={
'1':'a',
'2':'b',
'3':'c',
'4':'d',
'5':'e',
'6':'f',
'7':'g',
'8':'h',
'9':'i',
'10':'j',
'11':'k',
'12':'l',
'13':'m',
'14':'n',
'15':'o',
'16':'p',
'17':'q',
'18':'r',
'19':'s',
'20':'t',
'21':'u',
'22':'v',
'23':'w',
'24':'x',
'25':'y',
'26':'z'
}

n = int(input("Number of users to generate? > "))
for i in range(0,n):
    s=d[str(random.randrange(1,27))]
    s+=v[str(random.randrange(1,7))]
    s+=d[str(random.randrange(1,27))]
    s+=v[str(random.randrange(1,7))]
    for j in range(0,4):
        s+=str(random.randrange(0,10))
    print(s)
