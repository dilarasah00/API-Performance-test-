# Load Test Report

## Test Information
- **Scenario:** Load Test
- **Users:** 100
- **Spawn rate:** 10 users/s
- **Run-time:** 5 minutes
- **Host:** https://restful-booker.herokuapp.com
- **Notes:** CPU usage warning observed during the test. See Locust docs for distributed testing if needed.

## Task Distribution
| Task | Weight | Description |
|------|--------|-------------|
| Auth | 1 | Obtain token |
| Create Booking | 3 | Create a random booking |
| Get Booking | 2 | Retrieve the created booking |
| Delete Booking | 1 | Delete the created booking |

## Test Results
| Endpoint | # Req | # Fail | Avg (ms) | Min (ms) | Max (ms) | Median (ms) | Req/s |
|----------|-------|--------|-----------|----------|----------|-------------|-------|
| POST /auth | 20 | 0 | 5853 | 5589 | 8487 | 5700 | 0.07 |
| POST /booking | 8360 | 0 | 238 | 144 | 10628 | 160 | 27.89 |
| GET /booking/:id | 5484 | 0 | 183 | 146 | 5132 | 160 | 18.30 |
| DELETE /booking/:id | 2722 | 0 | 170 | 147 | 2701 | 160 | 9.08 |

## Response Time Percentiles (ms)
| Endpoint | 50% | 90% | 99% | Max |
|----------|-----|-----|-----|-----|
| POST /auth | 5700 | 6500 | 8500 | 8487 |
| POST /booking | 160 | 170 | 11000 | 10628 |
| GET /booking/:id | 160 | 170 | 5100 | 5132 |
| DELETE /booking/:id | 160 | 170 | 2700 | 2701 |

## Observations
- Auth request is significantly slower than other tasks (5–8.5 s) due to token generation and database access.
- Create/Get/Delete average response times are fast (150–250 ms), with occasional spikes likely due to CPU limits and Heroku cold starts.
- As the system warmed up, response times stabilized.
- CPU usage was high at times, indicating that a single machine may not handle higher load without distributed setup.
- No request failures were observed → all tasks succeeded.
