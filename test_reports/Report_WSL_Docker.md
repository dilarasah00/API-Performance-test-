This report includes comparing for performance test results between Windows and Docker + WSL2.

## 1.Normal Load Test

**Observations:**
The main difference appears in the auth endpoint response times.
Overall, average response times are similar across environments.
More importantly, the CPU behaves more stable with Docker and WSL2 compared to Windows.


Type     Name  # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------||-------|-------------|-------|-------|-------|-------|--------|-----------
POST     /auth       2     0(0.00%) |   1016     982    1049    982 |    0.01        0.00
POST     /booking [POST]    1358     0(0.00%) |    217     154    1354    210 |    4.54        0.00
DELETE   /booking/:id [DELETE]     436     0(0.00%) |    212     170     679    210 |    1.46        0.00
GET      /booking/:id [GET]     885     0(0.00%) |    210     168     652    210 |    2.96        0.00
--------||-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated    2681     0(0.00%) |    215     154    1354    210 |    8.96        0.00

Type     Name      50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------||--------|------|------|------|------|------|------|------|------|------|------|------
POST     /auth     1000   1000   1000   1000   1000   1000   1000   1000   1000   1000   1000      2
POST     /booking [POST]      210    210    210    210    220    220    330    830    880   1400   1400   1358
DELETE   /booking/:id [DELETE]      210    210    220    220    220    230    260    310    680    680    680    436
GET      /booking/:id [GET]      210    210    210    220    220    220    260    300    650    650    650    885
--------||--------|------|------|------|------|------|------|------|------|------|------|------
         Aggregated      210    210    210    210    220    220    270    650    980   1400   1400   2681


---

## 2.Load Test

**Observations:**
The biggest difference is seen in the auth endpoint response time and in the maximum response times across all endpoints.
The CPU does not give any warnings.


Type     Name                                                                      # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
POST     /auth                                                                         20     0(0.00%) |   1057     871    1912    950 |    0.07        0.00
POST     /booking [POST]                                                             8705     0(0.00%) |    214     153    1112    210 |   29.07        0.00
DELETE   /booking/:id [DELETE]                                                       2837     0(0.00%) |    210     154     917    210 |    9.48        0.00
GET      /booking/:id [GET]                                                          5719     0(0.00%) |    210     151     966    210 |   19.10        0.00
--------|------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                 17281     0(0.00%) |    213     151    1912    210 |   57.72        0.00


Type     Name                                                                              50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|----------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
POST     /auth                                                                            1000   1100   1100   1100   1900   1900   1900   1900   1900   1900   1900     20
POST     /booking [POST]                                                                   210    210    210    210    220    230    410    680    900   1100   1100   8705
DELETE   /booking/:id [DELETE]                                                             210    210    210    220    220    230    260    370    690    920    920   2837
GET      /booking/:id [GET]                                                                210    210    210    210    220    220    270    390    700    970    970   5719
--------|----------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
         Aggregated                                                                        210    210    210    210    220    220    330    650    900   1900   1900  17281


---

## 3.Stress Test

Response times are much more reasonable compared to Windows.
Especially, maximum response times are lower than in Windows.
The CPU does not give any warnings.

However, failures occur after updating all users. Unlike Windows, the POST /booking endpoint does not show errors.
The system cannot remain stable with 300 users, and failures accumulate quickly.



Type     Name                                                                      # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
POST     /auth                                                                         20     0(0.00%) |   1007     883    1298   1000 |    0.11        0.00
POST     /booking [POST]                                                            26076     0(0.00%) |    553     167    8050    340 |  144.89        0.00
DELETE   /booking/:id [DELETE]                                                       8501 8254(97.09%) |    245     161    6201    210 |   47.24       45.86
GET      /booking/:id [GET]                                                         17116   106(0.62%) |    542     171    6222    350 |   95.11        0.59
--------|------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                 51713 8360(16.17%) |    499     161    8050    270 |  287.35       46.45


Type     Name                                                                              50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|----------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
POST     /auth                                                                            1000   1000   1100   1100   1100   1300   1300   1300   1300   1300   1300     20
POST     /booking [POST]                                                                   340    530    730    840   1100   1500   1800   1900   5900   8000   8100  26076
DELETE   /booking/:id [DELETE]                                                             210    210    220    220    240    310    590    690   5300   6200   6200   8501
GET      /booking/:id [GET]                                                                350    530    690    830   1100   1500   1800   1900   5300   6200   6200  17116
--------|----------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
         Aggregated                                                                        270    460    610    750   1100   1400   1700   1900   5400   7000   8100  51713

Error report
# occurrences      Error
------------------|-----------------------------------------------------------------------------------------------------------------------------------------
106                GET /booking/:id [GET]: Get booking failed: Not Found
8254               DELETE /booking/:id [DELETE]: Delete booking failed: Forbidden
