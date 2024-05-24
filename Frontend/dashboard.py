import streamlit as st
from pymongo import MongoClient
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# MongoDB connection
client = MongoClient('mongodb+srv://atharvapdesai9:PlYP3eDjFjwKHo49@cluster0.uh8sdha.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ethereum_db']
collection = db['ethereum']

# Fetch block data
data = list(collection.find({}))

# Convert the fetched data to a Pandas DataFrame
df = pd.DataFrame(data)

# Convert hex values to integers where necessary
df['number'] = df['number'].apply(lambda x: int(x, 16))
df['gasLimit'] = df['gasLimit'].apply(lambda x: int(x, 16))
df['gasUsed'] = df['gasUsed'].apply(lambda x: int(x, 16))
df['size'] = df['size'].apply(lambda x: int(x, 16))
df['timestamp'] = df['timestamp'].apply(lambda x: int(x, 16))
df['difficulty'] = df['difficulty'].apply(lambda x: int(x, 16))
df['totalDifficulty'] = df['totalDifficulty'].apply(lambda x: int(x, 16))

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

# Title of the Streamlit app
st.title('Ethereum Block Data Visualization')

# Block Size Over Time
st.header('Block Size Over Time')
fig_size = px.line(df, x='timestamp', y='size', title='Block Size Over Time')
st.plotly_chart(fig_size, use_container_width=True)

# Add some spacing
st.markdown("---")

# Organize Gas Used vs Gas Limit and Difficulty Over Time in columns
st.header('Gas Usage and Difficulty Over Time')
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader('Gas Used vs Gas Limit')
    fig_gas = go.Figure()
    fig_gas.add_trace(go.Scatter(x=df['timestamp'], y=df['gasLimit'], mode='lines', name='Gas Limit'))
    fig_gas.add_trace(go.Scatter(x=df['timestamp'], y=df['gasUsed'], mode='lines', name='Gas Used'))
    fig_gas.update_layout(xaxis_title='Timestamp', yaxis_title='Gas')
    st.plotly_chart(fig_gas, use_container_width=True)

with col2:
    st.subheader('Difficulty Over Time')
    fig_difficulty = px.line(df, x='timestamp', y='difficulty')
    st.plotly_chart(fig_difficulty, use_container_width=True)

# Add some spacing
st.markdown("---")

# Transactions per Block and Average Gas Price per Block in columns
st.header('Transactions and Gas Price')
col3, col4 = st.columns(2, gap="large")

with col3:
    st.subheader('Transactions per Block')
    df['num_transactions'] = df['transactions'].apply(len)
    fig_transactions = px.line(df, x='timestamp', y='num_transactions', title='Transactions per Block')
    st.plotly_chart(fig_transactions, use_container_width=True)

with col4:
    st.subheader('Average Gas Price per Block')
    def avg_gas_price(transactions):
        if len(transactions) == 0:
            return 0
        total_gas_price = sum(int(tx['gasPrice'], 16) for tx in transactions)
        return total_gas_price / len(transactions)

    df['avg_gas_price'] = df['transactions'].apply(avg_gas_price)
    fig_avg_gas_price = px.line(df, x='timestamp', y='avg_gas_price', title='Average Gas Price per Block')
    st.plotly_chart(fig_avg_gas_price, use_container_width=True)

# Add some spacing
st.markdown("---")

# Miner Distribution
st.header('Miner Distribution')
miner_counts = df['miner'].value_counts().reset_index()
miner_counts.columns = ['miner', 'count']
fig_miner_distribution = px.pie(miner_counts, names='miner', values='count', title='Miner Distribution')
st.plotly_chart(fig_miner_distribution, use_container_width=True)

# Add some spacing
st.markdown("---")
