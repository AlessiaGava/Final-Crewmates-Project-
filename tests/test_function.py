# new_test_pyfile
import unittest
import sys
import os
import volley
import extra_function
import function
import csv_read

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestFunctions(unittest.TestCase):
    """Test case for correct creation and retrieval of
    volleyball players info from the database"""



    '''def test_first_input(self):
        db = csv_read.DataBase()
        print(function.check_player_role(db, "ANGELINA GIULIA"), "The role of ANGELINA GIULIA is SCHIACCIATRICE.")
        self.assertEqual(function.exist_player(db, "EGONU PAOLA"), function.check_player_role(db, "ANGELINA GIULIA"),
                        "The role of ANGELINA GIULIA is SCHIACCIATRICE.")'''

    def test_smoke_function(self):

        """smoke test: valid inputs"""

    db = csv_read.DataBase()

    self.assertEqual(function.check_player_all_stats(db, "ANGELINA GIULIA"),
                     "Team: BANCA VALSABBINA MILLENIUM BRESCIA, Nationality: ITA, B_year: 1997, Role: SCHIACCIATRICE, Height: 192")
    self.assertEqual(function.check_player_height(db, "ANGELINA GIULIA"),
                     "ANGELINA GIULIA is 192 cm tall.")
    self.assertEqual(function.check_player_nationality(db, "ANGELINA GIULIA"),
                     "The nationality of ANGELINA GIULIA is ITA.")
    self.assertEqual(function.check_player_birth(db, "ANGELINA GIULIA"),
                     "The birth year of ANGELINA GIULIA is 1997.")
    self.assertEqual(function.check_player_role(db, "ANGELINA GIULIA"),
                     "The role of ANGELINA GIULIA is SCHIACCIATRICE.")
    self.assertEqual(function.check_player_team(db, "ANGELINA GIULIA"),
                     "ANGELINA GIULIA plays for BANCA VALSABBINA MILLENIUM BRESCIA.")
    self.assertEqual(function.check_team(db, "BANCA VALSABBINA MILLENIUM BRESCIA"),
                     "The players of BANCA VALSABBINA MILLENIUM BRESCIA are: SALA CHIARA, BECHIS MARTA, ANGELINA GIULIA, JASPER MARRIT, PERICATI YLENIA, CVETNIC LEA, PARLANGELI FRANCESCA, BRIDI ULRIKE, BIGANZOLI FEDERICA, BOTEZAT ALEXANDRA, BERTI BEATRICE, VEGLIA TIZIANA, DECORTES CLARA, NICOLETTI ANNA.")


    def test_invalid_inputs_1(self):

        """test invalid inputs"""

        db = csv_read.DataBase()
        test_nobody = "NOBODY"

        self.assertRaises(TypeError, function.check_player_all_stats(db, test_nobody))
        self.assertEqual(function.check_player_height(db, test_nobody),
                         (test_nobody, " is None cm tall."))
        self.assertEqual(function.check_player_nationality(db, test_nobody),
                         ("The nationality of ", test_nobody, " None."))
        self.assertEqual(function.check_player_birth(db, test_nobody),
                         ("The birth year of ", test_nobody, " is None."))
        self.assertEqual(function.check_player_role(db, test_nobody),
                         ("The role of ", test_nobody, " is None."))
        self.assertEqual(function.check_player_team(db, test_nobody),
                         (test_nobody," plays for None."))
        self.assertEqual(function.check_team(db, test_nobody),
                         ("Sorry, we don't know who are the players of ", test_nobody,"."))

    def test_invalid_inputs_2(self):

        """test invalid inputs: integer"""

        db = csv_read.DataBase()
        test_nobody = 3

        self.assertRaises(TypeError, function.check_player_all_stats(db, test_nobody))
        self.assertEqual(function.check_player_height(db, test_nobody),
                         (test_nobody, " is None cm tall."))
        self.assertEqual(function.check_player_nationality(db, test_nobody),
                         ("The nationality of ", test_nobody, " None."))
        self.assertEqual(function.check_player_birth(db, test_nobody),
                         ("The birth year of ", test_nobody, " is None."))
        self.assertEqual(function.check_player_role(db, test_nobody),
                         ("The role of ", test_nobody, " is None."))
        self.assertEqual(function.check_player_team(db, test_nobody),
                         (test_nobody," plays for None."))
        self.assertEqual(function.check_team(db, test_nobody),
                         ("Sorry, we don't know who are the players of ", test_nobody,"."))


    def test_corner_case(self):

        """corner case: empty string"""

        db = csv_read.DataBase()
        test_nobody = ""

        self.assertRaises(TypeError, function.check_player_all_stats(db, test_nobody))
        self.assertEqual(function.check_player_height(db, test_nobody),
                         (test_nobody, " is None cm tall."))
        self.assertEqual(function.check_player_nationality(db, test_nobody),
                         ("The nationality of ", test_nobody, " None."))
        self.assertEqual(function.check_player_birth(db, test_nobody),
                         ("The birth year of ", test_nobody, " is None."))
        self.assertEqual(function.check_player_role(db, test_nobody),
                         ("The role of ", test_nobody, " is None."))
        self.assertEqual(function.check_player_team(db, test_nobody),
                         (test_nobody, " plays for None."))
        self.assertEqual(function.check_team(db, test_nobody),
                         ("Sorry, we don't know who are the players of ", test_nobody, "."))



if __name__ == '__main__':
    # basic test
    # unittest.main()

    # with more details
    unittest.main(verbosity=2)
