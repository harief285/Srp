from transaksi import Transaksi
from kartudebit import KartuDebit
from kartukredit import KartuKredit

# trans=Transaksi()
# trans.__init__()
# print(trans.do_payment())

debit=KartuDebit()
kredit=KartuKredit()

transaksi = Transaksi(debit)
transaksi.do_payment(25000000)

trans = Transaksi(kredit)
trans.do_payment(4000000)