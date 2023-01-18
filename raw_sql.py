query = "CREATE TABLE `CODE_POSITION` (	) COLLATE='latin1_swedish_ci' ENGINE=InnoDB"

sz = ""
with open('raw.csv') as f:
    line = f.readline()
    line = line[:-1]
    cols = line.split(',')

    for col in cols:
        sz += "`"+ col +"` INT NULL DEFAULT NULL, \n"


print(sz)    