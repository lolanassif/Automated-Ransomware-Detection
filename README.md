# Ransomware Detection System

A Python-based security project that detects ransomware-like behavior through real-time file monitoring and automated response.

## Overview
This project simulates a basic endpoint protection system by monitoring files inside a target folder, analyzing suspicious behavior, and taking action when potential ransomware activity is detected.

## Features
- Real-time file monitoring
- Behavior-based ransomware detection
- Risk scoring system
- Whitelist filtering to reduce false positives
- Automatic quarantine of suspicious files
- Event logging for detected threats

## Project Structure
- `monitor.py` → Monitors file activity in the target folder
- `detector.py` → Analyzes file behavior and assigns risk scores
- `response.py` → Quarantines suspicious files and logs incidents
- `logs.txt` → Stores warning and detection logs
- `testfolder/` → Folder used for testing file activity
- `quarantine/` → Stores isolated suspicious files

## Detection Logic
The system identifies suspicious activity based on:
- Suspicious file extensions
- Rapid file modifications
- Large file size changes
- Risk scoring with whitelist-based filtering

## Response Actions
When a file is classified as high risk, the system:
1. Detects the suspicious behavior
2. Logs the event
3. Moves the file to a quarantine folder
4. Renames it as a blocked file

## How to Run
1. Make sure Python is installed
2. Place the project files in one folder
3. Create a folder named `testfolder`
4. Run the monitoring script:

```bash
python monitor.py
