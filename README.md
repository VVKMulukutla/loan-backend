# Backend

This folder contains the backend code for the desktop apps project.

## Technologies Used

- Sanic: A Python web framework used for creating endpoints.
- MongoDB: A NoSQL database used for storing data.
- PyMongo: A Python library used as an ORM for MongoDB.

## Endpoints

The following endpoints are available:

- `POST /login`: Used for user login.
- `POST /signup`: Used for user signup.

## Usage

To use the backend code in this folder, follow these steps:

1. Install the required dependencies by running the following command in your terminal:

    ```shell
    pip install -r requirements.txt
    ```

2. Make sure you have MongoDB installed and running on your system. You can download MongoDB from the official website and follow the installation instructions.

3. Once MongoDB is set up, create a new database for the project.

4. Update the `config.py` file in the backend code with the appropriate database connection details.

5. Run the following command in your terminal to start the backend server:

    ```shell
    python app.py
    ```

6. The server will start running on `http://localhost:8000`. You can now make requests to the available endpoints.

## Requirements

To use the backend code in this folder, you need the following requirements:

- Python 3.6 or higher
- Sanic web framework
- MongoDB
- PyMongo library

Make sure you have these requirements installed before proceeding with the usage steps mentioned above.

## Utility Function

- `kyc_helper`: A utility function used for KYC (Know Your Customer) verification.

Please refer to the code files in this folder for more details on the implementation.

