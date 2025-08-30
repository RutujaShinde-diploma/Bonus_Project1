# Deployment Guide

## 🚀 Quick Deployment Options

### Option 1: Render (Recommended for Backend)

1. **Fork/Clone** this repository to your GitHub account
2. **Sign up** for [Render](https://render.com) (free tier available)
3. **Create New Web Service** from your GitHub repo
4. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Environment Variables**: Add your API keys if needed
5. **Deploy** and get your backend URL

### Option 2: Railway

1. **Sign up** for [Railway](https://railway.app)
2. **Connect** your GitHub repository
3. **Deploy** automatically
4. **Get** your backend URL

### Option 3: Vercel (Frontend Only)

1. **Upload** `index.html` to [Vercel](https://vercel.com)
2. **Update** the fetch URL in the HTML to point to your backend
3. **Deploy** and get your frontend URL

## 🔧 Environment Setup

### Backend Environment Variables

```bash
# Optional: For development
OPENAI_API_KEY=your_key_here
PORT=8000
```

### Frontend Configuration

Update the fetch URL in `index.html`:

```javascript
// Change this line in the JavaScript
const response = await fetch('https://your-backend-url.com/generate', {
    method: 'POST',
    body: formData
});
```

## 📁 File Structure for Deployment

```
Bonus_P1/
├── main.py              # Backend API
├── requirements.txt     # Python dependencies
├── index.html          # Frontend (can be hosted separately)
├── README.md           # Documentation
├── LICENSE             # MIT License
└── temp_files/         # Auto-created temp directory
```

## 🌐 CORS Configuration

The backend is already configured with CORS for all origins. For production, you may want to restrict this:

```python
# In main.py, update CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🔒 Security Considerations

- **API Keys**: Never commit API keys to your repository
- **File Uploads**: Consider adding file size limits for production
- **Rate Limiting**: Add rate limiting for production use
- **HTTPS**: Always use HTTPS in production

## 📊 Monitoring

### Health Check Endpoint

Your deployed app includes a health check at `/health`:

```bash
curl https://your-app-url.com/health
# Returns: {"status": "healthy"}
```

### Logs

Check your hosting platform's logs for:
- API requests
- Error messages
- Performance metrics

## 🚨 Troubleshooting

### Common Issues

1. **Port Binding**: Ensure your hosting platform allows the port you're using
2. **Dependencies**: Make sure all requirements are in `requirements.txt`
3. **File Permissions**: Ensure the app can create the `temp_files` directory
4. **CORS**: Check browser console for CORS errors

### Debug Mode

Enable debug logging by adding to `main.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Scaling Considerations

- **File Storage**: For production, consider using cloud storage (S3, etc.)
- **Database**: Add a database for user management if needed
- **Caching**: Implement Redis for API response caching
- **Load Balancing**: Use multiple instances behind a load balancer

## 🔄 Continuous Deployment

### GitHub Actions Example

```yaml
name: Deploy to Render
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Render
        uses: johnbeynon/render-deploy-action@v0.0.1
        with:
          service-id: ${{ secrets.RENDER_SERVICE_ID }}
          api-key: ${{ secrets.RENDER_API_KEY }}
```

## 📞 Support

- Check the main README for troubleshooting
- Review the technical writeup for implementation details
- Open issues on GitHub for bugs or feature requests

---

**Happy Deploying!** 🚀
