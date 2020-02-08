from fpdf impot FPDF

serial_data=['SERIAL NO: 2 Sample No..................0431/17-18........................','Name of customer KSAIL Address.....','Purpose of sampling: Assessment of effluent composition County: Kisumu','Date Sampled.......08/06/2018............Date Received.....................08/06/2018........................','Source............... Kibos distillery (B).........Date compiled.............25/06/2018.......................']
analysis_values = [['PARAMETERS','UNIT','RESULTS','WHO STANDARDS','KEBS STANDARDS'],['PH','pH Scale','5.8','6.5-8.5','6-9'],['PH','pH Scale','5.8','6.5-8.5','6-9'],['PH','pH Scale','5.8','6.5-8.5','6-9'],['PH','pH Scale','5.8','6.5-8.5','6-9']]
spacing=1
pdf = FPDF()
pdf.add_page()
pdf.image('certi_img.png', x=10, y=8, w=40)
pdf.set_font("Arial", size=10)
col_width = pdf.w / 2.7
row_height = pdf.font_size*1.8
pdf.set_x(50)
pdf.cell(col_width*2,row_height*spacing,txt="WATER RESOURCES MANAGEMENT AUTHORITY", border=1,align='C')
pdf.ln(row_height*spacing)
pdf.set_x(50)
pdf.cell(col_width*1.3,row_height*spacing*2,txt="TITLE: Water Sample Analytical Certificate-Effluent Results", border=1,align='C')
pdf.cell(col_width*0.7,row_height*spacing,txt='REF. NO: F/9/1/3', border=1,align='C')
pdf.ln(row_height*spacing)
pdf.set_x(50+col_width*1.3)
pdf.cell(col_width*0.7,row_height*spacing,txt='ISSUE NO: 04', border=1,align='C')
pdf.ln(row_height)
pdf.set_x(50)
pdf.cell(col_width*1.3,row_height*spacing,txt='DEPARTMENT: Technical', border=1,align='C')
pdf.cell(col_width*0.7,row_height*spacing,txt='REV. NO: 03', border=1,align='C')
pdf.ln(row_height*spacing)
pdf.set_x(50)
pdf.cell(col_width*1.3,row_height*spacing,txt='ISSUED BY: DTCM', border=1,align='C')
pdf.cell(col_width*0.7,row_height*spacing,txt='DATE OF ISSUE: 15th April, 2013', border=1,align='C')
pdf.ln(row_height*spacing)
pdf.set_x(50)
pdf.cell(col_width*1.3,row_height*spacing,txt='AUTHORIZED BY: TCM', border=1,align='C')
pdf.cell(col_width*0.7,row_height*spacing,txt='PAGE:3 of 3', border=1,align='C')
pdf.ln(row_height*spacing)
pdf.ln(5)
pdf.set_font("Arial", size=11)
for sd in serial_data:
	pdf.cell(pdf.w,8,txt=sd,align='L')
	pdf.ln(9)
pdf.ln(7)
pdf.set_font("Arial", size=8)
for avs in analysis_values:
	i = 1
	for av in avs:
		if i == 1:
			pdf.cell(pdf.w*0.3,row_height,txt=av,align='C',border=1)
		else:
			pdf.cell(pdf.w*0.15,row_height,txt=av,align='C',border=1)
		i = i + 1
	pdf.ln(row_height)
pdf.set_font("Arial", size=11)
pdf.ln(14)
pdf.cell(pdf.w,8,txt='Name of analyst ................................................................Signature..............................................................',align='L')
pdf.ln(18)
pdf.cell(pdf.w,8,txt='Comments by head of laboratory',align='L')
pdf.ln(14)
pdf.cell(pdf.w,8,txt='Name.................................................................................................................................... ...............',align='L')
pdf.ln(14)
pdf.cell(pdf.w,8,txt='Signature..............................................................................................Date.............................................',align='L')
pdf.ln(20)
pdf.cell(pdf.w,8,txt='Issued by:..............................................................................................',align='C')
pdf.ln(12)
pdf.cell(pdf.w,8,txt='(Deputy Technical Coordination Manager)',align='C')
pdf.ln(25)
pdf.cell(pdf.w,8,txt='Approved by:.............................................................................................',align='C')
pdf.ln(12)
pdf.cell(pdf.w,8,txt='(Technical Coordination Manager)',align='C')
pdf.output("simple_demo.pdf")
