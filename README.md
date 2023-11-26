## GEOG 6180 Final Project

This repository contains the outputs for my final project in GEOG 6180 Geoprocessing in Python. I used the `gtfs_functions` Python package to write two scripts that interpret General Transit Feed Specification data: one describes a single bus system and the other compares two bus systems.

Each folder contains the following: 
* A Jupyter notebook with the script and process notes.
* The GTFS feed(s) used for the project.
* The config files for the `kepler.gl` maps.
* Screenshots of the maps (since the widgets don't render in a static notebook).

Each script can theoretically be used with any GTFS feed, but there are two main limitations. First, the script does not fix a feed if it has preexisting errors. Second, the loading location in each config is set for the feeds used for this project.