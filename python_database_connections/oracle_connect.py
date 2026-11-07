
import oracledb
import getpass

try:
    # STEP 1: Initialize Oracle Client
    oracledb.init_oracle_client(
        lib_dir=r"C:\oracle DB\instantclient_19_32"
    )

    # STEP 2: Get password
    password = getpass.getpass("Enter Oracle password: ")

    # STEP 3: Create connection details
    dsn = oracledb.makedsn(
        "localhost",
        1521,
        service_name="XE"
    )

    # STEP 4: Connect to Oracle
    connection = oracledb.connect(
        user="PYTHON_APP",
        password=password,
        dsn=dsn
    )

    print("Successfully connected to Oracle Database!")

    # STEP 5: Create cursor
    with connection.cursor() as cursor:

     cursor.execute("""
        INSERT INTO STUDENTS_1
        (STUDENT_ID, STUDENT_NAME, AGE, COURSE)
        VALUES
        (:student_id, :student_name, :age, :course)
      """, 
     {
        "student_id": 108,
        "student_name": "Matt",
        "age": 24,
        "course": "PL/SQL"
     }
   

     )

     connection.commit()

     print("Student inserted successfully!")
     print("Rows inserted:", cursor.rowcount)
    # STEP 8: Close connection
    connection.close()

    print("Database connection closed.")

except oracledb.Error as error:
    print("Oracle Database Error:", error)

finally:
    if 'connection' in locals() and connection.is_healthy():
        connection.close()
