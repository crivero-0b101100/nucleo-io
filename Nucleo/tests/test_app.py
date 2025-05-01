import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.send_telegram_message')
    def test_webhook_valid_message(self, mock_send):
        """Test webhook endpoint with valid message"""
        test_data = {
            "message": {
                "chat": {"id": 123},
                "text": "hello"
            }
        }
        
        response = self.app.post('/webhook', json=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})
        
        # Verify that send_telegram_message was called with the correct arguments
        mock_send.assert_called_once()
        args = mock_send.call_args[0]
        self.assertEqual(args[0], 123)  # chat_id
        self.assertTrue("Reversed characters:" in args[1])  # response text

    def test_webhook_invalid_data(self):
        """Test webhook endpoint with invalid data"""
        response = self.app.post('/webhook', json={})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json["status"], "error")

    def test_health_endpoint(self):
        """Test health check endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json)

if __name__ == '__main__':
    unittest.main() 