import psycopg2
import csv
import os


# PostgreSQL-ге қосылу
try:
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1004',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    print("PostgreSQL-мен байланыс орнатылды!")
except Exception as e:
    print("PostgreSQL-ге қосыла алмадым:", e)
    exit()

# Кестені құру
try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            phone VARCHAR(20) UNIQUE
        );
    """)
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Кесте құруда қате:", e)

# CSV-тен дерек жүктеу
def insert_from_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute("SELECT * FROM phonebook WHERE phone = %s", (row["phone"],))
                if cur.fetchone() is None:
                    cur.execute(
                        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                        (row["username"], row["phone"])
                    )
        conn.commit()
        print("CSV деректері енгізілді.")
    except Exception as e:
        conn.rollback()
        print("Қате орын алды (CSV):", e)

# Қолмен қосу
def insert_from_console():
    try:
        username = input("Аты: ")
        phone = input("Телефон: ")
        cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
        conn.commit()
        print("Қолмен қосылды.")
    except Exception as e:
        conn.rollback()
        print("Қате орын алды (қолмен қосу):", e)

# Жаңарту
def update_user():
    try:
        old = input("Ескі ат: ")
        new = input("Жаңа ат: ")
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new, old))
        conn.commit()
        print("Жаңартылды.")
    except Exception as e:
        conn.rollback()
        print("Қате (жаңарту):", e)

# Іздеу
def search_user():
    try:
        name = input("Кімді іздейміз: ")
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (name,))
        result = cur.fetchall()
        if result:
            for row in result:
                print(row)
        else:
            print("Мәлімет табылмады.")
    except Exception as e:
        print("Қате (іздеу):", e)

# Жою
def delete_user():
    try:
        name = input("Кімді өшіреміз: ")
        cur.execute("DELETE FROM phonebook WHERE username = %s", (name,))
        conn.commit()
        print("Жойылды.")
    except Exception as e:
        conn.rollback()
        print("Қате (жою):", e)

# Мәзір
def menu():
    while True:
        print("\n----- PHONEBOOK МӘЗІРІ -----")
        print("1. CSV-тен жүктеу")
        print("2. Қолмен қосу")
        print("3. Жаңарту")
        print("4. Іздеу")
        print("5. Жою")
        print("0. Шығу")
        choice = input("Таңдаңыз: ")
        if choice == '1':
            insert_from_csv('labs/lab10/phonebook.csv')
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_user()
        elif choice == '4':
            search_user()
        elif choice == '5':
            delete_user()
        elif choice == '0':
            print("Бағдарлама аяқталды.")
            break
        else:
            print("Қате таңдау!")

# Іске қосу
try:
    menu()
except Exception as e:
    print("БАҒДАРЛАМА ҚАТЕЛІКПЕН ТОҚТАДЫ:", e)

cur.close()
conn.close()