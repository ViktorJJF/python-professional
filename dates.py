from datetime import datetime

def run():
    # my_date=datetime.date.today()
    date=datetime.utcnow()
    print('date: ', date)
    # print('my_date: ', my_date)

if __name__=='__main__':
    run()