import unittest

import mbti_personality_function

collected_responses = mbti_personality_function.response_collection()


class TestThatMbtiPersonalityFunctionsWorkCorrectly(unittest.TestCase):


    def test_twenty_responses_are_collected(self):
    
        self.assertTrue(len(collected_responses) == 20)
        
    def test_for_choices_and_count_of_responses_of_extrovert_vs_introvert_questions(self):
    
        expected = mbti_personality_function.extroverted_introverted_personality(collected_responses)
        actual = [['A.expend energy, enjoy groups', 'A.more outgoing, think out loud', 'A.seek many tasks, public activities, interaction with others', 'A.external, communicative, express yourself', 'A.active, initiate'], 5, 0]

        self.assertEqual(expected, actual)
        
    def test_for_choices_and_count_of_responses_of_sensing_vs_intuition_questions(self):
    
        expected = mbti_personality_function.sensing_vs_intuitive_personality(collected_responses)
        actual = [['A.Interpret literally', 'A.practical, realistic, experiential', 'A.standard, usual, conventional', 'A.focus on here-and-now', 'A.facts, things, what is'], 5, 0]

        self.assertEqual(expected, actual)
        
    def test_for_choices_and_count_of_responses_of_thinking_vs_feeling_questions(self):
    
        expected = mbti_personality_function.thinking_vs_feeling_personality(collected_responses)
        actual = [['B.empathetic, feeling, accommodating', 'B.tactful, kind, encouraging', 'B.gentle, tend to appreciate, conciliate', 'B.tender-hearted, merciful', 'B.sensitive, people-oriented, compassionate'], 0, 5]

        self.assertEqual(expected, actual)
        
    def test_for_choices_and_count_of_responses_of_judging_vs_perceptive_questions(self):
    
        expected = mbti_personality_function.judging_vs_perceptive_personality(collected_responses)
        actual = [['B.flexible, adaptable', 'B.unplanned, spontaneous', 'B.easy-going, live and let live', 'B.go with the flow, adapt as you go', 'B.latitude, freedom'], 0, 5]


        self.assertEqual(expected, actual)
        
        
