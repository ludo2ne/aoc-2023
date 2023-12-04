import os
import sys
import dotenv
import requests

dotenv.load_dotenv(override=True)


def import_input(day, year=2023):
    input_path = "data/day" + str(day) + ".txt"
    if not os.path.isfile(input_path):
        cookies = {"session": f"{os.environ['SESSION']}"}

        req = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies=cookies,
        )

        if req.status_code == 200:
            with open(input_path, "w") as file:
                file.write("\n".join(req.text.split("\n")))
        else:
            print(
                f"Failed to download the file. Status code: {req.status_code}",
                file=sys.stderr,
            )


if __name__ == "__main__":
    import_input(4)
