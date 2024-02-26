import streamlit as st
from PIL import Image
from helper import removeStreamlitElements, extraSpace
removeStreamlitElements()


t1, t2, t3= st.tabs(
    ['About Hazl','The Platform', 'App Gallery']
)

with t1:

    st.text('')

    st.header('''
        Think Differently for Cloud Computing 
    ''')

    st.text('')

    img_cloud_computing = Image.open('images/cloud_computing_3.png')
    st.image(img_cloud_computing)

    st.text('')

    st.markdown(
        '''
        :sparkle: At Hazl, we believe cloud computing 
        is a natural extension of personal computing. 
        Before the first personal computer assembled in 1970s, computers were 
        large mainframe machines that only used by business, governments, and 
        research facilities. The maturity of personal computing drastically 
        improved human productivity and brought about the dawn of Internet. 
        The same goes for cloud computing, which does not have to be difficult 
        and can be performed by anyone, not just professionals. 
        
        :sparkle: Our goal is to make it easy enough for individuals and organizations to utilize 
        cloud resources to build servers, web applications, and much more. Our platform simplifies the process of building servers and deploying
        applications, with minimal effort required on your part. Our App Gallery 
        provides apps that you can deploy to your servers instantly. This tutorial walks you through
        building your first virtual machine (VM) in cloud and deploy an application.

    ''')

    extraSpace()



with t2:
    st.text('')
    st.header('''Cloud Automation Made Easy''')
    st.text('')
    img_provision_vms = Image.open('images/hazl_workflow.png')
    st.image(img_provision_vms)
    st.text('')


    st.subheader('**Rapid VM Provisioning**')
    st.markdown('''
        Imagine being able to set up a VM in less than 10 minutes. 
        With Hazl, that's not just possible; it's a standard feature. Our streamlined 
        process ensures you can start building and deploying without delay.
    ''')
    st.text('')

    st.subheader('**Simplified Cloud Resource Management**')
    st.markdown('''
        Forget the complexity traditionally associated with setting up 
        cloud resources. Our platform automates the entire process, 
        allowing you to focus on what truly matters - your projects and innovations.
    ''')
    st.text('')  

    st.subheader('**Hybrid Cloud Flexibility**')
    st.markdown('''
        In today's digital landscape, being tied to a single cloud provider 
        is a limitation we don't believe you should have to endure. Hazl 
        introduces the freedom to seamlessly operate across multiple cloud 
        environments, including AWS, Azure, GCP, and more, giving you the flexibility 
        to choose the best services for your needs without any hassle.
    ''')
    st.text('')  


    st.subheader('**Your Personal App Gallery**')
    st.markdown('''
        The Hazl App Gallery redefines the concept of deploying web 
        applications. Think of it as your private app store, filled with your 
        creations, ready to be deployed to your servers in just a minute. 
        This means more time innovating and less time managing deployments.
    ''')
    st.text('')  


    st.subheader('**Accessible to All**')
    st.markdown('''
        We firmly believe that cloud computing should be accessible 
        to everyone, not just those with expert knowledge. Our platform 
        is built with this in mind, ensuring you can leverage cloud technology 
        regardless of your expertise level.
    ''')
    st.text('')  

    extraSpace()



with t3:
    st.text('')
    st.header('A Hub of Innovation and Collaboration')
    st.text('')

    img_app_gallery = Image.open('images/app_gallery_5.png')
    st.image(img_app_gallery)
    st.text('')

    st.subheader('**Continuously Growing Collection**')
    st.markdown('''
        We are always on the lookout for the next groundbreaking application. 
        We regularly enrich the App Gallery 
        with new, innovative applications, all of which are open-sourced for 
        public use. This ensures our users always have access to the latest tools 
        and technologies, empowering them to stay ahead in the fast-evolving digital landscape.
    ''')
    st.text('')  

    st.subheader('**Curated Open Source Projects**')
    st.markdown('''
        Beyond our creations, we dive into the vast world of popular 
        open-source projects, selecting the most impactful and useful 
        applications to add to our App Gallery. This curated approach 
        means users benefit from a rich repository of high-quality, vetted 
        applications ready to be deployed at a moment's notice.
    ''')
    st.text('')  

    st.subheader('**Personalized App Gallery**')
    st.markdown('''
        Recognizing the unique needs and creativity of our users, the 
        Hazl App Gallery offers the capability to upload your own 
        projects or applications. This personalization transforms the App 
        Gallery into your private repository, a tailored space where your 
        innovations can be stored, managed, and deployed with ease.
    ''')
    st.text('')  

    st.subheader('**Promotion of Developer Projects**')
    st.markdown('''
        We believe in supporting the developer community and providing 
        opportunities for visibility and growth. Developers interested 
        in promoting their projects or applications find a willing and 
        enthusiastic partner in Hazl. Our service team is committed to assisting 
        developers in showcasing their work to the public, providing a platform 
        for recognition and engagement.
    ''')
    st.text('')  

    extraSpace()



