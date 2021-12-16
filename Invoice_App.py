
# class declaration
class Invoice:
    # constructor declaration
    def __init__(self, part_num: str, part_description: str, quantity: int, price_per_item: float):
        # Global private variable declaration
        self.__part_num = part_num
        self.__part_description = part_description
        self.__quantity = quantity
        self.__price_per_item = price_per_item

    # set and get accessor for the instance variables
    def set_part_num(self, part_numb):
        if part_numb == '':
            self.__part_num = self.__part_num
        else:
            self.__part_num = part_numb

    def get_part_num(self):
        return self.__part_num

    def set_part_descript(self, part_descript):
        if part_descript == '':
            self.__part_description = self.__part_description
        else:
            self.__part_description = part_descript

    def get_part_descript(self):
        return self.__part_description

    def set_quantity(self, Qty: int):
        if Qty < 0:
            self.__quantity = self.__quantity
        else:
            self.__quantity = Qty

    def get_quantity(self):
        return self.__quantity

    def set_price_per_item(self, item_price: float):
        if item_price < 0:
            self.__price_per_item = self.__price_per_item
        else:
            self.__price_per_item = item_price

    def get_price_per_item(self):
        return self.__price_per_item

    def get_invoice_amount(self):
        return float(self.__quantity * self.__price_per_item)


def invoice_slip():  # main function where values are inserted and set to the accessor

    # the default values for the constructor
    new_invoice = Invoice('00001', 'Description', 3, 30.90)

    # inputs and assign them to setter methods
    part_number_input = str(input('Enter a part number : '))
    new_invoice.set_part_num(part_number_input)

    part_description_input = str(input('Enter a part description : '))
    new_invoice.set_part_descript(part_description_input)

    while True:  # check for valid inputs
        try:
            item_quantity_input = int(input('Enter item quantity : '))
            new_invoice.set_quantity(item_quantity_input)
        except ValueError:
            print('Invalid item quantity')
            continue
        break

    while True:   # check for valid inputs
        try:

            price_per_item_input = float(input('Enter item price : '))
            new_invoice.set_price_per_item(price_per_item_input)

        except ValueError:
            print('Invalid item price')
            continue
        break

    # The output of the invoice slip
    print("==========************================")
    print("WELCOME TO PABLO HARDWARE STORE")
    print('Part number :', new_invoice.get_part_num())
    print('Part description :', new_invoice.get_part_descript())
    print('Item quantity :', new_invoice.get_quantity())
    print('Item price : ${:.2f}'.format(new_invoice.get_price_per_item()))
    print('Invoice amount : ${:.2f}'.format(new_invoice.get_invoice_amount()))


invoice_slip()  # invoke the main function
