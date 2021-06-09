import xmlrpc.client
from functools import reduce

from routine import feature
from rpc.master import workers, checkQueue


class client:
    def __init__(self, Identification):
        self.code = Identification
        self.work = workers()

    def add_value(self):
        result = checkQueue.lrange(self.code, 0, -1)
        self.work.remove_worker()
        r = map(int, result)
        add = reduce(lambda x, y: x + y, r)
        print(add)

    def has_dic(self):
        result = checkQueue.lrange(self.code, 0, -1)
        self.work.remove_worker()
        for i in result:
            print(i, "\n")

    def input_file_and_create_worker(self):
        i = 0
        print("How many files do you want to enter?")
        num = input()
        while i < int(num):
            self.work.create_worker(self.code)
            i = i + 1
        self.work.list_worked()
        print("Name of files with " ","":")
        file = input()
        f = file.split(",")
        return f

    def choose_routine(self, list_file):
        task = feature.task1()
        print("If you want to countingWords, you write countW")
        print("If you want to wordCount, you write wordC")
        print("If you want another function, tou write the routine")
        routine = input()
        if routine == "countW":
            for i in list_file:
                Server.EnqueRedis(self.code, task.counting_Words(i))
            self.add_value()
        if routine == "wordC":
            for i in list_file:
                Server.EnqueRedis(self.code, task.word_Count(i))
            self.has_dic()
        if routine == "else":
            Server.EnqueRedis(self.code, routine)


if __name__ == '__main__':
    Server = xmlrpc.client.ServerProxy('http://localhost:9000')
    print("Enter your code for user:")
    code = input()
    c1 = client(code)
    if checkQueue.exists(code):
        checkQueue.delete(code)

    listable = c1.input_file_and_create_worker()
    c1.choose_routine(listable)
