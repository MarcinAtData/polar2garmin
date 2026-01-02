# Polar to Garmin Converter

+Converts and cleans TCX files exported from Polar sports watches for compatibility with Garmin devices.
+
+## Features
+
+- Removes `Author` and `Creator` XML elements
+- Removes Polar-specific device names (`Polar Verity Sense`)
+- Processes both `.tcx` and `.TCX` file extensions
+
+## Usage
+
+1. Place your TCX files in the `input/` directory
+2. Run the converter:
+   ```bash
+   python convert.py
+   ```
+3. Cleaned files will be saved to the `output/` directory
+
+## Requirements
+
+- Python 3.6+
+- No external dependencies (uses only standard library)
+
