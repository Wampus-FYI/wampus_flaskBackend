

# Wampus.fyi

We intend to develop a web-based application that democratizes information related to student housing at UT. We believe that easily accessible information and advanced models will make the house-shopping process more transparent and approachable for students. 

## Project Features

- Convenient access to current and previous rent prices paid for units at various properties for UT student housing.
- Individual renters can post their own listings for students to apply, avoiding a third-party realtor fee.
- View a heat map (of rent prices) of the area surrounding UT campus for students to visualize the rent prices paid concerning distance from campus.
- Determining (via an ML algorithm) a “value score” for available apartment leases based on different factors such as rent cost, amenities offered, apartment reviews, etc.

## Backend API

This application has a backend API built using Flask, which provides the following endpoints:

- `/listings` - GET, POST
- `/listings/<id>` - GET, PUT, DELETE
- `/prices` - GET
- `/heat_map` - GET
- `/value_scores` - GET

## MongoDB Connection

This application uses MongoDB to store and retrieve data. The `pymongo` package is used to interact with the MongoDB database.

To use this application, you must have a running instance of MongoDB and provide the connection details in a `.env` file in the root directory of the project:

```
MONGO_URI=<your-mongo-uri>
```

## Getting Started

To run this application, follow these steps:

1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment: `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows).
4. Install the required packages: `pip install -r requirements.txt`.
5. Create a `.env` file with your MongoDB connection details.
6. Run the application: `python app.py`.

## Contributors

<!-- 
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->