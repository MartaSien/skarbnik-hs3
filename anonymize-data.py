import pandas as pd

PATRONITE = "data/sensitive/raw/raport-wplat-patronow-rok-2026.csv"
PATRONITE_SAMPLE = "data/sample/raw/raport-wplat-patronow-rok-2026.csv"

BUDGET = "data/sensitive/raw/budżet HS3 - wyciąg z konta.xlsx"


class DataAnonymizer:
    def __init__(self):
        self.patronite = pd.read_csv(PATRONITE, header=0, sep=";")

    def save_data(self):
        self.patronite.to_csv(PATRONITE_SAMPLE, sep=";")

    def anonymize(self):
        cols = ["Patron", "Email", "Typ operacji", "ID Patrona", "Imię i nazwisko"]
        self.patronite[cols] = self.patronite[cols].apply(lambda x: pd.factorize(x)[0])


if __name__ == "__main__":
    da = DataAnonymizer()
    da.anonymize()
    da.save_data()
