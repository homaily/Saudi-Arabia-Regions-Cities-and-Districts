changes are in 
* `./json/light_cities.json` is a light version of `cities.json` with only important cities.
* `./json/citiesBasedOnRegion.json` is tree based structure where cities ordered based on their regions.

### why this fork ?
* `cities.json` contains cities, villages and districts (they were 3000+). In `light-cities.json` I kept only cities that has at least one district (now cities are only 108 and `cities.json` file was 600+ kb, now `light-cities.json` is only 13kb).
* The loaded file should be small to be used in client side so I removed unnecessary city attributes (now `citiesBasedOnRegion.json` file is 7kb).
* I need cities to be ordered based on their regions in tree based structure (I think its better for my case and also its better for IO so I don't have to iterate though all cities every time).

### My Case:
I've a dropdown of Saudi cities which I need them to be seen based on selected region.

### Credits
big thanks to @homaily.
