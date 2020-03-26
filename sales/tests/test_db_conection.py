
import cx_Oracle

if __name__ == '__main__':
    print("LOGIN CREDENTIALS".center(40, '='))
    username = 'dazhi'
    print(f"Username: {username}")
    password = input('Password: ')
    con = cx_Oracle.connect(username, password, 'oracle.cise.ufl.edu/orcl', encoding = 'UTF-8')
    cursor = con.cursor()
    for row in cursor.execute('select * from city'):
        print(row)
    con.commit()
