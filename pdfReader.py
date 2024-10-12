import PyPDF2
import csv
from bounce_scopper import read_valid_list

def write_csv(data):
    with open("new_list.csv", mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for line in data:
            # Write the entire phone number as a single element in the CSV row
            writer.writerow([{line["phone"]: line["providers"]}]) # Wrapping `line` in a list to avoid splitting it


def read_pdf(file_path):
	count = 0
	bonk_numbers = []
	try:
		# Open the PDF file
		with open(file_path, 'rb') as file:
			# Initialize a PDF reader
			reader = PyPDF2.PdfReader(file)
			
			# Loop through all the pages
			for page_num in range(len(reader.pages)):
				page = reader.pages[page_num]
				
				# Extract text from each page
				text = page.extract_text()
				
				# Print each line
				for text_line in text.split('\n'):
					for line in text_line.split(' '):
						if len(line) >= 10:
							
							
							if line[3] != "-" and line[8] != "-":
								break
							if line == "999-999-9999":
								break
							
							bonk_numbers.append(line)
		
		write_csv(bonk_numbers)			
	except Exception as e:
		print(f"An error occurred: {e}")


def read_json():
    get_list = read_valid_list()
    
    write_csv(get_list)	

    	
# Example usage

read_json()
