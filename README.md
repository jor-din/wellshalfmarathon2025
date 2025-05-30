# 🏃‍♀️ Strava Half-Marathon Training Analysis (Jan–May 2025)

This project analyzes my personal half-marathon training data using the Strava API. I used Python to extract, clean, and visualize metrics like distance, pace, heart rate, and cadence across a 17-week training block leading up to race day.

---

## 📌 Project Summary

- **Duration Analyzed**: Jan 6, 2025 – May 4, 2025
- **Race**: Maine Coast Half Marathon
- **Training Goal**: Track improvement in pace, distance, heart rate, and running efficiency
- **Tools Used**: Python, Pandas, Matplotlib, Strava API

---

## 🧪 Data Processing Steps

1. **Data Collection**  
   - Used [Strava API](https://developers.strava.com/) to pull run activities
   - Saved and exported raw activity data as CSV

2. **Cleaning & Transformation**  
   - Converted distance (meters → miles) and time (seconds → minutes)
   - Calculated pace in `MM:SS` format
   - Removed pace outliers (via IQR or reasonable range)
   - Adjusted cadence to total steps per minute (`SPM = cadence * 2`)

3. **Weekly Aggregation**  
   - Grouped activities by week (`start_date`)
   - Summarized:
     - Total weekly mileage
     - Average pace
     - Average heart rate (BPM)
     - Average cadence (SPM)
     - Average speed (m/s)

---

## 📊 Visualizations

All plots generated using `matplotlib`:
- Weekly Mileage Trends
- Weekly Average Pace (`MM:SS`)
- Heart Rate Over Time
- Cadence Improvements
  
![wellshalf2025 - viz](https://github.com/user-attachments/assets/4268a57f-3512-4f9e-b275-1aec48422670)


---


##  Key Insights

- 📈 **Mileage Growth**  
  Weekly mileage increased by **over 235%**, from 6.2 miles in Week 2 to a peak of 20.8 miles, showing strong volume progression and training consistency.

- ⏱️ **Pace Improvement**  
  Average pace dropped from **11:37 to 9:54 min/mi**, a **14.7% improvement** — reflecting increased aerobic capacity and efficient pacing.

- ❤️ **Cardiovascular Efficiency**  
  Despite faster paces, average heart rate decreased by up to **11 BPM**, indicating improved cardiovascular endurance and recovery.

- 🦶 **Cadence Optimization**  
  Cadence increased from **156 SPM to 178 SPM**, aligning with the ideal range for distance runners. This indicates better running form and stride economy.

- 🧠 **Smart Tapering**  
  Strategic mileage reductions before race week suggest proper tapering, helping me arrive at the start line fresh and race-ready.

- 🎯 **Consistent Progress**  
  The trends show steady progress across all metrics with minimal regressions — a strong sign of balanced training and sustainable improvement.

---



## 📂 File Structure

```bash
wellshalfmarathon2025/
├── strava_api.py              # Pulls data from Strava API
├── strava_cleaning.py         # Filters, cleans, and processes data
├── strava_analysis.py         # Generates plots and insights
├── strava_activities.csv
├── wellshalf2025 - viz.png       # Output visualizations
├── README.md
