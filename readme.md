# CSV Processor

## What Does the Code Do?
The CSV Processor is a Python script that processes CSV files. It extracts specified columns and filters rows based on a given start date.

## Installation
To use the CSV Processor, follow these steps:
1. Clone the repository to your local machine using Git:
   ```
   git clone https://github.com/yourusername/csv-processor.git
   ```

2. Navigate to the project directory:
   ```
   cd csv-processor
   ```

3. Install the required dependencies using pip:
   ```
   pip install pandas
   ```

## Generating the Executable
To generate the executable:
1. Navigate to the project directory where the `ing2actualCsv.py` file is located.

2. Run the following command in the terminal:
   ```
   pyinstaller --onefile ing2actualCsv.py
   ```

This will create a standalone executable file in the `dist` directory within the project folder.

## Launch Configuration (launch.json)
To debug the script using Visual Studio Code, you can use the following launch configuration:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File with Arguments",
            "type": "debugpy",
            "request": "launch",
            "program": "ing2actualCsv.py",
            "console": "integratedTerminal",
            "args": ["example.csv", "2024-03-05"],
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

Replace `"args": ["example.csv", "2024-03-05"]` with the appropriate arguments for your script.

Feel free to copy and paste these instructions for your project documentation. Let me know if you need further assistance!