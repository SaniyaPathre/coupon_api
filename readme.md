Coupon API
A simple Flask API for generating and validating coupons.

Table of Contents
Installation
Endpoints
Testing the API
Requirements
License
Installation
Clone the Repository
Clone the repository using Git:


Verify

Open In Editor
Edit
Copy code
git clone https://github.com/your-username/coupon-api.git
cd coupon-api
Install Requirements
Install the required packages using pip:


Verify

Open In Editor
Edit
Copy code
pip install -r requirements.txt
Run the Application
Run the Flask application:


Verify

Open In Editor
Edit
Copy code
flask run
Endpoints
Generate Coupon
URL: http://127.0.0.1:5000/generate_coupon
Method: POST
Content-Type: application/json
Request Body:
json

Verify

Open In Editor
Edit
Copy code
{
    "product_id": "123",
    "user_id": "456",
    "discount_value": 20
}
Response:
On success, returns a JSON object with the generated coupon ID.
Example:
json

Verify

Open In Editor
Edit
Copy code
{
    "coupon_id": "some-unique-id",
    "message": "Coupon generated successfully"
}
Validate Coupon
URL: http://127.0.0.1:5000/validate_coupon
Method: POST
Content-Type: application/json
Request Body:
json

Verify

Open In Editor
Edit
Copy code
{
    "coupon_id": "some-unique-id",
    "product_id": "123",
    "user_id": "456"
}
Response:
If the coupon is valid, returns a JSON object indicating validity and discount value.
Example:
json

Verify

Open In Editor
Edit
Copy code
{
    "valid": true,
    "discount_value": 20
}

Verify

Open In Editor
Edit
Copy code
+ If the coupon is invalid or expired, returns an error message.
+ Example:
json

Verify

Open In Editor
Edit
Copy code
{
    "error": "Invalid coupon"
}
Testing the API
You can test the API endpoints using PowerShell's Invoke-WebRequest cmdlet:

Generate Coupon
powershell

Verify

Open In Editor
Edit
Copy code
Invoke-WebRequest -Uri "http://127.0.0.1:5000/generate_coupon" -Method POST -ContentType "application/json" -Body '{"product_id": "123", "user_id": "456", "discount_value": 20}'
Validate Coupon
powershell

Verify

Open In Editor
Edit
Copy code
Invoke-WebRequest -Uri "http://127.0.0.1:5000/validate_coupon" -Method POST -ContentType "application/json" -Body '{"coupon_id": "some-unique-id", "product_id": "123", "user_id": "456"}'
Requirements
Python 3.x
Flask
Flask-Cors (if needed for cross-origin requests)