import json

class task1:
    result = {}  # Result form second feature

    # Auxiliary feature where get all words to diccionari
    def get_Word(self,file):
        dic = {}
        index = 0
        with open(file) as line:
            x = line.readlines()
        line.close()
        count = 0
        while count < len(x):
            m = x[count].split()
            for j in m:
                dic[index] = j.strip(",.")
                index = index + 1
            count = count + 1
        return dic.values()

    # Feature that return the number of words from file
    def counting_Words(self,file):
        return len(self.get_Word(file))

    # Feature that return a dictionari whit word and the number of repetition
    def word_Count(self,file):
        num = list(self.get_Word(file))
        j = 0
        while j < self.counting_Words(file):
            x = num.count(num[j])
            self.result[num[j]] = x
            j = j + 1
        return self.dic_ToString()

    # Feature that return a
    def dic_ToString(self):
        m = json.dumps(self.result)
        return m
