from models.transaction import Transaction

class TransactionService:

    # addTransaction()
    @staticmethod
    def addTransaction(transaction_data):
        transaction = Transaction(**transaction_data)
        transaction.save()
        return transaction 
    
    # getAllTransactions()
    @staticmethod
    def getAllTransactions():
        transactions = Transaction.objects.all()
        return transactions
    
    # findTransactionByUserId()
    @staticmethod
    def findTransactionByUserId(user_id):
        transactions = Transaction.objects(user_id=user_id)
        return transactions

    # markTransactionAsReturned()
    @staticmethod
    def markTransactionAsReturned(transaction_id):
        transaction = Transaction.objects(id=transaction_id).update_one(set__returned=True)
        return transaction

    # updateTransaction()
    @staticmethod
    def updateTransaction(transaction_id, update_data):
        transaction = Transaction.objects(id=transaction_id).update_one(**update_data)
        return transaction

    # deleteTransaction()
    @staticmethod
    def deleteTransaction(transaction_id):
        result = Transaction.objects(id=transaction_id).delete()
        return result