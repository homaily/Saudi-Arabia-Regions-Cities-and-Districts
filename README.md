# Saudi-Arabia-Regions-Cities-and-Districts
Raw data for Saudi Arabia's 13 regions, over 4580 cities and 3730 districts in both Arabic and English.

* The data is public data collected from https://maps.address.gov.sa/
* All coordinates in (Lat, Lon) aka (Y, X) format and 8 decimal points, except for MySQL files
* Mysql files coordinates are reversed (Lon, Lat) aka (X, Y) due to the way MySQL expect it
* Data points include:
  - Regions, Cities and Districts.
  - Names (Arabic & English).
  - Regions capital city, population & center point.
  - Regions boundaries.
  - Districts boundaries.
* Lite version includes all data points except GIS data (center point & boundaries).


## Data Use Cases
This is a list of some of the open source projects based on this data:
* [KSA Covid-19 cases map](https://github.com/0x0Faisal/Covid19-Map) by [@0x0Faisal](https://github.com/0x0Faisal).
* [Saudi_geo_clickhouse](https://github.com/swarnkiran88/swarnkiran88) by [@swarnkiran88](https://github.com/swarnkiran88).
* [Saudi_GIS_Data](https://github.com/usefksa/Saudi_GIS_Data) by [@usef_ksa](https://github.com/usef_ksa).
* [Manateq - a handy library for searching and listing regions, cities and districts in Saudi Arabia](https://github.com/nuhamozaini/Manateq) by [@nuhamozaini](https://github.com/nuhamozaini).



## Contributing
All contributions are welcome! 😊
Please only send PRs that benefit most users or have a common use case. For special use cases, please publish them to a separate repo.

## Issues
If you find an issue with the data please open an issue. If you're looking for help in using the data in your own projects, please use the appropriate forums, such as StackOverflow.


## License
[GPL-2.0](https://github.com/homaily/Saudi-Arabia-Regions-Cities-and-Districts/blob/master/LICENSE)