class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."
    
class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"    
    
class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"
    
def client_code(target: Target) -> None:
    print(target.request())
    
target = Target()
client_code(target)
adaptee = Adaptee()
adaptee.specific_request()

adapter = Adapter()
client_code(adapter)