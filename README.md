# pydb
A python database manager for any backend.  

## Creating a pydb
Creating your very own pydb is super simple! Add `main.py` to your project, add `from main import pydb` at the top of your code and create a pydb object with `[database name] = pydb([database name])`  


![image](https://user-images.githubusercontent.com/89071358/156818943-27fc4bd0-66b6-4518-a3da-9f43688b5302.png)


## Functions  

### Add value
![image](https://user-images.githubusercontent.com/89071358/156819408-2d3c94e6-d5a6-4775-8df3-2bbb838b57f2.png)  
This function takes in two arguments (column, data) and adds the data to the end of the specified column.  

### Modify value
![image](https://user-images.githubusercontent.com/89071358/156819981-c44ec8a8-01c4-4cef-9723-5ab26de319b4.png)  
This function takes in three arguments (column, row, new data) and changes the value at the row and column to a new value.  

### Get value
![image](https://user-images.githubusercontent.com/89071358/156820478-a403ec62-db4c-4632-82f3-a8ed7ce94d23.png)  
This function takes in two arguments (column, row) and returns the value stored at that position. Simple!  

### Add column
![image](https://user-images.githubusercontent.com/89071358/156820742-af858341-6f37-4f5e-9f4d-0f5621304b76.png)  
Takes no arguments and adds a new column to your database.  

### Remove column
![image](https://user-images.githubusercontent.com/89071358/156820914-d7ecbc67-373c-4a9e-8a35-61409c10355b.png)  
Removes a specified column.  

**Warning!**  
This cannot be undone!  

### Display column
![image](https://user-images.githubusercontent.com/89071358/156821306-f0f55f5e-ccec-4ca7-b316-8afda88044b2.png)  
Displays the contents of a column. Useful for debugging.  

## Importing and exporting
### Exporting a database
![image](https://user-images.githubusercontent.com/89071358/156821904-2ea77a09-f387-4c65-9691-9f3c2fb656c2.png)  
Exporting is just as simple as anything else. Simply use the *exportdb([database name])* function and add where you want to export your database to. It will export your data to a folder.  

### Importing a database
![image](https://user-images.githubusercontent.com/89071358/156823983-f44bf9b0-34b1-433b-8291-b3338f7ed9c7.png)  
To import your database from an export, use *importdb([database name])* to import all of the data to a pydb object. (this overwrites all existing data in the object)  
Note: always make sure to use the same name you used for the export when importing
