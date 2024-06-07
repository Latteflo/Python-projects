import tkinter as tk
from forex_python.converter import CurrencyRates

common_currency = ['USD', 'EUR', 'RON', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        self.master.title('Currency Converter')
        self.master.geometry('300x200')
        
    
        self.from_currency = tk.StringVar(self.master)
        self.from_currency.set('USD')
        self.from_currency_menu = tk.OptionMenu(self.master, self.from_currency, *common_currency)
        self.from_currency_menu.pack(pady=5)

        self.to_currency = tk.StringVar(self.master)
        self.to_currency.set('EUR')
        self.to_currency_menu = tk.OptionMenu(self.master, self.to_currency, *common_currency)
        self.to_currency_menu.pack(pady=5)

        self.amount_label = tk.Label(self.master, text='Amount:')
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack(pady=5)

        self.convert_button = tk.Button(self.master, text='Convert', command=self.convert_currency)
        self.convert_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text='Result:')
        self.result_label.pack(pady=5)

    def convert_currency(self):
        try:
            c = CurrencyRates()
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()
            amount = float(self.amount_entry.get())
            result = c.convert(from_currency, to_currency, amount)
            self.result_label.config(text=f'Result: {result:.2f}')
        except ValueError:
            self.result_label.config(text='Invalid input! Please enter a valid number.')
        except Exception as e:
            self.result_label.config(text=f'Error: {str(e)}')

if __name__ == '__main__':
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
