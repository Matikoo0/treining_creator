import openpyxl


def trening_generator(data,sheet):
    print("xd")



def create_exel_file(NAME:str):
    wb=openpyxl.Workbook()
    zal=wb.active
    zal.title="Założenia"
    sheet1=wb.create_sheet("1 Tydzien")
    wb.save(f"{NAME}.xlsx")


create_exel_file("test")
