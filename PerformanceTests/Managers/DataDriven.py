import csv
from threading import Lock


class Singleton(type):
    _instances = {}
    lastCsvfile = ""

    def __call__(cls, *args, **kwargs):
        if len(args) == 0:
            csvfileName = Singleton.lastCsvfile
        else:
            csvfileName = args[0]
        if cls not in cls._instances or csvfileName != Singleton.lastCsvfile:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            Singleton.lastCsvfile = args[0]

        return cls._instances[cls]


class DataDriven(metaclass=Singleton):
    def __init__(self, fileName):
        self._lock = Lock()
        self.queuee = list()
        with open(fileName, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.enqueue(row)

    def enqueue(self, data):
        if data not in self.queuee:
            self._lock.acquire()
            self.queuee.insert(0, data)
            self._lock.release()
            return True
        return False

    def Get(self):
        if len(self.queuee) > 0:
            self._lock.acquire()
            poped = self.queuee.pop()
            self.queuee.insert(0, poped)
            self._lock.release()
            return poped

    def size(self):
        return len(self.queuee)

    def printQueue(self):
        print(self.queuee)
