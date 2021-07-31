import csv
import os
import base64
import uuid
from shortner.constants import DOMAIN, RECORD_NOT_FOUND, SUCCESS, ERROR


fields = ("id", "actual_url")
header = "id,actual_url"
filedb_path = os.path.join(os.getcwd(), "./shortner/url_files/", "filedb.csv")


class FileDbManager:
    @staticmethod
    def get_unique_id():
        return uuid.uuid4().hex

    @staticmethod
    def generate_unique_path():
        return base64.b64encode(bytes(id)).decode("utf-8").strip()

    @staticmethod
    def create_db_file():
        f = open(filedb_path, "w")
        f.write(header)
        f.close()

    @staticmethod
    def extract_id(url):
        data = url.split("/")
        return data[len(data) - 1]

    @staticmethod
    def get_record(url: str) -> dict:
        try:
            with open(filedb_path, "r", encoding="utf_8_sig") as csvfile:
                for line in csvfile:
                    data = line.strip().split(",")
                    url_id = FileDbManager.extract_id(url)
                    if data[1] == url or data[0] == url_id:
                        return {
                            "status": SUCCESS,
                            "data": {
                                "id": data[0],
                                "actual_url": data[1],
                                "shorten_url": f"{DOMAIN}{data[0]}",
                            },
                        }
                return {"status": ERROR, "message": RECORD_NOT_FOUND}
        except FileNotFoundError:
            FileDbManager.create_db_file()
            return {"status": ERROR, "message": RECORD_NOT_FOUND}

    @staticmethod
    def add_record(url: str) -> dict:
        unique_id = FileDbManager.get_unique_id()
        new_row = {"id": unique_id, "actual_url": url}

        with open(filedb_path, "a") as dbfile:
            dictwriter_obj = csv.DictWriter(dbfile, fieldnames=fields)
            dictwriter_obj.writerow(new_row)
            dbfile.close()
        new_row["shorten_url"] = f"{DOMAIN}{unique_id}"
        return {"status": SUCCESS, "data": new_row}

    @staticmethod
    def get_record_by_id(uid):
        try:
            with open(filedb_path, "r", encoding="utf_8_sig") as csvfile:
                count = 0
                for line in csvfile:
                    count += 1
                    data = line.strip().split(",")
                    if data[0] == uid:
                        return {
                            "status": SUCCESS,
                            "data": {
                                "id": data[0],
                                "actual_url": data[1],
                                "shorten_url": f"{DOMAIN}{data[0]}",
                            },
                        }
                return {"status": ERROR, "message": RECORD_NOT_FOUND, "last": count}
        except FileNotFoundError:
            FileDbManager.create_db_file()
            return {"status": ERROR, "message": RECORD_NOT_FOUND, "last": 1}
