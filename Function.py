from csv_reader.csv_read import DataBase as db

#to be completed
def check_player_all_stats(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        teams = db_manager.get_all_by_name(volley_player)
        if teams:
            return
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

#check player, if it is in the database, gives back her height
def check_player_height(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        hg = db_manager.get_height_by_name(volley_player)
        if hg:
            return f'{volley_player} is high {hg[0]}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None

#check player, if it is in the database, gives back her nationality
def check_player_nationality(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        nat = db_manager.get_nationality_by_name(volley_player)
        if nat:
            return f'The nationality of {volley_player} is {nat[0]}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None

#check player, if it is in the database, gives back her birthday
def check_player_birth(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        bir = db_manager.get_birth_by_name(volley_player)
        if bir:
            return f'The birth date of {volley_player} is {bir[0]}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None

#check player, if it is in the database, gives back her role
def check_player_role(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        rol = db_manager.get_role_by_name(volley_player)
        if rol:
            return f'The birth date of {volley_player} is {rol[0]}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None

#check player, if it is in the database, gives back her team
def check_player_team(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        teams = db_manager.get_team_by_name(volley_player)
        if teams:
            return f'{volley_player} plays for {teams[0]}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None

#check team, if it is in the database, gives back its members
def check_team(db_manager, team_name):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        players = db_manager.get_player_by_team(team_name)

        if players:
            return f'The volley players of {team_name} are: {", ".join(x[0] for x in players)}.'
        return f"Sorry, we don't know who are the players of {team_name}."

    return None

if __name__ == '__main__':
    print(ce)
