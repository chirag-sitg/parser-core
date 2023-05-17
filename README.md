# Parser-core
This service is a utility that parses structured data and extracts coupon code from it.

## Pre-Requisites
- Running kafka server
- Python 3
- Pip

## Installation
1. Clone the repository.
2. Navigate to the service directory:
```cd parser-core``` 
3. Install the dependencies:
```pip install -r requirements.txt```
or
```pip3 install -r requirements.txt```

## Usage
4. Create .env in parser-core subdirectory file and copy the content of env example.
5. Run the Django server with the following command:
```python3 manage.py runserver```
6. Run the Faust worker with the following command:
```faust -A faust_app worker -l info```
