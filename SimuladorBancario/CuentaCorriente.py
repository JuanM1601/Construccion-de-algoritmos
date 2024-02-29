from CuentaAhorros import CuentaAhorros

class CuentaCorriente:

    """-----------------------------
    Atributos
    -----------------------------"""
    saldo = ""

    """-----------------------------
    Asociaciones
    -----------------------------"""

    saldoAhorros = CuentaAhorros()

    """-----------------------------
    Metodos
    -----------------------------"""
    def ConsultarSaldo(self):
        #Aqui va el codigo
        return self.saldo
    
    def ConsignarValor(self, saldo):
        nSaldo = self.saldo + ""
        self.saldo = nSaldo
        return "Ingrese valor a consignar" + ""
    
    def RetirarValor(self, saldo):
        nSaldo = self.saldo - ""
        self.saldo = nSaldo
        return "Ingrese valor a retirar" + ""
    
    def ConsultarSaldoCorriente(self):
        return self.saldo
