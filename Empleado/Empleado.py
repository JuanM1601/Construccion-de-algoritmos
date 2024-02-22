class Empleado:
    """---------------------------
    #Atributos
    ---------------------------"""
    nombre=0
    apellido=0

    """----------------------------
    #1 Masculino y 2 Femenino
    ----------------------------"""
    sexo=0
    salario=0

    """-----------------------------
    #Metodos
    -----------------------------"""

    def CambiarSalario(self, nuevoSalario):
        #Aqui va el codigo del metodo
        return 0 
    
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        #Aqui va el codigo del metodo
        return None
    
    def ConsultarSalario(self):
        #Aqui va el codigo
        return self.salario    
    
    def ConsultarNombre(self):
        #Aqui va el codigo
        return self.nombre   
    
    def CosultarApellido(self):
        #Aqui va el codigo
        return self.apellido
    
    def CosultarNombreCompleto(self):
        #Aqui va el codigo
        return self.nombre +" "+ self.apellido   
    
    def AumentoSalarial(self):
        nSalario = self.salario * 0.05  
        nSalario = nSalario + self.salario
        self.salario = nSalario
        return "El nuevo salario es de: "+self.salario
