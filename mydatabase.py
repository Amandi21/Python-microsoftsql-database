import pyodbc

# Establish a conn to the SQL Server instance
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=AMANDI¬\SQLEXPRESS; DATABASE=HAIRDRESSINGDB; Trusted_Connection=yes;')
# conx_string = "Trusted_connection=yes; DRIVER='{SQL Server}'; SERVER='AMANDI¬\SQLEXPRESS'; DATABASE='HAIRDRESSINGDB'"
# conn = pyodbc.connect(conx_string)
cursor = conn.cursor()



# Switch to the newly created database
cursor.execute("USE HAIRDRESSINGDB")
conn.commit()

# Create the table with five columns
cursor.execute('''
    CREATE TABLE Members (
        ID INT PRIMARY KEY,
        Surname VARCHAR(25),
        OtherNames VARCHAR(25),
        Email VARCHAR(25),
        DOB DATE,
        RoomNo VARCHAR(25)
    )
''')
conn.commit()

# Close the conn
conn.close()