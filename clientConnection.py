import subprocess
import threading

from config import AGRakClientVars


class AGRakClientHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__resetVars()

    def __makeThread(self):
        self.threadStatus = True
        self.thread = threading.Thread(target=self.__printOutPuts, daemon=True)
        self.thread.start()

    def __printOutPuts(self):
        while self.threadStatus:
            try:
                try:
                    response = self.process.stdout.readline().decode()
                except:
                    continue
                if response:
                    if (
                        self.waitingForConnect
                        and not AGRakClientVars.canConnect
                        and (
                            f"[{self.username}] Login successfully." in response
                            or f"[{self.username}] Welcome {self.username}!" in response
                        )
                    ):
                        AGRakClientVars.canConnect = True
                        self.connected = True
                        self.waitingForConnect = False
                        for client in AGRakClientVars.clients:
                            if client.waitingForRun:
                                client.waitingForRun = False
                                break

                    if "[CMSG]" not in response:
                        if " Reconnecting in " in response:
                            self.connected = False
                            if AGRakClientVars.canConnect or self.waitingForConnect:
                                AGRakClientVars.canConnect = False
                                self.waitingForConnect = True
                            else:
                                self.waitingForRun = True
                                self.disconnect()
                    print(response, end="")
            except Exception as e:
                print(f"Error in __printOutPuts: {e}")

    def __resetVars(self):
        self.connected = False
        self.waitingForConnect = False
        self.threadStatus = False
        self.waitingForRun = False

    def __command(self, command):
        command += "\n"
        self.process.stdin.write(command.encode())
        self.process.stdin.flush()

    def connect(self):
        if AGRakClientVars.canConnect and not self.connected and not self.waitingForRun:
            AGRakClientVars.canConnect = False
            self.waitingForConnect = True
            try:
                self.process = subprocess.Popen(
                    ["AGRakClient.exe", "--from-py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE
                )
            except Exception as e:
                print(f"Error occurred while running AGRakClient.exe: {e}")
                exit()
            self.__makeThread()

            self.__command(self.username)
            self.__command(self.password)

    def disconnect(self):
        if not self.threadStatus:
            return False
        self.process.kill()
        if self.waitingForConnect:
            AGRakClientVars.canConnect = True
        self.__resetVars()
        print(f"{self.username} disconnected.")
        return True
