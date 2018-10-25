"""
MIRAGE Console
mirage.py

Created by Shota Shimazu on 2018/06/05

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

import sys

from console.mgargparse import CommandActionStore, ArgumentsParser
from console.help.flow import VersionShowWorkFlow

def main():

    parser = ArgumentsParser()

    # Usage & Version
    # parser.add_argument("h", "help", None, "UsageShow")
    parser.add_argument("v", None, None, None, VersionShowWorkFlow)
    parser.add_argument("version", None, None, None, VersionShowWorkFlow)


    # Commands
    # parser.add_argument("new", "newproject", None, "ReactStartup")
    # parser.add_argument_with_subaction("new", "newproject", "react", None, "ReactStartup")
    # parser.add_argument_with_subaction("new", "newproject", "ng", None, "NgStartupWorkFlow")
    # parser.add_argument_with_subaction("new", "newproject", "mini", None, "MirageMinimumStartupWorkFlow")

    # parser.add_argument("b", "backup", "app", "DjangoBackupApp")

    # parser.add_argument("conf", "configure", None, "Configure")

    # parser.add_argument("c", "console", None, "DjangoConsole")
    # parser.add_argument_with_subaction("c", "console", "db", None, "DjangoDBConsole")

    # parser.add_argument("d", "destroy", "app", "DjangoDestroy")

    # parser.add_argument_with_subaction("db", "database", "migrate", None, "DjangoMigrate")
    # parser.add_argument_with_subaction("db", "database", "reset", None, "DjangoDBReset")
    # parser.add_argument_with_subaction("db", "database", "merge", None, "DjangoMergeMigration")

    # parser.add_argument("d", "destroy", None, "DjangoDestroy")

    # parser.add_argument("g", "generate", "app", "DjangoAppMake")

    # parser.add_argument("g", "generate", "model", "DjangoModelMake")

    # parser.add_argument("g", "generate", "module", "ModuleCreateFlow")

    # parser.add_argument("heroku", "heroku", "configure", "DjangoHerokuConfigure")

    # parser.add_argument("m", "manage", None, "DjangoManagePy")

    # parser.add_argument("s", "server", None, "DjangoDebugServer")
    # parser.add_argument("browser", "internal-browser", None, "DjangoLaunchBrowser")

    # parser.add_argument("t", "transfer", None, "MirageTransfer")

    # parser.add_argument("f", "file", None, "Touch")

    # parser.add_argument("+", "confscript", None, "MirageConfigScriptFlow")

    # parser.add_argument("?", "inquiry", "update", "UpdateCheckFlow")
    # parser.add_argument("?", "inquiry", "system", "SystemCheckFlow")

    # Excute
    parser.parse()
