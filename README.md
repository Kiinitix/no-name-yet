# Virtual Machine Introspection-Based Malware Detection Using Adversarial Autoencoder Neural Networks

This project implements a Virtual Machine Introspection (VMI)-based malware detection system in a virtualized cloud computing environment. The solution leverages adversarial autoencoder neural networks to detect malware and is designed to run as a menu-driven system with modular components for ease of scalability and maintenance.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [Main](#main)
  - [Model](#model)
  - [Data Loader](#data-loader)
  - [Prediction System](#prediction-system)
  - [Utilities](#utilities)
- [Dataset](#dataset)
- [Testing](#testing)
- [Contributing](#contributing)
- [Further Reading](#further-reading)

---

## Project Overview
This project aims to build a malware detection system in virtualized environments. By using **adversarial autoencoder neural networks**, the system can detect anomalies by analyzing system calls, memory footprints, and other introspection-based metrics from virtual machines. The core of the system is built in Python, and it is modular to support enhancements and scalability.

### Key Features:
- Menu-driven interaction.
- Modular and scalable design.
- Neural network-based malware detection.
- Virtual Machine Introspection-based features.
- Test coverage for core utilities.

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/kiinitix/no-name-yet.git
    cd vmi-malware-detection
    ```

2. **Install required packages**:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure that you have Python 3.8 or higher.

3. **Set up the dataset**:
   
    Download the dataset from the relevant source (see the [Dataset](#dataset) section below) and place it in the `data/` directory.

---

## Usage

1. **Run the main program**:

    ```bash
    python main.py
    ```

    The system will present a menu-driven interface where you can:
    - Load a dataset
    - Train the adversarial autoencoder model
    - Perform malware detection predictions
    - Exit the program

2. **Make Predictions**:
   After training the model, you can provide new input via the interface for real-time predictions.

---

## Modules

### Main
This is the entry point of the project, responsible for displaying the menu and handling user interaction.

### Model
Contains the neural network implementation, specifically the **Adversarial Autoencoder** used for malware detection.

### Data Loader
Handles loading and preprocessing of the dataset, including scaling and encoding.

### Prediction System
Handles input from the user and interfaces with the trained model to provide malware/benign predictions.

### Utilities
Contains utility functions for input validation, logging, and data manipulation. This module supports other parts of the system with common tasks.

---

## Dataset

This system requires a dataset of introspection features such as memory access patterns, system call logs, and network traffic details. Here are some publicly available datasets that can be used:

1. **UNSW-NB15**: A dataset containing network packets and system information, available at [UNSW-NB15 dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset).
2. **CICIDS 2017**: Contains data from a simulated network environment, available at [CICIDS Dataset](https://www.unb.ca/cic/datasets/ids-2017.html).

Ensure you preprocess the data and provide it in a compatible format (e.g., CSV files).

---

## Testing

Unit tests for utility functions and core features are located in the `tests/` directory.

1. **Run all tests**:

    ```bash
    python -m unittest discover tests/
    ```

Tests cover:
- User input validation
- Input conversion
- Basic data manipulations

For extensive testing, consider using additional frameworks like `pytest`.

---

## Contributing

We welcome contributions! Here’s how you can get involved:
1. Fork the project.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit and push to your branch (`git push origin feature-branch`).
5. Submit a pull request with a detailed description of your changes.

---

## Further Reading

If you'd like to dive deeper into the topics related to this project, check out these resources:

1. **Virtual Machine Introspection**:
   - Garfinkel, T., & Rosenblum, M. (2003). "A Virtual Machine Introspection-Based Architecture for Intrusion Detection." *Proceedings of NDSS*. [Link](https://www.usenix.org/conference/ndss-2003/virtual-machine-introspection-based-architecture-intrusion-detection)

2. **Adversarial Autoencoders**:
   - Makhzani, A., et al. (2015). "Adversarial Autoencoders." *arXiv preprint arXiv:1511.05644*. [Link](https://arxiv.org/abs/1511.05644)

3. **Cloud Malware Detection**:
   - Abu, R., Varol, A., & Kiraz, M. (2020). "A Survey on Malware Detection in Cloud Computing Systems." *IEEE Access*.

For further machine learning and deep learning reading:
- "Deep Learning with Python" by François Chollet (for fundamental deep learning concepts).
- "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron (great for practical machine learning).


