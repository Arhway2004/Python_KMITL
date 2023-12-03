# I would like to know how to return function as one line
# 3_1
def perm2(t):
    def generate_pairs(t, prefix):
        if len(prefix) == 2:
            print(prefix)
            return
        for i in range(len(t)):
            generate_pairs(t[:i] + t[i + 1:], prefix + (t[i],))

    generate_pairs(t, (), )


perm2((1, 2, 3))
# 3_2
def perm3(t):
    def generate_triples(t, prefix):
        if len(prefix) == 3:
            print(prefix)
            return
        for i in range(len(t)):
            generate_triples(t[:i] + t[i + 1:], prefix + (t[i],))

    generate_triples(t, ())

perm3((1, 2, 3, 4))

# 3_3
def perm(t, n):
    def generate_ntuples(t, prefix):
        if len(prefix) == n:
            print(prefix)
            return
        for i in range(len(t)):
            generate_ntuples(t[:i] + t[i + 1:], prefix + (t[i],))

    generate_ntuples(t, ())

perm((1, 2, 3), 3)
