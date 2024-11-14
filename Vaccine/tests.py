import unittest
from unittest.mock import patch, MagicMock
from vaccine import vaccine

class TestVaccineJuiceShop(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('requests.get')
    def test_injection_on_juice_shop_products(self, mock_get, mock_open):
        """
        Test SQL injection on Juice Shop's product search endpoint (GET).
        """
        # Mock a successful response from the server
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {'X-Powered-By': 'Express'}
        mock_response.text = 'Mock response text'
        mock_get.return_value = mock_response

        # Create instance of the vaccine class
        v = vaccine()

        # Set up Juice Shop's search endpoint
        v.url = 'http://localhost:3000/rest/products/search?searchTerm='
        v.methode = 'GET'
        v.outputfile = 'output.txt'

        # Mocking payloads that will be tested
        with patch('utils.payloads.injections_payloads', ["' OR 1=1--", "'; DROP TABLE users--"]):
            v.send_request()

        # Check if the GET requests were attempted
        mock_get.assert_called()  # Ensure GET was called
        mock_open().write.assert_called()  # Ensure that some response was written

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('requests.post')
    def test_injection_on_juice_shop_register(self, mock_post, mock_open):
        """
        Test SQL injection on Juice Shop's user registration endpoint (POST).
        """
        # Mock a successful response from the server
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {'X-Powered-By': 'Express'}
        mock_response.text = 'Mock response text'
        mock_post.return_value = mock_response

        # Create instance of the vaccine class
        v = vaccine()

        # Set up Juice Shop's user registration endpoint
        v.url = 'http://localhost:3000/rest/user/register'
        v.methode = 'POST'
        v.outputfile = 'output.txt'

        # Mocking payloads that will be tested
        with patch('utils.payloads.register_payloads', [
            {'email': "test@test.com", 'password': "' OR 1=1--"},
            {'email': "test@test.com", 'password': "'; DROP TABLE users--"}
        ]):
            v.send_request()

        # Check if the POST requests were attempted
        mock_post.assert_called()  # Ensure POST was called
        mock_open().write.assert_called()  # Ensure that some response was written

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('requests.get')
    def test_detect_database_on_juice_shop(self, mock_get, mock_open):
        """
        Test if the database detection works with Juice Shop's response headers.
        """
        # Mock a successful response from the server
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.headers = {'X-Powered-By': 'PostgreSQL'}
        mock_response.text = 'Mock response text'
        mock_get.return_value = mock_response

        # Create instance of the vaccine class
        v = vaccine()

        # Set up Juice Shop's version endpoint (example)
        v.url = 'http://localhost:3000/rest/admin/application-configuration'
        v.methode = 'GET'
        v.outputfile = 'output.txt'

        # Run the request to check for database headers
        v.send_request()

        # Ensure that file writing occurred (mock_open ensures we're not writing to disk)
        mock_open().write.assert_called_with('PostgreSQL database found\n')  # Check if the correct database was detected

if __name__ == '__main__':
    unittest.main()
