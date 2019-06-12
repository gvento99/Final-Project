import classifier
import pytest

def test_altered_find_in_list():
    """Tests the return of comparing two lists."""
    
    list1 = ["a","b","c","d","e"]
    list2 = ["c","e","g","z","z","t","p"]
    assert classifier.altered_find_in_list(list1,list2) == ["c","e"]
    
    list1 = []
    list2 = ["a","b","c"]
    assert classifier.altered_find_in_list(list1,list2) == []
    
    list1 = ["a","b","c","d"]
    list2 = ["e","f","g","h"]
    assert classifier.altered_find_in_list(list1,list2) == []
    
    list1 = ["a","b","c","d","e"]
    list2 = ["a","b","c","d","e"]
    assert classifier.altered_find_in_list(list1,list2) == ["a","b","c","d","e" ]
    
def test_enter_evaluater():
    """Tests the return of whether or not the keyword to enter another feature is present."""
    
    in1 = ["evaluateme"]
    assert classifier.enter_evaluater(in1) == True
    
    in1 = ["noword"]
    assert classifier.enter_evaluater(in1) == False
    
    in1 = ["noword", "noword", "noword", "evaluateme"]
    assert classifier.enter_evaluater(in1) == True
    
    in1 = []
    assert classifier.enter_evaluater(in1) == False
    
    in1 = ["EvaluateME"]
    assert classifier.enter_evaluater(in1) == False
