""" The interactive Python shell plugin. """


# Enthought library imports.
from enthought.envisage.api import ExtensionPoint, Plugin
from enthought.traits.api import Dict, List, Str


class PythonShellPlugin(Plugin):
    """ The interactive Python shell plugin. """

    # Extension point Ids.
    BINDINGS = 'enthought.plugins.python_shell.bindings'
    COMMANDS = 'enthought.plugins.python_shell.commands'
    VIEWS    = 'enthought.envisage.ui.workbench.views'

    #### 'IPlugin' interface ##################################################

    id   = 'enthought.plugins.python_shell'
    name = 'Acme Workbench'

    #### 'PythonShellPlugin' interface ########################################

    #### Extension points #####################################################

    bindings = ExtensionPoint(
        List(Dict), id=BINDINGS, desc="""

        This extension point allows you to contribute name/value pairs that
        will be bound when the interactive Python shell is started.

        e.g. Each item in the list is a dictionary of name/value pairs::

        {'x' : 10, 'y' : ['a', 'b', 'c']}

        """
    )

    commands = ExtensionPoint(
        List(Str), id=COMMANDS, desc="""

        This extension point allows you to contribute commands that are
        executed when the interactive Python shell is started.

        e.g. Each item in the list is a string of arbitrary Python code::

          'import os, sys'
          'from enthought.traits.api import *'

        Yes, I know this is insecure but it follows the usual Python rule of
        'we are all consenting adults'.
          
        """
    )

    #### Extension point contributions ########################################
             
    # Views.
    views = List(extension_point=VIEWS)
    
    ###########################################################################
    # 'PythonShellPlugin' interface.
    ###########################################################################

    #### Trait initializers ###################################################
    
    def _views_default(self):
        """ Trait initializer. """

        # Local imports.
        from view.python_shell_view import PythonShellView

        return [PythonShellView]
        
#### EOF ######################################################################
