#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
""" Wizard example. """


# Standard library imports.
import os
import sys

# Put the Enthought library on the Python path.
sys.path.append(os.path.abspath(r'..\..\..'))

# Enthought library imports.
from enthought.pyface.api import GUI, OK
from enthought.pyface.wizard.api import SimpleWizard, WizardPage
from enthought.traits.api import Color, HasTraits, Int, Str


class Details(HasTraits):
    """ Some test data. """

    name = Str
    color = Color


class SimpleWizardPage(WizardPage):
    """ A simple wizard page. """

    #### 'SimpleWizardPage' interface #########################################

    # The page color.
    color = Color

    ###########################################################################
    # 'IWizardPage' interface.
    ###########################################################################

    def _create_page_content(self, parent):
        """ Create the wizard page. """

        details = Details(color=self.color)
        details.on_trait_change(self._on_name_changed, 'name')

        return details.edit_traits(parent=parent, kind='subpanel').control

    ###########################################################################
    # Private interface.
    ###########################################################################

    #### Trait event handlers #################################################

    def _on_name_changed(self, new):
        """ Called when the name has been changed. """

        self.complete = len(new.strip()) > 0

        return


# Application entry point.
if __name__ == '__main__':
    # Create the GUI (this does NOT start the GUI event loop).
    gui = GUI()

    wizard = SimpleWizard(
        parent = None,
        title  = 'Create something magical',
        pages  = [
            SimpleWizardPage(id='foo', heading="The Red Page",
                    subheading="The default color on this page is red.",
                    color='red'),
            SimpleWizardPage(id='bar', heading="The Yellow Page",
                    subheading="The default color on this page is yellow.",
                    color='yellow'),
            SimpleWizardPage(id='baz', heading="The Green Page",
                    subheading="The default color on this page is green.",
                    color='green')
        ]
    )

    # Create and open the wizard.
    if wizard.open() == OK:
        print 'Wizard completed successfully'
    else:
        print 'Wizard cancelled'

##### EOF #####################################################################
