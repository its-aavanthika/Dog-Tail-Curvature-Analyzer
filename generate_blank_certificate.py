from PIL import Image

# Create a blank certificate template (white background)
width, height = 800, 600
certificate = Image.new('RGB', (width, height), color='white')
certificate.save('static/certificate_template.png')

print("✅ Blank certificate_template.png created in static/")
