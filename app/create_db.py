from app import dbs

# ---------------------------------------------------------------------------------------------------------

"""
// Creation of DB

dbname = 'trillodb'

con = psycopg2.connect(dbname='postgres', user='mallikamohta', host='localhost', port=5432)
cur = con.cursor()
cur.execute("select exists(SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('dbname'))")
result = cur.fetchall()
print(result[0][0])
"""

# ---------------------------------------------------------------------------------------------------------

res = dbs.Database().run_query("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='board'")

if res:
    print("Table exists")

if not res:
    query = "create table board (" \
                "id VARCHAR(36) PRIMARY KEY," \
                "title VARCHAR(100)," \
                "visibility VARCHAR(20) CHECK (visibility = 'public' or visibility = 'private') DEFAULT 'public');"
    dbs.Database().run_query(query)
    print("----------------------------------------------------")
    print("Board created")
    """query = "INSERT INTO board VALUES('1', 'test_board');"
    dbs.Database().run_query(query)
    print("----------------------------------------------------")"""

# ---------------------------------------------------------------------------------------------------------

res = dbs.Database().run_query("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='list'")

if res:
    print("Table exists")

if not res:
    query = "create table list (" \
            "id VARCHAR(36) PRIMARY KEY," \
            "title VARCHAR(100)," \
            "board_id VARCHAR(36)," \
            "FOREIGN KEY (board_id) REFERENCES board(id) ON DELETE CASCADE)"
    dbs.Database().run_query(query)
    print("----------------------------------------------------")
    print("List created")

# ---------------------------------------------------------------------------------------------------------

res = dbs.Database().run_query("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='card'")

if res:
    print("Table exists")

if not res:
    query = "create table card (" \
            "id VARCHAR(36) PRIMARY KEY," \
            "title VARCHAR(100)," \
            "description TEXT," \
            "list_id VARCHAR(36)," \
            "FOREIGN KEY (list_id) REFERENCES list(id) ON DELETE CASCADE) "
    dbs.Database().run_query(query)
    print("----------------------------------------------------")
    print("Card created")
    print("----------------------------------------------------")
