#  ScratchToCatrobat: A tool for converting Scratch projects into Catrobat programs.
#  Copyright (C) 2013-2016 The Catrobat Team
#  (<http://developer.catrobat.org/credits>)
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  An additional term exception under section 7 of the GNU Affero
#  General Public License, version 3, is available at
#  http://developer.catrobat.org/license_additional_term
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


class Message(object):
    class Type(object):
        ERROR = 0
        JOB_FAILED = 1
        JOB_RUNNING = 2
        JOB_ALREADY_RUNNING = 3
        JOB_READY = 4
        JOB_OUTPUT = 5
        JOB_PROGRESS = 6
        JOB_FINISHED = 7
        JOB_DOWNLOAD = 8
        JOBS_INFO = 9
        CLIENT_ID = 10

    def __init__(self, message_type, data):
        self.type = message_type
        self.data = data

    def as_dict(self):
        return self.__dict__
