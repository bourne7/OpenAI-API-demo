import datetime
import os
import sys
import common
import openai
from prettytable import PrettyTable


######################### File Management #########################


def file_list():
    resp = openai.File.list()
    print(resp)
    data = resp["data"]
    if data:
        table = PrettyTable()

        table.field_names = resp["data"][0].keys()

        for row in data:
            row["created_at"] = common.convert_timestamp_to_datetime(row["created_at"])
            table.add_row(row.values())

        print(table)


def file_upload():
    # I suppose that the pwd is the root of the project
    file_path = r"prompts\\fine_tuning.jsonl"
    ignore_path = r"ignore\\" + file_path
    if os.path.exists(ignore_path):
        file_path = ignore_path

    choice = input("Are you sure to upload " + file_path + " (y/n)?")
    if choice == "y":
        common.print_file(file_path)
        resp = openai.File.create(
            file=open(file_path, "rb"),
            purpose="fine-tune",
            user_provided_filename=file_path.replace("\\\\", "\\"),
        )
        print(resp)
    else:
        return


def file_delete():
    message = """
Please select the file (such as 'file-XXXX') you want to delete or:
all: delete all files
r: return to main menu
q: quit program
"""

    while True:
        choice = input(message)

        if choice == "all":
            print(common.GLOBAL_MESSAGE_NOT_SUPPORTED_YET)
        elif choice == "q":
            sys.exit()
        elif choice == "r":
            break
        else:
            print("Delete: ", choice)
            resp = openai.File.delete(choice)
            print(resp)


######################### Fine Tunes #########################


def fine_tunes_create_job():
    file_list()
    message = """
Please input the file (such as 'file-XXXX') you want to fine-tune or:
r: return to main menu
"""
    choice = input(message)

    if choice == "r":
        return
    else:
        print("Fine-tuning: ", choice)
        _create_fine_tune_with_file_id(choice)


def fine_tunes_list_job():
    resp = openai.FineTune.list()
    print(resp)
    data = resp["data"]
    if data:
        table = PrettyTable()

        table.field_names = (
            "created_at",
            "updated_at",
            "fine_tuned_model",
            "id",
            "status",
        )

        for row in data:
            created_at = common.convert_timestamp_to_datetime(row["created_at"])
            updated_at = common.convert_timestamp_to_datetime(row["updated_at"])
            table.add_row(
                (
                    created_at,
                    updated_at,
                    row["fine_tuned_model"],
                    row["id"],
                    row["status"],
                )
            )

        print(table)


def fine_tunes_retreve_job():
    message = """
Please input the job id (such as 'ft-XXXX') you want details about or:
r: return to main menu
"""
    choice = input(message)

    if choice == "r":
        return
    else:
        resp = openai.FineTune.retrieve(id=choice)
        print(resp)


def fine_tunes_cancel_job():
    message = """
Please input the job id (such as 'ft-XXXX') you want to cancel or:
r: return to main menu
"""
    choice = input(message)

    if choice == "r":
        return
    else:
        resp = openai.FineTune.cancel(id=choice)
        print(resp)


def fine_tunes_list_events():
    message = """
Please input the event id (such as 'ft-AF1WoRqd3aJAHsqc9NY7iL8F') you want details about or:
r: return to main menu
"""
    choice = input(message)

    if choice == "r":
        return
    else:
        resp = openai.FineTune.list_events(id=choice)
        print(resp)


def fine_tunes_delete_model():
    message = """
Please input the fine_tuned_model id (such as 'davinci:ft-personal:2023-05-18-11-16-51') you want to delete or:
r: return to main menu
"""
    choice = input(message)

    if choice == "r":
        return
    else:
        resp = openai.Model.delete(choice)
        print(resp)


######################### Support Methods #########################


def _create_fine_tune_with_file_id(training_file_id: str):
    resp = openai.FineTune.create(
        training_file=training_file_id,
        model="davinci",
        suffix=common.get_model_suffix(),
    )
    print(resp)


######################### Main #########################

if __name__ == "__main__":
    # print start time
    start_time = datetime.datetime.now()
    print(start_time, "Current working directory:", os.getcwd())

    # load global config
    common.load_config()

    # set openAI properties
    openai.api_key = common.GLOBAL_CONFIG["openAI"]["api_key"]
    proxy_str = common.GLOBAL_CONFIG["openAI"]["proxy"]
    if proxy_str:
        openai.proxy = proxy_str

    # main command router
    message = """
Official API: https://platform.openai.com/docs/api-reference/fine-tunes
[Main menu] Please select the function you want to execute:

11: file_list
12: file_upload
13: file_delete

21: fine_tunes_create_job
22: fine_tunes_list_job
23: fine_tunes_retreve_job
24: fine_tunes_cancel_job
25: fine_tunes_list_events
26: fine_tunes_list_model

q: quit program
"""
    while True:
        choice = input(message)

        if choice == "11":
            file_list()
        elif choice == "12":
            file_upload()
        elif choice == "13":
            file_delete()
        elif choice == "21":
            fine_tunes_create_job()
        elif choice == "22":
            fine_tunes_list_job()
        elif choice == "23":
            fine_tunes_retreve_job()
        elif choice == "24":
            fine_tunes_cancel_job()
        elif choice == "25":
            fine_tunes_list_events()
        elif choice == "26":
            fine_tunes_delete_model()
        elif choice == "q":
            break
        else:
            continue

    end_time = datetime.datetime.now()
    print(end_time, "Run time:", end_time - start_time)
