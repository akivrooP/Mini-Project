import pymysql  

class Db_operations:
    def __init__(self):
        pass

    def connect_db(self):
        try:
            connection = pymysql.Connect(host='localhost', port=3306, user='root', password='root', database='ipl_db', charset='utf8')
            print('DB connected')
            return connection
        except:
            print('DB connection failed')

    def disconnect_db(self, connection):
        try:
            connection.close()
            print('DB dis-connected')
        except:
            print('Error while disconnecting DB')

    def show_all_tables(self):
        query = 'show tables;'
        connection = self.connect_db()
        cursor = connection.cursor()
        count=cursor.execute(query)
        if count:
            tables = cursor.fetchall()
            for table in tables:
                #print(str(table)[1:-2])
                pass
        else:
            print("NO table created")
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return tables
    
    def get_player_id(self,name):
        query = f"select player_id from player where player_name = '{name}'"
        connection = self.connect_db()
        cursor = connection.cursor()
        id=cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return id
    
    
        
    def add_team(self,vtup):
        query = 'insert into team values(%s,%s,%s,%s,%s,%s,%s)'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query,vtup)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return vtup
    
    def del_team(self,id):
        query = f'delete from team where team_id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 0:
            return(f'team with id = {id} not found')
        else:
            return(f'teamwith id = {id} deleted')
        
    def update_team(self,tup):
        query = """UPDATE team SET team_name=%s, city=%s, coach=%s, captain=%s, no_of_players=%s, no_of_staff=%s WHERE team_id=%s"""
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query,tup)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return {"status": "success", "updated_team_id": tup[0]}
      
    def add_player(self,vtup):
        query = 'insert into player values(%s,%s,%s,%s,%s,%s)'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            cursor.execute(query,vtup)
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
            self.add_playerstats((vtup[0],vtup[4],0,0,0,0,0,0))
            return vtup
        except Exception as e:
            connection.rollback()
            cursor.close()
            self.disconnect_db(connection)
            return {"status": "error", "message": str(e)}
        
    def del_player(self,id):
        self.del_playerstats(id)
        query = f'delete from player where player_id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 0:
            return(f'player with id = {id} not found')
        else:
            return(f'player with id = {id} deleted')
        
    def update_player(self,tup):
        query = """UPDATE player SET player_name = %s,team_id = %s,nationality = %s,role = %s,age = %s WHERE player_id = %s"""
        connection = self.connect_db()
        cursor = connection.cursor()
        try:
            cursor.execute(query,tup)
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
            return {"status": "success", "updated_player_id": tup[0]}
        except :
            connection.rollback()
            cursor.close()
            self.disconnect_db(connection)
            return {"status": "error", "message": "cannot add player invalid team_id"}
       
           
    def add_stadium(self,vtup):
        query = 'insert into stadium values(%s,%s,%s,%s,%s,%s)'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query,vtup)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return vtup
        
    def del_stadium(self,id):
        query = f'delete from stadium where stadium_id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 0:
            return(f'stadium with id = {id} not found')
        else:
            return(f'stadium with id = {id} deleted')
        
    def update_stadium(self,tup):
        query = """UPDATE stadium SET stadium_name = %s,city = %s,capacity = %s,no_of_stands = %s,home_team_id = %s WHERE stadium_id = %s""" 
        connection = self.connect_db()
        cursor = connection.cursor()
        try:
            cursor.execute(query,tup)
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
            return {"status": "success", "updated_stadium_id": tup[0]}
        except Exception as e:
            connection.rollback()
            cursor.close()
            self.disconnect_db(connection)
            return {"status": "error", "message": str(e)}

    def add_playerstats(self,vtup):
        query = 'insert into playerstats values(%s,%s,%s,%s,%s,%s,%s,%s)'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query,vtup)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return vtup
        
    def del_playerstats(self,id):
        query = f'delete from playerstats where player_id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 0:
            return(f'playerstats with id = {id} not found')
        else:
            return(f'palyerstats with id = {id} deleted')
        
    def update_playerstats(self,vtup,pid):
        query1 = f'select * from playerstats where player_id = {pid}'
        query2 = f'delete from playerstats where player_id = {pid}'
        query3 = 'insert into playerstats values(%s,%s,%s,%s,%s,%s,%s,%s)'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query1)
        tup= list(cursor.fetchone())
        tup[2]+=1
        tup[3]+=int(vtup[-2])
        tup[4]+=int(vtup[-1])
        if int(vtup[-1])>=5:
            tup[-1]+=1
        if int(vtup[-2])>=100:
            tup[-2]+=1
        elif int(vtup[-2])>=50:
            tup[-3]+=1
        tup=tuple(tup)
        cursor.execute(query2)
        cursor.execute(query3,tup)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return "True"
        
        
    def add_match_stats(self,vtup):
        query1 = 'insert into match_stats values(%s,%s,%s,%s,%s,%s)'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query1,vtup)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return vtup
        
    def del_match_stats(self,name,id):
        query = f"delete from match_stats where pname = '{name}' and mid ={id} "
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 0:
            return(f'match_stats with id = {id} not found')
        else:
            return(f'match_stats with id = {id} deleted')
        
    def add_match(self,vtup):
        query = 'insert into matches values(%s,%s,%s,%s,%s,%s)'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query,vtup)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return vtup
        
    def del_match(self,id):
        query = f'delete from matches where match_id = {id} '
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 0:
            return(f'match with id = {id} not found')
        else:
            return(f'match with id = {id} deleted')
        
    def update_match(self,tup):
        query = """UPDATE matches SET match_date = %s,team1_id = %s,team2_id = %s,venue = %s,winner_team_id = %s WHERE match_id = %s"""
        connection = self.connect_db()
        cursor = connection.cursor()
        try:
            cursor.execute(query,tup)
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
            return {"status": "success", "updated_match_id": tup[0]}
        except Exception as e:
            connection.rollback()
            cursor.close()
            self.disconnect_db(connection)
            return {"status": "error", "message": str(e)}
        
    def display_table(self, table):
        query = f'SELECT * FROM {table}'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print(f'No rows found in the table')
                rows = []
            else:
                rows = cursor.fetchall()
            cursor.close()
            self.disconnect_db(connection)
            print(rows)
            return rows
        except Exception as e:
            print(f'Error in reading rows: {e}')
            return []

    def get_table_columns(self, table):
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            
            query = f"""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = '{table}'
            AND TABLE_SCHEMA = DATABASE()
            """
            cursor.execute(query)
            columns_info = cursor.fetchall()
            cursor.close()
            self.disconnect_db(connection)
            return [col[0] for col in columns_info]
        except Exception as e:
            print(f'Error getting columns for table {table}: {e}')
            return []

        
    def get_all_winner_teams(self):
        try:
            query = """SELECT 
            t1.team_name AS team1_name,
            t2.team_name AS team2_name,
            tw.team_name AS winner_team_name
            FROM matches m
            JOIN team t1 ON m.team1_id = t1.team_id
            JOIN team t2 ON m.team2_id = t2.team_id
            JOIN team tw ON m.winner_team_id = tw.team_id
            WHERE m.winner_team_id IS NOT NULL;
             """ 

            connection = self.connect_db()
            cursor =  connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            self.disconnect_db(connection)
            return data
        except Exception as e:
            return {"error": str(e)}


oprs = Db_operations()
