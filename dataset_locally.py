from deep_translator import GoogleTranslator
import tqdm
import pandas as pd
import csv,os,time
import random as rd
import logging as lg

lg.basicConfig(filename="log.txt",level=lg.DEBUG)

def g_translation_function_mr_en(inText):
  if len(inText)<=4999:
    outText = GoogleTranslator(source='mr', target='en').translate(inText)
    return outText
  else:
    return ""

def g_translation_function_mr_hi(inText):
  if len(inText)<=4999:
    outText = GoogleTranslator(source='mr', target='hi').translate(inText)
    return outText
  else:
    return ""

basepath = os.path.dirname(os.path.realpath(__file__))
folder_name = os.path.join(basepath,"data")
folder_name_done = os.path.join(basepath,"data","done")
folder_done_txt = os.path.join(basepath,"data","data_done")

if os.path.exists(folder_name) == False:
  os.mkdir(folder_name)
if os.path.exists(folder_name_done) == False:
  os.mkdir(folder_name_done)
if os.path.exists(folder_done_txt) == False:
  os.mkdir(folder_done_txt)

file_list = os.listdir(folder_name)

for file_no in file_list: 
  if file_no.endswith(".txt"):
    Flag = 0

    # for file in file_list:
    file_to_open = os.path.join(folder_name, file_no)
    
    file_to_done = os.path.join(folder_name_done, file_no)
    folder_done_txt_outpath = os.path.join(folder_done_txt, file_no)
    print(file_no,"--")
    filename_to_add = file_no.split("_")[1]
    filename_output = f"output_en_hi_{filename_to_add}_.csv"
    filename_output_path = os.path.join(folder_name_done,filename_output)
        
    # run only once to add header to csv
    # field names 
    fields_capt = ['mr_txt', 'en_txt', 'hi_txt'] 

    # writing header fields to csv file 
    with open(filename_output_path, 'w') as csvfile:
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        # writing the fields 
        csvwriter.writerow(fields_capt)

    df_source_mr_file = pd.read_csv(file_to_open, delimiter = "\t",names=["mr_txt"])
    df_len = len(df_source_mr_file)
    df_len_count = 0
    for ind in df_source_mr_file.index:
        df_len_count = df_len_count + 1
        en_txt = g_translation_function_mr_en(str(df_source_mr_file['mr_txt'][ind]))
        hi_txt = g_translation_function_mr_hi(str(df_source_mr_file['mr_txt'][ind]))
        cm_row = [df_source_mr_file['mr_txt'][ind],en_txt ,hi_txt]

        #randamize time to sleep
        if df_len_count%100==0:
          time_random = rd.choice((0.1,0.2,0.3,0.4,0.25,0.55,0.61))
          time.sleep(2*time_random)

        # writing fields to csv file 
        with open(filename_output_path, 'a+') as csvfile: 
          # creating a csv writer object 
          csvwriter = csv.writer(csvfile) 
          # writing the fields 
          csvwriter.writerow(cm_row)
          
    Flag = 1
    if Flag ==1:
      #move file to other dir if completed
      os.system(f"mv {file_to_open} {folder_done_txt_outpath}")
      print("Completed & done moving - ",file_no)
      lg.info(f"Completed & done moving - {file_no}")