import sys
import re

def copy_drawables(res_directory,target_selector,colors,prefix):
    target_selector = open(res_directory+'drawable/'+target_selector,'r')
    
    for color in colors:
        has_pressed_state = False
        #create selector file for the color
        selector = open(res_directory+'drawable/'+prefix+'_'+color+'_selector')
        for line in target_selector:
            line = str(line) # i think its already a string?
            if 'android:drawable=' in line && 'pressed' in line:
                has_pressed_state = True
                match = re.match('\"android:drawable\=.\"', line)
                line.replace(match.group(0),"android:drawable=\"@drawable/"+prefix+"_"+color+"pressed\"")
            else if 'android:drawable=' in line:
                match = re.match('\"android:drawable\=.\"', line)
                line.replace(match.group(0),"android:drawable=\"@drawable/"+prefix+"_"+color+"\"")
            selector.write(line)  
            
        #create  non pressed shape             
    
    
    
    
    

if __name__ == "__main__":
    args = sys.argv
    res_directory = None
    target_selector = None
    name_segment_to_replace = None
    prefix = ""
    colors = []
    for index, arg in enumerate(args):
        if arg == '-d':
            res_directory = args[index+1]
            if res_directory[-1:] != '/':
                res_directory = res_directory + '/'
            
        else if arg == '-target' || arg == '-t':
            target_selector = args[index+1]
            iftarget_selector[-4:] != '.xml':
                target_selector = target_selector + '.xml'
        
        else if arg == '-prefix' || arg == '-p':
            prefix = args[index+1]
            
#         else if arg == '-replace' || arg == '-r':
#             name_segment_to_replace = args[index+1]
            
        else if arg == '-colors':
        
            for color in args[index+1:]:
                if(color[0]=='-'):
                    break
                else:
                    colors.append(color)
                    
    copy_drawables(res_directory,target_selector,colors)
                
    
            
    
