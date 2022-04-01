from fileinput import filename
import streamlit as st
import converter
import pandas as pd
import time




def main():

    st.title('Simple file converter')

    buk = st.selectbox('do you want to create a bucket', ('select','Yes', 'No'))

    if buk == 'Yes':

        source_buck = st.text_input('Enter any unique source bucker name',on_change= lambda : st.write("value changed"))
        dest_buck = st.text_input('Enter any unique destination bucker name',on_change= lambda : st.write("value changed"))

        st.write('You entered:', source_buck, dest_buck)

        if source_buck!= "" and dest_buck!= "":

            try:
                converter.create_bucket(source_buck)
                converter.create_bucket(dest_buck)

            except Exception as e:
                st.warning('Bucket already exists')
                #st.write('Bucket already exists')
                #pass
        
        else:
            st.write('Please enter a valid & globally unique bucket name')


        op = st.selectbox('What would you like to convert?',("Select",'Excel', 'CSV'))

        st.write('You selected:', op)

        srcb = source_buck
        destb = dest_buck


        if op == 'Excel' and srcb!= "" and destb!= "":

            try:
                # converting csv to xlsx
                file =  st.file_uploader('Upload your file', type=['csv'])
                
                #st.write(type(file))

                if file != None:
            
                    st.write(file.name[:-4])
                    converter.upload_blob_from_memory(srcb, file.getvalue(), file.name)
                    st.write(converter.convert_to_xls(file.name,bukcet_name_d = srcb, bukcet_name_u = destb))
                    time.sleep(3)
                    converter.download_blob(destb, "converted"+file.name[:-4]+".xls", "converted"+file.name[:-4]+".xls")
                    exc = pd.read_excel("converted"+file.name[:-4]+".xls")
                    st.download_button(data= file.name[:-4]+".xls", file_name=file.name[:-4]+".xls",label='Download Excel')
                
                else:
                    st.write('Please upload a valid file')

            except Exception as e:
                st.write(e)
                st.write('Please upload a valid file')

        elif op == 'CSV' and srcb!= "" and destb!= "":

            try:
                # converting xlsx to csv
                file =  st.file_uploader('Upload your file', type=['xls', 'xlsx'])
                #st.write(type(file))
               

                if file!= None:
                    st.write(file.type)
                    v = file.name[:-4] if file.name[-4:] == '.xls' else file.name[:-5]
                    st.write(v)
                    #st.write(file.name[:-5])
                    converter.upload_blob_from_memory(srcb, file.getvalue(), file.name)
                    st.write(converter.convert_to_csv(file.name,bukcet_name_d = srcb, bukcet_name_u = destb))
                    time.sleep(3)
                    converter.download_blob(destb, "converted"+v+".csv", "converted"+v+".csv")
                    exc = pd.read_csv("converted"+v+".csv")
                    st.download_button(data=v+".csv", file_name=v+".csv",label="Download CSV")

                else:
                    st.write('Please upload a valid file')

            except Exception as e:
                st.write(e)
                st.write('Please upload a valid file')

        else:
            st.write('Please select a file')
  
    
    else:
        st.write('Please create a valid bucket first')


    

    






if __name__ == '__main__':
    main()
