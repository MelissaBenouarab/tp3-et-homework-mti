# Separate Interfaces
class Printable:
    def print_document(self, document):
        pass
class Scannable:
    def scan_document(self, document):
        pass
class Faxable:
    def fax_document(self, document):
        pass
# Implementing Classes
class BasicPrinter(Printable):
    def print_document(self, document):
        print(f"Basic Printing: {document}")
class AdvancedPrinter(Printable, Scannable, Faxable):
    def print_document(self, document):
        print(f"Advanced Printing: {document}")
    def scan_document(self, document):
        print(f"Advanced Scanning: {document}")
    def fax_document(self, document):
        print(f"Advanced Faxing: {document}")

if __name__ == '__main__' :
    document="tp3.pdf"

    basic=BasicPrinter()
    basic.print_document(document)

    advanced = AdvancedPrinter()
    advanced.print_document(document)
    advanced.scan_document(document)
    advanced.fax_document(document)