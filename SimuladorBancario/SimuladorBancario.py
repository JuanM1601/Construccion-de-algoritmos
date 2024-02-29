from CuentaCorriente import CuentaCorriente
from CuentaAhorros import CuentaAhorros


class SimuladorBancario:
    """-----------------------------
    Atributos
   -----------------------------"""
    cedula =0
    nombre =0
    mesActual =0

    """-----------------------------
    Asociaciones
    -----------------------------"""
    saldoCorriente = CuentaCorriente()
    saldoAhorros = CuentaAhorros()

    """-----------------------------
    Metodos
   -----------------------------"""
    
    def ConsignarCorriente(self, saldo):
        # Aqui va el codigo del metodo
        return self.saldoCorriente.ConsignarValor(saldo)
    
    def CalcularSaldo(self, saldoCorriente, saldoAhorros):
        sTotal = self.saldoCorriente() + self.saldoAhorros
        return "Su saldo total es de: " + sTotal
    
    def RetirarSaldo(self):
        self.saldo = 0
        return "El saldo de la cuenta es: "+ self.saldo
