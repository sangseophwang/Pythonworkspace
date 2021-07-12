import sqlite3

# sqlite3.Connection  연결 객체 생성
conn = sqlite3.connect('db.sqlite3')

cur = conn.cursor()

cur.execute(
    '''
    DROP TABLE IF EXISTS user
    '''
)
cur.execute(
    '''
    CREATE TABLE user (
        pk_user_id INTEGER,
        name TEXT,
        PRIMARY KEY (pk_user_id)
    )
    '''
)

# 데이터베이스의 CRUD
# Create / Read / Update / Delete

# CREATE 데이터 생성
cur.execute(
    '''
    INSERT INTO user
    VALUES (1, 'seop')
    '''
)

cur.execute(
    '''
    INSERT INTO user
    VALUES (?, ?) 
    ''',
    (2, '철수')
)

user_list = [
    (4, '연수'),
    (3, '영희'),
]

cur.executemany(
    '''
    INSERT INTO user
    VALUES (?, ?)
    ''',
    user_list
)

# READ (조회)
cur.execute(
    '''
    SELECT * FROM user
    '''
)

# row = cur.fetchone()
# print(row)

# rows = cur.fetchmany(size=2)
# print(rows)

rows = cur.fetchall()
print(rows)

# UPDATE
cur.execute(
    '''
    UPDATE user
    SET name='현영'
    WHERE pk_user_id = 4
    '''
    # WHERE pk_user_id >= 2 이런 식으로 범위 지정 가능
)

# DELETE
cur.execute(
    '''
    DELETE FROM user
    WHERE pk_user_id = 4
    '''
)

'''
UPDATE 테이블명
SET 컬럼명 = 값
[WHERE ]

DELETE FROM 테이블명
[WHERE 조건]
'''

conn.commit()
