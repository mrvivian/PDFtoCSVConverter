from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
import os
from datetime import datetime, timedelta

def create_sample_statement():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(current_dir, 'complex_test_statement.pdf')
        print(f"Creating PDF at: {output_path}")
        
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        story = []
        
        # Create more complex transaction data
        data = [
            ['Posting Date', 'Value Date', 'Narrative', 'Debit Amount', 'Credit Amount', 'Balance'],
            # Salary and regular income
            ['01/03/2024', '01/03/2024', 'SALARY PAYMENT - MONTHLY', '', '£3,500.00', '£3,500.00'],
            ['02/03/2024', '02/03/2024', 'FREELANCE WORK PAYMENT', '', '£750.00', '£4,250.00'],
            # Regular bills
            ['03/03/2024', '03/03/2024', 'RENT PAYMENT - MARCH', '£1,200.00', '', '£3,050.00'],
            ['04/03/2024', '04/03/2024', 'UTILITIES - ELECTRICITY & GAS', '£150.75', '', '£2,899.25'],
            ['05/03/2024', '05/03/2024', 'INTERNET & PHONE BILL', '£45.99', '', '£2,853.26'],
            # Shopping and groceries
            ['06/03/2024', '06/03/2024', 'SUPERMARKET SHOPPING - WEEKLY', '£85.50', '', '£2,767.76'],
            ['07/03/2024', '07/03/2024', 'ONLINE SHOPPING - AMAZON', '£120.00', '', '£2,647.76'],
            # Entertainment and dining
            ['08/03/2024', '08/03/2024', 'CINEMA TICKETS', '£25.00', '', '£2,622.76'],
            ['09/03/2024', '09/03/2024', 'RESTAURANT - GROUP DINNER', '£75.20', '', '£2,547.56'],
            # Transfers and savings
            ['10/03/2024', '10/03/2024', 'TRANSFER TO SAVINGS ACCOUNT', '£500.00', '', '£2,047.56'],
            ['11/03/2024', '11/03/2024', 'INTEREST PAYMENT - SAVINGS', '', '£15.50', '£2,063.06'],
            # ATM and cash transactions
            ['12/03/2024', '12/03/2024', 'ATM WITHDRAWAL - CASH', '£200.00', '', '£1,863.06'],
            ['13/03/2024', '13/03/2024', 'CASH DEPOSIT - BIRTHDAY GIFT', '', '£100.00', '£1,963.06'],
            # Subscription services
            ['14/03/2024', '14/03/2024', 'NETFLIX SUBSCRIPTION', '£10.99', '', '£1,952.07'],
            ['15/03/2024', '15/03/2024', 'SPOTIFY PREMIUM', '£9.99', '', '£1,942.08'],
            # Travel and transport
            ['16/03/2024', '16/03/2024', 'TRAIN TICKET - LONDON', '£45.00', '', '£1,897.08'],
            ['17/03/2024', '17/03/2024', 'UBER RIDE', '£15.50', '', '£1,881.58'],
            # Healthcare
            ['18/03/2024', '18/03/2024', 'DENTIST APPOINTMENT', '£85.00', '', '£1,796.58'],
            ['19/03/2024', '19/03/2024', 'PHARMACY - PRESCRIPTION', '£12.50', '', '£1,784.08'],
            # Miscellaneous
            ['20/03/2024', '20/03/2024', 'CHARITY DONATION', '£25.00', '', '£1,759.08'],
            ['21/03/2024', '21/03/2024', 'REFUND - ONLINE PURCHASE', '', '£50.00', '£1,809.08'],
        ]
        
        # Create table with enhanced styling
        table = Table(data)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (3, 1), (5, -1), 'RIGHT'),  # Align amounts to the right
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),  # Alternate row colors
        ])
        table.setStyle(style)
        
        story.append(table)
        doc.build(story)
        
        print(f"Complex test bank statement created successfully at: {output_path}")
        print(f"File exists: {os.path.exists(output_path)}")
        print(f"File size: {os.path.getsize(output_path)} bytes")
        
    except Exception as e:
        print(f"Error creating PDF: {str(e)}")

if __name__ == "__main__":
    create_sample_statement() 