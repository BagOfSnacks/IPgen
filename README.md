# IPgen
Generate list of random IP addresses and export them to a txt or json file.  
  
  
  
## Installation

### Prerequisites

```
Python: >= 3.11  
Pytest: >= 7.2.0 (testing-only)
```

To use this module, you'll need to have Python installed on your computer. You can download the latest version of Python from the [official Python website](https://www.python.org/downloads/).  

**`OPTIONAL:`** If you want to use and manage tests you also need a Pytest module, once/if you have Python installed on your computer, open up command line tool and type the following:  

```
pip install pytest
```

**`NOTE:`**  Make sure that you have PIP package mangaer installed on your device.  
  
  
### Repository Download

Once you have Python installed, you can clone this repository using the command:

```
git clone https://github.com/BagOfSnacks/IPgen.git
```
  
### Module Installation  
  
You can also download this module via PIP command:  
```
pip install https://github.com/BagOfSnacks/IPgen.git
```
  
  
## Usage

IPgen is a script launched via console and it also produces output to that console.
  
### Run IPgen from console
  
Navigate to the ```./IPgen/src``` directory containing the project code and run the script via command line tool using the command:
```
python3 -m IPgenhttps://github.com/BagOfSnacks/IPgen/edit/main/README.md#run-ipgen-from-console
```  
  
### Run module globally
  
If you have installed the package as a module as shown in [#Module Installation](https://github.com/BagOfSnacks/IPgen/edit/main/README.md#module-installation) part, you can use this module from anywhere via the same [command](https://github.com/BagOfSnacks/IPgen/edit/main/README.md#run-ipgen-from-console), without changing the current working directory.  
   
### Example usage and output
  
When executing script the console outputs all used flags and their values as well as a list of IP Addresses.

#### Example command
```
python -m IPgen -n 5 -v 6
```
  
After running the command, the following output should appear in the console:  
```
{'amount': 5, 'version': 6, 'info': None, 'txt': None, 'json': None}
[['7164:66FA:775F:BA8E:34C8:578B:1320:6325', '6209:A221:72AE:27EA:5CBD:21AD:EB7C:824E', 'AD4:5209:AF57:6C20:DDDA:6B7F:B881:417A', '1F44:895:A29F:132A:E8FA:A2D4:7325:F75', 'FFEE:8E76:7539:4A77:1AD9:9708:5816:4ED1']]
```
  
### Parameters
  
Although not required, the script accepts multiple parameters.  
To see list of parameters use ```python -m IPgen -h``` command.

List of flags:  

```
  -h, --help            show this help message and exit
  -n AMOUNT, --amount AMOUNT
                        Specify number of generated IP addresses
  -v {4,6}, --version {4,6}
                        Choose IP Address version  
                        Accepts integer of either "4" or "6" as input
  -i INFO, --info INFO  Display info of generated address(es) in JSON format
                        Creates an API call to http://ip-api.com/
                        Requires internet connection to work
  -t TXT, --txt TXT     Save list of addresses to a specified location as a .txt file
  -j JSON, --json JSON  Save list of addresses to a specified location as a json file
```  
  
Script also has a set of default parameters if none were specified:  
```python -m IPgen -n 1 -v 4```  
  
which is equal to: ```python -m IPgen```
  
  
  
### Example uses of parameters
  
Generate list of 5 IPv4 addresses:  
```
python -m IPgen -n 5
```
#### Output:
```
{'amount': 5, 'version': 4, 'info': None, 'txt': None, 'json': None}
[['81.254.6.39', '220.165.232.1', '129.26.77.86', '117.32.233.30', '239.32.51.148']]
```
  
Generate a single IPv6 address:
```
python -m IPgen -v 6
```

#### Output:
```
{'amount': 1, 'version': 6, 'info': None, 'txt': None, 'json': None}
[['8352:DC7D:95E:B400:E450:38F6:C58F:768E']]
```
  
Generate a list of 3 IPv4 addresses and save to a JSON file in the current directory:
```
python -m IPgen -n 3 -j example
```

#### Output:
```
{'amount': 5, 'version': 6, 'info': None, 'txt': None, 'json': 'example'}
[['4268:8607:2C07:8D85:88B9:668F:94FF:975D', '67E7:7EB6:4AF9:F82B:EC93:E538:E347:8003', 'BF07:A95A:FEC:C377:6A42:E16B:5576:1B01', '38D2:90CF:9D20:8669:39AC:60B2:3D8B:74F5', '4D3D:EA31:2D2A:8FBA:4EB8:27E2:1213:435']]
```
and creates a 'example.json' file in the current directory with these contents:
```
{
    "ip_addresses": [
        "4268:8607:2C07:8D85:88B9:668F:94FF:975D",
        "67E7:7EB6:4AF9:F82B:EC93:E538:E347:8003",
        "BF07:A95A:FEC:C377:6A42:E16B:5576:1B01",
        "38D2:90CF:9D20:8669:39AC:60B2:3D8B:74F5",
        "4D3D:EA31:2D2A:8FBA:4EB8:27E2:1213:435"
    ]
}
```
  
  
## Contributing

If you'd like to contribute to this repository, please fork the repository and create a new branch for your changes. Once you've made your changes, submit a pull request and your changes will be reviewed.

## License

The code in this repository is licensed under the MIT License. See the `LICENSE` file for more information.
