"""Automatically fetch the input while adhering to the automation rules by AOC"""

import json
from pathlib import Path
import requests as rq


def load_session_cookie() -> str:
    """Load session cookie from file"""

    with open("session.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["session"]


def fetch_input(year: int, day: int) -> str:
    """Fetch input string from Web"""

    headers = {"user-agent": "github.com/Yldrax/advent-of-code by yldrax@ylox.xyz"}
    cookies = {"session": f"{load_session_cookie()}"}
    try:
        r = rq.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            headers=headers,
            cookies=cookies,
            timeout=5,
        )
        r.raise_for_status()
    except rq.exceptions.HTTPError as err:
        raise SystemExit(err) from err

    return r.text


def load_input(year: int, day: int, reload: bool = False) -> str:
    """Load input from file if it exists or fetch from web"""
    file_path = Path(f"{year}/inputs/{day:02d}.txt")

    if reload or not file_path.exists():
        input_str = fetch_input(year, day)
        file_path.write_text(input_str, "utf-8")

    else:
        input_str = file_path.read_text("utf-8")

    return input_str


if __name__ == "__main__":
    print(load_input(2024, 1, reload=True))
