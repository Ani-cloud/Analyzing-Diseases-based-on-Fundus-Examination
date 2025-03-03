# Analyzing Diseases Based on Fundus Examination

## Project Overview
This project leverages fundus examination images to analyze and diagnose ocular diseases. By employing image processing and machine learning techniques, it aims to assist in identifying conditions such as diabetic retinopathy, glaucoma, and age-related macular degeneration (AMD).

## Features
- **Convolutional Neural Network (CNN) Model**: Implements a CNN for disease classification (`CNNModel.py`).
- **Graphical User Interface (GUI)**: Provides user-friendly interfaces for image analysis (`new_GUI_Master.py`, `GUI_Master_old.py`).
- **User Authentication**: Features login and registration functionalities (`login.py`, `final_gui_registration_page.py`).
- **Database Integration**: Utilizes a SQLite database to manage user data (`fundas.db`).
- **Visualization**: Includes accuracy and loss plots to evaluate model performance (`fundas_accuracy.png`, `loss.png`).

## Repository Structure
- `CNNModel.py`: Defines the CNN architecture for disease classification.
- `new_GUI_Master.py`: Main GUI for user interaction and image analysis.
- `login.py`: Manages user login functionality.
- `final_gui_registration_page.py`: Handles user registration processes.
- `fundas.db`: SQLite database storing user information.
- `fundas_accuracy.png` & `loss.png`: Visual representations of model performance.
- `Test Dataset/`: Directory containing test images for model evaluation.

## Installation Guide
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ani-cloud/Analyzing-Diseases-based-on-Fundus-Examination.git
   cd Analyzing-Diseases-based-on-Fundus-Examination
Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

Install dependencies:-
pip install -r requirements.txt

Initialize the database:-
python initialize_db.py

Run the application:-
python new_GUI_Master.py

Usage :- 
Launch the GUI: Run new_GUI_Master.py to open the application interface.
User Authentication: Register or log in to access features.
Image Analysis: Upload fundus images for disease prediction.
View Results: Obtain diagnostic results and view model performance metrics.

Future Enhancements :-
Model Optimization: Enhance the CNN model for improved accuracy.
Real-Time Analysis: Develop capabilities for real-time image processing.
Extended Database: Incorporate a broader range of ocular diseases into the analysis.

Contributors :-
Aniket Shinde
Omkar Shinde
Ashutosh singh
Jaydeep patil
Yugandharsinh patil
Ani-cloud (Project Lead)

Acknowledgments
Utilized publicly available fundus image datasets for model training and evaluation.
Leveraged open-source libraries and frameworks for development.
