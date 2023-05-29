import unittest
from unittest.mock import patch
from main import countdown

class CountdownTest(unittest.TestCase):

    def test_countdown(self):
        with patch('builtins.print') as mock_print:
            with patch('time.sleep') as mock_sleep:
                t = 5
                countdown(t)
                mock_sleep.assert_called_with(1) #verifica se o sleep foi chamado com o valor correto
                self.assertEqual(mock_sleep.call_count, t) #verifica se o sleep foi chamado a quantidade correta de vezes
                self.assertEqual(mock_print.call_count, t + 1) #verifica se o print foi chamado a quantidade correta de vezes

    def test_countdown_zero_time(self):
        with patch('builtins.print') as mock_print:
            with patch('time.sleep') as mock_sleep:
                t = 0
                countdown(t)
                mock_sleep.assert_not_called() # verifica se o sleep não foi chamado
                self.assertEqual(mock_print.call_count, 2) #verifica se o print foi chamado duas vezes('00:00' e Timer Complete) 

    def test_countdown_negative_time(self):
        with patch('builtins.print') as mock_print:
            with patch('time.sleep') as mock_sleep:
                t = -5
                countdown(t)
                mock_sleep.assert_not_called() #Verifica se o sleep não foi chamado
                # verifica se o print foi chamado duas vezes ('00:00' e 'Timer Complete')


    def test_countdown_print_output(self):
        with patch('builtins.print') as mock_print:
            with patch('time.sleep') as mock_sleep:
                t = 3
                countdown(t)
                expected_output = [
                    mock_print.call_args_list[i][0][0] for i in range(t + 1)
                ]
                self.assertEqual(
                    expected_output,
                    ['00:03', '00:02', '00:001', '00:00', 'Timer Completed']
                )


if __name__ == '__main__':
    unittest.main