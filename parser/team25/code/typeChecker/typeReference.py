# Author: Jorge Canté (JACL)

import os 
import json

path = 'data/type/'
dataPath = path + 'typeRef'
    
##################
# Databases CRUD #
##################

# CREATE a database checking their existence
def createDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)
        if database in data:
            return 2
        new = {database:{}}
        data.update(new)
        write(dataPath, data)
        return 0
    except:
        return 1

# READ and show databases by constructing a list
def showDatabases() -> list:
    try:
        initCheck()
        databases = []
        data = read(dataPath)
        for d in data:
            databases.append(d)
        return databases
    except:
        return []

# UPDATE and rename a database name by inserting new_key and deleting old_key
def alterDatabase(databaseOld: str, databaseNew) -> int:
    try:
        if not databaseOld.isidentifier() or not databaseNew.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)        
        if not databaseOld in data:
            return 2
        if databaseNew in data:
            return 3
        data[databaseNew] = data[databaseOld]
        data.pop(databaseOld)
        write(dataPath, data)
        return 0
    except:
        return 1

# DELETE a database by pop from dictionary
def dropDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        data.pop(database)
        write(dataPath, data)
        return 0
    except:
        return 1    


###############
# Tables CRUD #
###############

# CREATE a table checking their existence
def createTable(database: str, table: str, columns: dict) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not isinstance(columns, dict):
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2        
        if table in data[database]:
            return 3
        new = {table:{"columns":columns}}
        data[database].update(new)
        write(dataPath, data)
        dataTable = {}
        return 0
    except:
        return 1

# show databases by constructing a list
def showTables(database: str) -> list:
    try:
        initCheck()
        tables = []        
        data = read(dataPath)
        if not database in data:
            return None
        for d in data[database]:
            tables.append(d)
        return tables
    except:
        return []

# Add a PK list to specific table and database
def alterAddPK(database: str, table: str, constraint: str, column: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not constraint.isidentifier() \
        or not column.isidentifier():
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        if not table in data[database]:
            return 3
        # Modificacion propia
        if not column in data[database][table]['columns']:
            return 4
        data[database][table]['columns'][column]['PK'] = True
        data[database][table]['columns'][column]['PKConst'] = constraint
        write(dataPath, data)
        return 0
    except:
        return 1  

# Add a PK list to specific table and database
def alterDropPK(database: str, table: str, column: str) -> int:
    initCheck()
    dump = False
    with open('data/type/typeRef') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            if column not in data[database][table]['columns']:
                return 4            
            else:
                data[database][table]['columns'][column]['PK'] = False
                data[database][table]['columns'][column]['PKConst'] = None
                dump = True
    if dump:
        with open('data/type/typeRef', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1  

# Add a FK list to specific table and database
def alterAddFK(database: str, table: str, column: str, constraint: str, references: dict) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not constraint.isidentifier() \
        or not column.isidentifier() \
        or not isinstance(references, dict):
            raise Exception()
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        if not table in data[database]:
            return 3
        if not column in data[database][table]['columns']:
            return 4
        data[database][table]['columns'][column]['FK'] = True
        data[database][table]['columns'][column]['FKConst'] = constraint
        data[database][table]['columns'][column]['References'] = references
        write(dataPath, data)
        return 0
    except:
        return 1  

# Add a FK list to specific table and database
def alterDropFK(database: str, table: str, column: str) -> int:
    initCheck()
    dump = False
    with open('data/type/typeRef') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            if column not in data[database][table]['columns']:
                return 4            
            else:
                data[database][table]['columns'][column]['FK'] = False
                data[database][table]['columns'][column]['FKConst'] = None
                data[database][table]['columns'][column]['References'] = None
                dump = True
    if dump:
        with open('data/type/typeRef', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1  

# Rename a table name by inserting new_key and deleting old_key
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    try:
        if not database.isidentifier() \
        or not tableOld.isidentifier() \
        or not tableNew.isidentifier() :
            raise Exception()        
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        if not tableOld in data[database]:
            return 3
        if tableNew in data[database]:
            return 4            
        data[database][tableNew] = data[database][tableOld]
        data[database].pop(tableOld)
        write(dataPath, data)
        return 0
    except:
        return 1   

# add a column at the end of register with default value
def alterAddColumn(database: str, table: str, column: str, atributes: dict) -> int:
    initCheck()
    dump = False
    with open('data/type/typeRef') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            if column in data[database][table]['columns']:
                return 4
            newCol = {column:atributes}
            data[database][table]['columns'].update(newCol)
            dump = True
    if dump:
        with open('data/type/typeRef', 'w') as file:
            json.dump(data, file)

        return 0
    else:
        return 1  

# drop a column and its content (except primary key columns)
def alterDropColumn(database: str, table: str, column: str) -> int:
    initCheck()
    dump = False
    with open('data/type/typeRef') as file:
        data = json.load(file)
        if not database in data:
            return 2
        else:
            if not table in data[database]:
                return 3
            if not column in data[database][table]['columns']:
                return 5
            if data[database][table]['columns'][column]['FK']:
                return 4

            data[database][table]['columns'].pop(column)
            dump = True
    if dump:
        with open('data/type/typeRef', 'w') as file:
            json.dump(data, file)
        return 0
    else:
        return 1  
        
# Delete a table name by inserting new_key and deleting old_key
def dropTable(database: str, table: str) -> int:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        initCheck()
        data = read(dataPath)
        if not database in data:
            return 2
        if not table in data[database]:
            return 3
        data[database].pop(table)
        write(dataPath,data)
        return 0
    except:
        return 1

# Return columns of a table
def getColumns(database: str, table: str) -> list:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        initCheck()
        data = read(dataPath)
        if not database in data:
            return None
        if not table in data[database]:
            return None
        return data[database][table]['columns']
    except:
        return None

# Return state of existence of a column
def columnExist(database: str, table: str, column: str) -> bool:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() \
        or not column.isidentifier():
            raise Exception()             
        initCheck()

        cols = columnsTable(database,table)

        if cols:
            if column in cols:
                return True

        raise Exception()
    except:
        return False

# Return state of existence of a column
def tableExist(database: str, table: str) -> bool:
    try:
        if not database.isidentifier() \
        or not table.isidentifier() :
            raise Exception()             
        initCheck()
        data = read(dataPath)
        if not database in data:
            return False
        if not table in data[database]:
            return False
        return True
    except:
        return False

#############
# Utilities #
#############

# Check the existence of data and json folder and databases file
# Create databases files if not exists
def initCheck():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/type'):
        os.makedirs('data/type')
    if not os.path.exists('data/type/typeRef'):
        data = {}
        with open('data/type/typeRef', 'w') as file:
            json.dump(data, file)

# Read a JSON file
def read(path: str) -> dict:
    with open(path) as file:
        return json.load(file)    

# Write a JSON file
def write(path: str, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file)

# Show the complete file of databases and tables
def showJSON(fileName: str):
    initCheck()
    with open('data/type/'+fileName) as file:
        data = json.load(file)
        print(data)

# Delete all databases and tables by creating a new file
def dropAll():
    initCheck()
    data = {}
    with open('data/type/typeRef', 'w') as file:
        json.dump(data, file)
