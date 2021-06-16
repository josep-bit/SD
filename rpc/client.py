import xmlrpc.client

# nomber of workers
n_workers = 0
file = []

class client:
    def __init__(self, code):
        self.code = code

    def input_file_and_create_worker(self):
        global n_workers,n_file
        print("How many workers do you want to enter?")
        n_workers = input()
        print("Name of files with " ","":")
        file = input()
        f = file.split(",")
        return f

    def choose_routine(self):
        task = ''
        print("If you want to create worker, write createw")
        print("If you want to countingWords, write countW")
        print("If you want to wordCount,  write wordC")
        print("If you want another function,  write the routine")
        print("If you want to see workers, write listw")
        print("If you want to eliminate workers, write eliw")
        print("If you want to exit, write exit")
        routine = input()
        if routine == "createw":
            task = routine
        if routine == "countW":
            task = routine
        if routine == "wordC":
            task = routine
        if routine == "else":
            task = routine
        if routine == "listw":
            task = routine
        if routine == "eliw":
            task = routine
        if routine == "exit":
            task = routine
        return task


if __name__ == '__main__':
    Server = xmlrpc.client.ServerProxy('http://localhost:9000')
    print("Enter your code for user:")
    code = input()
    Server.deleteclient(code)
    client = client(code)
    task = client.choose_routine()
    while task !='exit':
        if task == "createw":
            file = client.input_file_and_create_worker()
            Server.createnWorkers(n_workers, code)
        if task == "listw":
            print(Server.list_worked())
        if task == "eliw":
            print("which is the id of worker to eliminate?")
            id_worker = input()
            Server.remove_worker(int(id_worker))
            print(Server.list_worked())
        if task == "countW":
            Server.EnqueRedisTask(file, task, code)
            print(Server.add_value(code))
        if task == "wordC":
            Server.EnqueRedisTask(file, task, code)
            x = Server.has_dic(code)
            for i in list(x):
                print(str(i))
        task = client.choose_routine()