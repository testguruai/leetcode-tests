
import pytest

class TestSolution:
    def test_fullJustify(self):
        s = Solution()
        words = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
        maxWidth = 30
        expected_output = ["Don't       go       around      ",
                           "saying  the  world  owes  you",
                           "a  living;  the  world  owes",
                           "you nothing; it was here first."]
        assert s.fullJustify(words, maxWidth) == expected_output

        words = ["This", "code", "is", "easy", "to", "test", "with", "pytest"]
        maxWidth = 12
        expected_output = ["This code is",
                           "easy to test",
                           "with pytest"]
        assert s.fullJustify(words, maxWidth) == expected_output

        words = ["Hello"]
        maxWidth = 5
        expected_output = ["Hello"]
        assert s.fullJustify(words, maxWidth) == expected_output

        words = ["Hi", "my", "name", "is", "Python."]
        maxWidth = 10
        expected_output = ["Hi my name",
                           "is Python."]
        assert s.fullJustify(words, maxWidth) == expected_output
        
        words = ["Use", "spaces", "to", "justify", "text."]
        maxWidth = 20
        expected_output = ["Use     spaces     to",
                           "justify      text."]
        assert s.fullJustify(words, maxWidth) == expected_output

