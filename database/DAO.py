from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.porzione import Porzione


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAllPorzioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct p.portion_display_name as porzione
from food_pyramid_mod.portion p
order by p.portion_display_name"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["porzione"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(calorie):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct p.portion_display_name as porzione
from food_pyramid_mod.portion p 
where p.calories <%s
order by p.portion_display_name"""

        cursor.execute(query,(calorie,))

        for row in cursor:
            result.append(row["porzione"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.p1 as v1,t2.p2 as v2,count( distinct t1.f1) as peso
from(select distinct p.food_code as f1, p.portion_display_name as p1
from food_pyramid_mod.portion p)as t1,(select distinct p.food_code as f2, p.portion_display_name as p2
from food_pyramid_mod.portion p)as t2 
where t1.f1=t2.f2 and t1.p1!=t2.p2 
group by t1.p1,t2.p2 """

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
