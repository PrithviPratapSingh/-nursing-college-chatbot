#!/usr/bin/env python3
"""
Test script for Nursing College Admission Chatbot
Verifies all requirements are properly implemented
"""

from chatbot import NursingCollegeChatbot

def test_positive_flow():
    """Test the complete positive conversation flow"""
    print("🧪 Testing Positive Flow...")
    chatbot = NursingCollegeChatbot()
    
    # Test responses for positive flow
    test_responses = [
        "yes",  # Admission interest
        "haan",  # Biology check
        "batao",  # Program details
        "tell me",  # Fee structure
        "ok",  # Hostel facilities
        "sure",  # College location
        "interested",  # Recognition
        "more",  # Clinical training
        "what",  # Scholarship
        "kya hai",  # Total seats
        "bilkul"  # Eligibility
    ]
    
    user_id = "test_user_positive"
    
    for i, response in enumerate(test_responses):
        bot_response = chatbot.get_response(user_id, response)
        print(f"Step {i+1}: User: '{response}' -> Bot responds with info")
        
        # Check if we got a meaningful response
        if len(bot_response) < 10:
            print(f"❌ Step {i+1} failed: Response too short")
            return False
    
    print("✅ Positive flow test passed!")
    return True

def test_negative_flow():
    """Test early termination with negative responses"""
    print("\n🧪 Testing Negative Flow...")
    chatbot = NursingCollegeChatbot()
    
    user_id = "test_user_negative"
    
    # Test negative response at admission interest
    response = chatbot.get_response(user_id, "no")
    if "धन्यवाद" in response or "Thank you" in response:
        print("✅ Negative flow test passed!")
        return True
    else:
        print("❌ Negative flow test failed")
        return False

def test_biology_requirement():
    """Test Biology requirement handling"""
    print("\n🧪 Testing Biology Requirement...")
    chatbot = NursingCollegeChatbot()
    
    user_id = "test_user_biology"
    
    # Start conversation
    chatbot.get_response(user_id, "yes")
    
    # Say no to Biology
    response = chatbot.get_response(user_id, "nahi")
    
    if "Biology आवश्यक है" in response:
        print("✅ Biology requirement test passed!")
        return True
    else:
        print("❌ Biology requirement test failed")
        return False

def test_response_detection():
    """Test response detection patterns"""
    print("\n🧪 Testing Response Detection...")
    chatbot = NursingCollegeChatbot()
    
    # Test positive patterns
    positive_patterns = ["haan", "yes", "batao", "tell me", "kya hai", "more", "ok", "sure", "interested", "bilkul", "zaroor"]
    
    for pattern in positive_patterns:
        if not chatbot.is_positive_response(pattern):
            print(f"❌ Failed to detect positive pattern: '{pattern}'")
            return False
    
    # Test negative patterns
    negative_patterns = ["nahi", "no", "not", "dont", "nope", "not interested"]
    
    for pattern in negative_patterns:
        if not chatbot.is_negative_response(pattern):
            print(f"❌ Failed to detect negative pattern: '{pattern}'")
            return False
    
    print("✅ Response detection test passed!")
    return True

def test_required_topics():
    """Test that all required topics are covered"""
    print("\n🧪 Testing Required Topics...")
    chatbot = NursingCollegeChatbot()
    
    user_id = "test_user_topics"
    
    # Go through complete flow and collect responses
    responses = []
    test_inputs = ["yes", "haan", "batao", "tell me", "ok", "sure", "interested", "more", "what", "kya hai", "bilkul"]
    
    for user_input in test_inputs:
        response = chatbot.get_response(user_id, user_input)
        responses.append(response)
    
    # Check for required topics
    required_topics = [
        "admission",  # Initial admission interest
        "Biology",  # Biology requirement
        "B.Sc Nursing",  # Program details
        "₹60,000",  # Fee structure
        "hostel",  # Hostel facilities
        "Delhi",  # College location
        "Indian Nursing Council",  # Recognition
        "Hospital",  # Clinical training
        "Scholarship",  # Scholarship options
        "60 seats",  # Total seats
        "PNT Exam"  # Eligibility criteria
    ]
    
    all_responses = " ".join(responses)
    missing_topics = []
    
    for topic in required_topics:
        if topic.lower() not in all_responses.lower():
            missing_topics.append(topic)
    
    if missing_topics:
        print(f"❌ Missing topics: {missing_topics}")
        return False
    else:
        print("✅ All required topics covered!")
        return True

def test_fee_structure():
    """Test detailed fee structure"""
    print("\n🧪 Testing Fee Structure...")
    chatbot = NursingCollegeChatbot()
    
    user_id = "test_user_fees"
    
    # Navigate to fee structure
    chatbot.get_response(user_id, "yes")  # Admission interest
    chatbot.get_response(user_id, "haan")  # Biology
    chatbot.get_response(user_id, "batao")  # Program details
    
    response = chatbot.get_response(user_id, "tell me")
    
    # Check for required fee information
    required_fees = [
        "₹60,000",  # Tuition fee
        "₹10,000",  # Bus fee
        "₹70,000",  # Total annual fees
        "₹30,000",  # 1st installment
        "₹20,000",  # 2nd installment
        "₹20,000"   # 3rd installment
    ]
    
    missing_fees = []
    for fee in required_fees:
        if fee not in response:
            missing_fees.append(fee)
    
    if missing_fees:
        print(f"❌ Missing fee information: {missing_fees}")
        return False
    else:
        print("✅ Fee structure test passed!")
        return True

def main():
    """Run all tests"""
    print("🚀 Starting Nursing College Chatbot Tests\n")
    
    tests = [
        test_positive_flow,
        test_negative_flow,
        test_biology_requirement,
        test_response_detection,
        test_required_topics,
        test_fee_structure
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The chatbot meets all requirements.")
    else:
        print("⚠️ Some tests failed. Please check the implementation.")
    
    return passed == total

if __name__ == "__main__":
    main() 