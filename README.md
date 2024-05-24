1
REAL TIME ETHEREUM BLOCK DATA 
DASHBOARD
Introduction
The Ethereum Block Data Analytics Application is a robust and comprehensive solution 
designed to fetch, store, and analyze Ethereum blockchain data. Leveraging the 
Alchemy API, MongoDB, and Streamlit, this project provides real-time and historical 
insights into Ethereum block data, enabling users to explore various blockchain metrics 
and trends through an interactive web interface.
Purpose
The primary goal of this project is to offer a seamless and efficient way to monitor and 
analyze Ethereum block data. By continuously retrieving block information and storing it 
in a database, the application allows users to visualize and understand key blockchain 
metrics, aiding in research, development, and decision-making processes related to 
blockchain technology.
Components
1. Backend:
● Retrieves Ethereum block data from the Alchemy API.
● Stores the data in MongoDB.
● Scheduled to run every 15 seconds to ensure data is up-to-date.
● FastAPI
2. Database:
● MongoDB is used to store block data as documents, enabling efficient 
querying and analysis.
2
3. Frontend:
● Two Streamlit applications for data visualization and analysis:
● block_data.py: Displays data related to a specific block.
● dashboard.py: Provides a broader view of blockchain metrics over 
time.
Technologies Used
● Alchemy API: For accessing Ethereum blockchain data.
● MongoDB: As a NoSQL database to store block data.
● Streamlit: For creating interactive Frontend.
● Docker: For containerizing the backend and frontend applications to ensure 
consistent and isolated environments.
● Python: The primary programming language for backend data retrieval and 
frontend applications.
● (FastAPI) : Web framework
● Plotly: To visualize data and plot graphs
3
How to Run
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
Screenshots : 
5
6
7
8
Demonstration Video : https://drive.google.com/drive/folders/1WzgUvJJhIiKobgWkiboEK10tGjqJ4uM
