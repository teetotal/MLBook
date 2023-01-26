def create_table():
    query = "CREATE TABLE `RAW` (	{0} ) COLLATE='utf8_general_ci' ENGINE=InnoDB;"
    sz = ""
    with open('raw.csv') as f:
        line = f.readline()
        line = line[:-1]
        cols = line.split(',')

        for col in cols:
            sz += "\n\t`"+ col +"` INT NULL DEFAULT NULL,"

        sz = sz[:-1]

    with open('create_table.sql', 'w') as f:
        f.write(query.format(sz))

def insert():    
    queries = []

    with open('raw.csv') as f:
        f.readline()

        while True:
            line = f.readline()
            if not line: break

            arr = line.split(',')
            sz = "INSERT INTO RAW VALUES("
            try: 
                for col in arr:                
                    val = 'null'
                    if len(col) > 0:
                        if col[-1] == '\n':
                            val = float(col[:-1])
                        else:                    
                            val = int(col)
                    
                    sz += str(val) + ","
                
                sz = sz[:-1]
                sz += ");\n"
                queries.append(sz)
            except:
                print("skip")
            
    
    with open('inserts.sql', "w") as f:
        f.writelines(queries)

insert()