import bcrypt
import connectionHandler


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    print(hashed_bytes.decode('utf-8'))
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@connectionHandler.connection_handler
def register(cursor, register, hash):
    cursor.execute("""
        INSERT INTO users (user_name, user_password)
        VALUES (%(register)s, %(hash)s);
        """, {'hash': hash, 'register': register})

@connectionHandler.connection_handler
def check_user(cursor,login):
    cursor.execute("""
            SELECT user_name FROM users
            WHERE  user_name= %(login)s;
            """, {'login': login})
    data = cursor.fetchall()
    return data

@connectionHandler.connection_handler
def login(cursor,user_name):
    cursor.execute("""
        SELECT user_password FROM users
        WHERE  user_name= %(login)s;
        """,{'login':user_name})
    data=cursor.fetchall()
    return data

@connectionHandler.connection_handler
def get_id_by_user_name(cursor, user_name):
    cursor.execute("""
                    SELECT user_id FROM users
                    WHERE user_name = %(user_name)s; 
                   """,
                   {'user_name': user_name})
    received_id = cursor.fetchone()
    return received_id