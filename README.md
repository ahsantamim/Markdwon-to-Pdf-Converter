📝 Markdown to PDF Converter

A simple and user-friendly Markdown to PDF Converter built with Python and PyQt. This application allows users to write and preview Markdown content in real-time and export it as a PDF file with a single click.

🚀 Features

✅ Live Markdown Preview – See changes instantly as you type.
✅ PDF Export – Convert your Markdown content to a clean PDF file.
✅ Syntax Highlighting – Supports standard Markdown syntax.
✅ Resizable Layout – Scrollable markdown editor and PDF viewer.
✅ Simple UI – Easy-to-use and intuitive design.

📸 Screenshots



🛠 Installation

1️⃣ Prerequisites

Ensure you have Python installed (>=3.8). You can download it from Python.org.

2️⃣ Clone the Repository

git clone https://github.com/yourusername/Markdown-to-PDF-Converter.git
cd Markdown-to-PDF-Converter

3️⃣ Install Dependencies

pip install -r requirements.txt

▶️ Usage

Run the application with the following command:

python app.py

📦 Creating an Executable (Windows)

To generate a standalone .exe file:

pyinstaller --onefile --windowed app.py

This will create an app.exe inside the dist folder.

🖼 Adding an Icon (Optional)

If you want to add a custom icon to the .exe file:

pyinstaller --onefile --windowed --icon=icon.ico app.py

❌ Troubleshooting

Icon error: If icon.ico is missing, either provide an .ico file or remove --icon=icon.ico from the PyInstaller command.

DLL missing error: Ensure your Python and dependencies are properly installed.

🤝 Contributing

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m 'Add feature')

Push to your branch (git push origin feature-name)

Open a Pull Request 🎉

📄 License

This project is licensed under the MIT License – feel free to use and modify!

Made with ❤️ by Ahsanul Karim

