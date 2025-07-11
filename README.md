# Nursing College Admission Chatbot

An AI-driven conversational chatbot designed to provide information about B.Sc Nursing program admission at a nursing college. The chatbot handles multi-step queries and maintains a professional, user-friendly tone throughout the conversation.

## Features

### 🤖 Conversational Flow
- **Initial Admission Interest**: Asks if user is interested in nursing college admission
- **Eligibility Check**: Verifies if user studied Biology in 12th grade
- **Program Details**: Provides information about B.Sc Nursing program
- **Fee Structure**: Detailed breakdown of annual fees and installment plans
- **Hostel Facilities**: Information about accommodation and training facilities
- **College Location**: Details about college location in Delhi
- **Recognition**: Information about Indian Nursing Council recognition
- **Clinical Training**: Details about training locations
- **Scholarship Options**: Available scholarship information
- **Total Seats**: Information about available seats
- **Eligibility Criteria**: Complete admission requirements

### 🎯 Key Capabilities
- **Multi-language Support**: Handles both Hindi and English responses
- **Smart Response Detection**: Recognizes positive/negative responses intelligently
- **Session Management**: Maintains conversation state for each user
- **Professional Tone**: Maintains consistent, friendly, and professional communication
- **User-friendly Interface**: Modern, responsive web interface

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the chatbot**:
   Open your web browser and go to: `http://localhost:5000`

## Usage

### Web Interface
1. Open the application in your browser
2. The chatbot will automatically start the conversation
3. Respond to questions using the text input or quick reply buttons
4. Use the "Reset" button to start a new conversation

### Command Line Testing
You can also test the chatbot directly from the command line:
```bash
python chatbot.py
```

### Response Guidelines
- **Positive Responses**: "Haan", "Yes", "Tell me more", "Kya hai?", "Batao"
- **Negative Responses**: "Nahi", "No", "Not interested"
- The chatbot will continue the conversation for any response other than explicit "No"

## Conversation Flow

### 1. Initial Admission Interest
- Asks if user is interested in nursing college admission
- Handles both positive and negative responses appropriately

### 2. Biology Eligibility Check
- Verifies if user studied Biology in 12th grade
- Informs about Biology requirement if not studied
- Continues only if Biology requirement is met

### 3. Program Information
- Describes B.Sc Nursing program as full-time
- Offers additional program details
- Maintains professional tone throughout

### 4. Fee Structure
Provides detailed fee breakdown:
- **Tuition Fee**: ₹60,000 INR
- **Bus Fee**: ₹10,000 INR
- **Total Annual Fees**: ₹70,000 INR

**Installment Plan**:
- 1st Installment: ₹30,000 (at admission)
- 2nd Installment: ₹20,000 (after first semester)
- 3rd Installment: ₹20,000 (after second semester)

### 5. Hostel and Training Facilities
**Accommodation Features**:
- 4x7 water and electricity supply
- CCTV surveillance for security
- On-site warden available

**Training Features**:
- Hospital training included
- Real patients during training

### 6. College Location
- Located in Delhi
- Offers additional location information

### 7. Recognition and Accreditation
- Recognized by Indian Nursing Council (INC) (Delhi)

### 8. Clinical Training Locations
- District Hospital (Backundpur)
- Community Health Centers
- Regional Hospital (Chartha)
- Ranchi Neurosurgery and Allied Science Hospital (Ranchi, Jharkhand)

### 9. Scholarship Options
- Government Post-Matric Scholarship (₹18k-₹23k)
- Labour Ministry Scholarships (₹40k-₹48k) for Labour Registration holders

### 10. Total Seats
- 60 seats available in the Nursing program

### 11. Eligibility Criteria
**Requirements**:
- Biology in 12th grade
- PNT Exam (must be passed)
- Age: 17 to 35 years

## Technical Architecture

### Core Components
- **`chatbot.py`**: Main chatbot logic with conversation state management
- **`app.py`**: Flask web application server
- **`templates/index.html`**: Modern, responsive web interface
- **`requirements.txt`**: Python dependencies

### State Management
The chatbot uses a state machine approach with the following states:
- `INITIAL`: Starting state
- `ADMISSION_INTEREST`: Checking admission interest
- `BIOLOGY_CHECK`: Verifying Biology eligibility
- `PROGRAM_DETAILS`: Providing program information
- `FEE_STRUCTURE`: Explaining fee structure
- `HOSTEL_FACILITIES`: Describing hostel facilities
- `COLLEGE_LOCATION`: Providing location information
- `RECOGNITION`: Explaining recognition
- `CLINICAL_TRAINING`: Describing training locations
- `SCHOLARSHIP`: Providing scholarship information
- `TOTAL_SEATS`: Informing about available seats
- `ELIGIBILITY`: Explaining eligibility criteria
- `END`: Conversation end

### Response Detection
- **Positive Patterns**: Recognizes "haan", "yes", "batao", "tell me", etc.
- **Negative Patterns**: Recognizes "nahi", "no", "not interested", etc.
- **Fallback**: Asks for clarification if response is unclear

## Features

### ✅ Implemented Requirements
- [x] Initial admission interest check
- [x] Biology eligibility verification
- [x] Program details with full-time mention
- [x] Detailed fee structure with installments
- [x] Hostel facilities description
- [x] College location information
- [x] Recognition and accreditation details
- [x] Clinical training locations
- [x] Scholarship options
- [x] Total seats information
- [x] Complete eligibility criteria
- [x] Professional and user-friendly tone
- [x] Multi-step query handling
- [x] Seamless user navigation

### 🎨 User Experience Features
- **Modern UI**: Beautiful, responsive web interface
- **Quick Replies**: One-click response buttons
- **Typing Indicators**: Visual feedback during bot responses
- **Session Persistence**: Maintains conversation state
- **Reset Functionality**: Start fresh conversations
- **Mobile Responsive**: Works on all device sizes

## File Structure
```
chatbot/
├── app.py                 # Flask web application
├── chatbot.py            # Main chatbot logic
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── templates/
    └── index.html       # Web interface template
```

## Testing

### Manual Testing
1. Start the application
2. Test positive flow: Answer "Haan" to all questions
3. Test negative flow: Answer "Nahi" to see early termination
4. Test mixed responses: Use various positive/negative responses
5. Test reset functionality: Use reset button to start fresh

### Expected Behaviors
- **Positive Flow**: Complete conversation through all topics
- **Negative Flow**: Polite termination with future assistance offer
- **Biology Check**: Proper handling of Biology requirement
- **Session Management**: Maintains state across interactions
- **Response Detection**: Handles various response formats

## Customization

### Adding New Topics
1. Add new state to `ConversationState` enum
2. Add state handling logic in `get_response()` method
3. Create corresponding message method
4. Update conversation flow logic

### Modifying Responses
Edit the message methods in `chatbot.py` to customize responses:
- `get_admission_interest_message()`
- `get_biology_check_message()`
- `get_program_details_message()`
- etc.

### Styling Changes
Modify the CSS in `templates/index.html` to change the appearance.

## Troubleshooting

### Common Issues
1. **Port already in use**: Change port in `app.py` line 28
2. **Dependencies not installed**: Run `pip install -r requirements.txt`
3. **Template not found**: Ensure `templates` folder exists
4. **Import errors**: Check Python version compatibility

### Debug Mode
The application runs in debug mode by default. Check the console for detailed error messages.

## License

This project is created for educational purposes as part of a prompt engineering assignment.

## Support

For issues or questions, please refer to the code comments and documentation within the files. 