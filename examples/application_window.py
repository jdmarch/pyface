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
""" Application window example. """


# Enthought library imports.
from pyface.api import ApplicationWindow, GUI
from pyface.action.api import Action, MenuManager, MenuBarManager
from pyface.action.api import StatusBarManager, ToolBarManager, Group


class MainWindow(ApplicationWindow):
    """ The main application window. """

    ###########################################################################
    # 'object' interface.
    ###########################################################################

    def __init__(self, **traits):
        """ Creates a new application window. """

        # Base class constructor.
        super(MainWindow, self).__init__(**traits)

        # Create an action that exits the application.
        exit_action = Action(name='E&xit', on_perform=self.close)
        
        # Test action to make all groups invisible.
        test_action = Action(name='&Toggle', on_perform=self.toggle)

        # Add a menu bar.
        self.menu_bar_manager = MenuBarManager(
            MenuManager(exit_action, name='&File')
        )

        # Add some tool bars.
        self.tool_bar_managers = [
            ToolBarManager(
                Group(exit_action, id='a'),
                Group(id='b'),
                Group(exit_action, exit_action, id='c'),
                Group(id='d'),
                Group(exit_action, exit_action, id='e'),
                name='Tool Bar 1', show_tool_names=False
            ),

            ToolBarManager(
                exit_action, name='Tool Bar 2', show_tool_names=False
            ),

            ToolBarManager(
                test_action, name='Tool Bar 3', show_tool_names=False
            ),
        ]

        # Add a status bar.
        self.status_bar_manager = StatusBarManager()
        self.status_bar_manager.message = 'Example application window'

        return
    
    def toggle(self):
        """ Toggle the visibility of the middle group in the first toolbar.
        """
        tbm = self.tool_bar_managers[0]
        mid_group = tbm.groups[2]
        visible = not mid_group.visible
        print '====='
        mid_group.print_traits()
        for item in mid_group._items:
            print '---'
            item.print_traits()
            item.visible = visible
        mid_group.visible = visible


# Application entry point.
if __name__ == '__main__':
    # Create the GUI (this does NOT start the GUI event loop).
    gui = GUI()

    # Create and open the main window.
    window = MainWindow()
    window.open()

    # Start the GUI event loop!
    gui.start_event_loop()

##### EOF #####################################################################
