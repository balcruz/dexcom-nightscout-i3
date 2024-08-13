import os
from nightscout import Nightscout


def main():
    host = os.getenv("NIGTHSCOUT_HOST")
    api_token = os.getenv("NIGTHSCOUT_API_TOKEN")
    tz = os.getenv("TIMEZONE")
    nightscout = Nightscout(host, api_token, tz)
    print(nightscout.pull_last_entry())


if __name__ == "__main__":
    main()
