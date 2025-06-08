def outed(meet, boss):
    score = 0
    for person, happiness in meet.items():
        if person == boss:
            score += happiness * 2
        else:
            score += happiness
    avg_score = score / len(meet.keys())
    
    if avg_score <= 5:
        return "Get Out Now!"
    else:
        return "Nice Work Champ!"