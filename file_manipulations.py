# imports
from openpyxl import load_workbook, Workbook
from openpyxl.styles import NamedStyle, Font
# from openpyxl.styles.colors import BLUE

dest_filename = "Human Design Data.xlsx"

# read in a file - allow them to choose a file

# export to XLSX


def create_workbook(info2prop: dict):
    """
    This function takes in a file name string and sets up
    the empty workbook with which to add data to.
    It returns the Workbook object to manipulate the data.
    """
    def create_style(wb):
        bold = NamedStyle(name="bold")
        bold.font = Font(bold=True)
        wb.add_named_style(bold)

    def create_sheets(new_wb: Workbook, sheets: list, data_dict: dict):
        for sheet in sheets:
            wbs = new_wb.create_sheet(sheet)

            cols = list()
            if sheet == "Type":
                cols = ["Type", "Strategy", "Signature", "Not-Self", "Pages"]
            elif sheet == "Centers":
                cols = ["Center", "Explanations", "Pages", "Definition", "Gates"]

            if len(cols) == 0:
                print("There was an issue with creating sheets!")
            else:
                # row = sheet.row_dimensions[1]
                dct_list = data_dict[sheet]
                # for col in wb_sheet.iter_cols(min_row=1, max_col=len(cols), max_row=2):
                #     loc = 0
                #     for cell in col:
                #         wbs[cell] = cols[loc]
                #         wbs[cell].style = 'bold'
                #         wbs.cell(row=2, column=col)
                #         loc += 1
                for idx, col_name in enumerate(cols):
                    wbs.cell(row=1, column=idx+1).value = col_name
                    for idx2, item in enumerate(dct_list):
                        idx2 += 1
                        wbs.cell(row=1+idx2, column=idx+1).value = item[col_name]

    workbook = Workbook()
    create_style(workbook)
    sheet_list = ["Type", "Centers"]
    create_sheets(workbook, sheet_list, info2prop)
    return workbook


def write2file(file_type: int, data_lst: dict):
    if file_type == 1:  # XLSX file
        wb = create_workbook(data_lst)
        wb.save(dest_filename)
    else:
        print("Other file types (like exporting to Google sheets) are not yet written.")

# export to Google sheet
