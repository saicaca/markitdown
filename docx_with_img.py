from src.markitdown import MarkItDown

if __name__ == '__main__':
    md = MarkItDown()
    result = md.convert("test_with_images.docx")
    # output the result to a file
    with open("test.md", "w", encoding="utf-8") as f:
        f.write(result.text_content)
    # print(result.text_content)