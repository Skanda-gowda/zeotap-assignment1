# Google Sheets Mimic Using Streamlit

A feature-rich, interactive web-based application that replicates essential functionalities of Google Sheets. Built using Streamlit, this app offers spreadsheet editing, mathematical operations, data quality enhancements, font styling, and data visualization, all wrapped in a sleek, intuitive interface.

---

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/2c8d7eeb-e5c9-4d69-b90d-99e8cc7b1fb6)

![image](https://github.com/user-attachments/assets/f2b76312-7511-44b2-9716-2d2cae385bac)

![image](https://github.com/user-attachments/assets/f7b9962c-954a-40f8-ac2a-c2413653537a)

![image](https://github.com/user-attachments/assets/03eb3a25-ffa4-4b87-85fa-27c2005d4fac)

![image](https://github.com/user-attachments/assets/7112d5b7-8fcb-4c94-a17c-2c79e36500c2)

---



## 🚀 Features

### 📝 Editable Spreadsheet
- Add, edit, and delete cells dynamically.
- Handles dynamic row and column updates efficiently.

### 📊 Mathematical Operations
- Perform operations like **SUM**, **AVERAGE**, **MAX**, **MIN**, and **COUNT** over specified cell ranges.

### 🧹 Data Quality Functions
- **TRIM**: Remove leading and trailing whitespaces.
- **UPPER/LOWER**: Convert text to uppercase or lowercase.
- **REMOVE_DUPLICATES**: Eliminate duplicate rows.
- **FIND AND REPLACE**: Search and replace text across the spreadsheet.

### 🎨 Font Styling
- Customize **font size**, **color**, and **style** (bold, italic) for specific cell ranges.
- Styled preview with a dark-themed spreadsheet for better visibility.

### 📈 Data Visualization
- Generate **bar charts** dynamically from spreadsheet data for quick insights.

### 💾 File Handling
- Save spreadsheets as Excel files and reload them seamlessly.

---

## 🛠️ Tech Stack

### 1. **Streamlit**
   - **Why**: Streamlit simplifies building interactive, user-friendly applications with minimal coding.
   - **Usage**: Provides the front-end interface, data interaction, and real-time updates.

### 2. **Pandas**
   - **Why**: Pandas is a robust library for data manipulation and analysis.
   - **Usage**: Manages the spreadsheet backend, applies data quality functions, and performs mathematical operations.

### 3. **NumPy**
   - **Why**: Ensures efficient numeric computations for data aggregation and analysis.
   - **Usage**: Facilitates operations like SUM, AVERAGE, MAX, and MIN.

### 4. **Matplotlib (via Streamlit Charts)**
   - **Why**: Supports simple and visually appealing data visualization.
   - **Usage**: Creates bar charts for data insights directly from the spreadsheet.

### 5. **Data Structures**
   - **DataFrame (Pandas)**:
     - **Why**: A tabular structure that mirrors spreadsheets and supports dynamic data operations.
     - **Usage**: Manages cell data, enabling seamless integration of features like data quality functions and range-based computations.
   - **Dictionary**:
     - **Why**: Efficiently maps font styles to specific cell ranges for rendering styled outputs.
     - **Usage**: Stores and applies font-related properties like size, color, and style.

---

## 📖 Setup Instructions

### 1. **Clone the Repository**
```
git clone <repository-url>
cd <repository-folder>
```
2. Set Up Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the Application
```
streamlit run app.py
```
5. Access the App
Open the link provided in the terminal (e.g., http://localhost:8501) in your browser.

🎯 Future Enhancements
Cell Dependency and Drag-to-Fill:

Add support for handling formulas and dependent cells.
Introduce drag-to-fill functionality for auto-generating data.
Advanced Visualizations:

Incorporate charts like pie charts and scatter plots for detailed insights.
Collaborative Editing:

Enable real-time collaboration for multiple users.
🤝 Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a new branch:
```
git checkout -b feature-branch
```
Make your changes and commit:
```
git commit -m "Description of changes"
```
Push your branch and open a pull request.
📜 License
This project is open-source and available under the MIT License.

🔗 Steps for Uploading to GitHub
Prepare the Project

Place the README.md file in the root directory.
Add a requirements.txt file listing dependencies:

pandas
numpy
streamlit
openpyxl
Initialize Git

```
git init
```
Add Files to Git

```
git add .
```
Commit Changes

```
git commit -m "Initial commit with Google Sheets mimic project"
```
Push to GitHub

```
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```
🔥 Ready to Explore?
Clone the repository, run the app, and experience the Google Sheets Mimic in action!








