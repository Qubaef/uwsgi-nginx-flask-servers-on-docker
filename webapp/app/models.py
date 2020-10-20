import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_chat_table()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    # create schema for ChatTable
    def create_chat_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Chat" (
          id INTEGER PRIMARY KEY,
          Message TEXT,
          Referer TEXT,
          CreatedOn Date DEFAULT CURRENT_DATE
        );
        """

        self.conn.execute(query)


class ChatTableModel:
    TABLENAME = "Chat"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    # get item by id
    def get_by_id(self, _id):
        where_clause = f"AND id={_id}"
        return self.list_items(where_clause)
    
    # create new item from given params
    def create(self, params):
        query = f'insert into {self.TABLENAME} ' \
                f'(Message, Referer) ' \
                f'values ("{params.get("message")}","{params.get("referer")}")'

        print(f"SQL: Executing {query}")

        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)
    
    # delete item by id
    def delete(self, item_id):
        query = f"DELETE FROM {self.TABLENAME} " \
                f"WHERE id = {item_id}"
        print(f"SQL: Executing {query}")
        self.conn.execute(query)

    # get all items as text
    def list_items(self, where_clause = ""):
        query = f"SELECT id, Message, Referer " \
                f"from {self.TABLENAME} WHERE 1=1 " + where_clause

        print(f"SQL: Executing {query}")
        
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result