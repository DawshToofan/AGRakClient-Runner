import atexit
import psutil
from time import sleep

from clientConnection import AGRakClientHandler
from config import AccountsVars
from config import AGRakClientVars


def main():
    for account in AccountsVars:
        AGRakClientVars.clients.append(AGRakClientHandler(account.username, account.password))

    duplicate_process = False
    # Kill AGRakClient process
    for p in psutil.process_iter():
        if "AGRakClient" in p.name():
            p.kill()
            duplicate_process = True

    if duplicate_process:
        print("A duplicate process using your accounts was found and will be terminated now. Waiting for 20 seconds...")
        sleep(20)

    while True:
        for client in AGRakClientVars.clients:
            client.connect()

        sleep(2)


def exit_handler() -> None:
    for client in AGRakClientVars.clients:
        client.disconnect()

    print("Bye bye")


if __name__ == "__main__":
    try:
        atexit.register(exit_handler)
        main()
    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting...")
    except Exception as e:
        print(f"We have encountered an exception in {__name__}: ", repr(e))
        main()
