#! /usr/bin/env python  

from fpdf import FPDF
import pathlib
import webbrowser
from coreapps.models.query import encoding




data_hasil_perhitungan = (
    {"Nama Peserta" : "andri","No Tes":"3351","Tanggal Tes":"20/06/2019",
        "Jenis Kelamin":"Laki-Laki","Tanggal Lahir":"16/03/1995","Pendidikan Terakhir":"S1",
        "Jurusan Pendidikan":"Psikologi","Kota":"Jakarta",
        "Perusahaan / Instansi":"PT Cipta Semesta ALam","Posisi / Jabatan":"Senior IT"
        },
    {"Openness to Experience" : "2.6","Unconvenionality":"3.4","Creativity":"4.5","Inquisitiveness":"3.7","Aesthetic Appreciation":""},
    {"Conscientiousness":"4.5","Prudence":"1.6","Perfectionism":"3.6","Diligence":"3.2","Organization":"4.6"},
    {"Agreeableness":"3.55","Patience":"4.3","Flexibility":"2.8","Gentleness":"2.6","Forgiveness":"2.44"},
    {"Extraversion":"2.7","Liveliness":"4.9","Sociability":"4.2","Social Boldness":"2.56","Social Self Esteem":"2.33"},
    {"Emotionality":"1.5","Sentimentality":"2.55","Dependence":"3.7","Anxiety":"4.6","Fearfulness":"4.56"},
    {"Honesty & Humility" : "3.22","Modesty":"2.14","Greed Avoidance":"4.33","Fairness":"3.22","Sincerity":"2.66"},
    {"Interstitial":"3.2"},
)



print(type(data_hasil_perhitungan))
print(data_hasil_perhitungan[1].keys())


def pdf_data(biodata,nilai):
    data_hasil_perhitungan = biodata
    data_dimensi = nilai
    
    pdf = FPDF(orientation="P",unit = 'mm',format = 'A4')

    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_top_margin(15)

    ah = pdf.font_size

    height = 2*pdf.b_margin
    width  = 2*pdf.l_margin

    pdf.cell(0,ah,"GAMBARAN KEPRIBADIAN",border = "B",ln=2,align = "C")
    # pdf.line(75,13,135,13)

    image1="binadata.png"
    pdf1 = "tuto1d.pdf"
    image2 ="image1.png"

    pdf.set_font('Arial', 'B', 11)

    pdf.ln(5)
    epw = pdf.w-2*pdf.l_margin
    th = pdf.font_size

    name_loc = str(pathlib.Path.cwd()/"controllers/reporting")
    print (name_loc)
    pdf.image(name_loc+"/"+image1,x=140,y=23,w=50,h=25,type="PNG")

    # menyajikan biodata untuk di tampilkan
    pdf.cell(50,th,"No Tes Peserta",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,str(data_hasil_perhitungan[0]),0,1)

    pdf.cell(50,th,"Tanggal Tes",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[1],0,1)

    pdf.cell(50,th,"Nama Peserta",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[2],0,1)

    pdf.cell(50,th,"Jenis Kelamin",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[3],0,1)

    pdf.cell(50,th,"Tanggal Lahir",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[4],0,1)

    pdf.cell(50,th,"Pendidikan Terakhir",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[5],0,1)

    pdf.cell(50,th,"Jurusan Pendidikan",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[6],0,1)

    pdf.cell(50,th,"Kota",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[7],0,1)

    pdf.cell(50,th,"Perusahaan / Instansi",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[8],0,1)

    pdf.cell(50,th,"Posisi / Jabatan",0,0)
    pdf.cell(3,th,":",0,0)
    pdf.cell(50,th,data_hasil_perhitungan[9],0,1)

    pdf.ln(5)

    pdf.cell(0,th,"Grafik HEXACO",0,1,"C")

    pdf.image(name_loc+"/"+image2,x=10,y=68,w=180,h=90,type="PNG")


    # pdf.multi_cell(20, th, 'Hello World! bisa ngggak',1,align = 'L')
    # pdf.cell(40, 0, 'Powered by FPDF.', 1, ln = 2,align =  'L')
    # pdf.ln(5)
    # pdf.cell(80 , 0,"disini data dari binakarir akan di sajikan",1,ln = 2,align = "L")

    # print (data_hasil_perhitungan)
    data_header = [["Aspek","Nilai","Kategori","Definisi","Ciri-ciri"]]
  
    # data_dimensi = []
    # for data in data_hasil_perhitungan:
    #     data_1 = data_hasil_perhitungan.index(data)
    #     if data_1 == 0:
    #         pass

    #     else :
    #         for key,value in data.items():
    #             data_dimensi.append([key,value,value,value])
    #     # print (f"this is {data_1}")
    # print (data_dimensi)

    epw = pdf.w - 2*pdf.l_margin
    print (pdf.l_margin)
    
    # Set column width to 1/4 of effective page width to distribute content 
    # evenly across table and page
    th = pdf.font_size

    col_width = epw/4
    pdf.ln(90)

    i = 0
    pdf.set_font('Arial', 'B', 11)

    pdf.cell(0,th,"Tabel Interpretasi",0,1,"C")

    pdf.set_font('Arial', 'B', 8)
    pdf.ln(4)

    pdf.ln(1)

    for datum in data_header:

        # Enter data in colums
        # pdf.cell(col_width, 2*th, str(datum), border=1)
        # Save top coordinate
        top = pdf.y
        # Calculate x position of next cell
        offset = pdf.x + 35
        pdf.multi_cell(35,10,str(datum[0]),1,"C")
        # Reset y coordinate
        pdf.y = top
        # Move to computed offset
        pdf.x = offset 
        pdf.multi_cell(15,10,str(datum[1]),1,"C")
        # pdf.ln(th)
        # Calculate x position of next cell
        pdf.y = top
        offset = pdf.x  + 50

        pdf.x = offset 
        pdf.multi_cell(15,10,str(datum[2]),1,"C")
        # pdf.ln(th)
        # Calculate x position of next cell
        pdf.y = top
        offset = pdf.x  + 65

        # Move to computed offset
        pdf.x = offset 
        pdf.multi_cell(60,10,str(datum[3]),1,"C")

        pdf.y = top
        offset = pdf.x  + 125

        # Move to computed offset
        pdf.x = offset 
        pdf.multi_cell(50,10,str(datum[4]),1,"C")



        # pdf.ln(th)    
    pdf.set_font('Arial', '', 8)

    pdf.set_auto_page_break(0)
    page_break_1 = 3
    page_break_2 = 11
    page_break_3  = 19
    page_break_4  = 27

    tinggi_kolom = 30
    # pdf.write("dsfsf")
    ujung_bawah = 175

    for datum in data_dimensi:
        print ( data_dimensi.index(datum))
        if data_dimensi.index(datum)%5 == 0:
            pdf.multi_cell(ujung_bawah,1,"","T",0)
            pass
        elif data_dimensi.index(datum) == page_break_1 :
            # pdf.multi_cell(ujung_bawah,1,"","T",0)
            pdf.add_page("P")
        elif data_dimensi.index(datum) == page_break_2 :
            # pdf.multi_cell(ujung_bawah,1,"","T",0)
            pdf.add_page("P")
 
        elif data_dimensi.index(datum) == page_break_3 :
            # pdf.multi_cell(ujung_bawah,1,"","T",0)
            pdf.add_page("P")

        elif data_dimensi.index(datum) == page_break_4 :
            # pdf.multi_cell(ujung_bawah,1,"","T",0)
            pdf.add_page("P")


            # pdf.ln(5)
        # Enter data in colums
        # pdf.cell(col_width, 2*th, str(datum), border=1)
        # Save top coordinate
        top = pdf.y
        # Calculate x position of next cell
        offset = pdf.x + 35
        if data_dimensi.index(datum) % 5 == 0:
            # pdf.ln(th)
            pdf.set_font('Arial', 'B', 8)
            pdf.multi_cell(50,tinggi_kolom,str(datum[0]),"T,L,R",0)
            pdf.multi_cell(ujung_bawah,1,"","T",0)

            if data_dimensi.index(datum) == 30:
                pdf.multi_cell(ujung_bawah,1,"","",0)
                # print("kesini")

            pdf.set_font('Arial', '', 8)



        else :
            pdf.multi_cell(50,tinggi_kolom,str(datum[0]),"T,L,R",0)
            pdf.multi_cell(ujung_bawah,1,"","T",0)

        # Reset y coordinate
        pdf.y = top
        # Move to computed offset
        pdf.x = offset 
        pdf.multi_cell(15,tinggi_kolom,str(datum[1]),"T,L,R","C")

       # Calculate x position of next cell
        pdf.y = top
        offset = pdf.x  + 50

        # Move to computed offset
        pdf.x = offset 

        pdf.multi_cell(15,tinggi_kolom,str(datum[4]),"T,L,R","C")

 
        # pdf.ln(th)
        # Calculate x position of next cell
        pdf.y = top
        offset = pdf.x  + 65

        # Move to computed offset
        pdf.x = offset 

        pdf.multi_cell(60,3,str(datum[2]),"T,L,R",0)

        pdf.y = top
        offset = pdf.x  + 125

        # Move to computed offset
        pdf.x = offset 
        pdf.multi_cell(50,3,str(datum[3]),"T,L,R",0)

        pdf.y = top
        offset = pdf.x  + 125

        # Move to computed offset
        pdf.x = offset 
        pdf.multi_cell(50,tinggi_kolom,"","L,R",0)


        # pdf.ln(th)

    pdf.output(str(name_loc)+"/"+str(pdf1), 'F')
    # webbrowser.open_new(name_loc+"/"+pdf1)