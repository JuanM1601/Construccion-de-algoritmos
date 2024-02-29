from Fecha import Fecha

class Empleado:
    """---------------------------
    #Atributos
    ---------------------------"""
    nombre = 0
    apellido = 0

    """----------------------------
    #1 Masculino y 2 Femenino
    ----------------------------"""
    sexo = 0
    salario = 0
    """-----------------------------
    Asociaciones
    -----------------------------"""
    fechaNacimiento = Fecha
    fechaIngreso = Fecha
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
    
    def DuplicarSalario(self):
        #Aqui va el codigo
        #Forma 1
        #self.salario = self.salario*2 
        self.salario *= 2

    def CalcularSalarioAnual(self):
        #Aqui va el codigo
        #Forma 1 
        SalarioAnual = self.salario*12
        return SalarioAnual
        #Forma 2
        #return self.salario*12
    
    def ConsultarDiaCumpleaños(self):
        return "El diaa de su cumpleaños es "+self.fechaNacimiento.ConsultarDia()
    
    def CalcularImpuesto(self):
        #Forma 1
        total = self.CalcularSalarioAnual()
        return (total * 19.5) / 100
