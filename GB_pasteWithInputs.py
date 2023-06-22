# 22-06-2023
# Python 3
# Golan van der Bend
# This is a Nuke Python script that lets you copy and paste the nodes with the inputs intact.
# My own test after watching Sebastian Schutt's video from Split the diff a year ago. 


import nuke 

def pasteWithInputs():

    selected = nuke.selectedNodes()
    
    # Get selected nodes + inputs
    nodesSelected = []
    nodesInput = []
    for node in selected:
        nodesSelected.append(node.name())
        
        for input in node.dependencies():
            nodesInput.append(input.name())
    
    # Create list with the nodes needed
    # inputs & unselected nodes 
    nodesInputUnselected = []
    nodesWithAddedButton = []
    for node in nodesInput:

        if node not in nodesSelected:
            nodesInputUnselected.append(node)

        else:
            nodesWithAddedButton.append(node)
    
    # Create button with inputs memory
    for node in nodesSelected:

        node = nuke.toNode(node)
        # create buttons: Tab, knob
        inputTab = nuke.Tab_Knob('Inputs', 'Inputs')
        node.addKnob(inputTab)
        inputsTextButton = nuke.Text_Knob('inputs', 'inputs') 
        node.addKnob(inputsTextButton)
    
        # loop thrue inputs
        inputsText = ''
        for i in range(node.inputs()):
            try:

                if node.input(i).name() in nodesInputUnselected:
                    inputToText = str(i) + ' ' + str(node.input(i).name())
                    print('input '+ inputToText)
                    inputsText = inputsText + inputToText + '\n'

            except AttributeError:
                pass 

        # add value to button
        node['inputs'].setValue(inputsText)
    
    # Copy nodes
    nuke.nodeCopy('%clipboard%')
    
    # there is alreadya selected nodes variable
    #selected = nuke.selectedNodes()
    
    # remove Tab en knob
    def removeKnobs():
        for node in selected:

            for knob in node.allKnobs(): # remove knob 'inputs'
                if knob.name() in ['inputs', 'Inputs']: 
                    node.removeKnob(knob)

            for knob in node.allKnobs(): # remove tab 'Inputs'
                if knob.name() == 'Inputs':
                    node.removeKnob(knob)
    removeKnobs()
        
    # Deselect all nodes. That way there is no input connection error with pasting the nodes. 
    for node in nuke.allNodes():
        node.setSelected(False)
    
    # Paste copied nodes. 
    nuke.nodePaste('%clipboard%')
    
    #Create new selection --> pasted nodes!
    selected = nuke.selectedNodes()
    
    # Set inputs for pasted nodes!
    for node in selected:
        try:

            if node['inputs'].value() == '':
                pass

            else:
                input = node['inputs'].value().split('\n')
    
                while("" in input):
                    input.remove("")

                if len(input) > 1:
                    for i in input:
                        i = i.split(' ')
                        i[0] = int(i[0])
                        node.setInput(i[0], nuke.toNode(i[1]))

                else:
                    i = input[0]
                    i = i.split(' ')
                    i[0] = int(i[0])
                    node.setInput(i[0], nuke.toNode(i[1]))

        except NameError:
            pass 
    
    # remove Tab en Knob on pasted nodes. 
    removeKnobs()

#pasteWithInputs()