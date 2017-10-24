from random import randint
import numpy

on = 0
positions = {}
starting_amt = 200
minimum_bet = 15
money = 0
max_odds_factor = 5

def roll_dice(call = 1):
	dice1 = randint(1, 6)
	dice2 = randint(1, 6)
	dice = dice1 + dice2

	if call == 1:
		if dice == 2:
			two()
		elif dice == 3:
			three()
		elif dice == 4:
			four()
		elif dice == 5:
			five()
		elif dice == 6:
			six()
		elif dice == 7:
			seven()
		elif dice == 8:
			eight()
		elif dice == 9:
			nine()
		elif dice == 10:
			ten()
		elif dice == 11:
			eleven()
		elif dice == 12:
			twelve()
	return dice

def clear_the_table():
	global positions
	global on

	positions = {}
	on = 0
	return positions

def max_possible_multiplier(num, bets):
	if num > bets:
		return bets
	else:
		return num


#	ROLLS

def two():
	global positions
	global money

	if on == 0:
		if "passline" in positions:
			del positions["passline"]
	elif on > 0:
		if "field" in positions:
			money += (positions["field"][1] * 2)

def three():
	global positions
	global money

	if on == 0:
		if "passline" in positions:
			del positions["passline"]
	elif on > 0:
		if "field" in positions:
			money += positions["field"][1]

def four():
	global on
	global money
	global positions

	if on == 0:
		on = 4
	elif on > 0:
		if "field" in positions:
			money += positions["field"][1]
		if "place" in positions:
			money += int((9*positions["place"][4])/5)
		if on == 4:
			on = 0
			if "passline" in positions:
				money += positions["passline"][1]
			if "pass_odds" in positions:
				money += (2 * positions["pass_odds"][1])


def five():
	global on
	global money
	global positions

	if on == 0:
		on = 5
	elif on > 0:
		if on == 5:
			on  = 0
			if "passline" in positions:
				money += positions["passline"][1]
			if "pass_odds" in positions:
				money += int((3 * positions["pass_odds"][1])/2)
		if "field" in positions:
			del positions["field"]
		if "place" in positions:
			money += int((7*positions["place"][5])/5)

def six():
	global on
	global money
	global positions

	if on == 0:
		on = 6
	elif on > 0:
		if on == 6:
			on = 0
			if "passline" in positions:
				money += positions["passline"][1]
			if "pass_odds" in positions:
				money += int((6 * positions["pass_odds"][1])/5)
		if "field" in positions:
			del positions["field"]
		if "place" in positions:
			money += int((7*positions["place"][6])/6)

def seven():
	global positions
	global money

	if on == 0:
		if "passline" in positions:
			money += positions["passline"][1]
	else:
		clear_the_table() # sets on to 0

def eight():
	global on
	global money
	global positions

	if on == 0:
		on = 8
	elif on > 0:
		if on == 8:
			on = 0
			if "passline" in positions:
				money += positions["passline"][1]
			if "pass_odds" in positions:
				money += int((6 * positions["pass_odds"][1])/5)
		if "field" in positions:
			del positions["field"]
		if "place" in positions:
			money += int((7*positions["place"][8])/6)

def nine():
	global on
	global money
	global positions

	if on == 0:
		on = 9
	elif on > 0:
		if "field" in positions:
			money += positions["field"][1]
		if "place" in positions:
			money += int((7*positions["place"][9])/5)
		if on == 9:
			on = 0
			if "passline" in positions:
				money += positions["passline"][1]
			if "pass_odds" in positions:
				money += int((3 * positions["pass_odds"][1])/2)

def ten():
	global on
	global money
	global positions

	if on == 0:
		on = 10
	elif on > 0:
		if "field" in positions:
			money += positions["field"][1]
		if "place" in positions:
			money += int((9*positions["place"][10])/5)
		if on == 10:
			on = 0
			if "passline" in positions:
				money += positions["passline"][1]
			if "pass_odds" in positions:
				money += (2 * positions["pass_odds"][1])

def eleven():
	global money
	global positions

	if on == 0:
		if "passline" in positions:
			money += positions["passline"][1]
	elif on > 0:
		if "field" in positions:
			money += positions["field"][1]

def twelve():
	global positions
	global money

	if on == 0:
		if "passline" in positions:
			del positions["passline"]
	elif on > 0:
		if "field" in positions:
			money += (positions["field"][1] * 2)

#	BETTING
def bet(type, amount, number = 0):
	global money
	global positions

	if type in positions:
		if type != "place" and type != "hardway" and type != "one_roll":
			positions[type][1] += amount
		elif type == "place":
			place(number, amount)
		elif type == "hardway":
			hardway(number, amount)
		elif type == "one_roll":
			one_roll(number, amount)
	else:
		if type == "pass_odds":
			if positions.get("passline") is None:
				amount = 0
			elif amount > (max_odds_factor * positions["passline"]):
				amount = max_odds_factor * positions["passline"]
			positions[type] = (number, amount)
		elif type == "dont_pass_odds":
			if positions.get("dont_passline") is None:
				amount = 0
			elif amount > (max_odds_factor * positions["dont_passline"]):
				amount = max_odds_factor * positions["dont_passline"]
			positions[type] = (number, amount)
		elif type == "place":
			place(number, amount)
		elif type == "hardway":
			hardway(number, amount)
		elif type == "one_roll":
			one_roll(number, amount)
		else:
			positions[type] = (number, amount)

	money -= amount


def passline(amount):
	position = {"passline": (0, amount)}
	return position

def field(amount):
	position = {"field": (0, amount)}
	return position

def come(amount):
	return position

def place(number, amount):
	global positions

	if positions.get("place") is None:
		positions["place"] = []
		for x in range(13):
			positions["place"].append(0)
	# print positions["place"]
	positions["place"][number] += amount

def dont_passline(amount):
	return position

def dont_come(amount):
	return position

def hardway(number, amount):
	return position

def one_roll(number, amount):
	return position

# ALGORITHMS

def passline_only(run, file_num, rounds=10000):

			if on == 0 and positions.get("passline") is None:
				if money > minimum_bet:
					bet("passline", minimum_bet)
				else:
					money = 0


def field_bet_only(run, file_num, rounds=10000):
	if on == 0 and positions.get("field") is None:
		if money > minimum_bet:
			bet("field", minimum_bet)
		else:
			money = 0


def six_and_eight(run, file_num, rounds=10000):
	if on == 0 and positions.get("passline") is None:
		if money > minimum_bet:
			bet("passline", minimum_bet)
		else:
			money = 0
	else:
		if money > 2 * minimum_bet:
			if "place" in positions:
				if positions["place"][6] == 0:
					bet("place", minimum_bet, 6)
				if positions["place"][8] == 0:
					bet("place", minimum_bet, 8)
			else:
				bet("place", minimum_bet, 8)
				bet("place", minimum_bet, 6)
		else:
			money = 0


def six_and_eight_field_odds_mix(run, file_num, rounds=10000):
	if on == 0 and positions.get("passline") is None:
		if money > minimum_bet:
			bet("passline", minimum_bet)
		else:
			money = 0
	else:
		if on == 6 or on == 8:
			#place
			if "place" in positions:
				if positions["place"][6] == 0 and money > minimum_bet and on == 8:
					bet("place", minimum_bet, 6)
				if positions["place"][8] == 0 and money > minimum_bet and on == 6:
					bet("place", minimum_bet, 8)
			else:
				if money > 2 * minimum_bet:
					if on == 8:
						bet("place", minimum_bet, 6)
					if on == 6:
						bet("place", minimum_bet, 8)
		elif on == 4 or on == 9 or on == 10:
			#field
			if positions.get("field") is None and money > minimum_bet:
				bet("field", minimum_bet)
		#odds
		if positions.get("pass_odds") is None and money > minimum_bet:
			bet("pass_odds", minimum_bet)


def odds_emphasis_plus_minimum_field(run, file_num, rounds=10000):
	if on == 0 and positions.get("passline") is None:
		if money > minimum_bet:
			bet("passline", minimum_bet)
		else:
			money = 0
	else:
		#odds
		if on == 6 or on == 8:
			if positions.get("pass_odds") is None and money > max_possible_multiplier(5, minimum_bets_available):
				bet("pass_odds", max_possible_multiplier(5, minimum_bets_available))
		elif on == 5 or on == 9:
			if positions.get("pass_odds") is None and money > max_possible_multiplier(3, minimum_bets_available) * minimum_bet:
				bet("pass_odds", max_possible_multiplier(3, minimum_bets_available) * minimum_bet)
		elif on == 4 or on ==10:
			if positions.get("pass_odds") is None and money > minimum_bet:
				bet("pass_odds", minimum_bet)
		#field
		if positions.get("field") is None and money > minimum_bet:
			bet("field", minimum_bet)


def all_out_odds(money, minimum_bets_available):
	if on == 0 and positions.get("passline") is None:
		if money > minimum_bet:
			bet("passline", minimum_bet)
		else:
			money = 0
	else:
		#odds
		if on == 6 or on == 8:
			if positions.get("pass_odds") is None and money > max_possible_multiplier(5, minimum_bets_available):
				bet("pass_odds", max_possible_multiplier(5, minimum_bets_available) * minimum_bet)
		elif on == 5 or on == 9:
			if positions.get("pass_odds") is None and money > max_possible_multiplier(4, minimum_bets_available) * minimum_bet:
				bet("pass_odds", max_possible_multiplier(4, minimum_bets_available) * minimum_bet)
		elif on == 4 or on ==10:
			if positions.get("pass_odds") is None and money > max_possible_multiplier(3, minimum_bets_available) * minimum_bet:
				bet("pass_odds", max_possible_multiplier(3, minimum_bets_available) * minimum_bet)



# PLAY

def playStrategy(strategyFunction, run, file_num, rounds=10000):
	global money

	turns = 0
	cash_balance_total = []
	max_balance = starting_amt
	clear_the_table()

	minimum_bets_available = money / minimum_bet

	while money > 0:
		while turns < rounds and money > 0:
			turns += 1

			minimum_bets_available = money / minimum_bet


			strategyFunction(money, minimum_bets_available)


			roll = roll_dice()


			# CALCULATE MAX WINNINGS
			if money > max_balance:
				max_balance = money

			cash_balance_total.append(money)
		break

	avg_cash = numpy.mean(cash_balance_total)
	std_dev_holdings = numpy.std(cash_balance_total)
	write_to_file(run, turns, max_balance, avg_cash, std_dev_holdings, file_num)

# OUTPUT

def write_to_file(run, turns, max_balance, avg_cash, std_dev_holdings, file_num):
	global starting_amt
	global minimum_bet

	f = open('results' + str(file_num) + '.csv', 'a')
	f.write("{}, {}, {}, {}, {}, {}, {}\n".format(run, starting_amt, minimum_bet, turns, max_balance, avg_cash, std_dev_holdings))
	f.close()
	


if __name__=="__main__":


	positions = {} # one position: { type: (value, amount) }
	clear_the_table()
	write_method = 'a'
	file_num = 1

	f = open('results' + str(file_num) + '.csv', write_method)
	f.write("{}, {}, {}".format(starting_amt, minimum_bet, max_odds_factor))
	f.write("\n\nmy_recent_strategy\n")
	f.write("Run, Starting Amount, Minimum Bet, Rolls, Max Cash, Avg Cash Balance, Std Dev Balance\n")
	f.close()

	for n in range(1, 1001):
		money = starting_amt
		playStrategy(all_out_odds, n, file_num)

	


