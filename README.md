**How to Run**
1. Clone the repository
(https://github.com/ATHARVA1202/Real-Time-Ethereum-Block-Dashboard)
2. Set up the environment variables
a. In the ‘Backend’ folder :
i. modify the .env file with your API keys and MongoDB URI
ii. Also modify the ‘config.py’ file present in the ‘app’ folder by 
inserting your ‘DB_NAME’ and ‘COLLECTION_NAME’
b. In the ‘Frontend’ folder : 
In files blockdata.py and dashboard.py modify the line no. 8, 9 and 10 
with your MongoDB URI, DB Name and Collection Name respectively
3. Run the containers using Docker
a. Run Docker Desktop to run the Docker engine
b. Go to the project directory in the terminal and run “docker-compose up”
command
c. Now you will see the project running and data being stored in the 
database periodically at an interval of 15 sec
backend-1 | DEBUG:root:Block data stored in MongoDB
d. To access the frontend, data visualizations and the graphs :
i. For block-data : http://localhost:8501/
4
ii. For the blockchain data and metrics across all Ethereum blocks : 
http://localhost:8502/
