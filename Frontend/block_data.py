import streamlit as st
from pymongo import MongoClient
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# MongoDB connection
client = MongoClient("mongodb+srv://atharvapdesai9:PlYP3eDjFjwKHo49@cluster0.uh8sdha.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["ethereum_db"]
collection = db["ethereum"]

def query_block_by_number(block_number_hex):
    # Query block data
    block = collection.find_one({"number": block_number_hex})
    return block

def main():
    st.title("Ethereum Block Explorer")

    # Input block number as hexadecimal
    block_number_hex = st.text_input("Enter block number (hexadecimal):")

    # Query block data
    if st.button("Query Block"):
        block = query_block_by_number(block_number_hex)
        if block:
            st.write("Block Data:")
            st.write(block)
            
            # Convert block data to a DataFrame for visualization
            transactions = block.get('transactions', [])
            if transactions:
                df = pd.DataFrame(transactions)

                # Convert hexadecimal values to integers
                df['gas'] = df['gas'].apply(lambda x: int(x, 16))
                
                st.write("Transactions DataFrame:")
                st.write(df)
                
                # Gas Usage Distribution
                # x-axis represents the gas used by transactions in the block, and the y-axis represents the frequency of gas usage. 
                st.subheader("Gas Used")
                fig = px.histogram(df, x='gas', title='Gas Used Distribution')
                st.plotly_chart(fig)

        else:
            st.write("Block not found.")

if __name__ == "__main__":
    main()
