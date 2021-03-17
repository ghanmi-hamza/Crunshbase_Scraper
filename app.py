from functions import Profile
from mongodb import MongoDb
from flask import Flask, render_template, request, redirect

app= Flask(__name__)

@app.route('/')
def start():
    return(render_template('view.html'))

@app.route('/',methods=['POST'])
def index():
    
    if request.method == 'POST':
        startup_list = request.form['username']  

    startup_list = list(set(startup_list.split(',')))
    startup_list_1 = []

    database_name = 'hamza'
    m=MongoDb(database_name)
    
    for startup in startup_list: 
        status = "running"
        if m.verify(startup):
            startup_data = m.show_data(startup)
            status = "succeeded"
            print(startup+' : '+status) 
           
        else:
            startup_list_1.append(startup)

    MAX_THREADS = 5
    if len(startup_list_1) >= 5:
        for i in range(0,(len(startup_list_1)//MAX_THREADS)*MAX_THREADS,MAX_THREADS):
            
            thread_1 = Profile(startup_list_1[i])
            thread_2 = Profile(startup_list_1[i+1])
            thread_3 = Profile(startup_list_1[i+2])
            thread_4 = Profile(startup_list_1[i+3])
            thread_5 = Profile(startup_list_1[i+4])

            thread_1.start()
            thread_2.start()
            thread_3.start()
            thread_4.start()
            thread_5.start()

            thread_1.join()
            thread_2.join()
            thread_3.join()
            thread_4.join()
            thread_5.join()

            if thread_1.status == 'succeeded':
                m.insert_data(collection = startup_list_1[i], data = thread_1.data)
            if thread_2.status == 'succeeded':
                m.insert_data(collection = startup_list_1[i+1], data = thread_2.data)
            if thread_3.status == 'succeeded':
                m.insert_data(collection = startup_list_1[i+2], data = thread_3.data)
            if thread_4.status == 'succeeded':
                m.insert_data(collection = startup_list_1[i+3], data = thread_4.data)
            if thread_5.status == 'succeeded':
                m.insert_data(collection = startup_list_1[i+4], data = thread_5.data)
            
        if len(startup_list_1) - (len(startup_list_1)//MAX_THREADS)*MAX_THREADS > 0 :
            for startup in startup_list_1[(len(startup_list_1)//MAX_THREADS)*MAX_THREADS:]:
                p=Profile(startup)
                p.run()
                if p.status == 'succeeded':
                    m.insert_data(collection = startup, data = p.data)
    else:
        for startup in startup_list_1:
            p=Profile(startup)
            p.run()
            if p.status == 'succeeded':
                m.insert_data(collection = startup, data = p.data)

    """
    while VERIFICATION:
        if i + MAX_THREADS <= len(startup_list_1): 
            for startup in startup_list_1[i:i+MAX_THREADS]:
                try :
                    print(startup+' : '+status) 
                    thread_startup = Profile(startup)   
                    thread_startup.start() 
                    #thread_startup.join()
                    #dic['thread'+str(startup)] =  
                    #thred_startup.join()    
                    #thread_+str(startup).start()                       
                    #p=Profile(startup)
                    #startup_data=p.scraping()
                    '''m.insert_data(collection = startup, data = startup_data)
                    status = "succeeded"
                    print(startup+' : '+status)'''
                except:
                    thread_startup.close_browser()
                    #p.close_browser()
        else :
            VERIFICATION = False
            for startup in startup_list_1[i:i+MAX_THREADS]:
                try :
                    print(startup+' : '+status) 
                    thread_startup = Profile(startup)   
                    thread_startup.start() 
                    #dic['thread'+str(startup)] =  
                    #thred_startup.join()    
                    #thread_+str(startup).start()                       
                    #p=Profile(startup)
                    #startup_data=p.scraping()
                    '''m.insert_data(collection = startup, data = startup_data)
                    status = "succeeded"
                    print(startup+' : '+status)'''
                except:
                    thread_startup.close_browser()
                    #p.close_browser()"""

    return(render_template('view1.html'))
    
if __name__=='__main__':
    app.run(debug=True)