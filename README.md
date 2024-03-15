# Description

The program query the IPStack API to get the Geolocation of the provided IP.
After downloading it print selected (at the moment latitude and longitude) information onto standard output.

# Prerequisites

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

# Details

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
