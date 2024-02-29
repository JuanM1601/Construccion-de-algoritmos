from CuentaCorriente import CuentaCorriente

class CuentaAhorros:

    """-----------------------------
    Atributos
    -----------------------------"""
    saldo =0

    """-----------------------------
    Asociaciones
    -----------------------------"""

    saldoAhorros = CuentaCorriente()

    """-----------------------------
    Metodos
    -----------------------------"""
    
    def ConsignarValor(self, saldo):
        nSaldo = self.saldo + ""
        self.saldo = nSaldo
        return "Ingrese valor a consignar"
    
    def RetirarValor(self, saldo):
        nSaldo = self.saldo - ""
        self.saldo = nSaldo
        return "Ingrese valor a retirar" + ""
    
    def TransferirSaldo(self, CuentaCorriente):
        self.saldo = self.saldo - self.saldo
        CuentaCorriente += self.saldo 
        return "El saldo finnal en la cuenta de ahorros es" + CuentaCorriente
    
    def DuplicarSaldo(self):
        #Forrma 1
        #self.saldo = self.saldo * 2
        #Forma 2
        self.saldo *= 2
        return "El saldo duplicado en su cuenta es: "+ self.saldo

    
