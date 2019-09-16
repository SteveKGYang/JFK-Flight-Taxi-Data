#coding=utf-8

with open("./airline_info/flights.csv") as f:
    f1 = open("./airline_JFK/JFK_arrival.csv","a+")
    count = 0
    for line in f:
        data = line.split(",")
        if len(data)>=10 and data[8]=='JFK':
            #输入数据分别是到达月份，到达天数，到达时间
            s = data[1]+','+data[2]+','+data[21]+'\n'
            f1.write(s)
        count += 1
        if count%100000==0:
            print(str(count)+' lines processed.')
    f1.close()
f.close()