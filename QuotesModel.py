class QuoteModel:
    def __init__(self):
        self.citas = ["As I said before, I never repeat myself.", "No free lunch", "May the Force be with you", "Make my day"]
    
    def get_quote(self, n):
        try:
            value = self.citas[n]
            return value
        except IndexError:
            raise Exception("Quote index out of range!")
        
    def add_quote(self, quote):
        self.citas.append(quote)