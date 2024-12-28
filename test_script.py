import json
import datetime
import random
from pathlib import Path

class TestLogger:
    def __init__(self, log_file="test_results.json"):
        self.log_file = log_file
        self.ensure_log_file_exists()
    
    def ensure_log_file_exists(self):
        if not Path(self.log_file).exists():
            with open(self.log_file, 'w') as f:
                json.dump([], f)
    
    def add_test_result(self, test_name, status, duration, error_message=None):
        try:
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
        except:
            logs = []
        
        result = {
            "test_name": test_name,
            "status": status,
            "duration": duration,
            "timestamp": datetime.datetime.now().isoformat(),
            "error_message": error_message
        }
        
        logs.append(result)
        
        with open(self.log_file, 'w') as f:
            json.dump(logs, f, indent=2)

def run_sample_test():
    """Sample test function to demonstrate logging"""
    logger = TestLogger()
    
    # Simulate some tests
    tests = ["test_login", "test_database", "test_api", "test_logout"]
    
    for test in tests:
        duration = random.uniform(0.1, 2.0)
        status = random.choice(["PASS", "FAIL"])
        error = "Connection timeout" if status == "FAIL" else None
        
        logger.add_test_result(test, status, duration, error)

if __name__ == "__main__":
    run_sample_test()
