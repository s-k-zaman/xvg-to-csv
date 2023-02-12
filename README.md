## Information
This script converts a XVG(gromacs output file) to a CSV file.
- `NOTE` currently works for xvg file having x-axis and y-axis.

## Prerequisites
You need to install `numpy` and `argparse` libraries.
```sh
pip install numpy argparse
```

## Usage
`python xvg-to-csv.py [...arguments]`

### arguments:
-h or --help :Shows all the options
```sh
python xvg-to-csv.py -h
```

-xvg or XVG :location/to/xvgFile/Name.xvg [default: test.xvg]
```sh
python xvg-to-csv.py -xvg ./yourFilename.xvg
```

-csv or CSV `optional` :location/to/save/csvFile/Name.csv [default: xvg file location]
```sh
python xvg-to-csv.py -xvg ./yourFilename.xvg -csv ./outputFileName.csv
```

-d or D `optional` :digits after decimal point [default: 7]
- following example shows: to change upto 3 digits after decimal point.
```sh
python xvg-to-csv.py -xvg ./yourFilename.xvg -d 3
```
