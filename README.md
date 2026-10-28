# ♻️ EcoTrack - Smart Garbage Management System

A web-based waste intelligence and analytics application built with **Python**, **Streamlit**, **Pandas**, and **Plotly**, designed to help municipalities, waste managers, and citizens monitor waste collection, categories, recycling efficiency, and environmental impact.

---

## 🌟 Key Features

1. **🏠 Real-time Home Dashboard**
   - KPI metrics: Total waste collected, recycling diversion rate, operational costs, active collection zones.
   - Interactive Plotly visualizations: Waste distribution donut chart, daily collection timeline, zone comparison, and disposal facility status.

2. **📊 Waste Data Management**
   - Upload custom `.csv` or `.xlsx` datasets.
   - Interactive multi-criteria filtering by zone, waste category, recyclable status, and date range.
   - Dynamic record logging form to add new waste collection entries directly in session.
   - One-click export of filtered data to CSV.

3. **🌱 Environmental Impact & Carbon Calculator**
   - Computes carbon offset (MT CO₂e avoided), trees preserved from recycled paper, energy conserved (kWh), and landfill volume saved ($m^3$).
   - Interactive gauge showing target vs. actual diversion rate.

4. **📖 Segregation & Rules Guide**
   - Color-coded educational cards (Green = Wet/Organic, Blue = Dry Recyclable, Red = Domestic Hazardous, Purple = E-Waste).

5. **🚀 Streamlit Community Cloud Ready**
   - Pre-configured `.streamlit/config.toml` and `requirements.txt` for one-click deployment.

---

## 📁 Project Structure

```
garbage_management_system/
├── app.py                     # Main Streamlit web application
├── requirements.txt           # Python dependencies for deployment
├── README.md                  # Documentation and deployment steps
├── .streamlit/
│   └── config.toml           # Theme and server configuration
└── data/
    └── sample_waste_data.csv  # Realistic starter dataset
```

---

## 💻 Local Setup & Execution

### Prerequisites
- Python 3.9+ installed on your computer.

### Steps
1. Open your terminal or command prompt and navigate to the project directory:
   ```bash
   cd garbage_management_system
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   The application will automatically open in your browser at `http://localhost:8501`.

---

## 🌐 Deploy to Streamlit Community Cloud (Free Public URL)

1. **Push to GitHub**:
   - Initialize git and commit the files inside `garbage_management_system/`:
     ```bash
     git init
     git add .
     git commit -m "Initial commit for Garbage Management System"
     git branch -M main
     git remote add origin https://github.com/<your-username>/garbage-management-system.git
     git push -u origin main
     ```
2. **Deploy on Streamlit Community Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
   - Click **New app**.
   - Select your repository (`garbage-management-system`), branch (`main`), and set the main file path to `app.py`.
   - Click **Deploy!**

Your app will be live with a public URL in 1–2 minutes!
