import ipywidgets as wg
import os

from IPython.display import display

from pycrop2ml_ui.browser.TkinterPath import getPath
from pycrop2ml_ui.menus.edition import editunit, editcomposition
from pycrop2ml_ui.model import MainMenu


class editMenu():
    """
    Class providing the display of the model edition menu for pycrop2ml's user interface.
    """

    def __init__(self, local):
           
        #outputs
        self._out = wg.Output()
        self._out2 = wg.Output()
        self.local=local

        #inputs

        self._selecter = wg.Dropdown(options=['None'],value='None',description='Model:',disabled=True,layout=wg.Layout(width='400px',height='35px'))
        
        if self.local==True:
            self._modelPath = wg.Textarea(value='',description='Model path:',disabled=True,layout=wg.Layout(width='400px',height='57px'))
            self._browse = wg.Button(value=False,description='Browse',disabled=False,button_style='primary')
            self._pathing = wg.VBox([wg.HBox([self._modelPath, self._browse]), self._selecter])
        
        else:
            self._modelPath = wg.Dropdown(options=['None'],value='None',description='Model path:',disabled=False,layout=wg.Layout(width='400px',height='35px'))
            self.tmp = [""]
            self.pkg_directory = "./packages"
            for f in os.listdir(self.pkg_directory):
                self.tmp.append(os.path.join(self.pkg_directory,f))
            self._modelPath.options = self.tmp 
            self._modelPath.disabled = False 
            self._pathing = wg.VBox([self._modelPath, self._selecter])  
        #buttons
        
        self._edit = wg.Button(value=False,description='Apply',disabled=False,button_style='success')
        self._cancel = wg.Button(value=False,description='Cancel',disabled=False,button_style='warning')

        #global displayer
        self._displayer = wg.VBox([wg.HTML(value='<font size="5"><b>Model edition : Selection</b></font>'), self._pathing, wg.HBox([self._edit, self._cancel])],layout=wg.Layout(align_items='center'))

        self._paths = dict()



    def _eventEdit(self, b):
        """
        Handles edit button on_click event
        """

        self._out.clear_output()
        self._out2.clear_output()
        
        typemodel = self._selecter.value.split('.')

        with self._out:
            if typemodel[0] == 'unit':
                try: 
                    unit = editunit.editUnit({'Path': os.path.join(self._modelPath.value, 'crop2ml'), 'Model type': typemodel[0], 'Model name': typemodel[1]}, self.local)
                    unit.displayMenu()
                except:
                    raise Exception('Could not load unit model edition menu.')

            else:
                try:            
                    composition = editcomposition.editComposition({'Path': os.path.join(self._modelPath.value, 'crop2ml'), 'Model type': typemodel[0], 'Model name': typemodel[1]}, self.local)
                    composition.displayMenu()
                except:
                    raise Exception('Could not load composition model edition menu.')



    def _eventBrowse(self, b):
        """
        Handles browse button on_click event
        """
        
        self._out2.clear_output()
        self._modelPath.value = getPath()

        if 'crop2ml' not in os.listdir(self._modelPath.value):
            self._modelPath.value = ''
            with self._out2:
                print('This repository is not a model package.')



    def _eventCancel(self, b):
        """
        Handles cancel button on_click event
        """

        self._out.clear_output()
        self._out2.clear_output()
        
        with self._out:
            try:
                tmp = MainMenu.mainMenu(self.local)
                tmp.displayMenu()
            except:
                raise Exception('Could not load mainMenu.')
            


    def _on_value_change(self, change):
        """
        Handles changes from the attribute _modelPath.

        Find every model in xml format in the selected path.
        """

        self._paths.clear()
        tmp = []
        for f in os.listdir(os.path.join(self._modelPath.value, 'crop2ml')):
            split = f.split('.')
            if all([split[-1] == 'xml', split[0] in ['unit','composition']]):
                self._paths[f] = os.path.join(self._modelPath.value, 'crop2ml', f)
                tmp.append(f)
        
        self._selecter.options = tmp    
        self._selecter.disabled = False



    def displayMenu(self):
        """
        Displays the model edition menu of pyrcop2ml's UI.

        This method is the only one available for the user in this class. Any other attribute or
        method call may break the code.
        """

        display(self._out)
        display(self._out2)

        with self._out:
            display(self._displayer)
        
        self._edit.on_click(self._eventEdit)
        if self.local == True: self._browse.on_click(self._eventBrowse)
        self._cancel.on_click(self._eventCancel)
        self._modelPath.observe(self._on_value_change, names='value')