# RESTful_API
## RESTful User Search API
This project implements a RESTful API with a linked database for searching and retrieving user information based on their first name. The API provides an endpoint that allows users to search for matching users by providing the beginning of their first name as a query parameter. If matching users are found, the API returns a JSON response containing the user details. If no matching users are found, the API fetches user data from an external source, saves them to the database, and then returns the newly added users in the response.

## Features
* Search for users based on the beginning of their first name.
* Retrieve user details including first name, last name, age, gender, email, phone, and birth date.
* Automatically fetch and add new users from an external source when no matches are found.
* Built using Python and Flask framework.
Utilizes SQLite as the database for storing user information.

## Getting Started
1. Clone the repository: git clone "https://github.com/sudhanshu9630/RESTful_API.git"
1. Install the required dependencies: pip install Flask flask_sqlalchemy requests
1. Run the Flask application: python app.py
1. Access the API endpoint in your browser or use tools like 'curl' or Postman.

## API Usage
### Endpoint
GET /api/users?first_name=<partial_first_name>

### Query Parameters
0. 'first_name': The partial first name to search for.

### Response
0. If matching users are found, returns a JSON response with user details.
0. If no matching users are found, fetches data from an external source, adds them to the database, and returns the newly added users.

## Contributing
Contributions to this project are welcome! Feel free to open issues and submit pull requests to suggest improvements, report bugs, or add new features.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
