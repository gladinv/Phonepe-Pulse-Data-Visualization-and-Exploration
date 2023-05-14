# Phonepe-Pulse-Data-Visualization-and-Exploration

## Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.

![MADE WITH PYTHON](http://ForTheBadge.com/images/badges/made-with-python.svg)  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gladinv-phonepe-pulse-data-visualization-and-explor-main-d3nkr9.streamlit.app/)

Disclaimer: This project is built for research purposes only. I, ***Gladin K. Varghese*** , as the developer am not responsible for any misuse of this project. I believe that this kind of technology should be accessible if needed for the correct reasons.
  
 ### This project is built using these libraries and modules:
 * Streamlit - Streamlit is an open-source app framework for Machine Learning and Data Science teams.
 * Pandas - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
 * Plotly - The plotly.express module (usually imported as px) contains functions that can create entire figures at once, and is referred to as Plotly Express or PX. Plotly Express is a built-in part of the plotly library, and is the recommended starting point for creating most common figures.
 * Sqlite3 - Python SQLite3 module is used to integrate the SQLite database with Python.

## Hosted on Streamlit Cloud [(read more about Streamlit Cloud)](https://streamlit.io/cloud):
[PhonePe Pulse Data Viz](https://gladinv-phonepe-pulse-data-visualization-and-explor-main-d3nkr9.streamlit.app/)

## Workflow
step-by-step explanation of the workflow of the Phonepe Pulse Data Visualization and Exploration App:

First, the necessary libraries are imported - streamlit for creating the app, and PIL and numpy for image processing.

Next, the images and videos to be displayed in the app are loaded.

The app is initialized with a title and a dropdown menu with options for navigating to different pages.

Depending on the option selected in the dropdown menu, different content is displayed.
If "Home" is selected, a brief description of PhonePe is displayed, along with the PhonePe logo and a promotional video. A download button is also provided for downloading the PhonePe app.

If "About" is selected, a more detailed description of the Indian digital payments industry and PhonePe's role in it is provided, along with the PhonePe Pulse logo, a promotional video, and a download button for the PhonePe app.

If "Contact" is selected, a picture and contact information for the app developer, along with links to their social media profiles, are displayed.

This section of the code is responsible for handling the search functionality of the application. It first displays a dropdown menu using st.selectbox() that allows the user to select the category they want to search by, which includes "Brand", "District", "Registered Users", "Top Transactions", and "Transaction Type".

Based on the user's selection, the code then calls one of the many functions that have been defined, which correspond to each of the search categories. Each of these functions execute a SQLite query to extract the relevant data from the aggregated_transactions, map_transactions, aggregated_users, and map_users tables.

These queries are constructed based on the user's selection and are executed using the cursor.execute() method. The results of the queries are then stored in a Pandas DataFrame, which is displayed to the user as a table using st.dataframe().

For example, if the user selects "Brand" from the dropdown menu, the code calls one of the three functions for brand search brand_(), brand_year(), and brand_state() depending on whether they want to search by brand type, brand type and year, or brand type, year, and state respectively. These functions extract the data from the aggregated_users table, and return a Pandas DataFrame that displays the results to the user.

This section of code is a conditional statement that executes two possible workflows based on the user's input in a dropdown menu.

The first option is "Transaction Type", where the user can select between two different types of views: "Tabular view" or "Plotly View". If the user selects "Tabular view", the script will generate three columns, where the user can select the transaction type, year, and state from three different dropdown menus. Depending on the options selected by the user, the code will generate a table that shows the transaction amount for the selected transaction type, year, and state.

If the user selects "Plotly view", the script will generate three columns as well. However, instead of generating dropdown menus, the script will display charts using the Plotly library. The first column will show a dropdown menu for selecting the transaction type, while the second column will show a dropdown menu for selecting the year. Finally, the third column will show a dropdown menu for selecting the state. Once the user has selected the appropriate options, the code will generate a chart that shows the transaction amount for the selected transaction type, year, and state.

The second option is "District". If the user selects "District", the script will display two options in a dropdown menu: "Tabular view" and "Plotly View". If the user selects "Tabular view", the script will display three columns, where the user can select the state, district, and year. Once the user has selected the appropriate options, the code will generate a table that shows the transaction amount for the selected state, district, and year.

If the user selects "Plotly view", the script will display three columns as well. The first column will show a dropdown menu for selecting the state, while the second column will show a dropdown menu for selecting the district. Finally, the third column will show a dropdown menu for selecting the year. Once the user has selected the appropriate options, the code will generate a chart that shows the transaction amount for the selected state, district, and year.

This is a Python script that generates an interactive dashboard using the Streamlit library. The script has two main sections: one for "Top Transactions" and the other for "Registered Users."

When the user selects "Top Transactions," the dashboard displays a selectbox with two options: "Tabular view" and "Plotly view." If the user chooses "Tabular view," the dashboard displays three selectboxes for "State," "Year," and "Quarter." Based on the user's choices, the dashboard generates a table that shows the transaction count for the selected state, year, and quarter.

If the user selects "Plotly view," the dashboard displays the same selectboxes for "State," "Year," and "Quarter." Based on the user's choices, the dashboard generates a bar chart that shows the transaction count for the selected state, year, and quarter.

When the user selects "Registered Users," the dashboard displays the same selectbox with two options: "Tabular view" and "Plotly view." If the user chooses "Tabular view," the dashboard displays three selectboxes for "State," "Year," and "Quarter." Based on the user's choices, the dashboard generates a table that shows the number of registered users for the selected state, year, and quarter.

If the user selects "Plotly view," the dashboard displays the same selectboxes for "State," "Year," and "Quarter." Based on the user's choices, the dashboard generates a bar chart that shows the number of registered users for the selected state, year, and quarter.

Overall, the dashboard allows the user to select a state, year, and quarter, and see either a table or a bar chart of transaction count or registered users.
