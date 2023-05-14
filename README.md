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
Here is a revised workflow for the PhonePe Pulse Data Visualization and Exploration App:

Import necessary libraries - Streamlit for creating the app, PIL and NumPy for image processing, Pandas for data manipulation and Plotly for data visualization.

Load images and videos to be displayed in the app.

Initialize the app with a title and a dropdown menu with options for navigating to different pages - Home, About, Contact, Top Transactions and Registered Users.

If "Home" is selected, display a brief description of PhonePe, along with the PhonePe logo and a promotional video. Provide a download button for downloading the PhonePe app.

If "About" is selected, display a more detailed description of the Indian digital payments industry and PhonePe's role in it, along with the PhonePe Pulse logo, a promotional video, and a download button for the PhonePe app.

If "Contact" is selected, display a picture and contact information for the app developer, along with links to their social media profiles.

If "Top Transactions" is selected, display a selectbox with two options: "Tabular view" and "Plotly view".
If "Tabular view" is selected, display three selectboxes for "State", "Year", and "Quarter". Based on the user's choices, generate a table that shows the transaction count for the selected state, year, and quarter.
If "Plotly view" is selected, display the same selectboxes for "State", "Year", and "Quarter". Based on the user's choices, generate a bar chart that shows the transaction count for the selected state, year, and quarter.

If "Registered Users" is selected, display the same selectbox with two options: "Tabular view" and "Plotly view".
If "Tabular view" is selected, display three selectboxes for "State", "Year", and "Quarter". Based on the user's choices, generate a table that shows the number of registered users for the selected state, year, and quarter.
If "Plotly view" is selected, display the same selectboxes for "State", "Year", and "Quarter". Based on the user's choices, generate a bar chart that shows the number of registered users for the selected state, year, and quarter.

If "Search" is selected, display a dropdown menu using st.selectbox() that allows the user to select the category they want to search by, which includes "Brand", "District", "Registered Users", "Top Transactions", and "Transaction Type".
Based on the user's selection, call the appropriate function that corresponds to each of the search categories. Each function executes a query to extract the relevant data from the database and returns a Pandas DataFrame that is displayed to the user as a table using st.dataframe().

If "Transaction Type" is selected, display a dropdown menu for selecting the type of view: "Tabular view" or "Plotly view".
If "Tabular view" is selected, display three dropdown menus for selecting the transaction type, year, and state. Based on the user's choices, generate a table that shows the transaction amount for the selected transaction type, year, and state.
If "Plotly view" is selected, display three columns. The first column shows a dropdown menu for selecting the transaction type, while the second column shows a dropdown menu for selecting the year. Finally, the third column shows a dropdown menu for selecting the state. Based on the user's choices, generate a chart that shows the transaction amount for the selected transaction type, year, and state.

If "District" is selected, display a dropdown menu with options for "Tabular view" or "Plotly View". If "Tabular view" is selected, display three columns where the user can select the state, district, and year. Based on the user's selection, the code generates a table that shows the transaction amount for the selected state, district, and year.
If "Plotly view" is selected, display three columns as well. The first column shows a dropdown menu for selecting the state, while the second column shows a dropdown menu for selecting the district. Finally, the third column shows a dropdown menu for selecting the year. Once the user has selected the appropriate options, the code generates a chart that shows the transaction amount for the selected state, district, and year using the Plotly library.

After the content is displayed based on the user's selection, the app is run using the streamlit run command on the command line.

When the app is run, it will display the selected content in the user's web browser. The user can interact with the app by selecting different options from the dropdown menus and buttons provided. The app will update the displayed content accordingly based on the user's selections.

Once the user is finished using the app, they can close the web browser window to exit the app. The code for the app can be modified and updated as needed to add new features or improve the functionality of the app.
