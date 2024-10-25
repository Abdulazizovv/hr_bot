import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from bot.data.config import CHANNEL_ID
from bot.loader import dp
from PIL import Image as PilImage


async def create_pdf_with_tables(filename, data, image_stream=None):
    buffer = io.BytesIO()  # In-memory buffer
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # Title with enhanced style
    title = Paragraph("<b><font size=16 color='darkblue'>Foydalanuvchi Ma'lumotlari</font></b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 20))

    # Define a utility function to create and style tables
    def create_table(data, col_widths):
        table = Table(data, colWidths=col_widths)
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        table.setStyle(table_style)
        return table

    # Adding image if available using Pillow
    if image_stream:
        try:
            # Use Pillow to open the image
            image_stream.seek(0)
            pil_image = PilImage.open(image_stream)
            
            # Convert to a format that ReportLab can handle (JPEG or PNG)
            img_buffer = io.BytesIO()
            pil_image.save(img_buffer, format="PNG")  # Save in PNG format
            img_buffer.seek(0)
            
            # Use ReportLab's Image with the modified buffer
            img = Image(img_buffer, 2*inch, 2*inch)
            img.hAlign = 'LEFT'  # Align to the left
            elements.append(img)
            elements.append(Spacer(1, 20))  # Add a spacer after the image to separate it from the next content
        except Exception as e:
            elements.append(Paragraph(f"Error displaying image: {e}", styles["Normal"]))

    # Basic information table
    basic_info_data = [
        ['Ism Familya', data.get('full_name')],
        ['Telefon raqam', data.get('phone_number')],
        ['Tug\'ilgan yil', data.get('birth_year')],
        ['Yo\'nalish', data.get('position')],
        ['Hudud', data.get('region')],
        ['Millat', data.get('nationality')],
        ['Ma\'lumot', data.get('education')],
        ['Oilaviy holat', data.get('marriage')],
    ]
    elements.append(Paragraph("<b>Asosiy Ma'lumotlar</b>", styles["Heading2"]))
    elements.append(create_table(basic_info_data, [150, 300]))
    elements.append(Spacer(1, 20))

    # Work experience table
    work_experience_data = [
        ['Ish tajribasi', data.get('experience')],
        ['Oylik maosh', data.get('salary')],
        ['Muddat', data.get('first_answer')],
        ['Sudlanganmi', data.get('convince')],
    ]
    elements.append(Paragraph("<b>Ish Tajribasi</b>", styles["Heading2"]))
    elements.append(create_table(work_experience_data, [150, 300]))
    elements.append(Spacer(1, 20))

    # Skills and languages table
    skills_data = [
        ['Haydovchilik guvohnomasi', data.get('driver_license')],
        ['Shaxsiy avtomobil', data.get('has_car')],
        ['Word dasturi bilish darajasi', data.get('third_answer')],
        ['Excel dasturi bilish darajasi', data.get('fourth_answer')],
        ['Boshqa dasturlar bilish darajasi', data.get('fifth_answer')],
    ]
    elements.append(Paragraph("<b>Ko'nikmalar va Dasturlar</b>", styles["Heading2"]))
    elements.append(create_table(skills_data, [200, 250]))
    elements.append(Spacer(1, 20))

    # Save the PDFfile_name, data.get("image")
    pdf.build(elements)
    buffer.seek(0)
    
    # Save the PDF to file
    with open(filename, 'wb') as pdf_file:
        pdf_file.write(buffer.getvalue())
    
    buffer.seek(0)  # Reset the buffer for further use
    return buffer  # Return buffer for uploading



async def upload_to_channel(pdf_buffer, image_file_id, caption_text):
    # Upload PDF
    pdf_message = await dp.bot.send_document(chat_id=CHANNEL_ID, document=("data.pdf", pdf_buffer), caption=caption_text)
    pdf_file_id = pdf_message.document.file_id

    # Upload Image if available
    image_file_id_uploaded = None
    if image_file_id:
        image_message = await dp.bot.send_photo(chat_id=CHANNEL_ID, photo=image_file_id)
        image_file_id_uploaded = image_message.photo[-1].file_id

    return pdf_file_id, image_file_id_uploaded