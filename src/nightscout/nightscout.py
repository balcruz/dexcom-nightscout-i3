from dateutil import parser
import fontawesome as fa
import json
import pytz
import requests


class Nightscout:
    def __init__(self, host, api_token, timezone):
        self.host = host
        self.api_token = api_token
        self.timezone = timezone
        self.api_url = build_url(self.host, self.api_token, "entries.json")

    def pull_last_entry(self):
        entries = pull_entries(self.api_url, self.timezone)
        return entries[0]


def pull_entries(api_url, timezone):
    r = requests.get(api_url)
    json_data = json.loads(r.text)
    parsed_data = parse_data(json_data, timezone)
    return parsed_data


def build_url(host, api_token, endpoint):
    return f"https://{host}/api/v1/{endpoint}?token={api_token}"


def parse_data(data, tz):
    cgm_list = []
    for d in data:
        direction_str = update_arrow(d.get("direction"))
        date_str = format_date(d["dateString"], tz)
        cgm_values = f"{str(d["sgv"])} {direction_str} {date_str}"
        cgm_list.append(cgm_values)
    return cgm_list


def format_date(utc_date, timezone):
    utc_dt = parser.parse(utc_date)
    local_tz = pytz.timezone(timezone)
    local_dt = utc_dt.astimezone(local_tz)
    local_time_str = local_dt.strftime("%b %d, %I:%M %p")
    return local_time_str


def update_arrow(value):
    match value:
        case "SingleUp":
            return fa.icons.get("arrow-up")
        case "SingleDown":
            return fa.icons.get("arrow-down")
        case "DoubleUp":
            return fa.icons.get("angles-up")
        case "DoubleDown":
            return fa.icons.get("angles-down")
        case "FortyFiveUp":
            return fa.icons.get("location-arrow")
        case "FortyFiveDown":
            return fa.icons.get("arrow-trend-down")
        case "Flat":
            return fa.icons.get("arrow-right")
        case _:
            return fa.icons.get("question")
