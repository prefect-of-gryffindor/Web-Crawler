import csv
a='''['2020-05-04', '2020-06-26', '2020-06-27', '2020-06-28', '2020-06-04', '2020-06-15', '2020-06-20', '2020-06-29', '2020-07-01', '2020-06-18', '2020-06-21', '2020-06-13', '2020-06-30', '2020-06-03', '2020-06-17', '2020-06-16', '2020-06-22', '2020-06-14', '2020-06-23', '2020-05-11', '2020-05-13', '2020-06-25', '2020-05-26', '2020-05-24', '2020-06-19', '2020-06-08', '2020-05-18', '2020-05-15', '2020-05-05', '2020-06-07', '2020-06-12', '2020-06-06', '2020-06-24', '2020-06-02', '2020-05-09', '2020-05-29', '2020-06-10', '2020-05-30', '2020-05-14', '2020-06-09', '2020-05-19', '2020-05-06', '2020-05-10', '2020-05-07', '2020-05-08', '2020-05-22', '2020-05-17', '2020-06-11', '2020-05-31', '2020-04-17', '2020-05-23', '2020-06-01', '2020-05-25', '2020-05-12', '2020-05-20', '2020-05-16', '2020-06-05', '2020-05-21', '2020-05-28']
'''
b='''[2, 38, 58, 50, 7, 33, 32, 55, 29, 56, 25, 31, 4, 6, 24, 24, 24, 21, 28, 5, 4, 23, 2, 4, 45, 6, 3, 5, 5, 5, 24, 5, 23, 5, 6, 5, 3, 3, 2, 3, 3, 3, 5, 4, 5, 2, 3, 1, 4, 1, 1, 2, 1, 1, 3, 1, 4, 2, 1]
'''
a=eval(a)
b=eval(b)
print(b)
data=[]
csvfile = open("csv_test.csv","w",newline = "")
writer = csv.writer(csvfile)
for aa,bb in zip(a,b):
    data.append([aa,bb])
writer.writerows(data)
#关闭csv对象
csvfile.close()