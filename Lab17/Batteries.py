class MobilePhone():

    nokiaN95 = list()

    def __init__(self,model='',company=None,price=0,owner='',idle_time=0,hours_talked=0,inch_size=0):  
        self.model=model
        self.company=company
        self.price=price
        self.owner=owner
        self.idle_time=idle_time
        self.hours_talked=hours_talked
        self.inch_size=inch_size
    
    def info(self):
        print(f'''Info about {self.model}:  
        Company {self.company}
        Price {self.price}
        Owner {self.owner}
        idle time {self.idle_time}
        hours talked {self.hours_talked}
        inch size {self.inch_size}''')

class GSM():
    callHistory = []
    def __init__(self,date,start,length):
        self.call_date = date
        self.startof_call = start
        self.call_length = length #seconds
    def add_call(self):
        GSM.callHistory.append(self.__dict__)
    def remove_calls():
        GSM.callHistory = []
    def gsm_return(self):
        return(str(self))
    def sum_call_price(price: float):
        calls_amount = len(GSM.callHistory)
        print('Price for all calls: {:.3f}EUR'.format(calls_amount*price))
    
class GSM_Test():
    list_of_phones = list()
    def phones(GSM_Class):
        GSM_Test.list_of_phones.append(GSM_Class('Gosho', 'Python', 'Programing', 'NetIT', 'python@org.bg', '089888888'))
        GSM_Test.list_of_phones.append(GSM_Class('Pesho', 'Java', 'Programing', 'NetIT', 'java@org.bg', '087888888'))
        GSM_Test.list_of_phones.append(GSM_Class('Acho', 'JavaScript', 'Programing', 'NetIT', 'jacasvript@org.bg', '089888888'))
        GSM_Test.list_of_phones.append(GSM_Class('Spas', 'Ruby', 'Programing', 'NetIT', 'ruby@org.bg', '098888888'))

class GSMCallHistoryTest():
    call_1 = GSM('21.02.2022', '14:02',120)
    call_2 = GSM('11.04.2022', '13:02',400)
    call_1.add_call()
    call_2.add_call()
    prev = ''
    curr = ''
    pos=0
    print(GSM.callHistory)
    for call in GSM.callHistory:
        pos+=1
        for i in list(call):
            if i == 'call_length':
                curr = i
                prev = i
                if not prev > curr:
                    curr = prev
    del GSM.callHistory[pos-1][curr]
    print(f'After removing the longest call: {GSM.callHistory}')
    print(f'How many calls: {pos}')
    
    GSM.sum_call_price(0.37)

# nokia_95 = MobilePhone('nokia 95', 'Nokia', 35, 'Andy', 4000, 100, 3) 
# nokia_95.info()
GSMCallHistoryTest()
