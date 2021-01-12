import unittest
import xls_reader.function as function
import xls_reader.xls_read as xls_read


class TestFunctions(unittest.TestCase):
    """
    Class that tests the functions of the function.py file.
    It verifies the correct retrieval of the volleyball players info from the database, and consequently
    checks that the database had been created correctly.
    It runs three kinds of tests:
    1. Smoke test;
    2. Invalid inputs test;
    3. Corner case test.

    :return: Returns an error message if the test fails
    :rtype: String
    """

    # file path
    _fp = ""

    def test_smoke_function(self):
        """
        Smoke test: tests the expected outcome of the valid inputs given to the functions.

        :return: Returns an error message if the test fails
        :rtype: String
        """

        db = xls_read.DataBase(self._fp)

        #print(function.check_player_all_stats(db, "ANGELINA GIULIA"))

        self.assertEqual(function.check_player_all_stats(db, "ANGELINA GIULIA")
                         , "Team: BANCA VALSABBINA MILLENIUM BRESCIA, Nationality: ITA, B_year: 1997, Role: "
                           "SCHIACCIATRICE, Height: 192")
        self.assertEqual(function.check_player_height(db, "ANGELINA GIULIA")
                         , "ANGELINA GIULIA is 192 cm tall.")
        self.assertEqual(function.check_player_nationality(db, "ANGELINA GIULIA")
                         , "The nationality of ANGELINA GIULIA is ITA.")
        self.assertEqual(function.check_player_birth(db, "ANGELINA GIULIA")
                         , "The birth year of ANGELINA GIULIA is 1997.")
        self.assertEqual(function.check_player_role(db, "ANGELINA GIULIA")
                         , "The role of ANGELINA GIULIA is SCHIACCIATRICE.")
        self.assertEqual(function.check_player_team(db, "ANGELINA GIULIA")
                         , "ANGELINA GIULIA plays for BANCA VALSABBINA MILLENIUM BRESCIA.")
        self.assertEqual(function.check_team(db, "BANCA VALSABBINA MILLENIUM BRESCIA")
                         , "The players of BANCA VALSABBINA MILLENIUM BRESCIA are: SALA CHIARA, BECHIS MARTA, "
                           "ANGELINA GIULIA, JASPER MARRIT, PERICATI YLENIA, CVETNIC LEA, PARLANGELI FRANCESCA, "
                           "BRIDI ULRIKE, BIGANZOLI FEDERICA, BOTEZAT ALEXANDRA, BERTI BEATRICE, VEGLIA TIZIANA, "
                           "DECORTES CLARA, NICOLETTI ANNA.")

    def test_invalid_inputs_1(self):
        """
        Test invalid inputs: tests the expected outcome of the invalid inputs given to the functions.
        The functions should return a message containing None.

        :return: Returns an error message if the test fails
        :rtype: String
        """

        db = xls_read.DataBase(self._fp)
        test_nobody = "NOBODY"

        #print(function.check_player_all_stats(db, test_nobody))

        self.assertRaises(TypeError, function.check_player_all_stats(db, test_nobody))
        self.assertEqual(function.check_player_height(db, test_nobody)
                         , (test_nobody + " is None cm tall."))
        self.assertEqual(function.check_player_nationality(db, test_nobody)
                         , ("The nationality of " + test_nobody + " is None."))
        self.assertEqual(function.check_player_birth(db, test_nobody)
                         , ("The birth year of " + test_nobody + " is None."))
        self.assertEqual(function.check_player_role(db, test_nobody)
                         , ("The role of " + test_nobody + " is None."))
        self.assertEqual(function.check_player_team(db, test_nobody)
                         , (test_nobody + " plays for None."))
        self.assertEqual(function.check_team(db, test_nobody)
                         , ("Sorry, we don't know who are the players of " + test_nobody + "."))

    def test_corner_case(self):
        """
        Corner case: tests the expected outcome of the corner case empty string given to the functions.
        The functions should return a message containing None.
        The test for the function "check_player_all_stats" passes if it raises a TypeError.

        :return: Returns an error message if the test fails
        :rtype: String
        """

        db = xls_read.DataBase(self._fp)
        test_nobody = ""

        self.assertRaises(TypeError, function.check_player_all_stats(db, test_nobody))
        self.assertEqual(function.check_player_height(db, test_nobody)
                         , (test_nobody + " is None cm tall."))
        self.assertEqual(function.check_player_nationality(db, test_nobody)
                         , ("The nationality of " + test_nobody + " is None."))
        self.assertEqual(function.check_player_birth(db, test_nobody)
                         , ("The birth year of " + test_nobody + " is None."))
        self.assertEqual(function.check_player_role(db, test_nobody)
                         , ("The role of " + test_nobody + " is None."))
        self.assertEqual(function.check_player_team(db, test_nobody)
                         , (test_nobody + " plays for None."))
        self.assertEqual(function.check_team(db, test_nobody)
                         , ("Sorry, we don't know who are the players of " + test_nobody + "."))


# to try the test locally
if __name__ == '__main__':
    TestFunctions._fp = "C:\\Users\\Alessia\\PycharmProjects\\volleyproject\\Data\\dataset_volley.xls"
    unittest.main()
