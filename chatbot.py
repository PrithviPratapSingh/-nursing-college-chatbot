import json
import re
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class ConversationState(Enum):
    INITIAL = "initial"
    ADMISSION_INTEREST = "admission_interest"
    BIOLOGY_CHECK = "biology_check"
    PROGRAM_DETAILS = "program_details"
    FEE_STRUCTURE = "fee_structure"
    HOSTEL_FACILITIES = "hostel_facilities"
    COLLEGE_LOCATION = "college_location"
    RECOGNITION = "recognition"
    CLINICAL_TRAINING = "clinical_training"
    SCHOLARSHIP = "scholarship"
    TOTAL_SEATS = "total_seats"
    ELIGIBILITY = "eligibility"
    END = "end"

@dataclass
class UserSession:
    user_id: str
    state: ConversationState
    responses: Dict[str, str]
    biology_studied: Optional[bool] = None
    admission_interested: Optional[bool] = None
    language: Optional[str] = None  # 'hi' for Hindi, 'en' for English

class NursingCollegeChatbot:
    def __init__(self):
        self.sessions: Dict[str, UserSession] = {}
        
    def get_session(self, user_id: str) -> UserSession:
        if user_id not in self.sessions:
            self.sessions[user_id] = UserSession(
                user_id=user_id,
                state=ConversationState.INITIAL,
                responses={}
            )
        return self.sessions[user_id]
    
    def detect_language(self, text: str) -> str:
        """Detect if the text is in Hindi (Devanagari script) or English."""
        # Check for any Devanagari character
        if any('\u0900' <= c <= '\u097F' for c in text):
            return 'hi'
        return 'en'
    
    def is_positive_response(self, text: str) -> bool:
        """Check if user response is positive"""
        positive_patterns = [
            r'\b(haan|yes|batao|tell me|kya hai|what|more|ok|okay|sure|bilkul|zaroor)\b',
            r'\b(interested|want|like|good|great|fine|alright)\b'
        ]
        text_lower = text.lower().strip()
        
        for pattern in positive_patterns:
            if re.search(pattern, text_lower):
                return True
        return False
    
    def is_negative_response(self, text: str) -> bool:
        """Check if user response is negative"""
        negative_patterns = [
            r'\b(nahi|no|not|dont|don\'t|na|nope)\b',
            r'\b(not interested|no thanks|no thank you)\b'
        ]
        text_lower = text.lower().strip()
        
        for pattern in negative_patterns:
            if re.search(pattern, text_lower):
                return True
        return False
    
    def get_response(self, user_id: str, user_message: str) -> str:
        session = self.get_session(user_id)
        lang = self.detect_language(user_message)
        session.language = lang
        
        # Handle initial greeting
        if session.state == ConversationState.INITIAL:
            session.state = ConversationState.ADMISSION_INTEREST
            return self.get_admission_interest_message(lang)
        
        # Handle admission interest
        elif session.state == ConversationState.ADMISSION_INTEREST:
            if self.is_positive_response(user_message):
                session.admission_interested = True
                session.state = ConversationState.BIOLOGY_CHECK
                return self.get_biology_check_message(lang)
            elif self.is_negative_response(user_message):
                session.admission_interested = False
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('admission_interest', lang)
        
        # Handle biology check
        elif session.state == ConversationState.BIOLOGY_CHECK:
            if self.is_positive_response(user_message):
                session.biology_studied = True
                session.state = ConversationState.PROGRAM_DETAILS
                return self.get_program_details_message(lang)
            elif self.is_negative_response(user_message):
                session.biology_studied = False
                return self.get_biology_required_message(lang)
            else:
                return self.get_clarification_message('biology_check', lang)
        
        # Handle program details
        elif session.state == ConversationState.PROGRAM_DETAILS:
            if self.is_positive_response(user_message):
                session.state = ConversationState.FEE_STRUCTURE
                return self.get_fee_structure_message(lang)
            elif self.is_negative_response(user_message):
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('program_details', lang)
        
        # Handle fee structure
        elif session.state == ConversationState.FEE_STRUCTURE:
            if self.is_positive_response(user_message):
                session.state = ConversationState.HOSTEL_FACILITIES
                return self.get_hostel_facilities_message(lang)
            elif self.is_negative_response(user_message):
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('fee_structure', lang)
        
        # Handle hostel facilities
        elif session.state == ConversationState.HOSTEL_FACILITIES:
            if self.is_positive_response(user_message):
                session.state = ConversationState.COLLEGE_LOCATION
                return self.get_college_location_message(lang)
            elif self.is_negative_response(user_message):
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('hostel_facilities', lang)
        
        # Handle college location
        elif session.state == ConversationState.COLLEGE_LOCATION:
            if self.is_positive_response(user_message):
                session.state = ConversationState.RECOGNITION
                return self.get_recognition_message(lang)
            elif self.is_negative_response(user_message):
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('college_location', lang)
        
        # Handle recognition
        elif session.state == ConversationState.RECOGNITION:
            if self.is_positive_response(user_message):
                session.state = ConversationState.CLINICAL_TRAINING
                return self.get_clinical_training_message(lang)
            elif self.is_negative_response(user_message):
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('recognition', lang)
        
        # Handle clinical training
        elif session.state == ConversationState.CLINICAL_TRAINING:
            if self.is_positive_response(user_message):
                session.state = ConversationState.SCHOLARSHIP
                return self.get_scholarship_message(lang)
            elif self.is_negative_response(user_message):
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('clinical_training', lang)
        
        # Handle scholarship
        elif session.state == ConversationState.SCHOLARSHIP:
            if self.is_positive_response(user_message):
                session.state = ConversationState.TOTAL_SEATS
                return self.get_total_seats_message(lang)
            elif self.is_negative_response(user_message):
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('scholarship', lang)
        
        # Handle total seats
        elif session.state == ConversationState.TOTAL_SEATS:
            if self.is_positive_response(user_message):
                session.state = ConversationState.ELIGIBILITY
                return self.get_eligibility_message(lang)
            elif self.is_negative_response(user_message):
                session.state = ConversationState.END
                return self.get_end_message(lang)
            else:
                return self.get_clarification_message('total_seats', lang)
        
        # Handle eligibility
        elif session.state == ConversationState.ELIGIBILITY:
            session.state = ConversationState.END
            return self.get_final_message(lang)
        
        # Handle end state
        elif session.state == ConversationState.END:
            return self.get_end_message(lang)
        
        return self.get_default_message(lang)

    # Message methods now accept lang ('hi' or 'en') and return the appropriate version
    def get_admission_interest_message(self, lang: str) -> str:
        if lang == 'hi':
            return "नमस्ते! 👋\n\nक्या आप Nursing College में admission लेना चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "Hello! 👋\n\nAre you interested in admission to the Nursing College?\n\n(Please respond with 'Yes' or 'No')"

    def get_biology_check_message(self, lang: str) -> str:
        if lang == 'hi':
            return "बहुत अच्छा! \n\nक्या आपने 12th में Biology पढ़ी है?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "Great!\n\nDid you study Biology in 12th grade?\n\n(Please respond with 'Yes' or 'No')"

    def get_biology_required_message(self, lang: str) -> str:
        if lang == 'hi':
            return "B.Sc Nursing में admission के लिए Biology आवश्यक है।"
        else:
            return "Biology is mandatory for admission to B.Sc Nursing."

    def get_program_details_message(self, lang: str) -> str:
        if lang == 'hi':
            return "B.Sc Nursing Program के बारे में जानकारी:\n\n🎓 **B.Sc Nursing Program**\n- यह एक full-time program है\n- 4 साल का undergraduate course\n- Practical training के साथ theoretical knowledge\n- Real patients के साथ hands-on experience\n\nक्या आप program के बारे में और जानकारी चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "About the B.Sc Nursing Program:\n\n🎓 **B.Sc Nursing Program**\n- This is a full-time program\n- 4-year undergraduate course\n- Theoretical knowledge with practical training\n- Hands-on experience with real patients\n\nWould you like more information about the program?\n\n(Please respond with 'Yes' or 'No')"

    def get_fee_structure_message(self, lang: str) -> str:
        if lang == 'hi':
            return "💰 **Fee Structure:**\n\n**Annual Fees Breakdown:**\n- Tuition Fee: ₹60,000 INR\n- Bus Fee: ₹10,000 INR\n- **Total Annual Fees: ₹70,000 INR**\n\n**Installment Plan:**\n- 1st Installment: ₹30,000 (admission के समय)\n- 2nd Installment: ₹20,000 (first semester के बाद)\n- 3rd Installment: ₹20,000 (second semester के बाद)\n\nक्या आप hostel facilities के बारे में जानना चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "💰 **Fee Structure:**\n\n**Annual Fees Breakdown:**\n- Tuition Fee: ₹60,000 INR\n- Bus Fee: ₹10,000 INR\n- **Total Annual Fees: ₹70,000 INR**\n\n**Installment Plan:**\n- 1st Installment: ₹30,000 (at the time of admission)\n- 2nd Installment: ₹20,000 (after the first semester)\n- 3rd Installment: ₹20,000 (after the second semester)\n\nWould you like to know about hostel facilities?\n\n(Please respond with 'Yes' or 'No')"

    def get_hostel_facilities_message(self, lang: str) -> str:
        if lang == 'hi':
            return "🏠 **Hostel Facilities:**\n\n**Accommodation:**\n- 4x7 water and electricity supply\n- CCTV surveillance for security\n- On-site warden available\n\n**Training Facilities:**\n- Hospital training included\n- Real patients के साथ practical training\n- Professional medical environment\n\nक्या आप college location के बारे में जानना चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "🏠 **Hostel Facilities:**\n\n**Accommodation:**\n- 4x7 water and electricity supply\n- CCTV surveillance for security\n- On-site warden available\n\n**Training Facilities:**\n- Hospital training included\n- Practical training with real patients\n- Professional medical environment\n\nWould you like to know about the college location?\n\n(Please respond with 'Yes' or 'No')"

    def get_college_location_message(self, lang: str) -> str:
        if lang == 'hi':
            return "📍 **College Location:**\n\nहमारा college Delhi में स्थित है।\n\nक्या आप location या surrounding area के बारे में और जानकारी चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "📍 **College Location:**\n\nOur college is located in Delhi.\n\nWould you like to know more about the location or surrounding area?\n\n(Please respond with 'Yes' or 'No')"

    def get_recognition_message(self, lang: str) -> str:
        if lang == 'hi':
            return "🏛️ **Recognition & Accreditation:**\n\nहमारा college officially recognized है:\n- **Indian Nursing Council (INC)** (Delhi) द्वारा\n\nक्या आप clinical training locations के बारे में जानना चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "🏛️ **Recognition & Accreditation:**\n\nOur college is officially recognized by:\n- **Indian Nursing Council (INC)** (Delhi)\n\nWould you like to know about clinical training locations?\n\n(Please respond with 'Yes' or 'No')"

    def get_clinical_training_message(self, lang: str) -> str:
        if lang == 'hi':
            return "🏥 **Clinical Training Locations:**\n\nहमारे students इन locations पर training करते हैं:\n\n- District Hospital (Backundpur)\n- Community Health Centers\n- Regional Hospital (Chartha)\n- Ranchi Neurosurgery and Allied Science Hospital (Ranchi, Jharkhand)\n\nक्या आप scholarship options के बारे में जानना चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "🏥 **Clinical Training Locations:**\n\nOur students receive training at the following locations:\n\n- District Hospital (Backundpur)\n- Community Health Centers\n- Regional Hospital (Chartha)\n- Ranchi Neurosurgery and Allied Science Hospital (Ranchi, Jharkhand)\n\nWould you like to know about scholarship options?\n\n(Please respond with 'Yes' or 'No')"

    def get_scholarship_message(self, lang: str) -> str:
        if lang == 'hi':
            return "🎓 **Scholarship Options:**\n\nAvailable scholarships:\n- **Government Post-Matric Scholarship:** ₹18k-₹23k\n- **Labour Ministry Scholarships:** ₹40k-₹48k (Labour Registration वालों के लिए)\n\nक्या आप total seats के बारे में जानना चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "🎓 **Scholarship Options:**\n\nAvailable scholarships:\n- **Government Post-Matric Scholarship:** ₹18k-₹23k\n- **Labour Ministry Scholarships:** ₹40k-₹48k (for those with Labour Registration)\n\nWould you like to know about total seats available?\n\n(Please respond with 'Yes' or 'No')"

    def get_total_seats_message(self, lang: str) -> str:
        if lang == 'hi':
            return "👥 **Total Seats Available:**\n\nNursing program में कुल **60 seats** available हैं।\n\nक्या आप eligibility criteria के बारे में जानना चाहते हैं?\n\n('Haan' या 'Nahi' में उत्तर दें)"
        else:
            return "👥 **Total Seats Available:**\n\nThere are a total of **60 seats** available in the Nursing program.\n\nWould you like to know about the eligibility criteria?\n\n(Please respond with 'Yes' or 'No')"

    def get_eligibility_message(self, lang: str) -> str:
        if lang == 'hi':
            return "✅ **Eligibility Criteria for Admission:**\n\n**Required Qualifications:**\n- Biology in 12th grade (mandatory)\n- PNT Exam (must be passed)\n- Age: 17 to 35 years\n\n**Additional Requirements:**\n- Good health and fitness\n- English language proficiency\n- Commitment to nursing profession\n\nधन्यवाद! 🙏"
        else:
            return "✅ **Eligibility Criteria for Admission:**\n\n**Required Qualifications:**\n- Biology in 12th grade (mandatory)\n- PNT Exam (must be passed)\n- Age: 17 to 35 years\n\n**Additional Requirements:**\n- Good health and fitness\n- English language proficiency\n- Commitment to the nursing profession\n\nThank you! 🙏"

    def get_final_message(self, lang: str) -> str:
        if lang == 'hi':
            return "🎉 **Thank you for your interest!**\n\nआपको हमारे B.Sc Nursing program के बारे में सभी जानकारी मिल गई है।\n\n**Next Steps:**\n- Application form भरें\n- Required documents तैयार करें\n- PNT Exam की तैयारी करें\n\nकोई और सवाल हो तो हमसे संपर्क करें!\n\nधन्यवाद! 🙏"
        else:
            return "🎉 **Thank you for your interest!**\n\nYou have received all the information about our B.Sc Nursing program.\n\n**Next Steps:**\n- Fill out the application form\n- Prepare the required documents\n- Prepare for the PNT Exam\n\nIf you have any more questions, feel free to contact us!\n\nThank you! 🙏"

    def get_end_message(self, lang: str) -> str:
        if lang == 'hi':
            return "धन्यवाद! 🙏\n\nआपका समय देने के लिए धन्यवाद। भविष्य में कोई सहायता चाहिए तो हमसे संपर्क करें।\n\nTake care! 👋"
        else:
            return "Thank you! 🙏\n\nThank you for your time. If you need any assistance in the future, feel free to contact us.\n\nTake care! 👋"

    def get_clarification_message(self, context: str, lang: str) -> str:
        clarifications = {
            'admission_interest': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप Nursing College में admission लेना चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Are you interested in admission to the Nursing College?"
            },
            'biology_check': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आपने 12th में Biology पढ़ी है?",
                'en': "Please reply with 'Yes' or 'No'. Did you study Biology in 12th grade?"
            },
            'program_details': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप program के बारे में और जानकारी चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Would you like more information about the program?"
            },
            'fee_structure': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप hostel facilities के बारे में जानना चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Would you like to know about hostel facilities?"
            },
            'hostel_facilities': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप college location के बारे में जानना चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Would you like to know about the college location?"
            },
            'college_location': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप college की recognition के बारे में जानना चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Would you like to know about the college's recognition?"
            },
            'recognition': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप clinical training locations के बारे में जानना चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Would you like to know about clinical training locations?"
            },
            'clinical_training': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप scholarship options के बारे में जानना चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Would you like to know about scholarship options?"
            },
            'scholarship': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप total seats के बारे में जानना चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Would you like to know about total seats available?"
            },
            'total_seats': {
                'hi': "Kripya 'Haan' ya 'Nahi' mein jawab dein. क्या आप eligibility criteria के बारे में जानना चाहते हैं?",
                'en': "Please reply with 'Yes' or 'No'. Would you like to know about the eligibility criteria?"
            },
        }
        return clarifications.get(context, {}).get(lang, "Please reply with 'Yes' or 'No'.")

    def get_default_message(self, lang: str) -> str:
        if lang == 'hi':
            return "माफ़ कीजिए, मैं समझ नहीं पाया। कृपया फिर से प्रयास करें।"
        else:
            return "I'm sorry, I didn't understand. Please try again."

if __name__ == "__main__":
    # Test the chatbot
    chatbot = NursingCollegeChatbot()
    
    print("=== Nursing College Chatbot Test ===")
    print("Type 'quit' to exit\n")
    
    user_id = "test_user"
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        response = chatbot.get_response(user_id, user_input)
        print(f"Bot: {response}\n") 