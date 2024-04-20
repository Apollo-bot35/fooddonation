import pymysql

class foodServices():
    def getalldata(self):
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("select * from donor")
        data=curs.fetchall()
        return data
    

    def getfood(self):
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("select * from food_item")
        data=curs.fetchall()
        return data


    
    
    