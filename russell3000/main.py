# This is a sample Python script.
import PyPDF2
import pdfplumber
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def process_data_ii():
    # Open the PDF file
    file = open("data/russell3000_out.txt", "w")
    file_name = 'data/US3000_QUARTERLY-DailyData-USD_StocksWeight_20240628.pdf'
    with pdfplumber.open(file_name) as pdf:
        # Specify the page number containing the table
        num_pages = len(pdf.pages)
        # Access the specific page
        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            # Extract tables from the page
            tables = page.extract_tables()

            # Process and print the first table (if there is one)
            if tables:
                for table in tables:
                    for row in table:  # Access the first table
                        if row[0].startswith("Russell 3000"):
                            continue
                        file.write(f"{row[0]}|{row[1]}\n")
            else:
                print("No tables found on this page.")


def process_data():
    # Use a breakpoint in the code line below to debug your script.

    # Open the PDF file
    file_name = 'US3000_QUARTERLY-DailyData-USD_StocksWeight_20240628.pdf'
    with open(file_name, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages
        num_pages = len(pdf_reader.pages)

        # Extract text from each page
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            print(f"Page {page_num + 1}:\n{text}\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_data_ii()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
