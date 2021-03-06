"""
File Name: advantagesavings.py
Feature: Here Defines The AdvantageSavings Class
"""

class AdvantageSavings():
	"""This class represents a Advantage Savings Account"""

	def __init__(self, name, pin, balance):
		"""Defining the attributes of the class"""
		self.monthly_maintenance_fee = 8.0
		self.withdrawal_limit_fee = 10
		
		self.atm_fee_for_bank_of_america = 'No ATM fee'
		self.atm_fee_for_non_bank_of_america_in_us = 2.50
		self.atm_fee_for_non_bank_of_america_outside_us = 5.00

		self.name = name
		self.pin = pin
		self.balance = balance

	def __repr__(self):
		"""Will return every detail when we print
		the object of this class"""
		return f'\nName: {self.name}\nPin: {self.pin}\nBalance: {self.balance}\n'

	def get_name(self):
		"""Returns the current Name"""
		return self.name

	def get_balance(self):
		"""Returns the current balance
		of this Account"""
		return self.balance

	def get_pin(self):
		"""Return the current Pin"""
		return self.pin

	def deposit(self, amount):
		"""add money to account balance and return"""
		self.balance+=amount
		return self.balance

	def transaction(self, amount):
		"""Do Withdraw if amount is >= 5.00$ and
		amount is less than balance and returnung
		new balance withdrawal limit fee is 10"""

		if self.balance>=5 and amount<=self.balance and amount>=5:
			self.balance-=(amount+self.withdrawal_limit_fee)
			return self.balance
		else:
			print('\n*****Transaction amount is greater than your current balance*******\n')
			return None

	def transfer(self, balance, amount):
		"""Transfering amount to another account, 
		if it's valid"""
		transfer_fee = 12.0
		if self.balance>=(amount+transfer_fee):
			balance+=amount
			self.balance-=(amount+transfer_fee)
			return balance, self.balance
		else:
			print('\n*****Given amount is greater than your balance or Your balance is Low****\n')
			return None

	def compute_fees(self, info='noatmfee'):
		"""Computing the additional Atm fees, info is
		telling wheter it is from america or outside"""
		if info=='inus':
			self.balance-=self.atm_fee_for_non_bank_of_america_in_us
			return self.balance
		elif info=='outsideus':
			self.balance-=self.atm_fee_for_non_bank_of_america_outside_us
			return self.balance
		else:
			return None

	def monthly_maintenance(self):
		"""This will automatically deduct monthly
		maintenance fee of your account"""
		self.balance-=self.monthly_maintenance_fee
		return self.balance
		
