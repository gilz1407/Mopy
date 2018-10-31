from Parsers.CSV.CsvParser import CsvParser

csvContent=CsvParser('./TestExample/names.csv')
mailLst=csvContent.GetColByName('email',',')
print(mailLst)