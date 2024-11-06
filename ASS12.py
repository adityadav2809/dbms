from pymongo import MongoClient

# MongoDB connection URI
MONGO_URI = "mongodb://localhost:27017/"  # Replace with your MongoDB URI if different

# Create a MongoDB client
client = MongoClient(MONGO_URI)

# Define the database and collection
db = client["ass12"]  # Replace with your actual database name
collection = db["connectivity"]  # Replace with your actual collection name

# ---- CRUD OPERATIONS ----

# CREATE operation: Insert a new document
def create_document(data):
    try:
        result = collection.insert_one(data)
        print("Document created with ID:", result.inserted_id)
    except Exception as e:
        print("Error creating document:", e)

# READ operation: Retrieve documents
def read_documents(query=None):
    try:
        # Find all documents if no query is provided
        documents = collection.find(query or {})
        for doc in documents:
            print(doc)
    except Exception as e:
        print("Error reading documents:", e)

# UPDATE operation: Update an existing document
def update_document(query, new_values):
    try:
        result = collection.update_one(query, {"$set": new_values})
        if result.matched_count > 0:
            print("Document updated successfully.")
        else:
            print("No matching document found.")
    except Exception as e:
        print("Error updating document:", e)

# DELETE operation: Delete a document
def delete_document(query):
    try:
        result = collection.delete_one(query)
        if result.deleted_count > 0:
            print("Document deleted successfully.")
        else:
            print("No matching document found.")
    except Exception as e:
        print("Error deleting document:", e)

# ---- MENU FUNCTION ----
def menu():
    while True:
        print("\nMenu:")
        print("1. Create Document")
        print("2. Read Documents")
        print("3. Update Document")
        print("4. Delete Document")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            city = input("Enter city: ")
            data = {"name": name, "age": age, "city": city}
            create_document(data)

        elif choice == '2':
            print("\nAll documents in collection:")
            read_documents()

        elif choice == '3':
            name = input("Enter name of the document to update: ")
            new_age = int(input("Enter new age: "))
            query = {"name": name}
            new_values = {"age": new_age}
            update_document(query, new_values)

        elif choice == '4':
            name = input("Enter name of the document to delete: ")
            query = {"name": name}
            delete_document(query)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# ---- EXECUTE MENU ----
if __name__ == "__main__":
    menu()
