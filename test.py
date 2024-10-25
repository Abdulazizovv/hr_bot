from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def create_styled_pdf(filename, data, image_stream=None):
    pdf = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    style_normal = styles["Normal"]
    style_heading = styles["Heading1"]

    # Title
    title = Paragraph("Ma'lumotlar va Tafsilotlar", style_heading)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Basic information table
    basic_info_data = [
        ['Tug\'ilgan Yil', 'Telefon Raqami', 'Soha Bo\'yicha Yo\'nalish', 'Viloyat'],
        [data.get('birth_year'), data.get('phone_number'), data.get('position'), data.get('region')]
    ]

    basic_info_table = Table(basic_info_data, colWidths=[100, 100, 120, 120, 120])
    basic_info_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    basic_info_table.setStyle(basic_info_style)
    elements.append(basic_info_table)
    elements.append(Spacer(1, 12))

    # Work experience
    work_experience_data = [
        ['№', 'Qaysi Korxona', 'Oylik', 'Muddat', 'Sudlanganmisiz'],
        ["1", data.get('first_answer'), data.get('salary'), data.get('second_answer'), data.get('convince')]
    ]

    work_experience_table = Table(work_experience_data, colWidths=[30, 200, 100, 80, 100])
    work_experience_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    work_experience_table.setStyle(work_experience_style)
    elements.append(work_experience_table)
    elements.append(Spacer(1, 12))


    # Software skills
    software_data = [
        ['№', 'Word', 'Excel', 'Boshqa'],
        ['1', data.get('third_answer'), data.get('fourth_answer'), data.get('fifth_answer')]
    ]

    software_table = Table(software_data, colWidths=[30, 100, 100, 100, 100])
    software_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    software_table.setStyle(software_style)
    elements.append(software_table)

    # Save the PDF
    pdf.build(elements)

# Create the PDF with the specified filename
create_styled_pdf("styled_example.pdf")
