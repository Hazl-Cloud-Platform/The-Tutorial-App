import streamlit as st
from PIL import Image
from helper import removeStreamlitElements, extraSpace
removeStreamlitElements()

t1, t2, t3 = st.tabs(
    ['AWS','Azure','GCP']
)



with t1:

    st.text('')

    st.markdown('''
        When you create a Hazl account, you'll go through a 
        standard sign-up process. After signing up, you'll be asked to 
        connect your AWS account in order to set up a role 
        that will enable Hazl to provide you with service.
        At Hazl, we take the security and reliability of 
        our service seriously, and we follow the best practices 
        recommended by AWS for setting up cross-account service. 
        To learn more about these practices, please visit 
        [Providing access to AWS accounts owned by third parties.]({})

    '''.format('https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html'))

    st.markdown('''
        To get started with setting up the cross-account 
        service, please follow these steps:
    ''')

    st.markdown('''
        :zero: This tutorial assumes you already have an AWS account.
        If you don't, please use [this link]({}). In the event that the 
        link does not work, you can search for "AWS Sign Up" to find 
        the appropriate page.
    '''.format('https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email')
    )

    st.text('')

    st.markdown('''
        :one: Once you have logged into your AWS account, navigate 
        to the top search bar and type in :orange[**IAM**]. This will 
        allow you to locate and access the :orange[**IAM**] service.
    ''')
    iam_service_img = Image.open('images/iam_service.png')
    st.image(iam_service_img)

    st.text('')
    st.text('')

    st.markdown('''
        :two: Under :orange[**Access management**], select :orange[**Roles**],
        then click the :orange[**Create role**] button. 
    ''')
    iam_create_role_img = Image.open('images/iam_create_role.jpg')
    st.image(iam_create_role_img)

    st.text('')
    st.text('')

    st.markdown('''
        :three: Under :orange[**Trusted entity type**], choose 
        :orange[**AWS account**]. Check the radio button for :orange[**Another AWS account**]
        and type in this Account ID: :blue[**419331123186**]. This is the
        Hazl's AWS account from which you will receive the service. \n
        Select the :orange[**Require external ID (Best practice when a third party will 
        assume this role)**] option. You may use any phase for the External ID as 
        you like. External ID serves as an extra layer of security 
        to help prevent any malicious cross-account manipulation 
        of resources. Click :orange[**Next**]
        to proceed.
    ''')

    trusted_entity_img = Image.open('images/iam_trusted_entity.jpg') 
    st.image(trusted_entity_img)

    st.text('')
    st.text('')

    st.markdown('''
        :four: In the :orange[**Add permissions**] step, you will add 3 policies
        to the role: :orange[AmazonEC2FullAccess], :orange[AmazonSSMFullAccess],
        and :orange[IAMFullAccess]. Search for each term in the search bar, select 
        its corresponding checkbox, and click :orange[**Next**] to proceed.
    ''')
    policy_img = Image.open('images/iam_policy.jpg') 
    st.image(policy_img)

    st.text('')
    st.text('')

    st.markdown('''

        :five: In the final step, enter the :orange[**Role name**] as 
        :blue[**HazlService**]. We recommend using this default name 
        if it is not already taken. However, if the name is already in use, 
        you can choose another name that best fits your naming convention. 

        Next, carefully review the trusted entities and ensure that all three permissions
        have been added. Once you have confirmed this, click on the 
        :orange[**Create role**] to complete the process.

    ''')
    role_review_img = Image.open('images/iam_role_review.png') 
    st.image(role_review_img)

    st.text('')
    st.text('')


    st.markdown('''
        :nine: Return to our app, under :orange[**Account**], select
        :orange[**Connect Clouds**]. Enter your 
        :orange[**AWS Account ID**] (NOT Hazl's AWS), the :orange[**Role name**], and 
        the :orange[**External ID**] that you created above.

    ''')
    connect_clouds_img = Image.open('images/connect_clouds.png') 
    st.image(connect_clouds_img)         

    extraSpace()



with t2:
    st.text('')
    st.text('Coming soon')


with t3:
    st.text('')
    st.text('Coming soon')
    