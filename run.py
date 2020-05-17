#!/usr/bin/env python3

from config import cfg

def run_app():
    from app import cli
    cli.run(cfg.token)


if (cfg.debug == True):
    run_app()
else:
    try:
        run_app()
    except:
        print("Failed to run the app. Try to run \"pip install -r requirements.txt\".\nYou should add your token and id in config.py file.")