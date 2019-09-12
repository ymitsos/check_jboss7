#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Check_MK Check JBoss
#
# Copyright 2019, Yannis Mitsos <yannis@mitsos.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

group = "activechecks"

register_rule(group,
    "active_checks:jboss",
    Dictionary(
        title = _("Check JBoss"),
        help = _("This check connects to JBoss admin endpoint to check if running."
                 "The check uses the active check <tt>nagios-plugin-jbossas7</tt>."),
        optional_keys = [ "action", "port" ],
        elements = [
            ( "description",
              TextUnicode(title = _("Service Description"),
                 help = _("The name of this active service to be displayed."),
                 allow_empty = False,
            )),
            ( "port",
                 Integer(
                     title = _("TCP Port"),
                     minvalue = 1,
                     maxvalue = 65535,
                     default_value = 9990
                 )
            ),
            ( "action",
                TextUnicode(
                    title = _("The action you want to take. Accepted values: server_status, heap_usage, non_heap_usage, eden_space_usage, old_gen_usage, perm_gen_usage, code_cache_usage, gctime, queue_depth, datasource, xa_datasource, threading"),
                    allow_empty = True,
                )
            ),
            ( "user",
                TextAscii(
                    title = _("JBoss User"),
                    help = _('The username used to connect to the JBoss'),
                    allow_empty = False,
                )
            ),
            ( "password",
                IndividualOrStoredPassword(
                    title = _("JBoss Password"),
                    help = _('The password used to connect to the JBoss'),
                    allow_empty = False,
                )
            ),
        ]
    ),
    match = 'all'
)
