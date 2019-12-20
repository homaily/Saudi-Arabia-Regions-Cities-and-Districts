changes are in 
* `./json/light_cities.json` is a light version of `cities.json` with only important cities.
* `./json/citiesBasedOnRegion.json` is tree based structure where cities ordered based on their regions.

### why this fork ?
* Cities were joined with villages and districts (they were 3000+). I removed the non important cities (now cities are only 108).
* The loaded file should be small to be used in client side (cities was 600+ kb now now only 13kb) so I remove unnecessary city attributes.
* I need cities to be ordered based on their regions in tree based structure (I think its better for my case and also its better for IO so I don't have to iterate though all cities every time).

### My Case:
I've a dropdown of Saudi cities which I need them to be seen based on selected region.

big thanks to @homaily.