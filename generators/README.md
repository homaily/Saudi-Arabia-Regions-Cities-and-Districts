# Objective
Generating `geojson` files from json files within the repository
## Set up the environment
Assuming you have `python` >= 3 installed, run
```shell
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Generate embedded regions file ()
`generate_embedded_regions.py` will combine the following files into one hierarchical file where region holds cities, and cities hold districts, all within one file. This file format is ideal for non-relational databases that encourages embedding, instead of referencing.   
    - `cities.json`  
    - `districts.json`  
    - `regions.json`

Run the following command,
```shell
python generate_embedded_regions.py
```

## Generate geojson files
`generate_geojson.py` will convert the following files, if they exist, to their geojson equivalent:  
    - `cities.json`  
    - `districts.json`  
    - `regions.json`  
    - `embedded_regions.json`    
  Run the following command
```shell
python generate_geojson.py
```
