import urllib.request
import pandas as pd

def csv_load(link, file_name):
    import urllib.request
    urllib.request.urlretrieve(link, file_name) 
    
    return None 

def organize_csv(csv_file):
    
    dataframe = pd.read_csv(csv_file)
    dataframe = dataframe.rename(columns = {'Finding Labels': 'finding_labels', 'Patient ID': 'patient_id'})
    dataframe = dataframe.drop(columns = ['Follow-up #', 'Patient Age', 'Patient Gender', 'View Position',
                                          'OriginalImage[Width', 'Height]', 'OriginalImagePixelSpacing[x', 'y]']) 
    dataframe = dataframe[(dataframe.finding_labels == 'No Finding') |
                      (dataframe.finding_labels == 'Atelectasis') |
                      (dataframe.finding_labels == 'Cardiomegaly') |
                      (dataframe.finding_labels == 'Consolidation') |
                      (dataframe.finding_labels == 'Edema') |
                      (dataframe.finding_labels == 'Effusion') |
                      (dataframe.finding_labels == 'Emphysema') |
                      (dataframe.finding_labels == 'Fibrosis') |
                      (dataframe.finding_labels == 'Hernia') |
                      (dataframe.finding_labels == 'Infiltration') |
                      (dataframe.finding_labels == 'Mass') |
                      (dataframe.finding_labels == 'Nodule') |
                      (dataframe.finding_labels == 'Pleural_Thickening') |
                      (dataframe.finding_labels == 'Pneumonia') |
                      (dataframe.finding_labels == 'Pneumothorax')]
    dataframe = pd.get_dummies(data = dataframe, prefix = '', columns = ['finding_labels'])
    
    return None
    