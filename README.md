# mongopython

install mongodb :

wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

sudo apt update

sudo apt install mongodb-org

sudo systemctl start mongod

sudo systemctl enable mongod


1) Registration Endpoint (POST request):
   URL: http://localhost:5000/registration
   JSON Payload:

   {
     "user_id": "12345",
     "mobilenumber": "9876543210"
   }


