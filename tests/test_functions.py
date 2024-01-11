import sys
sys.path.append('../Backend')
import pytest
from main import get_current_number
from unittest.mock import Mock

def test_get_current_number():
  # Create a moc for the Firestore document
    mock_doc = Mock()
    mock_doc.exists = True
    mock_doc.to_dict.return_value = {'count': 5}

   # Create a moc for the Firestore client
    mock_db = Mock()
    mock_db.collection().document().get.return_value = mock_doc

    # Calling a function with mocked up data
    assert get_current_number(mock_db, mock_db.collection().document()) == 5
