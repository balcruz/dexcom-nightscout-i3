import unittest
from nightscout import Nightscout
from unittest.mock import patch


class TestNightscout(unittest.TestCase):
    @patch("requests.get")
    def test_pull_entries(self, mock_get):
        # Mock the response from the Nightscout API
        mock_get.return_value.json.return_value = [
            {"dateString": "2024-08-12 12:00", "sgv": 120},
            {"dateString": "2024-08-12 12:05", "sgv": 125},
        ]
        mock_get.return_value.status_code = 200

        nightscout = Nightscout(
            host="mock_nightscout_url",
            api_token="test-token",
            timezone="America/Montevideo",
        )
        entries = nightscout.pull_last_entry()

        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["sgv"], 120)
        self.assertEqual(entries[1]["sgv"], 125)


if __name__ == "__main__":
    unittest.main()
