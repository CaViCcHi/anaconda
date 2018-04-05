# Ask vnc text spoke
#
# Copyright (C) 2013  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#

from pyanaconda.ui.tui.spokes import StandaloneTUISpoke
from pyanaconda.ui.tui.hubs.summary import SummaryHub
from pyanaconda.core.i18n import N_, _

from pyanaconda.core.util import is_unsupported_hw
from pyanaconda.product import productName

from simpleline.render.widgets import TextWidget

from pyanaconda.anaconda_loggers import get_module_logger
log = get_module_logger(__name__)

__all__ = ["WarningsSpoke"]


class WarningsSpoke(StandaloneTUISpoke):
    """
       .. inheritance-diagram:: WarningsSpoke
          :parts: 3
    """
    preForHub = SummaryHub
    priority = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = N_("Warnings")
        self.initialize_start()

        self._message = _("This hardware (or a combination thereof) is not "
                          "supported by Red Hat.  For more information on "
                          "supported hardware, please refer to "
                          "http://www.redhat.com/hardware.")
        # Does anything need to be displayed?
        # pylint: disable=no-member
        self._unsupported = productName.startswith("Red Hat ") and \
                            is_unsupported_hw() and \
                            not self.data.unsupportedhardware.unsupported_hardware

        self.initialize_done()

    @property
    def completed(self):
        return not self._unsupported

    def refresh(self, args=None):
        super().refresh(args)

        self.window.add_with_separator(TextWidget(self._message))

    # Override Spoke.apply
    def apply(self):
        pass
