import csv
import os
import base64
from shortner.constants import DOMAIN, RECORD_NOT_FOUND

fields = ("id", "actual_url", "shorten_url")
header = "id,actual_url,shorten_url\n"
filedb_path = os.path.join(os.getcwd(), "./shortner/url_files/", "filedb.csv")


class FileDbManager:
    @staticmethod
    def generate_unique_path(id):
        return base64.b64encode(bytes(id)).decode("utf-8").strip()

    @staticmethod
    def create_db_file():
        f = open(filedb_path, "w")
        f.write(header)
        f.close()

    @staticmethod
    def get_record(url: str) -> dict:
        try:
            with open(filedb_path, "r", encoding="utf_8_sig") as csvfile:
                count = 0
                for line in csvfile:
                    count += 1
                    data = line.split(",")
                    if data[1] == url:
                        return {
                            "result": True,
                            "data": {
                                "id": data[0],
                                "actual_url": data[1],
                                "shorten_url": data[2],
                            },
                        }
                return {"result": False, "message": RECORD_NOT_FOUND, "last": count}
        except FileNotFoundError:
            FileDbManager.create_db_file()
            return {"result": False, "message": RECORD_NOT_FOUND, "last": 1}

    @staticmethod
    def add_record(id: int, url: str) -> dict:
        new_row = {
            "id": id,
            "actual_url": url,
            "shorten_url": f"{DOMAIN}{FileDbManager.generate_unique_path(id)}",
        }

        with open(filedb_path, "a") as dbfile:
            dictwriter_obj = csv.DictWriter(dbfile, fieldnames=fields)
            dictwriter_obj.writerow(new_row)
            dbfile.close()
        return new_row
