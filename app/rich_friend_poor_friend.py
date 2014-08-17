import facebook
from glassdoor import get

#reference: http://www.salarylist.com/company/National-Grid-USA-Salary.htm, with some adjustment
def salary_to_category(salary):
    if (salary < 50000):
        return "poor"
    elif (salary > 200000):
        return "rich"
    else:
        return "doing okay"

def attempt_get_employer(user_data):
    try:
        return user_data["work"][0]["employer"]["name"]
    except:
        return None

def attempt_get_position(user_data):
    try:
        return user_data["work"][0]["position"]["name"]
    except:
        return None

def attempt_get_role_mean_salary(user_role, employer_data):
    try:
        for role in employer_data["salary"]:
            if role["position"] == user_role:
                return role["mean"]
        return None
    except:
        return None

def attempt_get_company_mean_salary(employer_data):
    try:
        salary = 0
        for role in employer_data["salary"]:
            print "role: " + str(role)
            salary += role["mean"]
        salary /= len(employer_data["salary"])
        return salary
    except:
        return None

def convert_facebook_data_to_salary_category(user_data):
    employer_glassdoor_data = get(user_data['employer'])
    salary = attempt_get_role_mean_salary(user_data['title'], employer_glassdoor_data)
    if salary is not None:
        print "mean salary of role: " + str(salary)
        print "your friend is " + salary_to_category(salary)
    else:
        company_salary = attempt_get_company_mean_salary(employer_glassdoor_data)
        if company_salary is not None:
          print "mean salary of company: " + str(company_salary)
          print "your friend is probably " + salary_to_category(company_salary)
        else:
          print "not enough data is available on your friend"
    print ""

def main():
    from facebook_friend_stalker import get_friend_data
    friend_data = get_friend_data()
    for user_data in friend_data:
        print "user data: " + str(user_data)
        convert_facebook_data_to_salary_category(user_data)

if __name__ == "__main__":
    main()
