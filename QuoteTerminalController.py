from QuotesModel import *
from QuoteTerminalView import *


class QuoteTerminalController:
    def __init__(self, model, vista):
        self.model = model
        self.vista = vista

    def run(self):
        while True:
            try:
                menu = self.vista.menu()
                if menu == "1":
                    n = int(self.vista.select_quote())
                    quote = self.model.get_quote(n)
                    self.vista.show(quote)
                elif menu == "2":
                    quote = self.vista.add_quote()
                    self.model.add_quote(quote)
                elif menu == "3":
                    break
            except IndexError as e:
                raise e
                
def main():
    model = QuoteModel()
    vista = QuoteTerminalView()
    controller = QuoteTerminalController(model, vista)
    controller.run()
    
main()