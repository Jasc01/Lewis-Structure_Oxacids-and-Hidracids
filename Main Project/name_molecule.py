'''
Compara los resultados de las funciones para buscar el nombre de la molécula
'''
def nameMolecule(formule):
    baseBadCase = "Ácido "
    if "O" in formule:
        name = nameOxacid(formule) if nameOxacid(formule) != baseBadCase else ClBrIOxacid(formule) if ClBrIOxacid(
            formule) != baseBadCase else specialOxacid(formule) if specialOxacid(formule) != baseBadCase else ""
    else:
        name = nameHidracid(formule) if nameHidracid(formule) != baseBadCase else ""
    return name

'''
Busca oxácidos
'''
def nameOxacid(formule):
    name = "Ácido "
    ionOxad = ["SO4", "CrO4", "MnO4", "BO3", "NO3"]
    sufOxad = ["Sulfur", "Crom", "Mangán", "Bór", "Nítr"]
    if not formule[1].isdigit():
        formule = formule[0] + "1" + formule[1:]
    ion = formule[2:]
    for i in range(len(ionOxad)):
        if ion == ionOxad[i]:
            name = name + sufOxad[i] + "ico"
    return name

'''
Busca Oxácidos
'''
def ClBrIOxacid(formule):
    name = "Ácido "
    ionClBrI = ["Cl", "Br", "I"]
    sufClBrI = ["clor", "brom", "yod"]
    if formule[2].isupper():
        formule = formule[0] + formule[1] + "o" + formule[2:]
    if len(formule) == 4:
        formule = formule + "1"
    ion = formule[1]
    for i in range(len(ionClBrI)):
        if ion == ionClBrI[i][0] and formule[4] == "1":
            name = name + "Hipo" + sufClBrI[i] + "oso"
        elif ion == ionClBrI[i][0] and formule[4] == "2":
            name = name + sufClBrI[i] + "oso"
        elif ion == ionClBrI[i][0] and formule[4] == "3":
            name = name + sufClBrI[i] + "ico"
        elif ion == ionClBrI[i][0] and formule[4] == "4":
            name = name + "Per" + sufClBrI[i] + "ico"
    return name

'''
Busca Oxácidos especiales
'''
def specialOxacid(formule):
    name = "Ácido "
    special = ["HNO2", "H2SO3", "H2Cr2O7", "H2MnO4", "H5IO6", "H2SeO2", "H2SeO3", "H2SeO4"]
    namespecial = ["Nitroso", "Sulfoso", "Dicrómico", "Permangánico", "Ortoperyódico", "Hiposelenioso", "Selenioso", "Selénico"]
    formspecial = formule
    for i in range(len(special)):
        if formspecial == special[i]:
            name = name + namespecial[i]
    return name

'''
Busca Hidrácidos
'''
def nameHidracid(formule):
    name = "Ácido "
    atomsHidr = ["Cl", "Br", "I", "F", "S", "Se", "B", "N"]
    sufHidr = ["Clor", "Brom", "Iod", "Fluor", "Sulf", "Selen", "Bor", "Nit"]
    if not formule[1].isdigit():
        formule = formule[0] + "1" + formule[1:]
    element = formule[2:]
    for i in range(len(atomsHidr)):
        if element == atomsHidr[i]:
            name = name + sufHidr[i] + "hídrico"
    return name