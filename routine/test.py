import feature


class main:

    r = feature.task1()
    j = list(r.getWord('prov.txt'))
    print(j)

    print(r.countingWords('prov.txt'))

    print(r.wordCount('prov.txt'))
