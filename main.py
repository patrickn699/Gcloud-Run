from xml.sax import parseString
import streamlit as st
import converter
import pandas as pd
import time




def main():

    st.title('Simple file converter')

    source_buck = st.text_input('Enter any unique source bucker name')
    dest_buck = st.text_input('Enter any unique destination bucker name')
    st.write('You entered:', source_buck, dest_buck)

    if source_buck!= "" and dest_buck!= "":

        try:
            converter.create_bucket(source_buck)
            converter.create_bucket(dest_buck)

        except Exception as e:
            st.write(e)
            st.write('Bucket already exists')
            pass
    
    else:
        st.write('Please enter a valid bucket name')


    op = st.selectbox(
     'What would you like to convert?',
     ("Select",'Excel', 'CSV'))

    st.write('You selected:', op)


    

    if op == 'Excel':

        try:
            # converting csv to xlsx
            file =  st.file_uploader('Upload your file', type=['csv'])
            #st.write(converter.convert_to_xls(st.file_uploader('Upload your file', type=['csv', 'xls', 'xlsx'])))
            converter.upload_blob_from_memory(source_buck, file, file.name+".csv")
            st.write(converter.convert_to_xls(file.name+".csv"))
            time.sleep(3)
            converter.download_blob(dest_buck, "converted"+file.name+".xls", "converted"+file.name+".xls")
            exc = pd.read_excel("converted"+file.name+".xls")
            st.download_button(data= exc, file_name=file.name+".xls")

        except Exception as e:
            st.write(e)
            st.write('Please upload a valid file')

    elif op == 'CSV':

        try:
            # converting xlsx to csv
            file =  st.file_uploader('Upload your file', type=['xls', 'xlsx'])
            converter.upload_blob_from_memory(source_buck, file, file.name+".xls")
            st.write(converter.convert_to_csv(file.name+".xls"))
            time.sleep(3)
            converter.download_blob(dest_buck, "converted"+file.name+".csv", "converted"+file.name+".csv")
            exc = pd.csv("converted"+file.name+".csv")
            st.download_button(data= exc, file_name=file.name+".csv")

        except Exception as e:
            st.write(e)
            st.write('Please upload a valid file')

    else:
        st.write('Please select a file')

    






if __name__ == '__main__':
    main()
