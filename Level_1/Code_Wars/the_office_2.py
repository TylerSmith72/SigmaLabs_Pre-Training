boredom_lookup = {
    "accounts": 1,
    "finance": 2,
    "canteen": 10,
    "regulation": 3,
    "trading": 6,
    "change": 6,
    "IS": 8,
    "retail": 5,
    "cleaning": 4,
    "pissing about": 25
}

def boredom(staff):
    
    boredom_score = sum(boredom_lookup[department] for department in staff.values())
    
    if boredom_score <= 80:
        return "kill me now"
    elif boredom_score < 100 and boredom_score > 80:
        return "i can handle this"
    elif boredom_score >= 100:
        return "party time!!"