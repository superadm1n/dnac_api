[![Documentation Status](https://readthedocs.org/projects/dnac-api/badge/?version=latest)](https://dnac-api.readthedocs.io/en/latest/?badge=latest)
# dnac_api
> Python API for interfacing with the Cisco DNA Center REST API


This project aims to integrate all major versions of the DNA Center Rest API
and provide a consistent, intuitive, and pythonic way of interfacing your script
or application with the DNA Center API.

## Documentation
Documentation for this project can be found at [ReadTheDocs](https://dnac-api.readthedocs.io/en/latest/index.html)

## Installation

```sh
git clone https://github.com/superadm1n/dnac_api
python setup.py dnac_api/setup.py
```

## Usage example

Using v1.1 of the API to get the number of hosts in the DNA Appliance
```python
from dnac_api.v1_1 import NetworkHost

dnac = NetworkHost('https://dnacserver.local', 'myUsername', 'myPassword')
print(dnac.num_of_hosts)

```

## Development setup

```sh
git clone https://github.com/superadm1n/dnac_api
cd dnac_api
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```



## Creator and Maintainer

Kyle Kowalczyk – [KyleTK.com](https://kyletk.com) | [Github](https://github.com/superadm1n)

Distributed under the GNU GPLv3 license. See ``LICENSE`` for more information.


## Contributing

1. Fork it (<https://github.com/superadm1n/dnac_api/fork>)
2. Create your feature branch (`git checkout -b feature/mynewfeature`)
3. Commit your changes (`git commit -am 'Explaning my feature.'`)
4. Push to the branch (`git push origin feature/mynewfeature`)
5. Create a new Pull Request
