```text
                           _            ___   ___  
                          (_)          / _ \ / _ \    not©         not©         not©         not©         not©         not©         not©         not©         not©
   __ _ __ _ __ _ __ ___ _ __ _ _  __ | (_) | (_) |        not©         not©         not©         not©         not©         not©         not©         not©         not©    
  / _` |/ _` |/ _` | '__/ __| |/ _` |   > _ < > _ <             not©         not©         not©         not©         not©         not©         not©         not©         not©     
 | (_| | (_| | (_| | |  (__| | (_| | || (_) | (_) |
  \__, |\__, |\__,_|_|\_ ___|_|\__,_|_| \___/ \___/                  
   __/ | __/ |                                       
  |___/ |___/


@ggarciar88  // HIL-Test-Automation-Framework

HIL Test Automation Framework
A lightweight Python-based test automation framework designed to simulate Hardware-in-the-Loop (HIL) testing environments. It automates command frame transmission, protocol response validation, and performance reporting.

Features
Simulation of network protocol communication (TCP/UDP)

Config-driven test execution using structured dictionaries/JSON configurations

Automated test reporting with execution metrics, timing, and pass/fail status

Extensible architecture suitable for software validation and CI pipelines

File Structure
hil_test_runner.py: Main test engine and simulation script

How It Works
Loads test cases containing target commands and expected outcomes.

Opens socket connections to simulate hardware endpoints.

Sends command frames, evaluates responses against expected criteria, and calculates execution latency.

Outputs a detailed JSON-formatted execution report.

How to Run
Install Python 3.

Run the framework script in your terminal:

 python3 hil_test_runner.py
Future Improvements
YAML/JSON external configuration file loading support

Integration with standard testing frameworks (pytest)

License
