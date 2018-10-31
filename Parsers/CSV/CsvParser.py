import csv
class CsvParser:
    def __init__(self,filePath):
        self.csvFile=open(filePath, 'r')

    def GetCsvLinesAsList(self,delimiter):
        return list(csv.reader(self.csvFile, delimiter=delimiter))

    def GetCsvLinesAsDictionary(self,delimiter):
        return csv.DictReader(self.csvFile, delimiter=delimiter)

    def GetColByName(self,colName,delimiter,descending=True):
        col=[]
        reader = csv.DictReader(self.csvFile, delimiter=delimiter)
        for row in reader:
            col.append(row[colName])
        return list.sort(col,reverse=descending)