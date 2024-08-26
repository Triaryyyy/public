import pymysql

def check(users_id, users_pw):
    
    # MariaDB 연결 설정
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'ya23101108!!',
        'database': 'Triary'  # 실제 데이터베이스 이름으로 변경
    }

    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        # 사용자 정보 조회 쿼리 실행
        query = "SELECT * FROM user WHERE users_id = %s AND users_pw = %s"
        cursor.execute(query, (users_id, users_pw))
        result = cursor.fetchone()

        def find_password(users_name, users_birth):
            conn = pymysql.connect(**config)
            cursor = conn.cursor()

            cursor.execute('''
                SELECT password
                FROM users
                WHERE users_name = ? AND users_birth = ?
            ''', (users_name, users_birth))
            
            result = cursor.fetchone()
            
            conn.close()

            if result:
                return result[0]  # 비밀번호 반환
            else:
                return None  # 일치하는 사용자 없음

                return result  # 조회 결과 반환 (없으면 None)

    except pymysql.Error as e:
        print(f"Error: {e}")
        return None

    finally:
        if conn:
            conn.close()