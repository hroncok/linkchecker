# -*- coding: iso-8859-1 -*-
"""Handle for unknown links"""
# Copyright (C) 2001-2004  Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import urlbase

import linkcheck
from linkcheck.i18n import _

class ErrorUrl (urlbase.UrlBase):
    """Unknown URL links"""

    def check_syntax (self):
        linkcheck.log.debug(linkcheck.LOG_CHECK, "checking syntax")
        self.url = self.base_url
        self.set_result(_("URL is unrecognized or has invalid syntax"),
                        valid=False)
        return False

    def get_cache_key (self):
        """cache key is the url"""
        return self.base_url

