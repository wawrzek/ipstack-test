# Description

The program query the IPStack API to get the Geolocation of the provided IP.
After downloading it print selected (at the moment latitude and longitude) information onto standard output.

# Prerequisites

- IPStack API key
- request python library

## IPStack API key
The key can be obtain from the https://ipstack.com/dashboard website.
The free plan allows to have 100 queries per month.
Please note, that registration even for free plan, requires providing credit card details. 

## Python libraries
This is a Python program which required the requests library.
If the library is not installed system wide all dependencies are defined in the requirements.txt file.
They can be install a Python virtual environment.

```
python -m venv ipstack
cd ipstack
source bin/active
git clone https://github.com/wawrzek/ipstack-test.git
cd ipstack-test
pip install -r requirements.txt
```

**Alternatively, use provided Dockerfile to create an image and run the program in a container.**

# Docker

Along the python program Dockerfile to create a docker container is provided.
The ip address is provided as a parameter of the run command.
Docker address the dependencies issue, but still requires the IPStack API key.
It should be mounted as a volume.

Below, an example of the command to run the docker container.

```
docker run -v ./.ipstack_key:/app/.ipstack_key ${image_name}:latest $1
```

## Shell script to run the docker

To make docker usage easier an extra script location.sh is provided.
It runs the image, and, if required, builds it first.
The script take the IP address as an input and mounts the .ipstack_key file.

## Technical comments

The image uses simple Python image based on the Alpine Linux.
To avoid running the program (and pip) as the root user, extra appuser is created.


# Python program details

## Input

The script required exactly one parameter to run.
It has to be a public IP address.

## Output

The output of the program consist of two float numbers.
They represent the
- latitude
- longitude

of the given IP.
Numbers in both columns have 6 decimal points.
Columns are 12 characters wide with string aligned to right and separated by 2 spaces.

## Errors
In case of a problem program will exit with a error defined in the EXIT dictionary.
The dictionary can be found in the script itself.
