import unittest
def calculate_price(price, cash_coupon, percent_coupon):
	subtotal = (price - cash_coupon)
	subtotal2 = subtotal * (1-(percent_coupon/100))
	tax = (.06 * subtotal2)

	if subtotal2 < 10:
		shipping = 5.95
	elif subtotal2 >= 10 and subtotal < 30:
		shipping = 7.95
	elif subtotal2 >= 30 and subtotal < 50:
		shipping = 11.95
	elif subtotal2 >= 50:
		shipping = 0.00

	print('Price is: ')
	print(price)
	print('Cash coupon is: ')
	print(cash_coupon)
	print('Precent coupon is: ')
	print(percent_coupon)
	print(percent_coupon/100)
	print('Subtotal: ')
	print(subtotal)
	print('Subtotal2: ')
	print(subtotal2)
	print('Shipping is: ')
	print(shipping)

	total = subtotal + shipping

	price_with_tax = subtotal2 + tax
	print('Price with tax:  ')
	print(price_with_tax)

	price_with_tax_and_shipping = '${:,.2f}'.format(price_with_tax + shipping)
	print('Price with tax and shipping:  ')
	print(price_with_tax_and_shipping)

price = float(input("What is the Price of the item: "))

cash_coupon = float(input("Enter the value of cash coupons: "))

percent_coupon = float(input("Enter your percentage discount amount: "))

calculate_price(price, cash_coupon, percent_coupon)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
