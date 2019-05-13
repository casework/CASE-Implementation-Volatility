# 'Approved for Public Release; Distribution Unlimited. Case Number 18-0922'.

# NOTICE
# 
# This software was produced for the U.S. Government under
# contract SB-1341-14-CQ-0010, and is subject to the Rights
# in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#
# (c) 2018 The MITRE Corporation. All Rights Reserved.


# Volatility
# Copyright (C) 2007-2013 Volatility Foundation
#
# This file is part of Volatility.
#
# Volatility is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Volatility is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Volatility.  If not, see <http://www.gnu.org/licenses/>.
#


try:
    import case
    import sys
    import datetime
    import getpass
    import volatility.plugins.taskmods as taskmods
    from volatility.renderers import TreeGrid
except ImportError as error:
    print("Error, failed to find %s" % (error))
    sys.exit()

class CaseCmdline(taskmods.DllList):
    """Display process command-line arguments"""
    def __init__(self, config, *args, **kwargs):
        taskmods.DllList.__init__(self, config, *args, **kwargs)
        config.add_option("VERBOSE", short_option = 'v',
                          default = False, cache_invalidator = False,
                          help = "Display full path of executable",
                          action = "store_true")

        # CASE Specific structure to create CASE Document.
        self.document = case.Document()
        self.instrument = self.document.create_CoreObject(
            'Tool',
            name='Volatility',
            version='2.6',
            toolType="Forensics",
            uri=" ".join(sys.argv)
        )
        self.performer = self.document.create_CoreObject('Identity',
            uri=getpass.getuser())
        self.performer.create_property_bundle('Username: ',
            Name=getpass.getuser())
        self.action = self.document.create_CoreObject('InvestigativeAction',
            startTime=datetime.datetime.now().isoformat(),
            endTime=datetime.datetime.now().isoformat())


    def unified_output(self, data):
        # blank header in case there is no shimcache data
        return TreeGrid([("Process", str),
                       ("PID", int),
                       ("CommandLine", str),
                       ], self.generator(data))

    def generator(self, data):
        for task in data:
            cmdline = ""
            name = str(task.ImageFileName)
            try:
                if self._config.VERBOSE and task.SeAuditProcessCreationInfo.ImageFileName.Name != None:
                    name = str(task.SeAuditProcessCreationInfo.ImageFileName.Name)
            except AttributeError:
                pass
            if task.Peb:
                cmdline = "{0}".format(str(task.Peb.ProcessParameters.CommandLine or '')).strip()
            yield (0, [name, int(task.UniqueProcessId), str(cmdline)])

    def render_text(self, outfd, data):
        for task in data:
            pid = task.UniqueProcessId
            name = str(task.ImageFileName)
            try:
                if self._config.VERBOSE and task.SeAuditProcessCreationInfo.ImageFileName.Name != None:
                    name = str(task.SeAuditProcessCreationInfo.ImageFileName.Name)
            except AttributeError:
                pass
            if task.Peb:
                cli=str(task.Peb.ProcessParameters.CommandLine)
            else:
                cli=""
            ### CASE structure from data extracted.
            self.action.create_property_bundle(
                'Process',
                performer=self.performer,
                instrument=self.instrument,
                ProcessID=pid,
                ProcessName=name,
                CommandLine=cli
            )
            print(self.document.serialize(format="json-ld", destination=None))
