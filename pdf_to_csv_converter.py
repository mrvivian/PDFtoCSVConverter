import pdfplumber
import pandas as pd
import argparse
import os
import re
import sys
from datetime import datetime

class BankStatementConverter:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.column_names = [
            'Posting Date', 
            'Narrative', 
            'Debit Amount', 
            'Credit Amount', 
            'Balance'
        ]
        print(f"Initializing converter for PDF: {pdf_path}")
        print(f"PDF exists: {os.path.exists(pdf_path)}")
        if os.path.exists(pdf_path):
            print(f"PDF size: {os.path.getsize(pdf_path)} bytes")

    def clean_amount(self, amount):
        """Clean amount strings and convert to proper format"""
        if pd.isna(amount):
            return ""
        try:
            # Convert to string and handle potential bytes
            if isinstance(amount, bytes):
                amount = amount.decode('utf-8', errors='ignore')
            amount = str(amount)
            
            # Remove £ symbol and any spaces
            amount = amount.replace('£', '').strip()
            # Remove any commas in the number
            amount = amount.replace(',', '')
            # Convert to float and format to 2 decimal places
            return f"{float(amount):.2f}"
        except (ValueError, AttributeError):
            return ""

    def clean_narrative(self, narrative):
        """Clean narrative text and escape any commas"""
        if pd.isna(narrative):
            return ""
        try:
            # Handle potential bytes
            if isinstance(narrative, bytes):
                try:
                    narrative = narrative.decode('utf-8', errors='ignore')
                except UnicodeDecodeError:
                    narrative = narrative.decode('latin1', errors='ignore')
            narrative = str(narrative)
            # Replace any commas with spaces to avoid CSV confusion
            return narrative.replace(',', ' ')
        except (UnicodeDecodeError, AttributeError):
            return str(narrative).encode('ascii', errors='ignore').decode()

    def extract_and_format_data(self):
        """Extract tables from PDF and format according to specifications"""
        try:
            print("Starting table extraction...")
            processed_rows = []
            
            with pdfplumber.open(self.pdf_path) as pdf:
                for page in pdf.pages:
                    # Extract tables from the page
                    tables = page.extract_tables()
                    
                    if tables:
                        for table in tables:
                            # Convert table to DataFrame
                            df = pd.DataFrame(table[1:], columns=table[0])
                            
                            # Process each row
                            for _, row in df.iterrows():
                                try:
                                    # Get the values, handling potential missing columns
                                    posting_date = str(row.get('Posting Date', '')) if pd.notna(row.get('Posting Date')) else ""
                                    narrative = self.clean_narrative(row.get('Narrative', ''))
                                    
                                    # Handle debit and credit amounts separately
                                    debit_amount = self.clean_amount(row.get('Debit Amount', '')) if pd.notna(row.get('Debit Amount')) else ""
                                    credit_amount = self.clean_amount(row.get('Credit Amount', '')) if pd.notna(row.get('Credit Amount')) else ""
                                    balance = self.clean_amount(row.get('Balance', '')) if pd.notna(row.get('Balance')) else ""

                                    # Format the row with all required columns
                                    formatted_row = f"{posting_date},,,{narrative},,,{debit_amount},{credit_amount},{balance}"
                                    processed_rows.append(formatted_row)
                                    print(f"Processed row: {formatted_row}")
                                except Exception as row_error:
                                    print(f"Error processing row: {row_error}")
                                    continue

            return processed_rows

        except Exception as e:
            print(f"Error processing PDF: {str(e)}")
            return []

    def save_to_csv(self, output_path):
        """Save the formatted data to CSV"""
        try:
            print(f"Attempting to save CSV to: {output_path}")
            formatted_rows = self.extract_and_format_data()
            if formatted_rows:
                with open(output_path, 'w', encoding='utf-8') as f:
                    # Write header row with all required columns
                    f.write("Posting Date,Narrative,Debit Amount,Credit Amount,Balance\n")
                    for row in formatted_rows:
                        f.write(f"{row}\n")
                print(f"Successfully saved data to {output_path}")
                print(f"CSV exists: {os.path.exists(output_path)}")
                print(f"CSV size: {os.path.getsize(output_path)} bytes")
            else:
                print("No data was extracted from the PDF")
        except Exception as e:
            print(f"Error saving to CSV: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Convert PDF bank statement to CSV')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('--output', '-o', help='Output CSV file path', 
                        default=f'output_{datetime.now().strftime("%d%m%Y")}.csv')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf_path):
        print(f"Error: PDF file not found at {args.pdf_path}")
        return
    
    converter = BankStatementConverter(args.pdf_path)
    converter.save_to_csv(args.output)

if __name__ == "__main__":
    main() 