import os
import subprocess


def gitclone(url):
    res = subprocess.run(["git", "clone", url], stdout=subprocess.PIPE).stdout.decode("utf-8")
    print(res)


def pipi(modulestr):
    res = subprocess.run(["pip", "install", modulestr], stdout=subprocess.PIPE).stdout.decode("utf-8")
    print(res)


def pipie(modulestr):
    res = subprocess.run(["git", "install", "-e", modulestr], stdout=subprocess.PIPE).stdout.decode("utf-8")
    print(res)


def wget(url, outputdir):
    res = subprocess.run(["wget", url, "-P", f"{outputdir}"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    print(res)


def createPath(filepath):
    os.makedirs(filepath, exist_ok=True)
