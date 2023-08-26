# PhonePe Pulse Data Visualization and Exploration

This project aims to extract, transform, and visualize data from the PhonePe Pulse GitHub repository. The goal is to provide insights and information in a user-friendly manner through a live geo visualization dashboard. The project includes steps to extract data, transform it, insert it into a MySQL database, and create an interactive dashboard using Streamlit and Plotly. The dashboard allows users to select different facts and figures for display.

## Installation

1. Clone the GitHub repository:
   ```
   git clone https://github.com/your-username/phonepe-pulse.git
   ```
2. Change to the project directory:
   ```
   cd phonepe-pulse
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
   The project utilizes the following libraries:
   - Streamlit: Python framework for building interactive web applications.
   - Plotly: Library for creating interactive and dynamic visualizations.
   - Pandas: Data manipulation and analysis library.
   - MySQL Connector: Python driver for connecting to MySQL databases.

4. Make sure you have a MySQL database server installed and running. Update the MySQL connection details in the code if necessary.

## Usage

1. Run the application:
   ```
   streamlit run app.py
   ```
2. Access the dashboard in your web browser at `http://localhost:8501`.

## Project Structure

- `app.py`: The main application file that defines the Streamlit dashboard and handles data retrieval and visualization.
- `data_extraction.py`: Contains the script to clone the PhonePe Pulse GitHub repository and extract the data.
- `data_transformation.py`: Includes functions for data cleaning and transformation using Python and Pandas.
- `database.py`: Handles the MySQL database connection and data insertion.
- `utils.py`: Utility functions for visualization and data retrieval.

## Data Extraction and Transformation

The data extraction is performed by running the `data_extraction.py` script. This script clones the PhonePe Pulse GitHub repository and stores the data in a suitable format such as CSV or JSON. The extracted data is then pre-processed and cleaned using the `data_transformation.py` script. Missing values are handled, and the data is transformed into a format suitable for analysis and visualization.

## Database Insertion

The `database.py` script establishes a connection to the MySQL database and inserts the transformed data using SQL commands. Make sure to update the MySQL connection details in the script before running it.

## Dashboard Creation

The main application file, `app.py`, creates an interactive dashboard using Streamlit and Plotly. The dashboard provides a user-friendly interface with dropdown options for users to select different facts and figures to display. Plotly's built-in geo map functions are utilized to visualize the data on a map. The dashboard dynamically fetches the data from the MySQL database using the `database.py` script and updates the visualizations accordingly.

## Additional Resources

- The `data` directory contains the extracted and transformed data files.
- The `images` directory includes images used in the dashboard.
- The `requirements.txt` file lists the required Python dependencies for the project.

## Conclusion

This project provides a comprehensive solution for extracting, transforming, and visualizing data from the PhonePe Pulse GitHub repository. The resulting dashboard offers valuable insights and information about PhonePe transactions in India. Users can explore various metrics and statistics in an interactive and visually appealing manner, aiding data analysis and decision-making.
