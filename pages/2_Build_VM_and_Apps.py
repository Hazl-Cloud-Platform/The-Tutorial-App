import streamlit as st
from PIL import Image
from helper import removeStreamlitElements, extraSpace
removeStreamlitElements()

t1, t2, t3 = st.tabs(
    ['Step 1: App Gallery','Step 2: Console','Step 3: One VM Multiple Apps']
)

with t1:

    st.text('')
    st.markdown('''
        Navigate to the App Gallery tab and select an app. In the Server Configuration 
        section, enter a VM name, select a cloud provider and server type, and specify 
        the VM disk size. Finally, assign a name to your app and initiate the build. 
        The build process involves two stages: initially, it connects to your cloud account 
        to provision a VM based on your preferences. Once the VM is provisioned, it retrieves 
        the application from the App Gallery repository and launches the server on a designated port.
    ''')
    img_first_vm_app = Image.open('images/first_vm_app_2.png') 
    st.image(img_first_vm_app)       
    extraSpace()


with t2:

    st.text('')
    st.markdown('''

        After successfully building the VM and app, their details will 
        appear in the Console tab. Located in the dropdown menu on the left, you 
        will find an :orange[Terminate] button. This button terminates the VM 
        along with any apps running on it, so exercise caution when using it.
        To continue for the next step, DO NOT terminate yet.
    ''')
    img_in_console = Image.open('images/in_console_1.png') 
    st.image(img_in_console)    
    extraSpace()

with t3:

    st.text('')
    st.markdown('''

        It is possible to deploy multiple apps on the same VM. Return 
        to the App Gallery and choose another app. You will notice that 
        the VM you previously built is available for selection. Assign a 
        name to your second app and start the build process.
    ''')
    img_in_console = Image.open('images/build_second_app_1.png') 
    st.image(img_in_console)   

    st.text('')
    st.text('')

    st.markdown('''

        Upon successfully building the second app, its details will be 
        visible in the Console tab, indicating that the VM is now hosting 
        two applications.
    ''')
    img_multiple_apps = Image.open('images/one_vm_multiple_apps_2.png') 
    st.image(img_multiple_apps)   
    extraSpace()
