# My_Repository
# 🚗 Vehicle Dashboard Web App

This is a **Streamlit** dashboard that visualizes data from a dataset of used vehicles in the United States. It provides interactive charts and filters to help users explore vehicle trends and distributions.

## 🌐 Live App

👉 [Click here to view the app on Render](https://my-repository-4-xmud.onrender.com/)  
*(Note: If the app is asleep, it may take a few moments to wake up.)*

## 📊 Features

- View total counts of each vehicle type
- Interactive histogram and scatter plots using Plotly
- Toggle filters using checkboxes
- Clean, simple user interface powered by Streamlit

## 🧰 Technologies Used

-  **Python 3.11**
-  Streamlit – https://streamlit.io
-  Pandas – https://pandas.pydata.org
-  NumPy – https://numpy.org
-  SciPy – https://scipy.org
-  Matplotlib – https://matplotlib.org
-  Plotly – https://plotly.com/python/
-  nbformat – https://nbformat.readthedocs.io/en/latest/

## 🗂️ Project Structure
My_Repository/ ├── .streamlit/ │ └── config.toml ├── app.py ├── vehicles_us.csv ├── requirements.txt └── README.md


## 🛠️ How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/JonPHames11/My_Repository.git
   cd My_Repository

python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On Mac/Linux

pip install -r requirements.txt

streamlit run app.py
