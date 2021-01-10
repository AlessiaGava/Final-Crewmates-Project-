from csv_reader.csv_read import DataBase as db #questo è da sistemare


def exist_player(db_manager, volley_player):

    if volley_player in db_manager.get_name():
        return True
    return False


def check_player_all_stats(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        data_al = db_manager.get_all_by_name(volley_player)
        if data_al:
            return f'Team: {data_al[1]}, Nationality: {data_al[6]}, B_year: {data_al[4]}, Role: {data_al[3]}, Height: {data_al[5]}'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'


def check_player_height(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        hg = db_manager.get_height_by_name(volley_player)
        if hg:
            return f'{volley_player} is high {hg}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None


def check_player_nationality(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        nat = db_manager.get_nationality_by_name(volley_player)
        if nat:
            return f'The nationality of {volley_player} is {nat}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None


def check_player_birth(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        bir = db_manager.get_birth_by_name(volley_player)
        if bir:
            return f'The birth date of {volley_player} is {bir}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None


def check_player_role(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        rol = db_manager.get_role_by_name(volley_player)
        if rol:
            return f'The role of {volley_player} is {rol}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None


def check_player_team(db_manager, volley_player):
    """
    """
    if not isinstance(db_manager, db):
        return f'the database was not loaded correctly.'

    if db_manager:
        teams = db_manager.get_team_by_name(volley_player)
        if teams:
            return f'{volley_player} plays for {teams}.'
        else:
            return f'Sorry, {volley_player} does not seem to be a known volley player.'

    return None


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


if __name__ == "__main__":
    play = 'ANGELINA GIULIA'
    team = "Banca Valsabbina Millenium Brescia"
    data = db()

    print(check_team(data, team))
    print(exist_player(data,play))

    print(check_player_all_stats(data, play))
    print(check_player_team(data, play))
    print(check_player_height(data, play))
    print(check_player_nationality(data, play))
    print(check_player_birth(data, play))
    print(check_player_role(data, play))

# wrong names work, everything else doesn't