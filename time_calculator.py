def add_time(start_time, duration_time,starting_day=""):
    
    l=start_time.split(":")
    t=l[1].split(" ")
    
    
    
    #week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    
    #diafinal=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
      
    week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    ready=[int(l[0]),int(t[0]),t[1]]
    
    duration=duration_time.split(":")
    duration=[int(duration[0]),int(duration[1])]
    
    if starting_day=="":
    
        if duration[0]==0 and duration[1]==0:
            if ready[1]<10:
                ready[1]="0{}".format(ready[1])
            
            return "{}:{} {}".format(ready[0], ready[1],ready[2])
        
        #x=ready[2]
        
        #print(type(duration[0]))
        dias=duration[0]//24
        
        if duration[0]==24 and duration[1]==0:
            return "{}:{} {} (next day)".format(ready[0], ready[1],ready[2])
        
        if duration[0]>24:   
            pico=duration[0]%24
            
        else:
            pico=duration[0]
       
        if ready[1]+duration[1]>59:
            minutos=ready[1]+duration[1]-60
            
            if minutos<10:
                minutos="0{}".format(minutos)
                
            if pico+ready[0]+1>11 and ready[2]=="PM":
                
                hora=pico+ready[0]+1-24
                ready[2]="AM"
                
                if dias==0:
                    return "{}:{} {} (next day)".format(hora, minutos,ready[2])
                else:
                    return "{}:{} {} ({} days later)".format(hora, minutos,ready[2],dias+1)
                
            elif pico+ready[0]+1>11 and ready[2]=="AM":
                ready[2]="PM"
                hora=pico+ready[0]+1-12
                if hora==0:
                    hora=12
                
                if dias==0:
                    return "{}:{} {}".format(hora, minutos,ready[2])
                else:
                    return "{}:{} {} ({} days later)".format(hora, minutos,ready[2],dias+1)
        else:
             minutos=ready[1]+duration[1]
             
             if minutos<10:
                 minutos="0{}".format(minutos)
             #return print(ready[2])
             
             if pico+ready[0]>11 and ready[2]=="PM":
                
                hora=pico+ready[0]-12
                ready[2]="AM"
             
                if dias==0:
                    return "{}:{} {} (next day)".format(hora, minutos,ready[2])
                else:
                    return "{}:{} {} ({} days later)".format(hora, minutos,ready[2],dias+1)
                
             
             elif pico+ready[0]>11 and ready[2]=="AM":
                
                ready[2]="PM"
                hora=pico+ready[0]-12
                
                if hora==0:
                    hora=12 
                
                if dias==0:
                    return "{}:{} {}".format(hora, minutos,ready[2])
             #   elif dias==1:
              #      ready[2]=x
              #      hora=pico+ready[0]-12
                #    return "{}:{} {} (next day)".format(hora, minutos,ready[2])
                else:
                    return "{}:{} {} ({} days later)".format(hora, minutos,ready[2],dias+1)  
    
             else:
                return "{}:{} {}".format(ready[0]+duration[0], ready[1]+duration[1],ready[2])
 
    else:
        starting_day=starting_day.lower()
        starting_day=starting_day[0].upper()+starting_day[1:]
        #buscar=week.index(starting_day)
        buscar=week.index(starting_day)
        if duration[0]==0 and duration[1]==0:
            if ready[1]<10:
                ready[1]="0{}".format(ready[1])
            
            return "{}:{} {}".format(ready[0], ready[1],ready[2])+", {}".format(week[(buscar+dias)%7])
        
        #x=ready[2]
        
        #print(type(duration[0]))
        dias=duration[0]//24
        
        if duration[0]==24 and duration[1]==0:
            return "{}:{} {}".format(ready[0], ready[1],ready[2])+", {} (next day)".format(week[(buscar+dias)%7])
        
        if duration[0]>24:   
            pico=duration[0]%24
            
        else:
            pico=duration[0]
       
        if ready[1]+duration[1]>59:
            minutos=ready[1]+duration[1]-60
            
            if minutos<10:
                minutos="0{}".format(minutos)
                
            if pico+ready[0]+1>11 and ready[2]=="PM":
                
                hora=pico+ready[0]+1-24
                ready[2]="AM"
                
                if dias==0:
                    return "{}:{} {}".format(hora, minutos,ready[2])+", {} (next day)".format(week[(buscar+dias+1)%7])
                else:
                    return "{}:{} {}".format(hora, minutos,ready[2])+", {} ({} days later)".format(week[(buscar+dias+1)%7],dias+1)
                
            elif pico+ready[0]+1>11 and ready[2]=="AM":
                ready[2]="PM"
                hora=pico+ready[0]+1-12
                if hora==0:
                    hora=12
                
                if dias==0:
                    return "{}:{} {}, {}".format(hora, minutos,ready[2],week[(buscar+dias+1)%7])
                else:
                    return "{}:{} {}, {} ({} days later)".format(hora, minutos,ready[2],week[(buscar+dias+1)%7],dias+1)
        else:
             minutos=ready[1]+duration[1]
             
             if minutos<10:
                 minutos="0{}".format(minutos)
             #return print(ready[2])
             
             if pico+ready[0]>11 and ready[2]=="PM":
                
                hora=pico+ready[0]-12
                ready[2]="AM"
             
                if dias==0:
                    return "{}:{} {}, {} (next day)".format(hora, minutos,ready[2],week[(buscar+dias+1)%7])
                else:
                    return "{}:{} {}, {} ({} days later)".format(hora, minutos,ready[2],week[(buscar+dias+1)%7],dias+1)
                
             
             elif pico+ready[0]>11 and ready[2]=="AM":
                
                ready[2]="PM"
                hora=pico+ready[0]-12
                
                if hora==0:
                    hora=12 
                
                if dias==0:
                    return "{}:{} {}, {}".format(hora, minutos,ready[2],week[(buscar+dias+1)%7])
             #   elif dias==1:
              #      ready[2]=x
              #      hora=pico+ready[0]-12
                #    return "{}:{} {} (next day)".format(hora, minutos,ready[2])
                else:
                    return "{}:{} {}, {} ({} days later)".format(hora, minutos,ready[2],week[(buscar+dias)%7],dias+1)  
    
             else:
                return "{}:{} {}, {}".format(ready[0]+duration[0], ready[1]+duration[1],ready[2],week[(buscar+dias)%7])


            
            

