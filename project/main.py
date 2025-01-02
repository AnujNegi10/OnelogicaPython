import streamlit as st
from manager.dash import DashboardManager

def main():
    st.title("Price Comparison Dashboard")

    query = st.text_input("Enter product name")
    if st.button("Search"):
        if query:
            dashboard = DashboardManager()
            results = dashboard.search_product(query)
            if results:
                st.write("Comparison Results:")
                for result in results:
                    st.write(f"Source: {result['source']} - Price: ₹{result['price']}")
            else:
                st.write("No results found.")
        else:
            st.error("Please enter a product name.")

if __name__ == "__main__":
    main()
