import xmlrpc.client

#number of files
n_files = 0

class client:
    def __init__(self, code):
        self.code = code

    def input_file_and_create_worker(self):
        global n_files
        print("How many files do you want to enter?")
        n_files = input()
        print("Name of files with " ","":")
        file = input()
        f = file.split(",")
        return f


    def choose_routine(self):
        task = ''
        print("If you want to countingWords, write countW")
        print("If you want to wordCount,  write wordC")
        print("If you want another function,  write the routine")
        routine = input()
        if routine == "countW":
            task = routine
        if routine == "wordC":
            task = routine
        if routine == "else":
            task = routine
        return task


if __name__ == '__main__':
    Server = xmlrpc.client.ServerProxy('http://localhost:9000')
    print("Enter your code for user:")
    code = input()
    Server.deleteclient(code)
    client = client(code)
    file = client.input_file_and_create_worker()
    Server.createnWorkers(n_files,code)
    task = client.choose_routine()
    Server.EnqueRedisTask(file,task,code)
