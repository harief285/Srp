from transaksi import Transaksi
from kartudebit import KartuDebit
from kartukredit import KartuKredit

# trans=Transaksi()
# trans.__init__()
# print(trans.do_payment())

debit=KartuDebit()
print(debit.do_transaction(1000))

kredit=KartuKredit()
print(kredit.do_transaction(2000))