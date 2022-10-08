
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

    sourceCell = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#F5F5F5',
        })

    row = 4
    col = 0
    ## start  header ##########
    # set width cell
    worksheet.set_column(0, 0, 25)

    worksheet.write(3, col, 'Source Name',headerCell)
    col = 1
    ## end header ############

    col = 0
    row = 4
    sources = Source.objects.filter(user=1)
    cellColor = ['#A52A2A','#7FFF00','#6495ED','#00FFFF','#B8860B','#006400','#483D8B']
    dt = datetime.strptime(date, '%Y-%m-%d')
    for source in sources:
        events = Event.objects.filter(
                        source__id=source.id,
                        date__year__gte=dt.year,
                        date__month__gte=dt.month,
                        date__year__lte=dt.year,
                        date__month__lte=dt.month)
        worksheet.write(row, col, source.name ,sourceCell)
        col +=1
        for day in range(1,daysInMonth+1):

            cell_format = workbook.add_format()
            if events.filter(date__day__exact=day).exists():
                event = events.filter(date__day__exact=day).first()
                cell_format = workbook.add_format({
                    'bold': 1,
                    'border': 1,
                    'align': 'center',
                    'valign': 'vcenter',
                    'fg_color': '#F5F5F5',
                    'bg_color': '#7FFF00',
                    })
                print(cellColor[event.color])
                cell_format.set_bg_color(cellColor[event.color])
                worksheet.write(row, col, str(day) ,cell_format)
            else:
                worksheet.write(row, col,'' ,sourceCell)

            col +=1
        col = 0
        row +=1

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data