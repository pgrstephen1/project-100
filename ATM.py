class ATM:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = 500

    def cashWithdrawl(balance):
        amount = int(input("what is the amount you want to withdraw: "))
        print("cash withdrawl complete")

    def balanceEnquiry(balance):
        print("original balance: ", balance)


stephen = ATM('Stephen',123456789, 500)
stephen.cashWithdrawl()
stephen.balanceEnquiry()