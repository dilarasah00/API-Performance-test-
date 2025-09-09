# Stress Test Report

## Test Information
- **Scenario:** Stress Test
- **Users:** 300
- **Spawn rate:** 20 user/s
- **Run-time:** 3 minutes
- **Host:** https://restful-booker.herokuapp.com
- **Notes:** CPU warning observed, some tasks started failing. System limits observed on a single machine.

## Task Distribution
| Task | Weight | Description |
|------|--------|-------------|
| Auth | 1 | Obtain token |
| Create Booking | 3 | Create a random booking |
| Get Booking | 2 | Retrieve the created booking |
| Delete Booking | 1 | Delete the created booking |

## Test Results
| Endpoint | # Req | # Fail | Avg (ms) | Min (ms) | Max (ms) | Median (ms) | Req/s | Fail % |
|----------|-------|--------|-----------|----------|----------|-------------|-------|---------|
| POST /auth | 40 | 0 | 9599 | 5473 | 26281 | 8300 | 0.22 | 0% |
| POST /booking | 19326 | 19 | 535 | 142 | 57067 | 160 | 107.53 | 0.10% |
| GET /booking/:id | 12615 | 129 | 355 | 143 | 25334 | 160 | 70.19 | 1.02% |
| DELETE /booking/:id | 6241 | 4973 | 355 | 142 | 26648 | 160 | 34.72 | 79.68% |

## Response Time Percentiles (ms)
| Endpoint | 50% | 90% | 99% | Max |
|----------|-----|-----|-----|-----|
| POST /auth | 8300 | 15000 | 26000 | 26281 |
| POST /booking | 160 | 590 | 55000 | 57067 |
| GET /booking/:id | 160 | 400 | 25000 | 25334 |
| DELETE /booking/:id | 160 | 550 | 27000 | 26648 |


## Observations
- Auth requests are very slow (5–26 s), can be optimized using token reuse.  
- Create/Get/Delete tasks mostly fast (median 160 ms), but spike and fail rate increase under high load.  
- Delete task failure rate ~80% → system limits observed on a single machine.  
- CPU usage warning → single machine cannot handle full load; distributed testing recommended.  
- Stress test clearly demonstrates the system’s upper limit behavior.
