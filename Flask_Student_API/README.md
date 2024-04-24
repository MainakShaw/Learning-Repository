## Flask Student Data API

This project demonstrates a simple Flask application that serves as a RESTful API for managing student data.

**Key Functionalities:**

* **Student Catalog:** Stores information about students (ID, name, address) in a JSON file.
* **CRUD Operations:**
    * **Create:** Add new students to the data catalog using a POST request.
    * **Read:** Retrieve all students using a GET request or get a specific student by ID using a GET request.
    * **Update:** Modify existing student information using a PUT request.
    * **Delete:** Remove a student from the data catalog using a DELETE request.
* **Error Handling:** Provides informative messages for invalid requests or missing data.

**Running the Application:**

1. Clone this repository or download the files.
2. Install Flask using `pip install Flask`.
3. Run the application using `python my_api.py`. 
4. The API will be accessible at `http://localhost:5000/` by default (port might vary).

**API Endpoints:**

| Method | URL                                              | Description                                        |
|---|---|---|
| GET   | `/get_students`                                       | Retrieves all students in the catalog.               |
| GET   | `/get_std_by_id/<int:std_id>`                         | Retrieves a specific student by their ID.            |
| POST  | `/add_student`                                       | Adds a new student to the catalog.                     |
| PUT   | `/update_std`                                       | Updates information for an existing student.         |
| DELETE | `/delete_user`                                      | Deletes a student from the catalog based on ID.      |

**Data Storage:**

Student data is stored in a JSON file (`student_db.json`) located in the project directory. 

**Feel free to explore and modify this code to build your own Flask API applications!**
