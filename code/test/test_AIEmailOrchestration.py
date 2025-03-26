import pytest
import pandas as pd
from AIEmailOrchestration import classify_email, extract_data_from_email, detect_duplicates, process_email

# Mock OpenAI API response
def mock_classify_email(email_text):
    return "Closing Notice: Reallocation Fees"

# Test email classification
def test_classify_email(monkeypatch):
    monkeypatch.setattr("AIEmailOrchestration.classify_email", mock_classify_email)
    
    email_text = "We need to process a reallocation fee for the closing notice."
    result = classify_email(email_text)
    assert result == "Closing Notice: Reallocation Fees"

# Test field extraction from email
def test_extract_data_from_email():
    email_text = "Deal Name: ABC123\nAmount: $100,000\nExpiration Date: 12/31/2025"
    result = extract_data_from_email(email_text, [])
    
    assert result["deal_name"] == "ABC123"
    assert result["amount"] == "100,000"
    assert result["expiration_date"] == "12/31/2025"

# Test duplicate detection
def test_detect_duplicates():
    email_text = "We would like a closing notice for deal ABC123."
    email_thread = "Re: Closing Notice Request"
    past_emails_df = pd.DataFrame({"email_content": ["We would like a closing notice for deal ABC123."]})

    is_duplicate, reason = detect_duplicates(email_text, email_thread, past_emails_df)
    
    assert is_duplicate is True
    assert reason == "Duplicate email detected"

# Test full email processing
def test_process_email(monkeypatch):
    monkeypatch.setattr("AIEmailOrchestration.classify_email", mock_classify_email)
    
    email_text = "We need a closing notice for deal ABC123, with an amount of $100,000 and expiration date 12/31/2025."
    email_thread = "Re: Closing Notice Request"
    past_emails_df = pd.DataFrame({"email_content": ["We need a closing notice for deal ABC123."]})

    result = process_email(email_text, [], email_thread, past_emails_df)

    assert result["classified_request"] == "Closing Notice: Reallocation Fees"
    assert result["extracted_fields"]["deal_name"] == "ABC123"
    assert result["extracted_fields"]["amount"] == "100,000"
    assert result["extracted_fields"]["expiration_date"] == "12/31/2025"
    assert result["is_duplicate"] is True

if __name__ == "__main__":
    pytest.main()
