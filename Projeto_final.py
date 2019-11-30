import threading as _

class banco(object):

    def __init__(self, nome=None, saldo=0.00):

        self.n = nome
        self.saldo = float(saldo)

    def get_nome(self):

        return self.n

    def get_saldo(self):

        return self.saldo

    def transfere(self, conta, dudu):

        transferencia = 10
        dudu.acquire()

        try:

            if self.saldo >= transferencia:

                conta.saldo += transferencia
                self.saldo -= transferencia

                print("\tsaldos atuais:\n")
                print(self.n,"= {:.2f}".format( self.get_saldo()), "\n")
                print(conta.get_nome(),"= {:.2f}".format( conta.get_saldo()), "\n")
                print("\tTransferencia efetuada.")
                print("-"*100)

        finally:

            dudu.release()


if __name__ == '__main__':

    cliente1 = banco("pedro", saldo=1000.00)
    cliente2 = banco("luana", saldo=0.00)

    print("\n\tSaldos iniciais:\n")
    print(cliente1.get_nome(),"=",cliente1.get_saldo(), "\n")
    print(cliente2.get_nome(),"=",cliente2.get_saldo(), "\n")
    print("\tTransferencia efetuada.\n")
    print("-"*100,"\n")

    lock = _.Lock()

    for a in range(0, 100):

        transacao = _.Thread(target=cliente1.transfere, args=(cliente2, lock))
        transacao.start()

        transacao2 = _.Thread(target=cliente2.transfere, args=(cliente1, lock))
        transacao2.start()
