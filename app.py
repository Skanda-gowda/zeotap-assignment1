import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Initialize session state ---
if "spreadsheet" not in st.session_state:
    st.session_state.spreadsheet = pd.DataFrame(
        [["" for _ in range(5)] for _ in range(5)], columns=list("ABCDE")
    )
if "styles" not in st.session_state:
    st.session_state.styles = {}

# --- Page Configurations ---
st.set_page_config(
    page_title="Google Sheets Mimic",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
        .main { background-color: #1a1a1a; color: white; }
        .stButton button { 
            background-color: #0073e6;
            color: white;
            border-radius: 5px;
            font-size: 16px;
            padding: 5px 20px;
        }
        .stButton button:hover {
            background-color: #005bb5;
        }
        table { 
            border-collapse: collapse; 
            width: 100%; 
            background-color: black;
        }
        table, th, td { 
            border: 1px solid #444; 
        }
        th, td { 
            text-align: left; 
            padding: 8px; 
            color: white;
        }
        tr:nth-child(even) { 
            background-color: #222; 
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Helper Functions ---
def perform_operation(data, operation, range_start, range_end):
    try:
        col_map = {chr(65 + i): i for i in range(len(data.columns))}
        start_row, start_col = int(range_start[1:]) - 1, col_map[range_start[0]]
        end_row, end_col = int(range_end[1:]) - 1, col_map[range_end[0]]
        subrange = data.iloc[start_row:end_row + 1, start_col:end_col + 1]
        subrange_numeric = subrange.apply(pd.to_numeric, errors="coerce")
        if operation == "SUM":
            return subrange_numeric.sum().sum()
        elif operation == "AVERAGE":
            return subrange_numeric.mean().mean()
        elif operation == "MAX":
            return subrange_numeric.max().max()
        elif operation == "MIN":
            return subrange_numeric.min().min()
        elif operation == "COUNT":
            return subrange_numeric.count().sum()
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Error: {e}"

def apply_data_quality_function(df, operation, find_text=None, replace_text=None):
    if operation == "TRIM":
        return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    elif operation == "UPPER":
        return df.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    elif operation == "LOWER":
        return df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    elif operation == "REMOVE_DUPLICATES":
        return df.drop_duplicates()
    elif operation == "FIND_AND_REPLACE" and find_text and replace_text:
        return df.replace(find_text, replace_text, regex=True)
    return df

def apply_styles_to_dataframe(df, styles):
    """Apply font styles to a DataFrame using pandas styling."""
    styled_df = df.style.set_table_styles(
        [{"selector": "table", "props": [("background-color", "black")]}]
    ).set_properties(
        **{"color": "white", "border-color": "#444", "text-align": "center"}
    )

    for (range_start, range_end), style in styles.items():
        col_map = {chr(65 + i): i for i in range(len(df.columns))}
        start_row, start_col = int(range_start[1:]) - 1, col_map[range_start[0]]
        end_row, end_col = int(range_end[1:]) - 1, col_map[range_end[0]]

        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                styled_df = styled_df.applymap(
                    lambda _: (
                        f"color: {style['font_color']}; "
                        f"font-size: {style['font_size']}px; "
                        f"font-style: {style['font_style']};"  # Correctly apply italic
                        f"font-weight: {'bold' if style['font_style'] == 'bold' else 'normal'};"  # Handle bold properly
                    ),
                    subset=(df.index[row], df.columns[col]),
                )
    return styled_df


# --- App Layout ---
st.title("📊 Google Sheets Mimic - Streamlit")
st.subheader("A spreadsheet-like interface for data management and visualization")

# --- Editable Spreadsheet ---
st.markdown("### ✍️ Editable Spreadsheet")
edited_spreadsheet = st.data_editor(
    st.session_state.spreadsheet,
    num_rows="dynamic",
    use_container_width=True,
)
st.session_state.spreadsheet = edited_spreadsheet

# --- Mathematical Operations ---
st.markdown("### 🧮 Mathematical Functions")
operation = st.selectbox("📋 Select Operation", ["SUM", "AVERAGE", "MAX", "MIN", "COUNT"])
range_start = st.text_input("🟢 Enter Start Cell (e.g., A1)", value="A1")
range_end = st.text_input("🔵 Enter End Cell (e.g., B3)", value="B3")
if operation and range_start and range_end:
    result = perform_operation(st.session_state.spreadsheet, operation, range_start, range_end)
    st.success(f"📌 Result of {operation} from {range_start} to {range_end}: **{result}**")

# --- Font Styling ---
st.markdown("### 🎨 Font Styling Options")
font_size = st.slider("🔠 Font Size (in px)", 8, 36, 12)
font_color = st.color_picker("🎨 Font Color", value="#FFFFFF")
font_style = st.selectbox("🖋️ Font Style", ["normal", "bold", "italic"])
if st.button("Apply Font Style"):
    st.session_state.styles[(range_start, range_end)] = {
        "font_size": font_size,
        "font_color": font_color,
        "font_style": font_style,
    }
    st.success(f"🎉 Font style applied to range {range_start}:{range_end}")

# --- Data Quality Functions ---
st.markdown("### 🛠️ Data Quality Functions")
data_quality = st.selectbox(
    "🧹 Select Data Quality Function",
    ["None", "TRIM", "UPPER", "LOWER", "REMOVE_DUPLICATES", "FIND_AND_REPLACE"],
)
if data_quality != "None":
    if data_quality == "FIND_AND_REPLACE":
        find_text = st.text_input("🔍 Find Text")
        replace_text = st.text_input("✏️ Replace With")
        if st.button("Apply Find and Replace"):
            st.session_state.spreadsheet = apply_data_quality_function(
                st.session_state.spreadsheet, data_quality, find_text, replace_text
            )
    else:
        if st.button(f"Apply {data_quality}"):
            st.session_state.spreadsheet = apply_data_quality_function(
                st.session_state.spreadsheet, data_quality
            )

# --- Data Visualization ---
st.markdown("### 📈 Data Visualization (SUM)")
chart_type = st.selectbox("📊 Select Chart Type", ["Bar Chart", "Line Chart", "Area Chart"])
chart_data = st.session_state.spreadsheet.apply(pd.to_numeric, errors="coerce").sum()

if chart_type == "Bar Chart":
    st.bar_chart(chart_data)
elif chart_type == "Line Chart":
    st.line_chart(chart_data)
elif chart_type == "Area Chart":
    st.area_chart(chart_data)

# --- Preview Styled Data ---
st.markdown("### 🔍 Preview Styled Spreadsheet")
styled_df = apply_styles_to_dataframe(st.session_state.spreadsheet, st.session_state.styles)
st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

# --- Save and Load ---
st.markdown("### 💾 Save and Load")
save_file = st.button("💾 Save File")
load_file = st.file_uploader("📂 Load Spreadsheet", type=["xlsx"])
if save_file:
    file_name = st.text_input("Enter file name", value="spreadsheet.xlsx")
    st.session_state.spreadsheet.to_excel(file_name, index=False)
    st.success(f"Spreadsheet saved as {file_name}!")
if load_file:
    try:
        st.session_state.spreadsheet = pd.read_excel(load_file)
        st.success("Spreadsheet loaded successfully!")
    except Exception as e:
        st.error(f"Error loading file: {e}")
