
from django.http.response import FileResponse
from source.models import Source,Event


import xlsxwriter
import io
from datetime import datetime,timedelta
import calendar

def createExcelFile(date):

    output      = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    currentDate = datetime.strptime(date, '%Y-%m-%d')
    daysInMonth= calendar.monthrange(currentDate.year, currentDate.month)[1]

    worksheet = workbook.add_worksheet('month')
    worksheet.set_default_row(20)

    headerCell = workbook.add_format({
        'bold': 1,
        # 'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#F5F5F5'})

    employeeCell = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#F5F5F5'})

    row = 4
    col = 0
    ## start  header ##########
    # set width cell
    worksheet.set_column(0, 0, 25)

    worksheet.write(3, col, 'Source Name',headerCell)
    col = 1

    sickIndex = col

    ## end header ############
    col = 0
    row = 4
    sources = Source.objects.filter(user=1)
    dt = datetime.strptime(date, '%Y-%m-%d')
    for source in sources:
        events = Event.objects.filter(
                        source__id=source.id,
                        date__year__gte=dt.year,
                        date__month__gte=dt.month,
                        date__year__lte=dt.year,
                        date__month__lte=dt.month)
        worksheet.write(row, col, source.name ,employeeCell)
        col +=1
        for day in range(1,daysInMonth+1):
            if events.filter(date__day__exact=day).exists():
                worksheet.write(row, col, str(day) ,employeeCell)
            else:
                worksheet.write(row, col,'' ,employeeCell)

            col +=1
        col = 0
        row +=1

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data