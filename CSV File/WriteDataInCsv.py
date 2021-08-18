import csv
f= open("C:/Users/ramadhma/Selenium/Write.csv",'w',newline="")
csv_W=csv.writer(f)
csv_W.writerow(['Hello',12,1312])
csv_W.writerow(['Hello1',13,1312131])
csv_W.writerow(['Hello11',14,13121313])
csv_W.writerow(['Hello111',15,13121313])
csv_W.writerow(['Hello1111',16,13121313])

f.close()