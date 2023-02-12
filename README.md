## Information
This script converts a XVG(gromacs output file) to a CSV file.
- currnty work for xvg file having x-axis and y-axis

## Prerequisites
Prerequistes are `numpy` and `argparse` libraries.
```sh
pip install numpy argparse
```

## Usage

usage:
```sh
python xvg-to-csv.py [...arguments]
```
- run `python xvg-to-csv.py -h` to see all the options

### arguments:

-h or --help  :Shows all the options
```sh
python xvg-to-csv.py -h
```

`-xvg or XVG location/to/xvgFile/Name.xvg [default: test.xvg]`
```sh
python xvg-to-csv.py -xvg ./yourFilename.xvg
```
or
```sh
python xvg-to-csv.py XVG ./yourFilename.xvg
```

`-csv or CSV    location/to/save/csvFile/Name.csv [optional, default: xvg file location]`
```sh
python xvg-to-csv.py -xvg ./yourFilename.xvg -csv ./outputFileName.csv
```
or
```sh
python xvg-to-csv.py XVG ./yourFilename.xvg CSV ./outputFileName.csv
```

`-d or D        digits after decimal point [optional, default: 7]`
following example shows: to change upto 3 digits after decimal point.
```sh
python xvg-to-csv.py -xvg ./yourFilename.xvg D 3
```
or
```sh
python xvg-to-csv.py -xvg ./yourFilename.xvg -d 3
```
