from tools.ai_email_writer import generate_email
from tools.ai_file_summarize import summarize_file
from tools.ai_code_explainer import explain_code
from tools.ai_resume_analyzer import analyze_resume
from tools.pdf_merger import merge_pdfs
from tools.file_parser import analyze_file
from tools.ai_website_summarizer import summarize_website
from tools.history import save_history

def main():

    while True:

        print("\n" + "=" * 50)
        print("🤖 AI AUTOMATION TOOLKIT")
        print("=" * 50)
        print("1. AI Email Writer")
        print("2. AI File Summarizer")
        print("3. AI Code Explainer")
        print("4. AI Resume Analyzer")
        print("5. PDF Merger")
        print("6. File Parser")
        print("7. Web Scrapper")
        print("8. Exit")
        choice = input("\nEnter your choice: ")

        try:

            # AI Email Writer
            if choice == "1":

                topic = input("Enter email topic: ")

                result = generate_email(topic)

                print("\n" + "=" * 50)
                print("GENERATED EMAIL")
                print("=" * 50)
                print(result)
                
                path = save_history("email", result)
                print(f"\nSaved to: {path}")

            # AI File Summarizer
            elif choice == "2":

                file_path = input("Enter text file path: ")

                result = summarize_file(file_path)

                print("\n" + "=" * 50)
                print("FILE SUMMARY")
                print("=" * 50)
                print(result)
                path = save_history("summary", result)
                print(f"\nSaved to: {path}")
                
            # AI Code Explainer
            elif choice == "3":

                print("\nPaste your code below.")
                print("Type END on a new line when finished.\n")

                lines = []

                while True:

                    line = input()

                    if line.strip().upper() == "END":
                        break

                    lines.append(line)

                code = "\n".join(lines)

                result = explain_code(code)

                print("\n" + "=" * 50)
                print("CODE EXPLANATION")
                print("=" * 50)
                print(result)
                path = save_history("explainer", result)
                print(f"\nSaved to: {path}")

            # AI Resume Analyzer
            elif choice == "4":

                print("\nPaste your resume text below.")
                print("Type END on a new line when finished.\n")

                lines = []

                while True:

                    line = input()

                    if line.strip().upper() == "END":
                        break

                    lines.append(line)

                resume_text = "\n".join(lines)

                result = analyze_resume(resume_text)

                print("\n" + "=" * 50)
                print("RESUME ANALYSIS")
                print("=" * 50)
                print(result)
                path = save_history("analyzer", result)
                print(f"\nSaved to: {path}")
            
            #PDF MERGER 
            elif choice == "5":
    
                pdfs = [
                        "data/input/file1.pdf",
                        "data/input/file2.pdf"
                ]

                result = merge_pdfs(
                                pdfs,
                                "data/output/merged.pdf"
                )
                print(result)
                path = save_history("merger", result)
                print(f"\nSaved to: {path}")
            
            #File Parser
            elif choice == "6":
                
                result = analyze_file("data/input/sample2.txt")
                print(result)
                path = save_history("file parser", result)
                print(f"\nSaved to: {path}")
                
            #Web Scrapper
            elif choice == "7":
                url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
                print(summarize_website(url))
                path = save_history("scrapper", result)
                print(f"\nSaved to: {path}")
                
            # Exit
            elif choice == "8":

                print("\nThank you for using AI Automation Toolkit!")
                break

            else:
                print("\nInvalid choice. Please try again.")

        except FileNotFoundError:
            print("\nFile not found.")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()