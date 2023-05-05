
import pytest
from solution import Solution

def test_numUniqueEmails_empty_list():
    s = Solution()
    assert s.numUniqueEmails([]) == 0

def test_numUniqueEmails_only_duplicates():
    s = Solution()
    emails = ['test.email+123@example.com', 'test.email+123@example.com', 'test.email+456@example.com']
    assert s.numUniqueEmails(emails) == 2

def test_numUniqueEmails_no_duplicates():
    s = Solution()
    emails = ['test.email+123@example.com', 'test.email+456@example.com', 'test.email+789@example.com']
    assert s.numUniqueEmails(emails) == 3

def test_numUniqueEmails_invalid_emails():
    s = Solution()
    emails = ['test.email+123@example.com', 'test.email+456@example', 'test.email789@example.com']
    assert s.numUniqueEmails(emails) == 2

def test_numUniqueEmails_mixed_case_emails():
    s = Solution()
    emails = ['Test.Email+123@Example.com', 'test.email+456@EXAMPLE.com', 'TeSt.eMaIl+789@ExAmPlE.CoM']
    assert s.numUniqueEmails(emails) == 3
