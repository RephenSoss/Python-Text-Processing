# Stephen Ross
# Create and enter sales data

# Import sqlite3 and connect to database
import sqlite3
conn = sqlite3.connect ('MyDbPy.db')


# Define functions for inserting data
def stores():
    stores1 = ((1, "Alexandria", "VA", "Urban", 200), (2, "Annapolis", "MD","Suburban", 400),
               (3, "Fairfax", "VA", "Suburban", 500), (4, "Hagerstown", "MD", "Rural", 300 ), 
                (5, "Richmond", "VA", "Urban", 400), (6, "Rockville", "MD", "Suburban", 500),
                 (7, "Rosslyn", "VA", "Urban", 200), (8, "Taneytown", "MD", "Rural", 100),
                 (9, "Washington", "DC", "Urban", 300), (10, "Westminster","MD","Rural", 300)) 
                
    cur = conn.cursor()
    cur.execute("Drop Table if Exists Stores")
    cur.execute("create table Stores (StoreID int not null, Town text, State text, Density text, Lot_Size int);")
    cur.executemany("INSERT INTO Stores VALUES (?,?,?,?,?)", stores1)
    conn.commit()
    print "Store rows inserted and committed."


def cars():
    cars1 = ((1, "Chevrolet", "Impala", 2014, 3), (2, "Chevrolet", "Malibu",2014, 3),
               (3, "Chevrolet", "Spark", 2014, 4), (4, "Ford", "Fusion", 2014, 3 ), 
                (5, "Ford", "Escape", 2014, 5), (6, "Hundai", "Accent", 2014, 1),
                 (7, "Hundai", "Sonata", 2014, 3), (8, "Kia", "Forte", 2014, 2),
                 (9, "Nissan", "Versa", 2014, 1), (10, "Toyota","Corolla",2014, 2),
                 (11, "Toyota", "RAV4", 2014, 5), (12, "Volkswagen", "Jetta", 2014, 4))
    cur = conn.cursor()
    cur.execute("Drop Table if Exists cars")
    cur.execute("create table Cars (CarID int not null, Make text, Model text, Model_Year int, Rate_Level int);")
    cur.executemany("INSERT INTO cars VALUES (?,?,?,?,?)", cars1)
    conn.commit()
    print "Car rows inserted and committed."

    
def plans():
    plans1 = ((1, "Personal", "Day", 0), (2, "Personal", "Week", 0), (3, "Personal", "Month", 0), 
              (4, "Business", "Day", 10), (5, "Business", "Week", 15), (6, "Business", "Month", 20), 
                (7, "Contract", "Day", 12), (8, "Contract", "Week", 18), (9, "Contract", "Month", 25), 
                (10, "Internal", "Unsspecified", 30))
    
    cur = conn.cursor()
    cur.execute("Drop Table if Exists plans")
    cur.execute("create table Plans (PlanID int not null, Discount_Type text, Duration text, Discount_Percentage int);")
    cur.executemany("INSERT INTO plans VALUES (?,?,?,?)", plans1)
    conn.commit()
    print "Plan rows inserted and committed."


def rates():
    rates1 = ((1, 25, 150, 600), (2, 30, 200, 800), (3, 35, 225, 850,), (4, 45, 265, 1000))
    cur = conn.cursor()
    cur.execute("Drop Table if Exists rates")
    cur.execute("create table Rates (RateID int not null, Daily int, Weekly int, Monthly int);")
    cur.executemany("INSERT INTO rates VALUES (?,?,?,?)", rates1)
    conn.commit()
    print "Rate rows inserted and committed."
    

def sales():
    cur = conn.cursor()
    cur.execute("Drop Table if Exists sales")
    cur.execute("create table Sales (TXTID int not null, StoreID int, CarID int, PlanID int, Unique_Sale int, Revenue int);")
   
# Create a dictionary from the txt file       
    with open('sales.txt') as f:
        data = [line.strip().split() for line in f.readlines()]
# Insert dictionary into databases
    for i in data:
        cur.executemany("INSERT INTO sales VALUES (?,?,?,?,?,?)", [i])    
    conn.commit()
#    cur.close()
    print "Sale rows inserted and committed."
    print "\n"



#def countrows():
#    cur = conn.cursor()
#    countrow = raw_input('Print the row in which you would like to count.')
#    cur.execute("Select * from 'countrow'")
#    for row in cur:
#        print str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\n"
##conn.close()
#
#
#countrows()



def countrows2():
    cur = conn.cursor()
    # Get List of Tables:      
    tableList = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY Name"
    cur.execute(tableList)
    # This lambda funtion creates a map for all the tables in the DB
    tables = map(lambda t: t[0], cur.fetchall())

    print "Tables     Columns     Rows       Cells"
    for table in tables:
        columns = "PRAGMA table_info(%s)" % table
        cur.execute(columns)
        numberOfColumns = len(cur.fetchall())
        rows = "SELECT Count() FROM %s" % table
        cur.execute(rows)
        numberOfRows = cur.fetchone()[0]
        numberOfCells = numberOfColumns*numberOfRows
        print("%s\t%d\t%d\t%d" % (table, numberOfColumns, numberOfRows, numberOfCells))


    print "\n"

def sumrev():
    cur = conn.cursor()
    revenues = """
            SELECT 
                town,
                make,
                sum(Revenue)
            From
                stores,
                cars,
                sales
            Where
                stores.storeID = sales.storeID and cars.CarID = Sales.CarID
            Group By 
                stores.town,
                Cars.make,
                Cars.model;"""
            
    cur.execute(revenues)
    printout = cur.fetchall()
    print printout
#




# Run Functions

stores()
cars()
plans()
rates()
sales() 
#countrows()
countrows2()
sumrev()


















