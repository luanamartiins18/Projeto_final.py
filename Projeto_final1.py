import threading as 


class Conta(object):

    def __init__(self, nome=None, saldo=0.00):

        self.n = nome
        self.saldo = float(saldo)

    def get_nome(self):

        return self.n

    def get_saldo(self):

        return self.saldo

    def transfere(self, conta, protect):
        transferencia = 10
        protect.acquire()
        try:
            if self.saldo >= transferencia:

                conta.saldo += transferencia
                self.saldo -= transferencia


                print(self.n,"{:.2f}".format( self.get_saldo()), "\n")
                print(conta.get_nome(),"{:.2f}".format( conta.get_saldo()), "\n")
                print('Transferencia efetuada\n')
                print("-"*100)

        finally:
            protect.release()



if __name__ == '__main__':

    cliente1 = Conta('pedro', saldo=1000.00)
    cliente2 = Conta('luana', saldo=0.00)
    print("Saldo inicial:\n")
    print(cliente1.get_nome(), cliente1.get_saldo(), "\n")
    print(cliente2.get_nome(), cliente2.get_saldo(), "\n")
    print('Transferencia efetuada\n')
    print("-"*100,"\n")


    lock = _.Lock()

    aleatorio = 10

    for a in range(0, 100):
        thread = _.Thread(target=cliente1.transfere, args=(cliente2, lock))
        thread.start()

        thread = _.Thread(target=cliente2.transfere, args=(cliente1, lock))
        thread.start()
