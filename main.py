import os
from datetime import datetime

class pydb:
    # __init__
    def __init__(self, ID:str):
        self.id = ID
        self.columns = [[]]
    # append a value to the end of a specified column
    def add(self, column:int, data):
        self.columns[column].append(data)
    # modify the value at a given column and row
    def modify(self, column:int, row:int, data):
        self.columns[column][row] = data
    # return the value at a given column and row
    def get(self, column:int, row:int):
        return self.columns[column][row]
    # add a column to the database
    def add_column(self):
        self.columns.append([])
    # remove a column from the database (doesn't work)
    def remove_column(self,column:int):
        self.columns.remove(column)
    # print out the contents of a column
    def displaycolumn(self,column:int):
        print(f"""
        Contents of column {column}
        ===============================""")
        for i in self.columns[column]:
            print(i)
        print(f"""
        length of column: {len(self.columns[column])}""")
    # export to a specific path
    def exportdb(self,path:str):
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + "/index.pydbi", 'w') as f:
            w = self.id + "\n"
            w += str(len(self.columns))
            f.write(w)
            f.close() 
        with open(path + "/columns.pydbc", 'w') as f:
            w = ""
            cols = len(self.columns)
            col = 0
            for i in self.columns:
                for j in i:
                    t = type(j)
                    if t == str:
                        w += 'Y`\Qiraz\n'
                    elif t == int:
                        w += '6_>8RSX0\n'
                    elif t == float:
                        w += '@Bd9Riao\n'
                    elif t == bool:
                        w += "CbMwvQv'\n"
                    else:
                        w += 'Y`\Qiraz\n'
                    w += str(j) + '\n'
                col += 1
                if col < cols:
                    w += 'I)oN]1#(\n'
            f.write(w)
            f.close()
    # import a pre-existing pydb from a path
    def importdb(self,path:str):
        with open(path + '/index.pydbi', 'r') as f:
            contents = f.readlines()
            self.id = str(contents[0])
            self.id = self.id[0: -1]
            for i in range(int(contents[1]) - 1):
                self.columns.append([])
            f.close()
        with open(path + '/columns.pydbc', 'r') as f:
            contents = f.readlines()
            col = 0
            for i in contents:
                if i == "Y`\Qiraz\n": # str
                    nexttyp = 'str'
                elif i == '6_>8RSX0\n': # int
                    nexttyp = 'int'
                elif i == "@Bd9Riao\n": # float
                    nexttyp = 'flo'
                elif i == "CbMwvQv'\n": # bool
                    nexttyp = 'boo'
                elif i == "I)oN]1#(\n": # new column
                    col += 1
                else:
                    if nexttyp == "str":
                        self.columns[col].append(str(i)[0: -1])
                    elif nexttyp == "int":
                        self.columns[col].append(int(i))
                    elif nexttyp == "flo":
                        self.columns[col].append(float(i))
                    elif nexttyp == "boo":
                        self.columns[col].append(bool(i))
                    else:
                        print("error: unknown")
                        quit()
            f.close()


# shell script to run when module is run as a script
def shell():
    error_logs = []
    while True:
        db = pydb(input("initialise database > "))

        if db.id == "import":
            try:
                db.importdb(input("import path > "))
            except FileNotFoundError:
                print("an error occurred while executing your command. error code - 0x4645")
                error_logs.append(("import", "0x4645 ", "FileNotFoundError", str(datetime.now())))
                continue
            except:
                print("an error occurred while executing your command. error code - 0x5645")
                error_logs.append(("import", "0x3f3f ", "Unknown", str(datetime.now())))
                continue
        
        while True:
            try:
                c = input(f"#{db.id}~ ")
                c = c.lower()
                if c == "help":
                    print("""
                    pydb shell help
                    ========================================================================================================
                    av - add a value to the end of a specified column - parameters: column, datatype, data
                    mv - modify the value at a specific column and row - parameters: column, row, datatype, data
                    gv - get the value at a specific column and row - parameters: column, row
                    ac - add a column to the current database - no parameters
                    rc - remove a column - parameters: column
                    dc - display the data in a column - parameters: column
                    ex - export the current database - no parameters
                    reinit - reinitialise the shell, restarting into a new shell session - no parameters
                    el - display all recent error logs - no parameters
                    es - end the shell session - no parameters
                    ========================================================================================================""")
                elif c == "av":
                    col = int(input("column > "))
                    datyp = input("data type > ")
                    strval = input("data > ")
                    if datyp == "str":
                        db.add(col, strval)
                    elif datyp == "int":
                        db.add(col, int(strval))
                    elif datyp == "float":
                        db.add(col, float(strval))
                    elif datyp == "bool":
                        db.add(col, bool(strval))
                    else:
                        raise ValueError("Unknown data type. Available types are: str, int, float, bool")
                elif c == "mv":
                    col = int(input("column > "))
                    row = int(input("row > "))
                    datyp = input("data type > ")
                    strval = input("data > ")
                    if datyp == "str":
                        db.modify(col, row, strval)
                    elif datyp == "int":
                        db.modify(col, row, int(strval))
                    elif datyp == "float":
                        db.modify(col, row, float(strval))
                    elif datyp == "bool":
                        db.modify(col, row, bool(strval))
                    else:
                        raise ValueError("Unknown data type. Available types are: str, int, float, bool")
                elif c == "gv":
                    col = int(input("column > "))
                    row = int(input("row > "))
                    print(f"value: {db.get(col, row)}")
                    print(f"type: {type(db.get(col, row))}")
                elif c == "ac":
                    db.add_column()
                elif c == "rc":
                    col = int(input("column > "))
                    confirm = input("are you sure? (y/n) > ")
                    if confirm.lower == "y":
                        db.remove_column(col)
                elif c == "dc":
                    col = int(input("column > "))
                    db.displaycolumn(col)
                elif c == "ex":
                    path = input("export path > ")
                    db.exportdb(path)
                elif c == "reinit":
                    break
                elif c == "el":
                    print("\ncurrent session error logs")
                    print('\n')
                    for i in error_logs:
                        print(i)
                elif c == "es":
                    quit()
                else:
                    print("command not found -- enter 'help' for more information")
            except IndexError:
                print("an error occurred while executing your command. error code - 0x4945")
                error_logs.append((c, "0x4945 ", "IndexError", str(datetime.now())))
            except ValueError:
                print("an error occurred while executing your command. error code - 0x5645")
                error_logs.append((c, "0x5645 ", "ValueError", str(datetime.now())))
            except Exception:
                print("an error occurred while executing your command. error code - 0x3f3f")
                error_logs.append((c, "0x3f3f ", "Unknown", str(datetime.now())))

if __name__ == "__main__":
    shell()