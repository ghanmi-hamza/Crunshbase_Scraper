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
        if m.verify(startup):
            #startup_data = m.show_data(startup)
            if m.verify_status(startup, status='succeeded') :
                pass
            elif m.verify_status(startup, status='failed') :
                startup_list_1.append(startup)
                m.update_status(startup, {'status' : 'running'})
                
           
        else:
            m.insert_data(startup, {'status' : 'running'})
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

            
            m.replace_data(collection = startup_list_1[i], data = thread_1.data)
            
            m.replace_data(collection = startup_list_1[i+1], data = thread_2.data)
            
            m.replace_data(collection = startup_list_1[i+2], data = thread_3.data)
            
            m.replace_data(collection = startup_list_1[i+3], data = thread_4.data)
            
            m.replace_data(collection = startup_list_1[i+4], data = thread_5.data)
            
        if len(startup_list_1) - (len(startup_list_1)//MAX_THREADS)*MAX_THREADS > 0 :
            for startup in startup_list_1[(len(startup_list_1)//MAX_THREADS)*MAX_THREADS:]:
                p=Profile(startup)
                p.run()

                m.replace_data(collection = startup, data = p.data)
    else:
        for startup in startup_list_1:
         #   list_thread.append(Profile(startup))
            p=Profile(startup)
            p.run()
            
            m.replace_data(collection = startup, data = p.data)

    return(render_template('view1.html'))
    
if __name__=='__main__':
    app.run(debug=True)