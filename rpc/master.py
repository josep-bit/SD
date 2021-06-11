from functools import reduce
from xmlrpc.server import SimpleXMLRPCServer
from multiprocessing import Process
import logging
from redis import Redis
from routine import feature
checkQueue = Redis(host='localhost', port=6379, db=0)

# global var
id_worker = 0
dic = {}
proc = Process


class master:
    def __init__(self, id):
        self.id = id
        # Routine that execute the server rpc

    def EnqueRedis(self, key, feature):
        checkQueue.lpush(key, feature)

    def ping(self):
        return True


    def add_value(self,code):
        result = checkQueue.lrange(code, 0, -1)
        r = map(int, result)
        add = reduce(lambda x,y: x+y,r)
        print(add)

    def has_dic(self,code):
        result = checkQueue.lrange(code, 0, -1)
        for i in result:
            print(i, "\n")

    def task_to_do(self, key):
        while not quit():
            job = checkQueue.blpop(key, 10)
            result = eval(job)
            checkQueue.lpush(key, result)

    def createnWorkers(self, n_files, key):
        i = 0
        while i < int(n_files):
            self.create_worker(key)
            self.list_worked()
            i += 1

    def EnqueRedisTask(self,list,task,key):
        f = feature.task1()
        t = ''
        if task == 'countW':
            for i in list:
                t = f.counting_Words(i)
                self.EnqueRedis(key,t)
            self.add_value(key)
            self.remove_worker()
        else:
            for i in list:
                t = f.word_Count(i)
                self.EnqueRedis(key,t)
            self.has_dic(key)
            self.remove_worker()


    def create_worker(self, key):
        global proc, id_worker, dic
        proc = Process(target=self.task_to_do, args=(key,))
        proc.start()
        dic[id_worker] = proc
        id_worker += 1

    def list_worked(self):
        i = 0
        while i < id_worker:
            print("Worker", dic[i])
            i = i + 1

    def remove_worker(self):
        proc.kill()

    def deleteclient(self,code):
        if checkQueue.exists(code):
            checkQueue.delete(code)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    Server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True)
    Server.register_introspection_functions()
    Server.register_multicall_functions()
    Server.register_instance(master('Server'))

    # Start the server
    try:
        print('Use Control-C to exit')
        Server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
