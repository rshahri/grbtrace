# grbtrace 🌌⚡

A modular Python pipeline for detecting and analyzing Gamma-Ray Bursts (GRBs) from time-series data produced by high-energy observatories such as the Fermi Gamma-ray Burst Monitor (GBM).

---

## 📚 Overview

**grbtrace** provides an end-to-end workflow for GRB analysis:

1. Simulate synthetic GRB light curves for method development  
2. Load real telescope FITS data (CTIME / TTE products)  
3. Detect burst emission intervals  
4. Extract key temporal features (e.g., T90, peak rate, fluence)  
5. Visualize burst structure and detection windows  

The project bridges astrophysical signal processing with modern data-science workflows, enabling reproducible experimentation and future ML-based burst characterization.

---

## 🚀 Features

- 📥 Load and parse GBM FITS data (CTIME currently supported, TTE planned)  
- 🎲 Generate synthetic GRB light curves for pipeline validation  
- 🔍 Detect burst emission using threshold-based detection  
- 📏 Extract astrophysical features (T90 duration, peak rate, fluence proxy)  
- 📊 Visualize light curves with detection overlays  
- 🧪 Unit-tested feature extraction for regression safety  
- 🔧 Modular design for future extensions (Bayesian Blocks, ML classification)

---

## 🧠 Project Motivation

GRB analysis pipelines often require domain knowledge and specialized tooling.  
**grbtrace** aims to provide a lightweight, educational, and extensible framework that allows:

- students to explore high-energy astrophysics data  
- researchers to prototype detection methods  
- data scientists to experiment with real astronomical time series  

---

## ▶️ Getting Started

Clone the repository and run the notebooks:

```bash
git clone https://github.com/rshahri/grbtrace.git
cd grbtrace
```

Then open:

- 01_phase1_simulated_pipeline.ipynb → synthetic validation

- 02_phase2_real_data_pipeline.ipynb → real GBM analysis

---

## 🔮 Roadmap

- Automatic background modeling for robust burst isolation

- Bayesian Blocks burst detection

- Multi-energy feature extraction (hardness ratio)

- Batch processing of multiple GRB triggers

- ML-based GRB classification and clustering

---

## 📖 Acknowledgments

Data used in examples originates from the NASA Fermi Gamma-ray Burst Monitor (GBM) archive.
