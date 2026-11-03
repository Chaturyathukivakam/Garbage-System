<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:14532D,50:16A34A,100:4ADE80&height=220&section=header&text=EcoTrack%20%7C%20Garbage%20Management&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Smart%20Waste%20Intelligence%20and%20Environmental%20Impact%20Analytics&descSize=16&descAlignY=62" width="100%" alt="EcoTrack Header Banner"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/>
  <img src="https://img.shields.io/badge/Status-Deployed-success?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/github/stars/Chaturyathukivakam/Garbage-System?style=for-the-badge&color=yellow" alt="Stars"/>
</p>

---

## 📋 Executive Summary

Rapid urbanization has intensified municipal solid waste management challenges. Traditional waste tracking relies heavily on fragmented logs and retrospective audits, making it difficult for civic administrators to optimize segregation efficiency, identify underperforming collection zones, and quantify environmental offsets.

**EcoTrack** is a centralized waste intelligence and analytics web application developed with **Python**, **Streamlit**, **Pandas**, and **Plotly**. It equips municipal authorities, facility supervisors, and sustainability stakeholders with real-time operational visibility into daily waste collection volumes, segregation compliance, and ecological benefits (including carbon offset calculations and landfill space conservation).

---

## 📑 Table of Contents

- [Key Features & Capabilities](#-key-features--capabilities)
- [System Architecture & Data Flow](#-system-architecture--data-flow)
- [Tech Stack Breakdown](#-tech-stack-breakdown)
- [Quickstart & Local Execution](#-quickstart--local-execution)
- [Project Directory Layout](#-project-directory-layout)
- [Author & Contributions](#-author--contributions)

---

## ✨ Key Features & Capabilities

- **Real-Time Operational Dashboard** — Live KPI overview displaying total waste tonnage, diversion rate percentage, operating logistics costs, and active collection zones.
- **Interactive Multi-Domain Analytics** — Plotly-driven visualizations including category breakdown donut charts, timeline trends across dates, and zone-level comparison bars.
- **Dynamic Waste Logging & Data Ingestion** — Upload custom `.csv` or `.xlsx` logs, apply real-time filters by category/zone/recyclability, and dynamically log new collection batches in session.
- **Environmental Impact & Carbon Calculator** — Formulated computations assessing metric tons of CO₂ equivalent avoided, mature trees saved, electrical energy conserved (kWh), and landfill volume spared ($m^3$).
- **Color-Coded Segregation Taxonomy** — Standardized operational guidelines (Organic/Wet, Recyclable Dry, Domestic Hazardous, and E-Waste).

---

## 🏗️ System Architecture & Data Flow

```mermaid
flowchart TD
    A["📥 Waste Collection Data<br/>(CSV / Manual Input)"] --> B["🧹 Data Pipeline (Pandas)<br/>Validation · Type Parsing · Zone Grouping"]
    B --> C{"📊 Analytics Engine"}
    C --> D["📈 KPI & Timeline Metrics<br/>Tonnage · Cost · Diversion Rate"]
    C --> E["🌱 Carbon Calculator<br/>CO₂e Offset · Landfill Volume Saved"]
    C --> F["🍩 Category Breakdown<br/>Plotly Donut & Bar Charts"]
    D --> G["🖥️ Interactive Streamlit Interface"]
    E --> G
    F --> G
```

---

## 🛠️ Tech Stack Breakdown

| Category | Technology | Purpose |
|----------|------------|---------|
| **Core Language** | Python 3.9+ | Application logic and analytics execution |
| **Interactive UI** | Streamlit | Responsive browser-based dashboard interface |
| **Data Processing** | Pandas | Dataframe transformations, cleansing, and aggregations |
| **Visualization** | Plotly Express & Graph Objects | Dynamic charting, interactive gauges, and timeline distributions |
| **Deployment** | Streamlit Cloud / Docker | Containerized and cloud-hosted application access |

---

## 🚀 Quickstart & Local Execution

### Prerequisites

- Python 3.9 or higher
- `pip` package manager

### Installation & Launch

```bash
# 1. Clone the repository
git clone https://github.com/Chaturyathukivakam/Garbage-System.git
cd Garbage-System

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the application
streamlit run app.py
```

The application will automatically start and open in your default browser at `http://localhost:8501`.

---

## 📂 Project Directory Layout

```
Garbage-System/
├── app.py                                    # Main Streamlit analytics application
├── requirements.txt                          # Python dependencies
├── presentation.html                         # Interactive browser presentation deck
├── Alliance_Garbage_Management_Presentation.pptx # Project presentation slide deck
├── Garbage_Management_System_Presentation.pptx  # Summary presentation
├── .streamlit/
│   └── config.toml                           # Streamlit server & UI theme config
├── data/
│   └── sample_waste_data.csv                 # Standardized reference dataset
└── README.md                                 # Technical documentation
```

---

## 👤 Author & Contributions

**Thukivakam Chaturya**

[![GitHub](https://img.shields.io/badge/GitHub-14532D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Chaturyathukivakam)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-16A34A?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thukivakam-chaturya-206023326/)
[![Portfolio](https://img.shields.io/badge/Portfolio-4ADE80?style=for-the-badge&logo=vercel&logoColor=black)](https://chaturyathukivakam.github.io/3D-Portfolio/)

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:14532D,50:16A34A,100:4ADE80&height=100&section=footer" width="100%" alt="EcoTrack Footer Banner"/>
</p>
