#coding=utf-8

for i in range(11,13):
    with open("./taxi_data_2015/yellow_tripdata_2015-"+str(i)+".csv") as f:
        f1 = open("./processed_taxi_in_data_2015/airdata"+str(i)+".csv", "a+")
        longitude = 73 + float(46) / 60 + float(44) / 3600
        latitude = 40 + float(38) / 60 + float(23) / 3600
        print(longitude)
        print(latitude)
        count = 0
        count1 = 0
        for line in f:
            data = line.split(",")
            if data[0] == 'VendorID':
                continue
            if len(data) >= 13 and abs(abs(float(data[9])) - longitude) <= (1e-2) * 1.1 and abs(
                    abs(float(data[10])) - latitude) <= (1e-2) * 1.1:
                # if len(data)>=13 and data[8] == '132':
                # 输入的数据分别是接客时间，乘客下车时间，乘客数量，行驶里程，起始地点，到达地点,获得车资
                date1 = int(data[1].split(" ")[0].split("-")[2])
                timet = data[1].split(" ")[1];
                time1 = int(timet.split(":")[0]) * 3600 + int(timet.split(":")[1]) * 60 + int(timet.split(":")[2])
                date2 = int(data[2].split(" ")[0].split("-")[2])
                timet = data[2].split(" ")[1];
                time2 = int(timet.split(":")[0]) * 3600 + int(timet.split(":")[1]) * 60 + int(timet.split(":")[2])
                s = str(date1) + ',' + str(time1) + ',' + str(date2) + ',' + str(time2) + "," + data[3] + ',' + data[
                    4] + ',' + data[5] + ',' + data[6] + ',' + data[9] + ',' + data[10] + ',' + data[12] + '\n'
                # s = str(date1) + ',' + str(time1) + ',' + str(date2) + ',' + str(time2) + '\n'
                f1.write(s)
                count1 += 1
            count += 1
            if count % 2000000 == 0:
                print(str(count) + ' lines processed.')
        f1.close()
        print("Totally " + str(count1) + ' lines in the file.')
    f.close()
