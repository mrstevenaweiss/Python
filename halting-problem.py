
def halting(procedure, input):
    if 'procedure halts':
        return 'halt'
    else:
        return 'loops forever'


def kopy(procedure):
    if halting(procedure, procedure) == "loops forever":
        return 'halt'
    else: 
