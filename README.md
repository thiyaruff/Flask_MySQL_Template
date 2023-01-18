
# flask SQLAlchemy with MySQL template 

falsk project with one model (students)

with full crud (GET, POST, DELETE, PUT)

RESTAPI

## Installation

1. Clone the repository.
2. creat virtualenv: Create a `.env` file in the root directory and set the following environment
3. Install the dependencies:
 `pip install -r requirements.txt`
4. Run the application: py app.py


## install MySQL on your computer, remmeber yuor password and change it in the app.py 

app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'name of the schema'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:[your password]@localhost/[name of the schema]'

## todo test use Thunder_client

## Author

Thiya Ruff




