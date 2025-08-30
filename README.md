# Text to PowerPoint Generator

Transform your text, markdown, or prose into beautiful PowerPoint presentations using AI and custom templates. This web application intelligently analyzes your content and generates structured slides while preserving the visual style of your uploaded PowerPoint template.

## ✨ Features

- **AI-Powered Content Analysis**: Uses LLM APIs to intelligently structure text into logical slides
- **Template Style Preservation**: Maintains colors, fonts, layouts, and images from your uploaded template
- **Flexible Input**: Accepts markdown, prose, or any text format
- **Custom Guidance**: Optional instructions for tone, structure, or use case
- **Multiple LLM Support**: Works with OpenAI, Anthropic, and Google Gemini
- **Secure**: Never stores or logs your API keys
- **Instant Download**: Get your generated presentation as a .pptx file

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- An LLM API key (OpenAI recommended for best results)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Bonus_P1
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8000`

## 📖 Usage

### Step 1: Enter Your Content
- Paste or type your text content (minimum 100 characters)
- Add optional guidance (e.g., "turn into an investor pitch deck")

### Step 2: Provide API Credentials
- Enter your LLM API key
- Select your preferred LLM provider

### Step 3: Upload Template
- Upload a PowerPoint template (.pptx or .potx file)
- The generated presentation will use this template's styling

### Step 4: Generate & Download
- Click "Generate Presentation"
- Download your new PowerPoint file

## 🏗️ Architecture

### Backend (FastAPI)
- **`/generate` endpoint**: Handles text processing and PowerPoint generation
- **LLM Integration**: Processes text using user-provided API keys
- **PowerPoint Generation**: Uses `python-pptx` to create presentations
- **Template Processing**: Extracts and applies styles from uploaded templates

### Frontend (HTML/JavaScript)
- **Responsive Design**: Clean, modern interface using Tailwind CSS
- **Form Validation**: Ensures proper input before submission
- **Progress States**: Loading, success, and error handling
- **File Download**: Automatic download trigger for generated presentations

### Key Technologies
- **FastAPI**: Modern, fast web framework for Python
- **python-pptx**: PowerPoint file manipulation
- **OpenAI API**: LLM integration for content structuring
- **Tailwind CSS**: Utility-first CSS framework

## 🔧 Configuration

### Environment Variables
Create a `.env` file for local development:
```env
OPENAI_API_KEY=your_key_here
```

### API Providers
The application supports multiple LLM providers:
- **OpenAI** (GPT-3.5/4) - Recommended
- **Anthropic** (Claude)
- **Google Gemini**

## 📁 Project Structure

```
Bonus_P1/
├── main.py              # FastAPI backend application
├── index.html           # Frontend interface
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── LICENSE             # MIT License
└── temp_files/         # Temporary file storage (auto-created)
```

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment
1. **Backend**: Deploy to Render, Railway, or any Python hosting service
2. **Frontend**: Host `index.html` on Vercel, Netlify, or any static hosting
3. **Update API URLs**: Modify frontend to point to your deployed backend

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## 🧪 Testing

### Manual Testing
1. Start the application
2. Open the web interface
3. Test with sample text and template
4. Verify PowerPoint generation and download

### Sample Data
- **Text**: Any long-form content (articles, reports, notes)
- **Templates**: Standard PowerPoint templates (.pptx/.potx)
- **Guidance**: "professional presentation", "investor pitch", "research summary"

## 🔒 Security Features

- **No API Key Storage**: Keys are never stored or logged
- **File Validation**: Only accepts PowerPoint file formats
- **Temporary Storage**: Generated files are cleaned up automatically
- **CORS Support**: Configurable for production deployment

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your API key is correct
   - Check API provider status
   - Ensure sufficient API credits

2. **Template Issues**
   - Use standard .pptx/.potx formats
   - Avoid corrupted or password-protected files
   - Ensure template has proper slide layouts

3. **Generation Failures**
   - Check minimum text length (100 characters)
   - Verify template file upload
   - Check browser console for errors

### Debug Mode
Enable debug logging by modifying `main.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- python-pptx for PowerPoint manipulation
- OpenAI for LLM capabilities
- Tailwind CSS for the beautiful UI components

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the code comments for implementation details

---

**Happy Presenting!** 🎯📊
