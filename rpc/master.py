from xmlrpc.server import SimpleXMLRPCServer
from multiprocessing import Process
import logging
from redis import Redis

checkQueue = Redis(host='localhost', port=6379, db=0)

# global var
id_worker = 0
dic = {}
proc = Process


class master:
    # Routine that execute the server rpc
    def EnqueRedis(self, key, feature):
        checkQueue.lpush(key, feature)

    def ping(self):
        return True


class workers:

    def task_to_do(self, key):
        while not quit():
            job = checkQueue.blpop(key, 10)
            result = eval(job)
            checkQueue.lpush(key,result)

    def create_worker(self, key):
        global proc, id_worker, dic
        proc = Process(target=self.task_to_do, args=(key,))
        proc.start()
        dic[id_worker] = proc
        id_worker += 1

    def list_worked(self):
        i = 0
        while i < id_worker:
            print("Worker",dic[i])
            i = i + 1

    def remove_worker(self):
        proc.kill()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    Server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True)
    Server.register_introspection_functions()
    Server.register_multicall_functions()
    Server.register_instance(master())

    # Start the server
    try:
        print('Use Control-C to exit')
        Server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
