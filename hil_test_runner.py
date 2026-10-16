import socket
import json
import sys
import time

CONFIG_DATA = {
    "target_host": "127.0.0.1",
    "target_port": 8080,
    "timeout": 2.0,
    "test_cases": [
        {"id": "TC_001", "command": "READ_STATUS", "expected": "STATUS_OK"},
        {"id": "TC_002", "command": "SET_VOLTAGE_12V", "expected": "ACK_VOLTAGE"},
        {"id": "TC_003", "command": "TRIGGER_RESET", "expected": "SYSTEM_REBOOTING"}
    ]
}

def run_simulation(config):
    results = []
    print("Iniciando simulador HIL...")
    
    for tc in config["test_cases"]:
        start_time = time.time()
        success = False
        response = ""
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(config["timeout"])
            sock.connect((config["target_host"], config["target_port"]))
            sock.sendall(tc["command"].encode("utf-8"))
            response = sock.recv(1024).decode("utf-8").strip()
            sock.close()
            
            if tc["expected"] in response:
                success = True
        except Exception as e:
            response = f"ERROR: {str(e)}"
            success = False
            
        duration = time.time() - start_time
        results.append({
            "id": tc["id"],
            "command": tc["command"],
            "success": success,
            "response": response,
            "duration": round(duration, 4)
        })
        
    return results

if __name__ == "__main__":
    report = run_simulation(CONFIG_DATA)
    print(json.dumps(report, indent=4))
