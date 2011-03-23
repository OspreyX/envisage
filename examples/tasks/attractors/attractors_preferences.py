# Enthought library imports.
from enthought.envisage.ui.tasks.api import PreferencesPane, TaskFactory
from enthought.preferences.api import PreferencesHelper
from enthought.traits.api import Bool, Dict, Enum, List, Property, Str, \
    Unicode, cached_property
from enthought.traits.ui.api import EnumEditor, HGroup, VGroup, Item, Label, \
    View


class AttractorsPreferences(PreferencesHelper):
    """ The preferences helper for the Attractors application.
    """

    #### 'PreferencesHelper' interface ########################################

    # The path to the preference node that contains the preferences.
    preferences_path = 'example.attractors'

    #### Preferences ##########################################################

    # The task to activate on app startup if not restoring an old layout.
    default_task = Str

    # Whether to always apply the default application-level layout.
    # See TasksApplication for more information.
    always_use_default_layout = Bool


class AttractorsPreferencesPane(PreferencesPane):
    """ The preferences pane for the Attractors application.
    """

    #### 'PreferencesPane' interface ##########################################

    # The factory to use for creating the preferences model object.
    model_factory = AttractorsPreferences

    #### 'AttractorsPreferencesPane' interface ################################

    task_factories = List(TaskFactory)
    task_map = Property(Dict(Str, Unicode), depends_on='task_factories')

    view = View(
        VGroup(HGroup(Item('always_use_default_layout'),
                      Label('Always use the default active task on startup'),
                      show_labels = False),
               HGroup(Label('Default active task:'),
                      Item('default_task',
                           editor=EnumEditor(name='handler.task_map')),
                      enabled_when = 'always_use_default_layout',
                      show_labels = False),
               label='Application startup'),
        resizable=True)

    ###########################################################################
    # Private interface.
    ###########################################################################

    @cached_property
    def _get_task_map(self):
        return dict((factory.id, factory.name)
                    for factory in self.task_factories)
