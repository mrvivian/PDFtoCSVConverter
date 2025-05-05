import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from pdf_to_csv_converter import BankStatementConverter
import sys
from datetime import datetime

class ConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Statement PDF to CSV Converter")
        self.root.geometry("800x600")
        
        # Configure style
        style = ttk.Style()
        style.configure('TButton', padding=6)
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # File Selection Section
        ttk.Label(main_frame, text="PDF to CSV Converter", style='Header.TLabel').grid(row=0, column=0, columnspan=3, pady=10)
        
        # Input File Selection
        ttk.Label(main_frame, text="Input PDF File:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.input_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.input_path, width=60).grid(row=1, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_input).grid(row=1, column=2)
        
        # Output File Selection
        ttk.Label(main_frame, text="Output CSV File:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.output_path, width=60).grid(row=2, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_output).grid(row=2, column=2)
        
        # Convert Button
        ttk.Button(main_frame, text="Convert", command=self.convert_file).grid(row=3, column=0, columnspan=3, pady=20)
        
        # Log Section
        ttk.Label(main_frame, text="Conversion Log:", style='Header.TLabel').grid(row=4, column=0, columnspan=3, sticky=tk.W, pady=5)
        
        # Create Text widget for logging
        self.log_text = tk.Text(main_frame, height=15, width=80)
        self.log_text.grid(row=5, column=0, columnspan=3, pady=5)
        
        # Scrollbar for log
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.log_text.yview)
        scrollbar.grid(row=5, column=3, sticky=(tk.N, tk.S))
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        # Redirect stdout to the Text widget
        sys.stdout = self
        
    def write(self, text):
        """Handle stdout redirection"""
        self.log_text.insert(tk.END, text)
        self.log_text.see(tk.END)
        self.root.update()
        
    def flush(self):
        """Required for stdout redirection"""
        pass
        
    def browse_input(self):
        """Handle input file selection"""
        filename = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.input_path.set(filename)
            # Auto-generate output filename with date
            base_name = os.path.splitext(filename)[0]
            date_str = datetime.now().strftime("%d%m%Y")
            output_name = f"{base_name}_converted_{date_str}.csv"
            self.output_path.set(output_name)
            
    def browse_output(self):
        """Handle output file selection"""
        filename = filedialog.asksaveasfilename(
            title="Save CSV File",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if filename:
            self.output_path.set(filename)
            
    def convert_file(self):
        """Handle file conversion"""
        input_file = self.input_path.get()
        output_file = self.output_path.get()
        
        if not input_file or not output_file:
            messagebox.showerror("Error", "Please select both input and output files")
            return
            
        if not os.path.exists(input_file):
            messagebox.showerror("Error", "Input PDF file does not exist")
            return
            
        try:
            # Clear log
            self.log_text.delete(1.0, tk.END)
            
            # Log start of conversion
            print(f"\n=== Starting conversion at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
            print(f"Input file: {input_file}")
            print(f"Output file: {output_file}")
            
            # Create converter instance and convert
            converter = BankStatementConverter(input_file)
            converter.save_to_csv(output_file)
            
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                # Show success message
                messagebox.showinfo("Success", 
                                  f"Conversion completed successfully!\nOutput saved to: {output_file}")
            else:
                messagebox.showwarning("Warning", 
                                     "The conversion completed but no data was extracted. Please check the log for details.")
            
        except Exception as e:
            error_msg = f"Error during conversion: {str(e)}"
            print(f"\nERROR: {error_msg}")
            messagebox.showerror("Error", error_msg)

def main():
    root = tk.Tk()
    app = ConverterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 