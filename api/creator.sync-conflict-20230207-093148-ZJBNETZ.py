import openpyxl


def trening_generator(data,sheet):
    print("xd")



def create_exel_file(NAME:str):
    wb=openpyxl.Workbook()
    sheet1=wb.create_sheet("Założenia")
    sheet1.title="Założenia"
    wb.save(f"{NAME}.xlsx")


create_exel_file("test")
