import json
import random
import time
import schedule

def random_json_generator():
    data = {
        "id" : random.randint(1,1000),
        "name" : random.choice(["Alice", "Bob", "Charlie", "Diana"]),
        "age" : random.randint(18,30),
        "timestamp" : time.strftime("%Y-%m-%d %H:%M:%S"),
        "location": {
            "latitude": round(random.uniform(-90, 90), 6),
            "longitude": round(random.uniform(-180, 180), 6)
        }
    }
    return json.dumps(data)

def emit_json():
    random_json = random_json_generator()   
    print(random_json)

def main():
    schedule.every(1).minutes.do(random_json_generator)
    
    print("JSON simulator started. Emitting every 1 minutes...")
    while True:
        schedule.run_pending()
        time.sleep(1)  # Prevent excessive CPU usage

if __name__ == "__main__":
    main()

