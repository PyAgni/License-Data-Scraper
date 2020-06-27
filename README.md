# License-Data-Scraper
Scrapes Driving License data from govt. website

---

## Steps to run this Python CLI application

1. **Install the required files**

    ``` pip install -r requirements.txt```
  
2. **Run the python file**

    Suppose License number is - DL0420110149646 and DOB is 09-02-1976 then run ->
    
    ```python main.py -dl DL-0420110149646 -dob 09-02-1976```
    
    It takes 2 arguments -dl and -dob. Run ```python main.py --help``` for more information.

3. The output of displayed on the screen and is also saved as driver_data.json in the project root directory.
---

**Sample output**

```$ python main.py -dl DL-0420110149646 -dob 09-02-1976```
```
Data received ->

{'Class Of Vehicle': [{'COV Category': 'NT',
                       'COV Issue Date': '01-Mar-2011',
                       'Class Of Vehicle': 'ADPVEH'}],
 'Driver Details': {'Current Status': 'ACTIVE',
                    'Date Of Issue': '01-Mar-2011',
                    "Holder's Name": 'ANURAG BREJA',
                    'Last Transaction At': 'ZONAL OFFICE, WEST DELHI, '
                                           'JANAKPURI',
                    'Old / New DL No.': 'DL-0420110149646'},
 'Validity': {'Hazardous Valid Till': 'NA',
              'Hill Valid Till': 'NA',
              'Non-Transport': {'from': ' 01-Mar-2011', 'to': ' 08-Feb-2026'},
              'Transport': {'from': ' NA', 'to': ' NA'}}}

Driver Details Successfully stored in driver_data.json
```

**Screenshot**

![alt text](/screenshot.png)
