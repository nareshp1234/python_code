# Get Xray Vulnerabilities Script

Script will get xray vulnerability data based on repository name, cvss score and scan date.

## Workflow

- Validates input parameters passed to the script.
- Gets current date and time.
- Updates reportname.
- Updates request with repository name/s matching with or without wildcard (`*`, `?`), cvss score and scan date.
- Sends request to generate vulnerability data.
- Checks for status of report based on report id.
- Exports csv report based on colums defined under `COLUMN_LIST`.

## Prerequisites

- Python 3.6+
- Required Python packages: `numpy`, `pandas`, `python-dateutil` `requests`
- update script with below items
   *  SOURCE_JPD_URL = `<Url of JPD>`
   *  JPD_TOKEN = `Access token of JPD`
   *  COLUMN_LIST = `List of vulnerability data columns that need to be displayed in csv report`

## Usage

1. **Clone the repository**:

   ```sh
   git clone <PS Scripts repo>
   cd Hillsidetechnology
   ```

2. **Install required Python libraries**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the script**:

   ```sh
   python getxrayvulnerabilitydata.py <reponame> <cvss_score> <scan_date>
   ```

  Example:
  
   ```sh
   python getxrayvulnerabilitydata.py blr-docker-ps-td 10 2024-08-26
   ```