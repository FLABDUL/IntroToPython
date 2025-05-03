class Report:
    def __init__(self, content):
        self.content = content

    def format_to_pdf(self):
        # SRP violation: formatting logic in the same class
        pass

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.content)

class ReportSrp:
    def __init__(self, content):
        self.content = content

class PDFFormatter:
    def format(self, report):
        # Convert report.content to PDF format
        pass

class FileSaver:
    def save(self, content, filename):
        with open(filename, 'w') as f:
            f.write(content)
