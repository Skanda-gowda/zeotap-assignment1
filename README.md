# zeotap-assignment1
Google Sheets Mimic Using Streamlit
A powerful web-based application built with Streamlit that replicates essential features of Google Sheets, including spreadsheet editing, data quality functions, mathematical operations, font styling, and data visualization with a sleek and intuitive user interface.

Features
Editable Spreadsheet: Edit a dynamic spreadsheet with customizable rows and columns.
Mathematical Operations: Perform operations like SUM, AVERAGE, MAX, MIN, and COUNT over specified cell ranges.
Data Quality Functions: Trim whitespace, change case (UPPER/LOWER), remove duplicates, and perform find-and-replace operations.
Font Styling: Customize font size, color, and style (italic, bold) for specific cell ranges.
Preview Styled Spreadsheet: Visualize the styled spreadsheet with improved contrast and aesthetics.
Data Visualization: Generate bar charts based on spreadsheet data.
File Handling: Save spreadsheets to and load spreadsheets from Excel files.
Tech Stack
1. Streamlit
Why: Provides a fast, efficient way to create interactive, data-driven web applications with Python.
Usage: Handles the front-end rendering, interactivity, and user interface of the application.
2. Pandas
Why: Offers robust data manipulation and analysis capabilities.
Usage: Manages spreadsheet data, applies data quality functions, and performs mathematical operations.
3. NumPy
Why: Efficiently handles numeric operations and supports mathematical calculations.
Usage: Ensures smooth operations for numeric computations in the spreadsheet.
4. Data Structures
DataFrame (Pandas):
Why: Provides a tabular structure that closely resembles a spreadsheet, making it an ideal choice for this project.
Usage: Stores and manipulates spreadsheet data dynamically, ensuring compatibility with mathematical and data quality operations.
Dictionary:
Why: Lightweight and efficient for storing styles associated with specific cell ranges.
Usage: Maps font styles (size, color, etc.) to cell ranges for applying custom formatting.
5. Matplotlib (via Streamlit Bar Charts)
Why: Offers built-in support for data visualization with simple integration.
Usage: Renders bar charts for visualizing column-wise data summaries.
Key Design Decisions
Dynamic Spreadsheet Editing:

Achieved using Streamlit’s st.data_editor, allowing users to interactively edit spreadsheet cells.
Mathematical Operations:

Designed a helper function (perform_operation) to calculate aggregates over cell ranges.
Handled cell referencing by mapping column letters (e.g., A, B) to DataFrame indices.
Font Styling:

Used custom HTML rendering for styling specific cell ranges.
Incorporated support for bold, italic, and dynamic font sizes/colors.
Data Quality Functions:

Implemented reusable functions to clean and process spreadsheet data (e.g., trimming, case conversion, and duplicate removal).
File Handling:

Integrated support for reading and writing Excel files using Pandas for persistent storage of spreadsheet data.
User Interface:

Optimized the UI with dark-mode aesthetics, improved cell visibility, and a responsive layout.
Setup Instructions
Clone the Repository:

bash
Copy
Edit
git clone <repository-url>
cd <repository-folder>
Set Up Virtual Environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Application:

bash
Copy
Edit
streamlit run app.py
Access the App:

Open the link provided in the terminal (e.g., http://localhost:8501) in your browser.
Future Enhancements
Add support for cell dependency and drag-to-fill operations.
Incorporate more advanced data visualizations (e.g., pie charts, scatter plots).
Introduce collaborative editing features for real-time updates.
Contributing
Feel free to fork the repository, make changes, and submit a pull request. Contributions are always welcome!

License
This project is open-source and available under the MIT License.

Let me know if you need help refining the structure or adding specific details!
