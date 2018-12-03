# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

from inginious.frontend.pages.utils import INGIniousAuthPage
from inginious.frontend.web_utils import see_other_exception


def get_menu(app, current, renderer, plugin_manager, user_manager):
    default_entries = []

    default_entries += [("profile", "<i class='fa fa-user fa-fw'></i>&nbsp; " + _("My profile")),
                        ("bindings", "<i class='fa fa-id-card-o fa-fw'></i>&nbsp; " + _("Authentication bindings"))]

    if app.allow_deletion:
        default_entries += [("delete", "<i class='fa fa-user-times fa-fw'></i>&nbsp; " + _("Delete my account"))]

    # Hook should return a tuple (link,name) where link is the relative link from the index of the preferences.
    additional_entries = [entry for entry in plugin_manager.call_hook('prefs_menu') if entry is not None]

    return renderer.preferences.menu(default_entries + additional_entries, current)


class RedirectPage(INGIniousAuthPage):
    """ Redirect preferences to /profile """

    def GET_AUTH(self):  # pylint: disable=arguments-differ
        """ GET request """

        raise see_other_exception('/preferences/profile')

    def POST_AUTH(self, courseid):  # pylint: disable=arguments-differ
        """ POST request """
        return self.GET_AUTH()