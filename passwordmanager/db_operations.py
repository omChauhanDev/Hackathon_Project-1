import sqlite3


class DbOperations:

    def connect_to_db(self):
        conn =  sqlite3.connect("password_records.db")
        return conn


    def create_table(self, table_name = "password_info"):
        conn = self.connect_to_db()
        query = f'''
        CREATE TABLE IF NOT EXISTS {table_name}(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            website TEXT NOT NULL, 
            username VARCHAR(200) DEFAULT NULL, 
            password VARCHAR(50)
            );
            '''
        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            

    def create_record(self, data, tabel_name = "password_info"):
        website = data['website']
        username = data['username']
        password = data['password']
        
        
        conn = self.connect_to_db()
        query = f'''
        INSERT INTO {tabel_name} ('website', 'username', 'password') VALUES
        (?, ?, ?);
            '''

        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username, password))
               

    def show_record(self, table_name = "password_info"):
        conn = self.connect_to_db()
        query = f'''
        SELECT * FROM  {table_name};
            '''

        with conn as conn:
            cursor = conn.cursor()
            list_records = cursor.execute(query)
            return list_records
    
    def update_record(self, data, tabel_name = "password_info"):
        ID = data["ID"]
        website = data['website']
        username = data['username']
        password = data['password']
        conn = self.connect_to_db()
        query = f'''
        UPDATE {tabel_name} SET website = ?, username = ?, password = ? WHERE ID = ?;
        '''
        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username, password, ID))

    def delete_record(self, ID, table_name="password_info"):
        conn = self.connect_to_db()
        query = f'''
        DELETE FROM {table_name} WHERE ID = ?
        ;
        '''
        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (ID, ))
