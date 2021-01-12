from xls_read import DataBase


def exist_db(my_db):
    """
    This function checks if the database has been created.

    :param my_db: the database
    :type my_db: Object
    :return: True or False
    :rtype: Boolean
    """
    if not isinstance(my_db, DataBase):
        return False
    return True


def exist_player(my_db, volley_player):
    """
    This function checks if the name of the volleyball player exists in the database.

    :param my_db: the database
    :type my_db: Object
    :param volley_player: name of the player
    :type volley_player: String
    :return: True or False
    :rtype: Boolean
    """
    if volley_player in my_db.get_name():
        return True
    return False


def check_player_all_stats(my_db, volley_player):
    """
    This function returns all the info about a volleyball player.

    :param my_db: the database
    :type my_db: Object
    :param volley_player: name of the player
    :type volley_player: String
    :return: all the info about the volleyball player
    :rtype: String
    """
    data_al = my_db.get_all_by_name(volley_player)
    if not data_al:
        return None
    return f'Team: {data_al[1]}, Nationality: {data_al[6]}, B_year: {data_al[4]}, Role: {data_al[3]}, ' \
           f'Height: {data_al[5]}'


def check_player_height(my_db, volley_player):
    """
    This function, given the database and the name of the volleyball player, returns her height using the method
    get_height_by_name of the my_db object.

    :param my_db: the database
    :type my_db: Object
    :param volley_player: name of the player
    :type volley_player: String
    :return: the height of the volleyball player
    :rtype: String
    """
    hg = my_db.get_height_by_name(volley_player)
    return f'{volley_player} is {hg} cm tall.'


def check_player_nationality(my_db, volley_player):
    """
    This function, given the database and the name of the volleyball player, returns her nationality using the method
    get_nationality_by_name of the my_db object.

    :param my_db: the database
    :type my_db: Object
    :param volley_player: name of the player
    :type volley_player: String
    :return: the nationality of the volleyball player
    :rtype: String
    """
    nat = my_db.get_nationality_by_name(volley_player)
    return f'The nationality of {volley_player} is {nat}.'


def check_player_birth(my_db, volley_player):
    """
    This function, given the database and the name of the volleyball player, returns her year of birth using the method
    get_birth_by_name of the my_db object.

    :param my_db: the database
    :type my_db: Object
    :param volley_player: name of the player
    :type volley_player: String
    :return:the year of birth of the volleyball player
    :rtype: String
    """
    bir = my_db.get_birth_by_name(volley_player)
    return f'The birth year of {volley_player} is {bir}.'


def check_player_role(my_db, volley_player):
    """
    This function, given the database and the name of the volleyball player, returns her role using the method
    get_role_by_name of the my_db object.

    :param my_db: the database
    :type my_db: Object
    :param volley_player: name of the player
    :type volley_player: String
    :return: the role of the volleyball player
    :rtype: String
    """
    rol = my_db.get_role_by_name(volley_player)
    return f'The role of {volley_player} is {rol}.'


def check_player_team(my_db, volley_player):
    """
    This function, given the database and the name of the volleyball player, returns her team using the method
    get_team_by_name of the my_db object.

    :param my_db: the database
    :type my_db: Object
    :param volley_player: name of the player
    :type volley_player: String
    :return: the team of the volleyball player
    :rtype: String
    """
    teams = my_db.get_team_by_name(volley_player)
    return f'{volley_player} plays for {teams}.'


def check_team(my_db, team_name):
    """
    This function, given the database and the name of the volleyball team, returns its members using the method
    get_player_by_team of the my_db object.

    :param my_db: the database
    :type my_db: Object
    :param team_name: name of the team
    :type team_name: String
    :return: the members of the volleyball team
    :rtype: String
    """
    players = my_db.get_player_by_team(team_name)
    if players:
        return f'The players of {team_name} are: {", ".join(x[0] for x in players)}.'
    return f"Sorry, we don't know who are the players of {team_name}."


if __name__ == "__main__":
    play = 'ANGELINA GIULIA'
    #play = 'NOBODY'
    team = 'BANCA VALSABBINA MILLENIUM BRESCIA'
    data = DataBase("C:\\Users\\Alessia\\PycharmProjects\\volleyproject\\Data\\dataset_volley.xlsx")

    print(check_team(data, team))
    print(check_player_all_stats(data, play))
    print(check_player_team(data, play))
    print(check_player_height(data, play))
    print(check_player_nationality(data, play))
    print(check_player_birth(data, play))
    print(check_player_role(data, play))
