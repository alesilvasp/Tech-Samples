from fpdf import FPDF

pdf_w = 210
pdf_h = 297

class CertificateModel(FPDF):

    def lines(self):
        self.set_line_width(0.0)
        self.set_draw_color(10, 54, 157)
        self.rect(2.0, 5.0, 206.0,293.0)
        self.rect(3.0, 6.0, 204.0,291.0) 

    def titles(self):
        self.set_xy(0.0, 5.0)
        self.set_font('Arial', 'B', 32)
        self.set_text_color(10, 54, 157)
        self.cell(w=210.0, h=40.0, align='C', txt="Nome da empresa", border=0)

    def logo_image(self):

        logo_w=36
        logo_h=10

        self.set_xy((pdf_w/2 - logo_w/2), 2)
        self.image(name='https://i.ibb.co/449FLvH/tech-samples-logo.png', link='', w=36, h=10)
    
    def subtitles(self):
        self.set_xy(0.0, 15.0)
        self.set_font('Arial', 'B', 24)
        self.set_text_color(10, 54, 157)
        self.cell(w=210.0, h=60.0, align='C', txt="Dados da amostra", border=0)

    def texts(self, analysis):

        # initial position (mm)
        self.set_xy(10.0, 55.0)
        self.set_text_color(10, 54, 157)
        self.set_font('Arial', '', 16)

        self.cell(w=pdf_w/2, h=10.0, txt=f"Classe do Produto: {analysis['class']['name']} + 'IASDIOAOISDJAOISDJOIASJDIOJA'")
        self.cell(w=pdf_w/2, h=10.0, txt=f"Laudo N°: {analysis['id']}")
        
        self.ln(10)

        self.cell(w=pdf_w/2, h=10.0, txt=f"Lote: {analysis['batch']}")
        self.cell(w=pdf_w/2, h=10.0, txt=f"Data de análise: {analysis['made']}")

        # line break
        self.ln(10)

        # captions
        self.set_draw_color(0, 0, 0)
        self.rect(5.0, 80.0, 200, 24)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 24)
            
        self.cell(w=0, h=24, txt="Tipo de Análise", align='C')

        self.ln(16)
        self.set_font('Arial', '', 16)

        self.cell(w=pdf_w/4 + 10, h=16, txt="Parâmetro")
        self.cell(w=pdf_w/4, h=16, txt="Resultado")
        self.cell(w=pdf_w/4, h=16, txt="Unidade")
        self.cell(w=pdf_w/4, h=16, txt="Status")

        self.ln(10)

        # analysis results
        self.set_text_color(10, 54, 157)

        for type in analysis['class']['types']:

            self.set_font('Arial', 'B', 24)
            
            self.cell(w=0, h=24, txt=f"{type['name']}", align='C')

            self.ln(16)

            for parameter in type['parameters']:
                
                self.set_font('Arial', '', 16)

                self.cell(w=pdf_w/4 + 10, h=16, txt=f"{parameter['name']}")

                self.cell(w=pdf_w/4, h=16, txt=f"{parameter['result']}")

                self.cell(w=pdf_w/4, h=16, txt=f"{parameter['unit']}")

                if parameter['is_approved']: 
                    self.cell(w=pdf_w/4, h=16, txt=f"Aprovado")
                else: 
                    self.cell(w=pdf_w/4, h=16, txt=f"Reprovado")
    
                self.ln(10)

        self.ln(10)

        self.set_font('Arial', 'B', 24)
        self.cell(w=0, h=24, txt=f"Responsável técnico: {analysis['analyst_name']}" )
