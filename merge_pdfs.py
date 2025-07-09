from PyPDF2 import PdfReader, PdfWriter

def combine_pdfs(pdf1_path, pdf2_path, output_path):
    try:
        # Create PdfReader objects for the two input PDFs
        pdf1 = PdfReader(pdf1_path)
        pdf2 = PdfReader(pdf2_path)

        # Create a PdfWriter object for the output PDF
        writer = PdfWriter()

        # Add pages from the first PDF
        for page in pdf1.pages:
            writer.add_page(page)

        # Add pages from the second PDF
        for page in pdf2.pages:
            writer.add_page(page)

        # Write the combined PDF to the output file
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        print(f"Successfully combined PDFs into '{output_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    pdf1_path = "/home/ywerner/OneDrive/Wichtig/References/2.pdf"  # Replace with the path to your first PDF
    pdf2_path = "/home/ywerner/OneDrive/Wichtig/References/1.pdf"  # Replace with the path to your second PDF
    output_path = "/home/ywerner/OneDrive/Wichtig/References/3.pdf"  # Replace with the desired output file path

    combine_pdfs(pdf1_path, pdf2_path, output_path)
