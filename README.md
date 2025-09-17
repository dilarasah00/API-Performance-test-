# Booking API Performance Test Project

This project contains performance tests (Normal Load, Load, and Stress) for the Auth, Create, Get, and Delete endpoints of the Booking API.


## Tech Stack
- **Language:** Python  
- **Frameworks:** Locust

## Project Folder Structure
```
/
├──endpoints/
│ ├── auth.py 
│ └── booking.py
│
├── scenarios/
│ ├── load_test.py
│ ├── normal_load.py
│ └── stress_test.py 
│
├── tasks/
│ └── booking_tasks.py
│
├── test_reports/
│ ├── load_test_report.py
│ ├── normal_load_report.py
│ └── stress_test_report.py 
│
├── utils/
│  └── data_factory.py
│
└── requirements.txt
```


## 🧪 Running the Test Cases

### 1️⃣ Prepare the environment
 
Clone the project and install the dependencies to run tests:

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install required packages
pip install -r requirements.txt
```
---

### 2️⃣ Running the tests


Run normal_load.py:

```bash
locust -f scenarios/normal_load.py --users 20 --spawn-rate 2 --run-time 5m --headless --host=https://restful-booker.herokuapp.com
```

Run load_test.py:

```bash
locust -f scenarios/load_test.py --users 100 --spawn-rate 10 --run-time 5m --headless  --host=https://restful-booker.herokuapp.com

```

Run stress_test.py:

```bash
locust -f scenarios/stress_test.py --users 300 --spawn-rate 20 --run-time 3m --headless --host=https://restful-booker.herokuapp.com
```


## 📊 Test Reports

All test reports are saved in the `test_reports/` folder:

- **Normal Load:** `normal_load_report.md`  
- **Load Test:** `load_test_report.md`  
- **Stress Test:** `stress_test_report.md`  
- **Test with WSL + Docker :** `Report_WSL_Docker.md`
> **Note:** Due to CPU limitations on a single machine, tests were run with **reduced users and runtime** to preserve the test logic. These settings were chosen to demonstrate the performance testing approach while avoiding system crashes.


---

## 🐳 Running the Test with WSL + Docker

1️⃣ Clone the repository inside WSL2:

```bash
git clone https://github.com/dilarasah00/API-Performance-test-.git
cd <repo-folder>
```

2️⃣ Build the Docker image:

```bash
docker build -t booking-test .
```

3️⃣ Run the Docker container:

```bash
docker run -it --rm -v /home/dilara/projects/PerformanceTests:/app -w /app booking-test bash
```

4️⃣ Inside the container, run tests as usual:

```bash
locust -f scenarios/normal_load.py --users 20 --spawn-rate 2 --run-time 5m --headless --host=https://restful-booker.herokuapp.com
locust -f scenarios/load_test.py --users 100 --spawn-rate 10 --run-time 5m --headless --host=https://restful-booker.herokuapp.com
locust -f scenarios/stress_test.py --users 300 --spawn-rate 20 --run-time 3m --headless --host=https://restful-booker.herokuapp.com
```


> **Note:** These results come from a single run for each test. In real situations, tests should be run several times and averages or medians should be used to get more reliable results.>
