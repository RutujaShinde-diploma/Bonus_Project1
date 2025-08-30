# Technical Write-up: Text to PowerPoint Generator

## How Input Text is Parsed and Mapped to Slides

The application uses a sophisticated approach to transform raw text into structured slide content:

### 1. **LLM-Powered Content Analysis**
The core of our text parsing relies on Large Language Models (specifically OpenAI's GPT models) to intelligently analyze and structure content. When a user submits text, the system:

- **Sends the text to the LLM** with a carefully crafted prompt that requests JSON-formatted slide structure
- **Uses the optional guidance** (e.g., "investor pitch deck") to inform the LLM's decision-making process
- **Generates a structured response** containing slide titles and bullet points in a consistent format

### 2. **Intelligent Slide Structure Generation**
The LLM processes the input text and returns a JSON array where each slide contains:
- **Title**: A concise, descriptive heading for the slide
- **Content**: An array of bullet points or content items that logically group together

The system automatically determines the optimal number of slides (typically 3-8) based on content length and complexity, ensuring that information is distributed evenly and logically across the presentation.

### 3. **Fallback Mechanism**
If the LLM API call fails or returns invalid JSON, the system implements a robust fallback:
- **Text segmentation**: Splits the input text into chunks of approximately 50 words per slide
- **Automatic titling**: Creates slide titles from the first few words of each chunk
- **Content preservation**: Ensures no information is lost, even when AI processing fails

## How the App Applies Visual Style and Assets from the Template

### 1. **Template Style Extraction**
The application preserves the visual identity of uploaded PowerPoint templates through:

- **Layout preservation**: Uses the template's existing slide layouts (slide_layouts[1] for content slides)
- **Style inheritance**: Automatically applies the template's color schemes, fonts, and formatting
- **Master slide utilization**: Leverages the template's master slide definitions for consistent styling

### 2. **Image and Asset Reuse**
Rather than generating new images with AI (as per requirements), the system:

- **Preserves existing images**: Maintains all images, graphics, and visual elements from the original template
- **Applies template branding**: Ensures the generated presentation maintains the professional look and feel of the uploaded template
- **Consistent visual hierarchy**: Uses the template's predefined color schemes and typography

### 3. **Smart Content Placement**
The generated slides are intelligently structured within the template's design framework:

- **Title positioning**: Automatically places slide titles in the designated title areas
- **Content formatting**: Formats bullet points and text content according to the template's content placeholders
- **Layout adaptation**: Adapts to different template layouts while maintaining visual consistency

### 4. **Template Compatibility**
The system handles various template types and complexities:

- **Standard templates**: Works seamlessly with common PowerPoint templates
- **Custom layouts**: Adapts to templates with unique slide layouts and designs
- **Professional themes**: Preserves corporate branding and design standards

This approach ensures that users can upload their company templates, brand guidelines, or custom designs and receive generated presentations that look as if they were created by a professional designer using the same template, while maintaining the content structure and flow determined by AI analysis of their input text.

The result is a presentation that combines the intelligence of AI content structuring with the visual polish and brand consistency of professional PowerPoint templates.
