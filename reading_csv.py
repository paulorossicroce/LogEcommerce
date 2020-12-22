import csv
def input_csv():
  import csv
  f = open('input.csv')
  csv_f = csv.reader(f)
  tw = []

  i = int(0)
  tw1 = int(0)
  tw2 = int(0)
  tw3 = int(0)
  tw4 = int(0)
  tw5 = int(0)

  for row in csv_f:
    tw.append(int(row[1]))
  for i in range(360):
    if tw[i] == 1:
      tw1 = int(tw1 + 1)
    if tw[i] == 2:
      tw2 = int(tw2 + 1)
    if tw[i] == 3:
      tw3 = int(tw3 + 1)
    if tw[i] == 4:
      tw4 = int(tw4 + 1)
    if tw[i] == 5:
      tw5 = int(tw5 + 1)

  return tw1, tw2, tw3, tw4, tw5


input_csv()

