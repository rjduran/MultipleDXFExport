#Author-
#Description-

import adsk.core, adsk.fusion, traceback
import os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        
        sketches = []
        for seln in ui.activeSelections:
            sketch = adsk.fusion.Sketch.cast(seln.entity)
            if sketch:
                sketches.append(sketch)

        folderdlg = ui.createFolderDialog()
        folderdlg.title = 'Please select a folder to save dxf files:' 
        res = folderdlg.showDialog()
        if res == adsk.core.DialogResults.DialogOK:
            folder = folderdlg.folder
            for sketch in sketches:
                fullpath = os.path.join(folder, sketch.name)
                sketch.saveAsDXF(fullpath + '.dxf')
                    
        else:
            ui.messageBox('No folder is selected.')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
