from datetime import datetime

import pytz

bogota_timezone=pytz.timezone("America/Santiago")
bogota_date=datetime.now(bogota_timezone)

print('bogota_date: ', bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))