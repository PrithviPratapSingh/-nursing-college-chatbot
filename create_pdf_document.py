#!/usr/bin/env python3
"""
PDF Document Generator for Nursing College Admission Chatbot
Creates a comprehensive document with conversation flow and visual diagrams
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPDF
import os

def create_title_page(canvas, doc):
    """Create a professional title page"""
    canvas.saveState()
    
    # Title
    canvas.setFont("Helvetica-Bold", 24)
    canvas.drawCentredString(4.25*inch, 9*inch, "Nursing College Admission Chatbot")
    
    # Subtitle
    canvas.setFont("Helvetica", 16)
    canvas.drawCentredString(4.25*inch, 8.5*inch, "AI-Driven Conversational Flow Documentation")
    
    # Author
    canvas.setFont("Helvetica", 12)
    canvas.drawCentredString(4.25*inch, 7.5*inch, "Prompt Engineering Assignment")
    canvas.drawCentredString(4.25*inch, 7.2*inch, "LiaPlus AI")
    
    # Date
    canvas.setFont("Helvetica", 10)
    canvas.drawCentredString(4.25*inch, 6.5*inch, "July 2025")
    
    # Features
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(1*inch, 5.5*inch, "Key Features:")
    
    features = [
        "• Multi-language Support (Hindi/English)",
        "• Intelligent Response Detection",
        "• Complete Admission Information Flow",
        "• Professional User Interface",
        "• Session Management",
        "• Real-time Language Switching"
    ]
    
    canvas.setFont("Helvetica", 10)
    y_position = 5.2
    for feature in features:
        canvas.drawString(1.2*inch, y_position*inch, feature)
        y_position -= 0.3
    
    canvas.restoreState()

def create_conversation_flow_diagram():
    """Create a visual conversation flow diagram"""
    drawing = Drawing(400, 600)
    
    # Define colors
    start_color = colors.green
    process_color = colors.blue
    decision_color = colors.orange
    end_color = colors.red
    
    # Create flow elements
    elements = [
        # Start
        {"type": "oval", "text": "START", "x": 200, "y": 550, "width": 80, "height": 40, "color": start_color},
        
        # Initial Question
        {"type": "rect", "text": "Admission\nInterest?", "x": 200, "y": 480, "width": 100, "height": 50, "color": process_color},
        
        # Decision 1
        {"type": "diamond", "text": "User\nResponse", "x": 200, "y": 400, "width": 80, "height": 60, "color": decision_color},
        
        # Biology Check
        {"type": "rect", "text": "Biology\nCheck", "x": 200, "y": 320, "width": 100, "height": 50, "color": process_color},
        
        # Decision 2
        {"type": "diamond", "text": "Biology\nStudied?", "x": 200, "y": 240, "width": 80, "height": 60, "color": decision_color},
        
        # Program Details
        {"type": "rect", "text": "Program\nDetails", "x": 200, "y": 160, "width": 100, "height": 50, "color": process_color},
        
        # Fee Structure
        {"type": "rect", "text": "Fee\nStructure", "x": 200, "y": 80, "width": 100, "height": 50, "color": process_color},
        
        # End
        {"type": "oval", "text": "END", "x": 200, "y": 20, "width": 80, "height": 40, "color": end_color},
    ]
    
    # Draw elements
    for element in elements:
        if element["type"] == "oval":
            drawing.add(renderPDF.drawOval(drawing, element["x"], element["y"], element["width"], element["height"], 
                                         fillColor=element["color"], strokeColor=colors.black))
        elif element["type"] == "rect":
            drawing.add(renderPDF.drawRect(drawing, element["x"], element["y"], element["width"], element["height"], 
                                         fillColor=element["color"], strokeColor=colors.black))
        elif element["type"] == "diamond":
            drawing.add(renderPDF.drawPolygon(drawing, [(element["x"], element["y"]+element["height"]/2),
                                                       (element["x"]+element["width"]/2, element["y"]),
                                                       (element["x"]+element["width"], element["y"]+element["height"]/2),
                                                       (element["x"]+element["width"]/2, element["y"]+element["height"])],
                                            fillColor=element["color"], strokeColor=colors.black))
    
    # Add text labels
    for element in elements:
        drawing.add(String(element["x"] + element["width"]/2, element["y"] + element["height"]/2, 
                          element["text"], textAnchor="middle", fontSize=8))
    
    return drawing

def create_detailed_flow_table():
    """Create a detailed conversation flow table"""
    data = [
        ['Step', 'State', 'Bot Question', 'User Response', 'Next Action'],
        ['1', 'INITIAL', 'Are you interested in admission?', 'Yes/No', 'Check Biology'],
        ['2', 'BIOLOGY_CHECK', 'Did you study Biology in 12th?', 'Yes/No', 'Program Details'],
        ['3', 'PROGRAM_DETAILS', 'Want more program info?', 'Yes/No', 'Fee Structure'],
        ['4', 'FEE_STRUCTURE', 'Want hostel facilities info?', 'Yes/No', 'Location'],
        ['5', 'COLLEGE_LOCATION', 'Want location details?', 'Yes/No', 'Recognition'],
        ['6', 'RECOGNITION', 'Want clinical training info?', 'Yes/No', 'Scholarship'],
        ['7', 'CLINICAL_TRAINING', 'Want scholarship info?', 'Yes/No', 'Total Seats'],
        ['8', 'TOTAL_SEATS', 'Want eligibility criteria?', 'Yes/No', 'Eligibility'],
        ['9', 'ELIGIBILITY', 'Final information provided', 'Any', 'END']
    ]
    
    table = Table(data, colWidths=[0.5*inch, 1.2*inch, 2*inch, 1.2*inch, 1.2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    return table

def create_language_detection_table():
    """Create a table showing language detection patterns"""
    data = [
        ['Language', 'Detection Method', 'Example Inputs', 'Response Language'],
        ['Hindi', 'Devanagari Script', 'हाँ, नहीं, बताओ', 'Hindi'],
        ['English', 'Latin Script', 'Yes, No, Tell me', 'English'],
        ['Mixed', 'Script Detection', 'Haan, Yes, बताओ', 'Detected Language']
    ]
    
    table = Table(data, colWidths=[1*inch, 1.5*inch, 1.5*inch, 1*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    return table

def create_response_patterns_table():
    """Create a table showing response detection patterns"""
    data = [
        ['Response Type', 'Patterns', 'Examples'],
        ['Positive', 'haan, yes, batao, tell me, kya hai, more, ok, sure', 'Haan, Yes, Tell me more'],
        ['Negative', 'nahi, no, not, dont, nope, not interested', 'Nahi, No, Not interested'],
        ['Clarification', 'unclear responses', 'Maybe, I think so, Not sure']
    ]
    
    table = Table(data, colWidths=[1.5*inch, 2.5*inch, 1.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    return table

def create_fee_structure_table():
    """Create a detailed fee structure table"""
    data = [
        ['Fee Component', 'Amount (INR)', 'Due Date'],
        ['Tuition Fee', '₹60,000', 'Annual'],
        ['Bus Fee', '₹10,000', 'Annual'],
        ['Total Annual Fees', '₹70,000', 'Annual'],
        ['1st Installment', '₹30,000', 'At Admission'],
        ['2nd Installment', '₹20,000', 'After 1st Semester'],
        ['3rd Installment', '₹20,000', 'After 2nd Semester']
    ]
    
    table = Table(data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    return table

def create_eligibility_table():
    """Create an eligibility criteria table"""
    data = [
        ['Requirement', 'Details', 'Status'],
        ['Biology in 12th', 'Mandatory subject', 'Required'],
        ['PNT Exam', 'Must be passed', 'Required'],
        ['Age', '17 to 35 years', 'Required'],
        ['Health', 'Good health and fitness', 'Required'],
        ['English Proficiency', 'Basic English knowledge', 'Required'],
        ['Commitment', 'To nursing profession', 'Required']
    ]
    
    table = Table(data, colWidths=[2*inch, 2*inch, 1*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.purple),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lavender),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    return table

def generate_pdf():
    """Generate the complete PDF document"""
    doc = SimpleDocTemplate("Nursing_College_Chatbot_Documentation.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.darkgreen
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )
    
    # Build the document
    story = []
    
    # Title Page
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Table of Contents", title_style))
    story.append(Spacer(1, 20))
    
    toc_items = [
        "1. Project Overview",
        "2. Conversation Flow Structure", 
        "3. Language Detection System",
        "4. Response Pattern Analysis",
        "5. Fee Structure Details",
        "6. Eligibility Criteria",
        "7. Technical Implementation",
        "8. User Interface Features",
        "9. Testing and Validation",
        "10. Conclusion"
    ]
    
    for item in toc_items:
        story.append(Paragraph(item, body_style))
    
    story.append(PageBreak())
    
    # 1. Project Overview
    story.append(Paragraph("1. Project Overview", title_style))
    story.append(Paragraph("""
    The Nursing College Admission Chatbot is an AI-driven conversational system designed to provide comprehensive 
    information about B.Sc Nursing program admission. The chatbot handles multi-step queries and maintains a 
    professional, user-friendly tone throughout the conversation.
    """, body_style))
    
    story.append(Paragraph("Key Features:", heading_style))
    features = [
        "• Multi-language Support (Hindi/English)",
        "• Intelligent Response Detection",
        "• Complete Admission Information Flow", 
        "• Professional User Interface",
        "• Session Management",
        "• Real-time Language Switching"
    ]
    
    for feature in features:
        story.append(Paragraph(feature, body_style))
    
    story.append(PageBreak())
    
    # 2. Conversation Flow Structure
    story.append(Paragraph("2. Conversation Flow Structure", title_style))
    story.append(Paragraph("""
    The chatbot follows a structured conversation flow with 11 main states, each handling specific information 
    requests and user interactions. The flow is designed to be intuitive and comprehensive.
    """, body_style))
    
    # Add the detailed flow table
    story.append(Paragraph("Detailed Conversation Flow:", heading_style))
    story.append(create_detailed_flow_table())
    story.append(Spacer(1, 20))
    
    story.append(PageBreak())
    
    # 3. Language Detection System
    story.append(Paragraph("3. Language Detection System", title_style))
    story.append(Paragraph("""
    The chatbot implements intelligent language detection to provide responses in the user's preferred language. 
    The system detects Hindi (Devanagari script) and defaults to English for other inputs.
    """, body_style))
    
    story.append(create_language_detection_table())
    story.append(Spacer(1, 20))
    
    story.append(PageBreak())
    
    # 4. Response Pattern Analysis
    story.append(Paragraph("4. Response Pattern Analysis", title_style))
    story.append(Paragraph("""
    The chatbot uses pattern matching to understand user responses and determine the appropriate next action. 
    This ensures smooth conversation flow and accurate information delivery.
    """, body_style))
    
    story.append(create_response_patterns_table())
    story.append(Spacer(1, 20))
    
    story.append(PageBreak())
    
    # 5. Fee Structure Details
    story.append(Paragraph("5. Fee Structure Details", title_style))
    story.append(Paragraph("""
    The chatbot provides detailed fee information including annual costs, installment plans, and payment schedules 
    to help students understand the financial requirements.
    """, body_style))
    
    story.append(create_fee_structure_table())
    story.append(Spacer(1, 20))
    
    story.append(PageBreak())
    
    # 6. Eligibility Criteria
    story.append(Paragraph("6. Eligibility Criteria", title_style))
    story.append(Paragraph("""
    Clear eligibility requirements are presented to help students understand if they qualify for the B.Sc Nursing program.
    """, body_style))
    
    story.append(create_eligibility_table())
    story.append(Spacer(1, 20))
    
    story.append(PageBreak())
    
    # 7. Technical Implementation
    story.append(Paragraph("7. Technical Implementation", title_style))
    story.append(Paragraph("""
    The chatbot is built using Python with Flask framework, featuring state machine architecture for conversation 
    management and responsive web interface for optimal user experience.
    """, body_style))
    
    tech_details = [
        "• Backend: Python Flask",
        "• Frontend: HTML5, CSS3, JavaScript",
        "• State Management: Custom state machine",
        "• Language Detection: Unicode script analysis",
        "• Response Patterns: Regular expression matching",
        "• Session Management: User session tracking"
    ]
    
    for detail in tech_details:
        story.append(Paragraph(detail, body_style))
    
    story.append(PageBreak())
    
    # 8. User Interface Features
    story.append(Paragraph("8. User Interface Features", title_style))
    story.append(Paragraph("""
    The web interface provides a modern, responsive design with intuitive navigation and user-friendly features.
    """, body_style))
    
    ui_features = [
        "• Modern, responsive design",
        "• Quick reply buttons (Haan, Nahi, Yes, No)",
        "• Real-time typing indicators",
        "• Session persistence",
        "• Reset functionality",
        "• Mobile-responsive layout",
        "• Professional color scheme",
        "• Smooth animations and transitions"
    ]
    
    for feature in ui_features:
        story.append(Paragraph(feature, body_style))
    
    story.append(PageBreak())
    
    # 9. Testing and Validation
    story.append(Paragraph("9. Testing and Validation", title_style))
    story.append(Paragraph("""
    Comprehensive testing ensures the chatbot meets all requirements and provides accurate information delivery.
    """, body_style))
    
    testing_points = [
        "• Positive conversation flow testing",
        "• Negative response handling",
        "• Language detection accuracy",
        "• Biology requirement validation",
        "• Fee structure accuracy",
        "• Eligibility criteria verification",
        "• Session management testing",
        "• User interface responsiveness"
    ]
    
    for point in testing_points:
        story.append(Paragraph(point, body_style))
    
    story.append(PageBreak())
    
    # 10. Conclusion
    story.append(Paragraph("10. Conclusion", title_style))
    story.append(Paragraph("""
    The Nursing College Admission Chatbot successfully implements all required features including multi-step 
    conversational flow, language detection, comprehensive information delivery, and professional user experience. 
    The system provides accurate, helpful information to prospective students while maintaining a friendly and 
    professional tone throughout the interaction.
    """, body_style))
    
    # Build the PDF
    doc.build(story, onFirstPage=create_title_page)
    
    print("PDF document generated successfully: Nursing_College_Chatbot_Documentation.pdf")

if __name__ == "__main__":
    try:
        generate_pdf()
        print("✅ PDF document created successfully!")
        print("📄 File: Nursing_College_Chatbot_Documentation.pdf")
    except Exception as e:
        print(f"❌ Error generating PDF: {e}") 