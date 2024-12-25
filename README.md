# AGRakClient-Runner

**AGRakClient-Runner** is a Python-based tool designed to manage multiple accounts for the SA-MP (San Andreas Multiplayer) server **Arsacia Game** by interacting with the **AGRakClient** executable. This runner automates the process of launching and managing connections for multiple accounts simultaneously.

## Features
- Multi-account management
- Simplified setup and execution
- Seamless integration with **AGRakClient**

## Requirements
To use AGRakClient-Runner, ensure the following prerequisites are met:

1. **Python** is installed on your system (Python 3.7 or later is recommended).
2. The `AGRakClient.exe` file is present in the same directory as this runner.
3. A properly configured `Runner.xml` file is available in the directory.

## How to Use
### Step 1: Prepare the Environment
1. Clone or download the AGRakClient-Runner repository.
2. Ensure that `AGRakClient.exe` (available in the AGRakClient repository) is in the same directory as the runner script.
3. Create a `Runner.xml` file with the following content:

   ```xml
   <users>
       <user username="Your account 1 username" password="Your account 1 password" />
       <user username="Your account 2 username" password="Your account 2 password" />
	   .
	   .
	   .
   </users>
   ```

   - Replace `Your account 1 username` and `Your account 1 password` with your actual credentials for the first account.
   - Repeat this for additional accounts.

### Step 2: Install Dependencies
AGRakClient-Runner may require additional Python libraries. Install them using:

```bash
pip install -r requirements.txt
```

(Note: The repository includes a `requirements.txt` file if libraries are necessary.)

### Step 3: Run the Script
Execute the runner script by running:

```bash
python Runner.py
```

The script will:
- Read the credentials from `Runner.xml`.
- Launch **AGRakClient.exe** for each account listed.

## Donations
If you find AGRakClient-Runner helpful and would like to support its development, consider making a donation:  
[Support AGRakClient-Runner](https://reymit.ir/dawshtoofan)

Thank you for using AGRakClient-Runner!
