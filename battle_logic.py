def battle_logic(attack, defense, crit=1):
    """
    Calculates total damage based on attack, defense and crit multiplyer
    """
    raw_damage = (attack - defense) * crit
    return max(0, raw_damage)
