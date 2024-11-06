import mysql.connector
from mysql.connector import Error

# Database connection configuration
config = {
    'user': 'aditya',               # Your MySQL username
    'password': 'Aditya@2003',      # Your MySQL password
    'host': 'localhost',            # MySQL server host
    'database': 'ass8'              # Database name
}

def create_connection():
    """Establish a connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Successfully connected to the MySQL database.")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def create_name(connection, name, age, city):
    """Insert a new name along with age and city into the database."""
    query = "INSERT INTO names (name, age, city) VALUES (%s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(query, (name, age, city))
    connection.commit()
    print(f"Name '{name}' with age {age} and city '{city}' has been added to the database.")

def read_names(connection):
    """Fetch and display all names along with age and city from the database."""
    query = "SELECT * FROM names"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    
    print("Names in the database:")
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, City: {row[3]}")

def update_name(connection, name_id, new_name, new_age, new_city):
    """Update an existing name along with age and city in the database."""
    query = "UPDATE names SET name = %s, age = %s, city = %s WHERE id = %s"
    cursor = connection.cursor()
    cursor.execute(query, (new_name, new_age, new_city, name_id))
    connection.commit()
    print(f"Name ID {name_id} has been updated to '{new_name}' with age {new_age} and city '{new_city}'.")

def delete_name(connection, name_id):
    """Delete a name from the database by its ID."""
    query = "DELETE FROM names WHERE id = %s"
    cursor = connection.cursor()
    cursor.execute(query, (name_id,))
    connection.commit()
    print(f"Name ID {name_id} has been deleted from the database.")

def menu():
    """Display a menu and execute user-selected option."""
    print("\nMenu:")
    print("1. Add Name")
    print("2. View Names")
    print("3. Update Name")
    print("4. Delete Name")
    print("5. Exit")

def main():
    """Main function to execute database operations."""
    connection = create_connection()
    
    if connection is not None:
        while True:
            menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                city = input("Enter city: ")
                create_name(connection, name, age, city)

            elif choice == '2':
                read_names(connection)

            elif choice == '3':
                name_id = int(input("Enter the ID of the name to update: "))
                new_name = input("Enter new name: ")
                new_age = int(input("Enter new age: "))
                new_city = input("Enter new city: ")
                update_name(connection, name_id, new_name, new_age, new_city)

            elif choice == '4':
                name_id = int(input("Enter the ID of the name to delete: "))
                delete_name(connection, name_id)

            elif choice == '5':
                print("Exiting the program.")
                connection.close()
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
