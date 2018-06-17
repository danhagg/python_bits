import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):  # creates 1) survey instance 2) list of responses
        """Create a survey and a set of responses for use in all test methods"""
        question = "What language did you first learn?"
        # self prefix means following can be used anywhere in class
        # methods simpler as neither has to make a survey instance or response
        self.my_survey = AnonymousSurvey(question)  # survey instance
        self.responses = ['English', 'French', 'Latin']  #  list of responses

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question = "what language did you first learn to speak"
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test three individual reponses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
