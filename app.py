import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import klib
#import pyautogui
import time

st.set_page_config(
     page_title="Exploratory data Analysis",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
)

max_width_str = f"max-width: 1600px;"
st.markdown(
	f"""
		<style>
			.reportview-container .main .block-container {{{max_width_str}}}
		</style>    
	""",
	unsafe_allow_html=True
)

st.set_option('deprecation.showPyplotGlobalUse', False)


def main():
    #st.title("Welcome to Data Explorer & Cleaning App")
    st.title("Exploratory Data Analysis Application")
    
   #example_datasets,user_dataset,clean_your_dataset=st.columns([8,8,8])
    #example_datasets,user_dataset=st.columns([8,8])
    st.subheader("Select an option from below dropdown where you want to carry Data Analysis")
    option=st.selectbox("",["Sample datasets","Your Dataset"],help="You can try EDA on our sample datasets & then carry out on your dataset. You can delete your dataset once EDA is Complete.")
    st.image(image="ia.jpg")
    #st.header("Data Analysis Made Easy an app Developed to help you")
    #example_datasets.checkbox("Work with Stored datasets")
    #user_dataset.checkbox("Work with your Custom dataset")
    #if example_datasets.checkbox("Want to do an analysis on Sample datasets",help="Work with our stored datasets"): 
    if option == "Sample datasets":
    #if st.checkbox("Work with Stored datasets"):
        st.header("You are exploring Pre-Stored datasets")
        FOLDER_PATH='datasets'
        filename=file_selector(FOLDER_PATH)
        st.success(f"you have selected {filename} Dataset")
        explore_data(FOLDER_PATH,filename)
#        if st.button("Reset"):
#            st.success("We are ressting the application")
#            time.sleep(1)
#            pyautogui.hotkey("ctrl","F5")  
            
    #if clean_your_dataset.button("Clean your Dataset"): 
    #    st.info("We are working on this feature")
    #   if st.button("Go Back"):
    #       pyautogui.hotkey("ctrl","F5")
            
    #if user_dataset.checkbox("Want to do an analysis on Your datasets. (CSV)",help="Currently we are accepting only csv datasets. You can delete your dataset once analysis is done"):
    if option == "Your Dataset":
        fname=dataset_uploader()
        FOLDER_PATH="user_dataset"
        file_path=os.path.join(FOLDER_PATH,fname)
        FLAG=0
        #st.write(f"we have recieved {fname} from you")
        if fname:
            st.header("Lets Explore Your datset")
            explore_data(FOLDER_PATH,fname)
        if st.button(f"Delete Your Dataset {fname}"):
            if fname=="":
                st.error("You have not uploaded any dataset")
            else:
                os.remove(file_path)
                st.success("We have Deleted your dataset")
                progress=st.progress(0)
                for i in range(1,100):
                    time.sleep(0.1)
                    progress.progress(i+1)
                #time.sleep(1)
#                pyautogui.hotkey("ctrl","F5")
                #FLAG=0
#        if st.button("Reset the App"):
#            if fname=="":
#                st.success("There is no dataset to delete")
#                st.success("We are ressting the application")
#                progress=st.progress(0)
#                for i in range(1,100):
#                    time.sleep(0.1)
#                    progress.progress(i+1)
               # time.sleep(1)
#                pyautogui.hotkey("ctrl","F5")    
#            else:
#                os.remove(file_path)
#                st.success(f"We have Deleted your dataset {fname}")
#                st.success("We are ressting the application")
#                progress=st.progress(0)
#                for i in range(1,100):
#                    time.sleep(0.1)
#                    progress.progress(i+1)
                #time.sleep(1)
#                pyautogui.hotkey("ctrl","F5")    
    #if user_dataset.checkbox("Clean Your Dataset"):
    #    new_df=k
          
    hide_menu_style="""
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    </style>
    """
    st.markdown(hide_menu_style,unsafe_allow_html=True)       

    

#@st.cache(suppress_st_warning=True)
def explore_data(FOLDER_PATH,filename):
    df=pd.read_csv(os.path.join(FOLDER_PATH,filename))
    all_columns=df.columns.tolist()
    #selected_columns=st.selectbox("Select The column or columns", all_columns)
    #new_df=df[selected_columns]
    
    if st.checkbox("Show Dataset"):
        number=st.number_input("Number of rows to view",10,10000,1000,step=5)
        st.dataframe(df.head(number))
    
    if st.checkbox("Show Columns"):
        st.write(df.columns)
    
    #if st.checkbox("Show Missing Values"):
    #    st.write(klib.missingval_plot(df))

        
    #Show Shape
    if st.checkbox("Show Shape"):
        st.write(df.shape)
        data_dim=st.radio("Show Dimensions by ",("Rows","Columns"))
        if data_dim == 'Columns':
            st.text("Numbers of columns are")
            st.write(df.shape[1])
        if data_dim == 'Rows':
            st.text("Numbers of Rows are")
            st.write(df.shape[0])
        else:
            st.write(df.shape)
        #Select Columns
    if st.checkbox("Select Columns"):
        all_columns=df.columns.tolist()
        selected_columns=st.multiselect("Select all columns you want to see",all_columns)
        new_df=df[selected_columns]
        st.dataframe(new_df)
    
    #Show Values
    if st.checkbox("Value Counts"):
        st.text("Value Counts By Target Class")
        st.write(df.iloc[:,-1].value_counts())
        
    if st.checkbox("Show Datatypes"):
        st.write(df.dtypes.astype(str))
        
    if st.checkbox("Show Coorelation Matrix"):
        st.write(klib.corr_mat(df))
        #st.write(klib.cat_plot(df))
        #st.write(klib.dist_plot(df))
        #st.graphviz_chart(klib.cat_plot(df))
        
    if st.checkbox("Summary"):
        st.write(df.describe().T)
    st.header("Data Visualization")
    
    
    #Seaborn
    if st.checkbox("Correlation Plot [Seaborn]"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()
    
    #Count Plot
    if st.checkbox("Plot of value Counts"):
        st.text("Value COunts by Target")
        all_columns_names=df.columns.tolist()
        primaryCol=st.selectbox("Primary Column to GROUP bY",all_columns_names)
        selected_columns_names=st.multiselect("Select Columns",all_columns_names)
        if st.button("Plot"):
            st.text("Generating Plot")
            if selected_columns_names:
                vc_plot=df.groupby(primaryCol)[selected_columns_names].count()
            else:
                vc_plot=df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind='bar'))
            st.pyplot()
            
    #pie chart
    if st.checkbox("Pie Plot"):
        all_columns_names=df.columns.tolist()
        if st.button("Generate Pie Plot"):
            st.success(f"Generating A Pie Chart")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%%%%%%%"))
            st.pyplot()
            
    #cutomizable plot
    st.header("Customizable Plot")
    all_columns_names=df.columns.tolist()
    st.info("Select the the type of Plot you want to draw")
    type_of_plot=st.selectbox("",["area","bar","line","histogram","box","kde"])
    selected_columns_names=st.multiselect("Select the columns name",all_columns_names)
    if st.button("Generate Plot"):
        st.success(f"Generating {type_of_plot} for {selected_columns_names}")
        #plot by streamlit
        
        if type_of_plot=="area":
            cust_data=df[selected_columns_names]
            st.area_chart(cust_data)
        
        elif type_of_plot=="bar":
            cust_data=df[selected_columns_names]
            st.bar_chart(cust_data)
        
        elif type_of_plot=="line":
            cust_data=df[selected_columns_names]
            st.line_chart(cust_data)   
        
     
        elif type_of_plot:
            cust_plot=df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()
            
            
def save_uploaded_file(uploadedFile):
    with open(os.path.join("user_dataset",uploadedFile.name),"wb") as f:
        f.write(uploadedFile.getbuffer())
    #st.success(f"You have saved the file {uploadedFile.name}")
    return uploadedFile.name
    
def dataset_uploader():
    #datafile=st.file_uploader("Upload a file",type=['csv'])
    datafile=st.file_uploader("Upload file", type=['csv'])
    #df1=pd.read_csv(st.file_uploader("Upload a file",type=['csv']))
    fname=""
    if datafile is not None:
        file_details={'filename':datafile.name,"FileType":datafile.type}
        df1=pd.read_csv(datafile)
        st.success(f"Here is your Dataset {datafile.name}")
        st.dataframe(df1)
        fname=save_uploaded_file(datafile)
    return fname
        

def file_selector(folder_path):
        filenames=os.listdir(folder_path)
        st.info("Select any sample Dataset from below dropdown or work with the default")
        selected_filename=st.selectbox("",filenames)
        return (selected_filename)
    

if __name__=='__main__':
    main()
    
