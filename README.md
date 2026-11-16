# ⚡ EV Range Estimation & Energy Consumption Analyzer

A Python tool that estimates the driving range of an electric vehicle and
analyzes its energy consumption from vehicle/driving data, with charts and a
user interface.

## 📌 Problem Statement
Range anxiety is one of the biggest barriers to EV adoption. Real range
changes with speed, load and driving conditions, so a single manufacturer
figure can be misleading. This project estimates range from [inputs, e.g.
battery capacity, speed, consumption] and shows how energy is being used.

## ✨ Features
- Range estimation from [battery capacity, consumption rate, speed, etc.]
- Energy consumption analysis [per km / per trip / by speed]
- Visualizations of [consumption vs speed, range comparison, etc.]
- User interface to enter parameters and view results
- Results saved to `range_results.csv`

## 🛠️ Tech Stack
Python · [Pandas · NumPy · Matplotlib] · [Tkinter / Streamlit / Flask]

## 📂 Project Structure
```
EV-Range-Estimation-Energy-Consumption-Analyzer/
│
├── data/
│   └── ev_data.csv              # Input dataset (vehicle / driving data)
│
├── modules/
│   ├── range_calculation.py     # Range estimation logic
│   ├── energy_analysis.py       # Energy consumption analysis
│   └── Visualiz.py              # Charts and visualizations
│
├── interface/
│   └── interface.py             # User interface
│
├── app.py                       # Main entry point
├── range_results.csv            # Generated output
└── README.md
```

## ⚙️ How It Works
1. `data/ev_data.csv` supplies the vehicle and driving data.
2. `modules/range_calculation.py` computes the estimated range using
   `Range (km) = Usable Battery Energy (kWh) / Consumption (kWh/km)`
   [adjust to your actual formula].
3. `modules/energy_analysis.py` analyzes energy consumption.
4. `modules/Visualiz.py` generates the plots.
5. `interface/interface.py` lets the user enter inputs and view results.
6. Output is saved to `range_results.csv`.

## 🚀 Getting Started
```bash
git clone https://github.com/Yashu219/EV-Range-Estimation-Energy-Consumption-Analyzer.git
cd EV-Range-Estimation-Energy-Consumption-Analyzer
pip install -r requirements.txt
python app.py
```

## 📊 Results
- [Key finding 1, e.g. how consumption changes with speed]
- [Key finding 2, e.g. estimated range for the tested vehicle]

| Interface | Chart |
|-----------|-------|
| ![Interface](screenshots/interface.png) | ![Chart](screenshots/chart.png) |

## 🔮 Future Improvements
- Real-time data from the vehicle or battery sensors
- Temperature, terrain and regenerative braking effects
- ML model for more accurate range prediction
- Web deployment

## 👩‍💻 Author
**Yashaswini A** · yashaswinia21@gmail.com · [GitHub](https://github.com/Yashu219)
