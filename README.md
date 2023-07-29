# How to install Gunicorn server in any python app
1. Create server.py file in root directory (find code in this repo)
2. Add gunicorn, gevent in requirements.txt and install using pip3
3. Copy code from code.py and paste it into start file

# How to install http server (not recommended for production, less secure)
1. Create index.html file (Find Code in this repo)
2. Create server.py file (Find Code in thsi repo)
3. Put following code to start server and your app
     python3 server.py &    #this is your server
     python3 main.py        #this is your app starting code
