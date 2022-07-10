#Package            Version     Latest    Type
#------------------ ----------- --------- -----
#certifi            2022.5.18.1 2022.6.15 wheel
#charset-normalizer 2.0.12      2.1.0     wheel
#prompt-toolkit     1.0.14      3.0.30    wheel
#requests           2.27.1      2.28.1    wheel
#setuptools         62.0.0      63.1.0    wheel
#starlette          0.19.1      0.20.4    wheel
#typing_extensions  4.2.0       4.3.0     wheel
#urllib3            1.26.9      1.26.10   wheel
#uvicorn            0.17.6      0.18.2    wheel

import os
lst = ["certufi","charset-normalizer",
     "prompt-toolkit","requests","setuptools",
     "starlette","typing_extensions","urllib3","uvicorn"]

for x in lst:
   os.system("pip install -U {}".format(x))
