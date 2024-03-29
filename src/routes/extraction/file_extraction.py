from docx2pdf import convert
import fitz


def extract_from_file(filename):
    fileObj = fitz.open("temp_files/" + filename)
    result = ""
    for page in fileObj:
        result += page.get_text() + chr(12)
    tmp_type = "PDF"
    # print(result, file=sys.stderr)
    result = result.encode("ascii", "ignore")
    result = result.decode()
    result = result.replace("\x92", "")
    result = result.replace("\x0c", "")
    return {"type": tmp_type, "article": result}


def extract_from_docx(filename):
    convert(
        f"temp_files/{filename}",
        output_path=f"temp_files/{filename.split('.')[0]}.pdf",
    )
    return extract_from_file(f"{filename.split('.')[0]}.pdf")
