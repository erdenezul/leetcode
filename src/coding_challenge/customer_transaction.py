import requests


class TransactionSolution:
    def totalAmount(self):
        r = requests.get("https://cdn.sablecard.com/challenge/transactions-v2.json")
        txs = r.json()
        return sum((row.get("amount") for row in txs))
