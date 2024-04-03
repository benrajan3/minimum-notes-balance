import unittest
from main import balance_change
class TestNotesBalance(unittest.TestCase):
    available_notes = [[100,0],[50,2],[20,5],[10,5],[5,5],[1,5]]
    empty_note = [[100,0],[50,0],[20,0],[10,0],[5,0],[1,0]]
    
    def test_balance(self):

        result = balance_change(95, self.available_notes)
        self.assertEqual(result, [50,20,20,5])

    def test_zero_balance(self):

        result = balance_change(0, self.available_notes)
        self.assertEqual(result, "No balance required to return.")

    def test_empty_note(self):

        result = balance_change(100, self.empty_note)
        self.assertEqual(result, "There is not enough note to return the balance.")
