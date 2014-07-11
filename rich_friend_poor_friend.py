import facebook
from glassdoor import get

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

def main():
    oauth_access_token = "CAACEdEose0cBAAWcpqQiNLfU6if4aPDHorjDlHSkwzyEWYHwmZAqyAZAcjwiA3EtNYFF1eDbFiZAVx88JZBKddcZCWZADuI6VTsSBbxgchSlY8pPkgC8KzeeIyCo6qKmhMklR3GBccPCz8t3RZACE1MIKw3LAEuoLHz8qZAkUJ5gggmEdwZCx0sDc4dmkxGQGbbsKOOSa65bDDwZDZD"
    graph = facebook.GraphAPI(oauth_access_token)
    user = graph.get_object("me")
    friends = graph.get_connections(user["id"], "friends")

    for friend in friends["data"]:
        print friend["name"]
        friend_data = graph.get_object(friend["id"])
        current_employer = attempt_get_employer(friend_data)
        if current_employer is not None:
            print "current employer: " + current_employer

            employer_glassdoor_data = get(current_employer)
            salary = attempt_get_role_mean_salary(attempt_get_position(friend_data), employer_glassdoor_data)
            if salary is not None:
                print "mean salary of role: " + str(salary)
            else:
                print "mean salary of company: " + str(attempt_get_company_mean_salary(employer_glassdoor_data))

    print "end"

if __name__ == "__main__":
    main()
