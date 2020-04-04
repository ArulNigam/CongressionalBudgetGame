# Name: Arul Nigam
# Date: 04 April 2020

######################################
## This game is designed to teach   ##
## students about how Congress      ##
## appropriates the                 ##
## "discretionary spending"         ##
## portion of the federal budget    ##
## each year, and includes just     ##
## a few of the many considerations ##
## in the process.                  ##
######################################

import random, time


class Constituent:
    def __init__(self):
        self.happiness = random.randint(50, 52)
        self.pronoun = random.choice(["his", "her"])
        self.income = 10000 * random.randint(3, 8)
        if random.random() < 0.25:
            self.income *= 5
        if random.random() < 0.05:
            self.income *= 10
        if random.random() < 0.01:
            self.income *= 10
        if random.random() < 0.0001:
            self.income *= 5
        self.issues = []
        possible_issues = ["Military", "Space", "Health", "Housing", "Energy", "Veterans"]
        random.shuffle(possible_issues)
        number_of_issues = random.randint(0, 5)
        for i in range(number_of_issues):
            self.issues.append(possible_issues.pop(0))
        if self.pronoun == "his":
            first_names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas",
                           "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven",
                           "Andrew", "Kenneth", "Joshua", "George", "Kevin", "Brian", "Edward", "Ronald", "Timothy",
                           "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Stephen", "Jonathan",
                           "Larry",
                           "Justin", "Scott", "Brandon", "Frank", "Benjamin", "Gregory", "Samuel", "Raymond", "Patrick",
                           "Alexander", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Henry", "Douglas", "Adam",
                           "Peter", "Nathan", "Zachary", "Walter", "Kyle", "Harold", "Carl", "Jeremy", "Keith", "Roger",
                           "Gerald", "Ethan", "Arthur", "Terry", "Christian", "Sean", "Lawrence", "Austin", "Joe",
                           "Noah",
                           "Jesse", "Albert", "Bryan", "Billy", "Bruce", "Willie", "Jordan", "Dylan", "Alan", "Ralph",
                           "Gabriel", "Roy", "Juan", "Wayne", "Eugene", "Logan", "Randy", "Louis", "Russell", "Vincent",
                           "Philip", "Bobby", "Johnny", "Bradley"]
        else:  # self.pronoun == "her
            first_names = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah",
                           "Karen", "Nancy", "Margaret", "Lisa", "Betty", "Dorothy",
                           "Sandra", "Ashley", "Kimberly", "Donna", "Emily", "Michelle", "Carol", "Amanda", "Melissa",
                           "Deborah", "Stephanie", "Rebecca", "Laura", "Sharon", "Cynthia", "Kathleen", "Helen", "Amy",
                           "Shirley", "Angela", "Anna", "Brenda", "Pamela", "Nicole", "Ruth", "Katherine", "Samantha",
                           "Christine", "Emma", "Catherine", "Debra", "Virginia", "Rachel", "Carolyn", "Janet", "Maria",
                           "Heather", "Diane", "Julie", "Joyce", "Victoria", "Kelly", "Christina", "Joan", "Evelyn",
                           "Lauren", "Judith", "Olivia", "Frances", "Martha", "Cheryl", "Megan", "Andrea", "Hannah",
                           "Jacqueline", "Ann", "Jean", "Alice", "Kathryn", "Gloria", "Teresa", "Doris", "Sara",
                           "Janice",
                           "Julia", "Marie", "Madison", "Grace", "Judy", "Theresa", "Beverly", "Denise", "Marilyn",
                           "Amber",
                           "Danielle", "Abigail", "Brittany", "Rose", "Diana", "Natalie", "Sophia", "Alexis", "Lori",
                           "Kayla", "Jane"]
        last_initials = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.name = random.choice(first_names) + " " + last_initials[random.randint(0, 25)] + "."


def generate_scenarios(constituents_who_care):
    possible_scenarios = {
        "Military": [["The Department of Defense wants to purchase new F-35 fighter jets for the Air Force.", 2, 3],
                     ["The Department of Defense wants to expand nuclear research.", 1, 5],
                     ["The intelligence community wants to develop new cryptography tools.", 5, 2]],
        "Space": [["NASA is planning to send 4 astronauts to the moon in the next 5 years.", 7, 5],
                  ["The President wants to create a new branch of the armed forces, called the Space Force.", 3, 3]],
        "Health": [["The Department of Health and Human Services needs to purchase medical protection masks.", 4, 2],
                   ["The Center for Disease Control and Prevention wants to research vaccines for common diseases.", 3,
                    3]], "Housing": [[
                                         "The Department of Housing and Urban Development wants to expand affordable housing options for Americans.",
                                         2, 1]],
        "Energy": [["The Department of Energy wants to research solar energy.", 5, 2]],
        "Veterans": [["The Department of Veterans' Affairs wants to build new hospitals for veterans.", 6, 3]]}
    issues = []
    for i in constituents_who_care.keys():
        issues.append(i)
    random.shuffle(issues)
    scenarios_list = []
    for issue in issues:
        temp_list = possible_scenarios[issue]  # description, cost, benefit
        for i in range(len(temp_list)):
            scenarios_list.append([issue, temp_list[i][0], temp_list[i][1], temp_list[i][2]])
    random.shuffle(scenarios_list)
    return scenarios_list


def get_approval(constituents):
    happiness = 0
    for constituent in constituents:
        happiness += constituent.happiness
    return round(happiness / len(constituents), 1)


def get_constituents_who_care(issues, constituents):
    ret = {}
    for issue in issues:
        ret[issue] = []
        for constituent in constituents:
            for personal_issue in constituent.issues:
                if personal_issue == issue:
                    ret[issue].append(constituent)
    return ret


def print_attributes(constituents, issue):
    for constituent in constituents:
        print("\t", constituent.name, "cares about", issue, "issues and", constituent.pronoun, "happiness level is",
              str(constituent.happiness) + "%.")
    print()


def turn(to_play, tax_rate, tax_revenue, spending_level, constituents_list, constituents_who_care, year, total_income):
    scenarios_done = 0
    while scenarios_done < 2 and len(to_play) > 0:
        temp = to_play.pop(0)
        issue = temp[0]
        description = temp[1]
        cost = temp[2]
        benefit = temp[3]
        print()
        print("Issue:", description)
        print()
        print("If you fund this program, it would make", len(constituents_who_care[issue]), "constituent(s)",
              str(benefit) + "% happier, and", len(constituents_list) - len(constituents_who_care[issue]),
              "constituent(s) " + str(cost) + "% less happy.")
        temp_answer = "1"
        while temp_answer != "Y" and temp_answer != "N":
            temp_answer = input("Do you want to see which constituents care about this issue? (type Y or N):\n").strip().upper()
        if temp_answer == "Y":
            if len(constituents_who_care[issue]) == 0:
                print("None of your constituents care about this", issue, "issue.")
            else:  # someone does care
                print(
                    "These constituent(s) care about this issue:")  ###########################DEAL WITH 1 VS MULTIPLE CONSTITUENTS
                print_attributes(constituents_who_care[issue], issue)
        print("The cost of solving this issue is", "$" + "{:,}".format(int(0.01 * cost * total_income)), "or a",
              str(cost) + "% increase in taxes.")
        temp_answer = "1"
        while temp_answer != "Y" and temp_answer != "N":
            temp_answer = input("Will you fund the program? (type Y or N):\n").strip().upper()
        if temp_answer == "Y":
            temp_answer2 = "1"
            while temp_answer2 != "T" and temp_answer2 != "B":
                temp_answer2 = input("Will you raise taxes (type T) or borrow money (B) to fund the program?:\n").strip().upper()
            if temp_answer2 == "T":
                tax_rate += cost
                tax_revenue = tax_rate * total_income
                spending_level = tax_rate * total_income
                for constituent in constituents_list:
                    if constituent in constituents_who_care[issue]:
                        constituent.happiness += benefit
                    else:
                        constituent.happiness -= cost
            if temp_answer2 == "B":
                spending_level += cost
                for constituent in constituents_list:
                    if constituent in constituents_who_care[issue]:
                        constituent.happiness += benefit
                    else:
                        constituent.happiness -= cost
        scenarios_done += 1
        print("--------------------------------------------------------------------------------------------------")
    return get_approval(constituents_list), to_play, tax_rate, tax_revenue, spending_level, year + 2


def main():
    name = ""
    while name == "":
        name = input("Please enter your name:\n").strip().title()
    difficulty = ""
    while difficulty != "EASY" and difficulty != "MEDIUM" and difficulty != "HARD":
        difficulty = input("Please choose a difficulty level (type EASY, MEDIUM, or HARD):\n").strip().upper()
    if difficulty == "HARD":
        num_constit = 10000  # number of constituents the player must consider
    elif difficulty == "MEDIUM":
        num_constit = 1000
    else:  # difficulty == "HARD"
        num_constit = 500
    constituents_list = []
    for i in range(num_constit):
        constituents_list.append(Constituent())
    tax_rate = 10
    tax_revenue = 0
    spending_level = 0
    constituents_who_care = get_constituents_who_care(["Military", "Space", "Health", "Housing", "Energy", "Veterans"],
                                                      constituents_list)
    approval = 100.0
    to_play = generate_scenarios(constituents_who_care)
    year = 2020
    total_income = 0
    for constituent in constituents_list:
        total_income += constituent.income
    print()
    print("You are taking on the role of a member of the U.S. House of Representatives, serving")
    print("two-year terms. You are tasked with crafting the discretionary part of the federal")
    print("budget. Listen to your constituents and create a budget that meets the need of the most")
    print("people, and try to get re-elected as many times as you can!")
    print()
    input("Press enter when you are ready to begin. Good luck!\n").strip().upper()
    while approval >= 50.0 and len(to_play) > 0:
        approval, to_play, tax_rate, tax_revenue, spending_level, year = turn(to_play, tax_rate, tax_revenue,
                                                                              spending_level, constituents_list,
                                                                              constituents_who_care, year, total_income)
        if approval >= 50.0 and len(to_play) > 0:
            print("Congratulations! You were re-elected in the", year, "election. Time to work on solving more issues!")
            time.sleep(2.5)
        elif len(to_play) > 0:
            print(
                "You raised taxes too high or did not tend to the issues your constituents care about, so you were not re-elected in the",
                year, "election.")
            print("You only received", str(approval) + "% of the vote. Here are your final results: ")
        else:  # ran out of scenarios
            print(
                "You've addressed all of the issues we have so far...good job! Check back later for more! Here are your final results: ")
    # print("The deficit (revenue - spending) is:", "$" + "{:,}".format(tax_revenue - spending_level))  #############################################################################################################################################################################SPECIAL CASE IF IT IS NEGATIVE
    print("The tax rate is", str(tax_rate) + "% and the total tax revenue is",
          "$" + "{:,}".format(int(0.01 * tax_rate * total_income)))
    print()
    print("Thank you for your service in Congress, Representative", name + "!")


if __name__ == '__main__':
    main()
