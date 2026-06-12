from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_file):

    merger = PdfMerger()

    try:
        for pdf in pdf_files:
            merger.append(pdf)

        merger.write(output_file)
        merger.close()

        return f"PDFs merged successfully into {output_file}"

    except Exception as e:
        return f"Error: {e}"