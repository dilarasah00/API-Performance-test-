# Normal Load Test Report

## Test Information
- **Scenario:** Normal Load
- **Users:** 20
- **Spawn rate:** 2 users/s
- **Run-time:** 5 minutes
- **Host:** https://restful-booker.herokuapp.com

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
| POST /auth | 4 | 0 | 1890 | 1208 | 2584 | 1700 | 0.01 |
| POST /booking | 1359 | 0 | 191 | 148 | 1730 | 160 | 4.54 |
| GET /booking/:id | 885 | 0 | 175 | 148 | 645 | 160 | 2.95 |
| DELETE /booking/:id | 440 | 0 | 183 | 149 | 782 | 160 | 1.47 |

**Notes:**
- The Auth request is slower compared to other tasks (1.2–2.5 s).
- Create/Get/Delete average response times are 150–200 ms.
- No failures → all requests were successful.
- Task weights are reflected correctly in the request distribution.

## Response Time Percentiles (ms)
| Endpoint | 50% | 90% | 99% | Max |
|----------|-----|-----|-----|-----|
| POST /auth | 2100 | 2600 | 2600 | 2584 |
| POST /booking | 160 | 220 | 1700 | 1730 |
| GET /booking/:id | 160 | 200 | 650 | 645 |
| DELETE /booking/:id | 160 | 210 | 780 | 782 |
