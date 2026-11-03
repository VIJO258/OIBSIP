# BMI Calculator

A simple, desktop BMI Calculator written in Python for the OASIS INFOBYTE Python Programming Internship, Task 2. It uses Tkinter, which is included with most Python installations, and does not require external libraries.

## Requirements

- Python 3
- Visual Studio Code (optional, but recommended)

## Create and run in VS Code on Windows

1. Open the project folder in Visual Studio Code.
2. Open `bmi_calculator.py` and make sure Python 3 is installed. If VS Code asks you to select an interpreter, choose your Python 3 installation.
3. Open **Terminal > New Terminal**.
4. Run:

   ```powershell
   python bmi_calculator.py
   ```

   If `python` is not recognized, try `py bmi_calculator.py`.
5. The BMI Calculator window opens. Enter your weight in kilograms and height in metres, then select **Calculate BMI**. Use **Clear** to start over.

## What it does

- Accepts weight in kilograms and height in metres.
- Shows a helpful message for non-numeric entries, negative measurements, or zero height.
- Calculates BMI with `weight / (height * height)` and displays it rounded to two decimal places.
- Displays the BMI category based on the unrounded BMI value.

## BMI categories

- Underweight: below 18.5
- Normal weight: 18.5 to below 25
- Overweight: 25 to below 30
- Obese: 30 or above