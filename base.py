import os
import sqlite3

# Создание папки бля хранения баз
path = os.getcwd()
print("Текущая рабочая директория %s" % path)
folder_name = "base"
try:
    os.mkdir(folder_name)
except OSError:
    print("Создать директорию %s не удалось или она уже создана." % folder_name)
else:
    print("Успешно создана директория %s " % folder_name)

# base_connect = sqlite3.connect(:memory:)

medDB = r'base/Med.db'


# Универсальный обработчик запросов в базу --------------------------------
def request_SQL(click_base, query, data_tuple):
    try:
        base_connect = sqlite3.connect(click_base)
        base_cursor = base_connect.cursor()
        if data_tuple == 'addBase':
            base_cursor.execute(query)

        elif data_tuple == 'select':

            base_cursor.execute(query)
            # n = base_cursor.fetchall()
            n = base_cursor.fetchone()
            return n

        elif data_tuple == 'select2':
            base_cursor.execute(query)
            n = base_cursor.fetchall()
            return n

        elif data_tuple == 'del':
            base_cursor.execute(query)
            base_connect.commit()

        else:
            print(query)
            print(data_tuple)
            base_cursor.execute(query, data_tuple)
            base_connect.commit()

    except sqlite3.IntegrityError:
        print("Не удалось подключится к базе!")

    finally:
        if base_cursor is not None:
            base_cursor.close()

        if base_connect is not None:
            base_connect.close()


# Каждая новая база со своим классом
class base_Products:
    query = '''CREATE TABLE IF NOT EXISTS med(id INT PRIMARY KEY,
                                                    name TEXT,
                                                    form TEXT,
                                                    app TEXT,
                                                    date TEXT,
                                                    link TEXT);'''
    request_SQL(medDB, query, 'addBase')


def addObject_in_Base(objType, l1, l2, l3, l4, l5):
    if objType == 'med':
        name_block = objType
        base_block = medDB

    query = """select max(id) from {}""".format(name_block)

    if request_SQL(base_block, query, 'select')[0] == None:
        id = 1

    else:
        id = request_SQL(base_block, query, 'select')[0] + 1

    query = """INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?);""".format(name_block)
    data_tuple = (id, l1, l2, l3, l4, l5)

    request_SQL(base_block, query, data_tuple)


# -------------------------------------------------------------------------------

def ListWidget_Object_in_Base(objType):
    if objType == 'med':
        name_block = objType
        base_block = medDB

    query = """SELECT * FROM {} ORDER BY name""".format(name_block)
    return request_SQL(base_block, query, 'select2')


def Del_Object_in_Base(name_med):
    base_connect = sqlite3.connect(r'base/Med.db')
    base_cursor = base_connect.cursor()
    base_cursor.execute("DELETE from med where name = ?", (name_med,))
    base_connect.commit()


def Search_Objects_inBase(name_med):
    print(name_med)
    name_med = "'%" + name_med + "%'"
    print(name_med)
    base_connect = sqlite3.connect(r'base/Med.db')
    base_cursor = base_connect.cursor()
    base_cursor.execute("""SELECT * from med where name like {}""".format(name_med))
    n = base_cursor.fetchall()
    print(n)
    return n


def Search_Dublicate_inBase(name_med):
    base_connect = sqlite3.connect(r'base/Med.db')
    base_cursor = base_connect.cursor()
    base_cursor.execute("SELECT ?, count(*) from med WHERE name = ? GROUP BY ? HAVING count(*) > 0", (name_med,
                                                                                                      name_med,
                                                                                                      name_med))
    n = base_cursor.fetchone()
    return n
