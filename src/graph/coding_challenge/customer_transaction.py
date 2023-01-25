import requests


class TransactionSolution:
    def timeline(self):
        r = requests.get("https://cdn.sablecard.com/challenge/transactions-v2.json")
        print(r.json())
        print(dir(r))


if __name__ == "__main__":
    s = TransactionSolution()
    s.timeline()
