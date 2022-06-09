#!/usr/bin/python3

import os
import sys
import datetime

class Settings:
    def __init__(self):
        relative_path = "./Nsyncfile"
        self.header_template = """# Jerome's Daily Log, {}

## Goals for today

## Accomplished today

## Deadlines and Deliverables

"""

        self.cute_date_format = lambda d: "{0} {d.day}, {d.year}".format(d.strftime("%B"), d=d)
        self.filename_date_format = lambda d: "{d.month}-{d.day}-{d.year}".format(d=d)
        self.ok = True
        if not file_exists(relative_path):
            self.ok = False
            self.error = "{} config file does not exist".format(relative_path)
        
def file_exists(file_path):
    return os.path.isfile(file_path)

def directory_exists(dir_path):
    return os.path.isdir(dir_path)

def ls():
    return os.listdir(".")

def mkdir(dir_path):
    os.mkdir(dir_path)

def pwd():
    return os.getcwd()

def cd(dir_path):
    print("Changing working directory to `{}`".format(dir_path))
    os.chdir(dir_path)

def shell_cmd(command):
    print("Executing shell command `{}`".format(command))
    os.system(command)

def apply_file_extension(base_name, extension):
    return "{}.{}".format(base_name, extension)

if __name__ == "__main__":
    print("Synchronizing journal...")
    settings = Settings()
    if not settings.ok:
        print("Error: {}".format(settings.error))
        sys.exit()

    current_datetime = datetime.datetime.now()
    today_dir_path = settings.filename_date_format(current_datetime)
    if directory_exists(today_dir_path):
        print("Today's directory already exists.")
    else:
        print("Creating today's directory.")
        mkdir(today_dir_path)
        with open(os.path.join(today_dir_path, apply_file_extension(today_dir_path, "md")), "w") as f:
            f.write(settings.header_template.format(settings.cute_date_format(current_datetime)))

    print("Converting Markdown to PDF.")
    calling_dir = pwd()
    for elem in ls():
        if directory_exists(elem):
            today_dir_path = elem
            cd(today_dir_path)
            shell_cmd("pandoc {} -o {}".format(apply_file_extension(today_dir_path, "md"), apply_file_extension(today_dir_path, "pdf")))
            cd(calling_dir)
    print("Done.")

