import sys
import logging
import xml.etree.ElementTree as ET


class AccountConfig:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class AGRakClientConfig:
    def __init__(self):
        self.canConnect = True
        self.clients = []


class StreamToLogger:
    def __init__(self, logger, log_level):
        self.logger = logger
        self.log_level = log_level

    def write(self, message):
        if message.strip():
            try:
                safe_message = message.strip().encode("utf-8", "ignore").decode("utf-8", "ignore")
                self.logger.log(self.log_level, safe_message)
            except Exception as e:
                print(f"Logging error: {e}")

    def flush(self):
        pass


logger = logging.getLogger("RedirectedOutput")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("Runner.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

sys.stdout = StreamToLogger(logger, logging.INFO)
sys.stderr = StreamToLogger(logger, logging.ERROR)

AGRakClientVars = AGRakClientConfig()

file_path = "Runner.xml"
AccountsVars = []

try:
    tree = ET.parse(file_path)
    root = tree.getroot()
except ET.ParseError as e:
    print(f"XML parsing error: {e}")

for user in root.findall("user"):
    username = user.get("username")
    password = user.get("password")
    AccountsVars.append(AccountConfig(username, password))
