import pytest

def test_shouldPrintMessage():
    logger = Logger()
    
    # Test a message that should be printed immediately
    assert logger.shouldPrintMessage(0, "test") == True
    
    # Test a message that shouldn't be printed yet because it was printed within the last 10 seconds
    assert logger.shouldPrintMessage(8, "test") == False
    
    # Test a message that should be printed again after the 10 second threshold has passed
    assert logger.shouldPrintMessage(15, "test") == True
    
    # Test a new message that should be printed immediately
    assert logger.shouldPrintMessage(20, "new test") == True
    
    # Test a message that was previously printed but should now be reprinted due to 10 second threshold
    assert logger.shouldPrintMessage(25, "test") == True
    
    # Test a new message with the same timestamp as a previously printed message
    assert logger.shouldPrintMessage(25, "newer test") == True
    
    # Test a message that shouldn't be printed because it was just printed within 10 seconds
    assert logger.shouldPrintMessage(28, "new test") == False