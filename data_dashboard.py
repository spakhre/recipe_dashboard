import sqlite3
import csv

def build_meal():
    FILENAME = "meal_planner.db"
    conn = sqlite3.connect(FILENAME)
    cur = conn.cursor()

# Create table FoodMenu
    cur.execute('''
    CREATE TABLE IF NOT EXISTS "FoodMenu"(
      "Menu_Id" TEXT,
      "Consume_Date" TEXT,
      "Food_Name" TEXT,
      "Category" TEXT,
      "Calories" INTEGER,
      "Protein" INTEGER,
      "Carbohydrates" INTEGER,
      "Sugars" INTEGER,
      "Fiber" INTEGER,
      "Total_Fat" INTEGER,
      "Calcium" INTEGER,
      "Sodium" INTEGER      
    );
    ''')


    print("FoodMenu table created")

    fname="Food_Menu.csv"
# Import Data from csv to sqlite
    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for record in csv_reader:
            print(record)  # get list of records but might not be very useful for large data. Better to get the total # uploaded
            Menu_Id=record[0] #Unique records
            Consume_Date=record[1]
            Food_Name=record[2]
            Category=record[3]
            Calories=record[4]
            Protein=record[5]
            Carbohydrates=record[6]
            Sugars=record[7]
            Fiber=record[8]
            Total_Fat=record[9]
            Calcium=record[10]
            Sodium=record[11]

# Insert Into database field
        cur.execute('''INSERT INTO FoodMenu (Menu_Id,Consume_Date,Food_Name,Category,Calories,Protein,Carbohydrates,Sugars,Fiber,Total_Fat,Calcium,Sodium)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ''', (Menu_Id,Consume_Date,Food_Name,Category,Calories,Protein,Carbohydrates,Sugars,Fiber,Total_Fat,Calcium,Sodium))
        conn.commit()
    conn.close()

build_meal()


