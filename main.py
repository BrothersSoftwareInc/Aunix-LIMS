from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.base        import runTouchApp
from kivy.config      import Config
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang        import Builder
from kivy.utils       import platform
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.button import Button
import json
from threading import Thread
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, ListProperty
import socket
import time
import paho.mqtt.client as paho
from kivy.utils import get_color_from_hex
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
import datetime
from kivy.lib import osc
from kivy.utils import platform
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from functools import partial
from kivy.uix.stacklayout import StackLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.clock import Clock
import json
from fpdf import FPDF



database_dict = {}
test_dict = {}
sample_id = ''
database_data = {}
newsamplescreen1_inputstr = {'Client Name':'','Sample Name':'', 'Sample Type': '','Sample ID':'','Date Sampled':'','Date Received':'','Date Compiled':'','Source':'','Purpose Of Sampling':'','Country':'' }
newsamplescreen2_inputstr = {'TDS':'' ,'EC':'' ,'TSS':'' ,'Oil & grease':'' ,'Heavy metalsAs':'' ,'Hg,Pb':'' ,'Nitrates':'' ,'Nitrites':'' ,'Total Phosphorus':'' ,'total Nitrogen':'' ,'Pesticides and Volatile Substances':'' ,'Ammonia-N':'' ,'BOD':'' ,'COD':'' ,'sulphide':'' ,'Zn':'' ,'Cu':'' ,'Se':'' ,'Total Alkalinity':''}
chemical_tests = ['PH','Color','Turbidity','Permangante value','Conductivity','Iron','Manganese','Calcium','Magnesium','Sodium','Potassium','Total Hardness','Total Alkalinity','Chloride','Fluoride','Nitrate','Nitrite','Ammonia','Total Nitrogen','Sulphate','Orthophosphate','TSS','Free Carbon dioxide','Dissolved Oxygen','TDS']
waste_water_tests = ['Temperature','PH','Conductivity','BOD','COD','Heavy metals-Chromium, Cr','Lead, Pb','Mercury, Hg','Copper, Cu','Cadmium, Cd','Zinc, Zn','Total Alkalinity','TSS','TDS','Oil & Grease','permanganate value','Salinity','Sulphides','Total Nitrogen as N','Total Phosphorous as P','Detergents(MBAS)']
other_tests = ['Pesticides','Free Chlorine','Residual Chlorine','Total & Feacal coliforms','Bact parameter']
tests_list = {'Other Indivisual Analysis':other_tests,'Chemical Analysis':chemical_tests,'Waste Water Analysis':waste_water_tests}
all_test_list = chemical_tests + waste_water_tests + other_tests
pricing= {'PH':200,'Color':200,'Turbidity':300,'Permangante value':500,'Conductivity':300,'Iron':700,'Manganese':700,'Calcium':400,'Magnesium':400,'Sodium':350,'Potassium':350,'Total Hardness':600,'Total Alkalinity':350,'Chloride':300,'Fluoride':400,'Nitrate':500,'Nitrite':500,'Ammonia':500,'Total Nitrogen':600,'Sulphate':400,'Orthophosphate':400,'TSS':400,'Free Carbon dioxide':200,'Dissolved Oxygen':300,'TDS':300,'Pesticides':8000,'Free Chlorine':300,'Residual Chlorine':300,'Total & Feacal coliforms':2000,'Bact parameter': 500,'BOD': 1000,'COD':1000,'Heavy metals-Chromium, Cr':1000,'Lead, Pb':1000,'Mercury, Hg':1000,'Copper, Cu':1000,'Cadmium, Cd':1000,'Zinc, Zn':1000,'Oil & Grease':600,'permanganate value':600,'Salinity':300,'Sulphides':350,'Total Phosphorous':500,'Detergents(MBAS)':1500,'Temperature':200}

for t in all_test_list:
	test_dict[t] = ''

class NewSampleScreenManagement(ScreenManager):
	def __init__(self,**kwargs):
		super(NewSampleScreenManagement, self).__init__(**kwargs)
		global test_dict
		global database_dict
		global sample_id
		global database_data
		for t in all_test_list:
			test_dict[t] = ''
		database_dict = {}
		with open('records.json') as readfile:
			database_data = json.load(readfile)
		print database_data
		database_len = len(database_data.keys())
		sample_id = str(database_len + 1)
		print database_len

class DatabaseScreenManagement(ScreenManager):
	def __init__(self,**kwargs):
		super(DatabaseScreenManagement, self).__init__(**kwargs)
		self.sample_data = {}


class Field(BoxLayout):
	pass

class Sld(Slider):
	pass

class chek(BoxLayout):
	def __init__(self,**kwargs):
		super(chek, self).__init__(**kwargs)


	def on_chk_active(self):
		self.included = 1
		test_dict[self.ids.checklabel.text] = 1


		

class MainScreen(BoxLayout):
	def __init__(self,**kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.data1 = newsamplescreen1_inputstr
		self.data2 = newsamplescreen2_inputstr
		self.new_sample_loaded = False

	def	start_new_sample(self,but):
		global database_dict_arr
		self.ids.screenmanage.clear_widgets()
		self.ids.lab1.color = (1,1,1,1)
		self.ids.lab1.color = (1,1,1,1)
		self.ids.lab1.color = (1,1,1,1)
		but.color = (1,0,0,1)
		database_dict_arr = [{},{},{}]
		self.ids.screenmanage.add_widget(NewSampleScreenManagement())

	def	start_sample_database(self,but):
		self.ids.screenmanage.clear_widgets()
		self.ids.lab1.color = (1,1,1,1)
		self.ids.lab1.color = (1,1,1,1)
		self.ids.lab1.color = (1,1,1,1)
		but.color = (1,0,0,1)
		self.ids.screenmanage.add_widget(DatabaseScreenManagement())

	def	start_certificate(self,but):
		self.ids.screenmanage.clear_widgets()
		self.ids.lab1.color = (1,1,1,1)
		self.ids.lab1.color = (1,1,1,1)
		self.ids.lab1.color = (1,1,1,1)
		but.color = (1,0,0,1)
		self.ids.screenmanage.add_widget(NewSampleScreenManagement())
	
	def load_form(self):
		print 'yes'


class tests(BoxLayout):
	def __init__(self,**kwargs):
		super(tests, self).__init__(**kwargs)

class PriceTag(BoxLayout):
	def __init__(self,**kwargs):
		super(PriceTag, self).__init__(**kwargs)

class NewSampleScreen3(Screen):
	def __init__(self,**kwargs):
		super(NewSampleScreen3, self).__init__(**kwargs)



class NewSampleAnalysisSelection(Screen):
	def __init__(self,**kwargs):
		super(NewSampleAnalysisSelection, self).__init__(**kwargs)
		self.loaded = False

	def scroll_change(self, value):
		print value
		self.ids.scrv.scroll_y = value

	def load_form(self):
		
		if not self.loaded:
			for key in tests_list:
				self.ids.form.bind(minimum_height=self.ids.form.setter('height'))
				self.field_data = []
				self.test_field = tests(size_hint_y=None,height=400)
				self.test_field.ids.lab.text = key
				for analys in tests_list[key]:

					self.field_checks = chek(name=analys)
					self.test_field.ids.checks.add_widget(self.field_checks)
				self.field_data.append(self.test_field)
				self.ids.form.add_widget(self.test_field)
			self.loaded = True

	def slider_change(self,value):
		print value
		if value >= 0:
	#this to avoid 'maximum recursion depth exceeded' error
			self.ids.slider.value=value


	def next(self):
		self.data_dict = {}
		self.parent.transition = SlideTransition(direction='left')
		scr_no = int(self.name) + 1
		scr_no_str = str(scr_no)
		self.parent.current= scr_no_str
		# database_dict_arr[2] = test_dict
		# print database_dict_arr


	def previous(self):
		self.parent.transition = SlideTransition(direction='left')
		scr_no = int(self.name) - 1
		scr_no_str = str(scr_no)
		self.parent.current= scr_no_str

class NewSampleScreen(Screen):
	def __init__(self,**kwargs):
		super(NewSampleScreen, self).__init__(**kwargs)

	def start(self):
		self.parent.transition = SlideTransition(direction='left')
		self.parent.current='1'





class NewSampleDetails(Screen):
	def __init__(self,**kwargs):
		super(NewSampleDetails, self).__init__(**kwargs)
		self.loaded = False
		self.data_dict = {}
		self.sample_id = ''

	def load_form(self):
		#print self.dict
		global sample_id
		if not self.loaded:
			self.field_data = []
			for key in newsamplescreen1_inputstr:
				self.ids.form.bind(minimum_height=self.ids.form.setter('height'))
				self.field = Field(height=110,size_hint_y=None,label_name=key)
				c =  str(sample_id)
				if key == 'Sample ID':
					print 'yes'
					self.field.ids.field_input.text = c
					print c
					print sample_id
				self.field_data.append(self.field)
				self.ids.form.add_widget(self.field)
			self.loaded = True

	def scroll_change(self, value):
		self.ids.scrv.scroll_y = value


	def slider_change(self,value):

		if value >= 0:
	#this to avoid 'maximum recursion depth exceeded' error
			self.ids.slider.value=value

	def next(self):
		global database_dict_arr
		self.data_dict = {}
		self.parent.transition = SlideTransition(direction='left')
		scr_no = int(self.name) + 1
		scr_no_str = str(scr_no)
		self.parent.current= scr_no_str
		for field in self.field_data:
			self.data_dict[field.ids.field_name.text] = field.ids.field_input.text
		database_dict['SampleDetails'] = self.data_dict 
		print self.parent.database_dict

	def previous(self):
		self.parent.transition = SlideTransition(direction='left')
		scr_no = int(self.name) - 1
		scr_no_str = str(scr_no)
		self.parent.current= scr_no_str


class NewSampleAnalysisValues(Screen):
	def __init__(self,**kwargs):
		super(NewSampleAnalysisValues, self).__init__(**kwargs)
		self.loaded = False
		self.last_dict = {}
		for t in all_test_list:
			self.last_dict[t] = ''
		self.field_data = []

	def load_form(self):
		#print self.dict
		if test_dict != self.last_dict:
			self.loaded = False
		if not self.loaded:
			#self.field_data = []
			for key in test_dict:
				if test_dict[key] == 1 and self.last_dict[key] != 1:
					self.last_dict[key] = 1
					self.ids.form.bind(minimum_height=self.ids.form.setter('height'))
					self.field = Field(height=110,size_hint_y=None,label_name=key)
					self.field_data.append(self.field)
					self.ids.form.add_widget(self.field)
			self.loaded = True

	def scroll_change(self, value):
		self.ids.scrv.scroll_y = value


	def slider_change(self,value):

		if value >= 0:
	#this to avoid 'maximum recursion depth exceeded' error
			self.ids.slider.value=value

	def next(self):
		global database_dict_arr
		self.data_dict = {}
		self.parent.transition = SlideTransition(direction='left')
		scr_no = int(self.name) + 1
		scr_no_str = str(scr_no)
		self.parent.current= scr_no_str
		for field in self.field_data:
			self.data_dict[field.ids.field_name.text] = field.ids.field_input.text
		database_dict['AnalysisReport'] = self.data_dict 
		print self.parent.database_dict

	def previous(self):
		self.parent.transition = SlideTransition(direction='left')
		scr_no = int(self.name) - 1
		scr_no_str = str(scr_no)
		self.parent.current= scr_no_str


class Billing(Screen):
	def __init__(self,**kwargs):
		super(Billing, self).__init__(**kwargs)
		self.loaded = False
		self.data_dict = {}
		self.total = 0
		self.last_dict = {}
		self.pricetagdict = {}

	def load_form(self):
		global test_dict
		self.ids.form.clear_widgets()
		self.pricetagdict = {}
		self.total = 0
		for key in test_dict:
			if test_dict[key] == 1:
				self.last_dict[key] = 1
				self.ids.form.bind(minimum_height=self.ids.form.setter('height'))
				testname = key
				testprice = pricing[key]
				pricetag = PriceTag(height=70,size_hint_y = None)
				pricetag.ids.test_name.text = testname
				pricetag.ids.price.text = str(testprice)
				self.total = self.total + testprice
				self.ids.form.add_widget(pricetag)
				self.pricetagdict[testname] = str(testprice)

		totpricetag = PriceTag(height=70, size_hint_y=None)
		totpricetag.ids.test_name.font_size= '18sp'
		totpricetag.ids.test_name.text = 'Total'
		totpricetag.ids.price.text = str(self.total)
		self.pricetagdict['Total'] = str(self.total)
		self.ids.form.add_widget(totpricetag)

		self.loaded = True



	def scroll_change(self, value):
		self.ids.scrv.scroll_y = value


	def slider_change(self,value):

		if value >= 0:
	#this to avoid 'maximum recursion depth exceeded' error
			self.ids.slider.value=value
	
	def submit(self):
		global database_dict
		global database_data
		print 'database_data' 
		print database_data
		database_dict['Pricing'] = self.pricetagdict
		database_dict = {sample_id:database_dict}
		database_data.update(database_dict) 		
		with open('records.json','w') as writefile:
			json.dump(database_data,writefile)
		self.ids.submitbtn.disabled = True
	

	def generate_certi(self):
		global units
		serial_data=['SERIAL NO: 2 Sample No..................'+database_dict[sample_id]['SampleDetails']['Sample ID']+'/18-19........................','Name of customer  '+database_dict[sample_id]['SampleDetails']['Client Name'],'Purpose of sampling: '+database_dict[sample_id]['SampleDetails']['Purpose Of Sampling']+' County: '+database_dict[sample_id]['SampleDetails']['Country'],'Date Sampled.......'+database_dict[sample_id]['SampleDetails']['Date Sampled']+'............Date Received.....................'+database_dict[sample_id]['SampleDetails']['Date Received']+'........................','Source............... '+database_dict[sample_id]['SampleDetails']['Source']+'.........Date compiled.............'+database_dict[sample_id]['SampleDetails']['Date Compiled']+'.......................']
		analysis_values = [['PARAMETERS','UNIT','RESULTS','WHO STANDARDS','KEBS STANDARDS']]
		for anal_vals in database_dict[sample_id]['AnalysisReport']:
			anal_arr = [anal_vals,'',str(database_dict[sample_id]['AnalysisReport'][anal_vals]),'','']
			analysis_values.append(anal_arr)
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
		pdf.output("demo_certi.pdf")


	def previous(self):
		self.parent.transition = SlideTransition(direction='left')
		scr_no = int(self.name) - 1
		scr_no_str = str(scr_no)
		self.parent.current= scr_no_str

class DatabaseDetailWidget(Label):
	pass

class DatabaseSampleScreen(Screen):
	def __init__(self,**kwargs):
		super(DatabaseSampleScreen, self).__init__(**kwargs)
		
	def scroll_change(self, value):
		self.ids.scrv.scroll_y = value


	def slider_change(self,value):

		if value >= 0:
	#this to avoid 'maximum recursion depth exceeded' error
			self.ids.slider.value=value

	def load_form(self):
		self.ids.form.clear_widgets()
		for key in self.parent.sample_data:
			self.ids.form.bind(minimum_height=self.ids.form.setter('height'))
			self.category = DatabaseDetailWidget(text=key,height=60,size_hint_y=None,font_size='20')
			self.ids.form.add_widget(self.category)
			for subkey in self.parent.sample_data[key]:
				self.ids.form.bind(minimum_height=self.ids.form.setter('height'))
				self.subcategory = DatabaseDetailSubWidget(item=subkey,subitem=str(self.parent.sample_data[key][subkey]),height=40,size_hint_y=None)			
				self.ids.form.add_widget(self.subcategory)

	
	def previous(self):
		self.parent.transition = SlideTransition(direction='left')
		self.parent.current = 'databasemainscreen'



class DatabaseDetailSubWidget(BoxLayout):
	pass
class DatabaseWidget(BoxLayout):
	pass

class Loading(Screen):
	def __init__(self,**kwargs):
		super(Loading, self).__init__(**kwargs)	
		Clock.schedule_once(self.goto_database,1)

	def goto_database(self,dt):
		print 'yes reached'
		self.parent.transition = SlideTransition(direction='left')
		print 'yes'
		self.parent.current = 'databasemainscreen'

class DatabaseMainScreen(Screen):
	def __init__(self,**kwargs):
		super(DatabaseMainScreen, self).__init__(**kwargs)	

	
	def scroll_change(self, value):
		self.ids.scrv.scroll_y = value


	def slider_change(self,value):

		if value >= 0:
	#this to avoid 'maximum recursion depth exceeded' error
			self.ids.slider.value=value

	def load_form(self):
		self.ids.form.clear_widgets()
		self.parent.sample_id = {}
		with open('records.json') as readfile:
			self.newdata = json.load(readfile)
			self.currentkey = ''
		for key in self.newdata:
			self.ids.form.bind(minimum_height=self.ids.form.setter('height'))
			sampledetails = self.newdata[key]['SampleDetails']
			sampleanalysis = self.newdata[key]['AnalysisReport']
			samplepricing = self.newdata[key]['Pricing']
			subheading_str = 'Sample ID: ' + sampledetails['Sample ID'] + '    Client Name: '+ sampledetails['Client Name'] + '    Sample Type: ' + sampledetails['Sample Type']
			self.datawidget = DatabaseWidget(heading=sampledetails['Sample Name'],subheading=subheading_str,height=100,size_hint_y=None,samplekey=key)
			self.datawidget.ids.viewbut.bind(on_press=self.view)
			self.ids.form.add_widget(self.datawidget)

	def view(self,instance):
			
			self.parent.sample_data = self.newdata[instance.sample]
			self.parent.transition = SlideTransition(direction='left')
			self.parent.current = 'databasesamplescreen'


presentation = Builder.load_file("layout.kv")

	




class MyApp(App):

	def build(self):
	    return presentation


if __name__ == '__main__':
	MyApp().run()
