Project: antiHIV

Development process of Project:

1) Retrieve all the bioactivity data for anti-cancer is downloaded from NCI 
(https://wiki.nci.nih.gov/display/NCIDTPdata/Chemical+Data)
(https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data)
./data/aids_ec50_may04.txt                         #####ec50 data
./data/chembl_human_hiv_10um.tab                   #####ec50 data from chembl
./data/Open_2D_Oct2014.smi or nciopenb_smi.zip     #####SMILES string for all compounds

2) active and inactive compound information was obtained using python script (active(<10000 nm) and inactive(>100000 nm))
python step1a_get_data_active_inactive.py
input: ./data/aids_ec50_may04.txt
output: ./data/aids_ec50_may04_active.txt
output: ./data/aids_ec50_may04_inactive.txt

python step1b_get_data_smi
input: ./data/aids_ec50_may04_active.txt
input: ./data/aids_ec50_may04_inactive.txt
input: ./data/chembl_HIV_active.smi
input: ./data/Open_2D_Oct2014.smi
output: ./data/chembl_NCI_aids_active.smi
output: ./data/chembl_NCI_aids_inactive.smi

3) remove the conflict compounds between active and inactive compounds using python script 
python step3a_get_similarity_remove.py
python step3b_get_finaldata_remove.py
input: ./data/chembl_NCI_aids_active.smi
input: ./data/chembl_NCI_aids_inactive.smi
output: ./data/chembl_NCI_aids_active_final.smi
output: ./data/chembl_NCI_aids_inactive_final.smi

4) get the balance dataset by random selection of the inactive compounds using python script 
python step3_get_inactive_random.py
input: ./data/chembl_NCI_aids_inactive_final.smi
output: ./data/chembl_NCI_aids_inactive_final_ok.smi

5) write fingerprint of active and inactive compunds for the generation of predict model 
python step4_write_bitzp_and_shuffle.py
input: ./data/chembl_NCI_aids_inactive_final.smi
input: ./data/chembl_NCI_aids_inactive_final_ok.smi
output: ./data/alldata.pkl.z
output: ./data/alldatalabel.pkl.z

6) cross validation of random forest (search best parameters)
python step5_RF_model_performance.py
output: ./data/RF_performance_final.txt

7) cross validation of support vector machine (search best parameters)
python step6_SVM_model_performance1.py
python step6b_SVM_model_performance2.py
output: ./data/svm_performance_final.txt

8) generated final model using above parameters(RF and SVM)
python step7_generate_model.py
output: ./data/HIV_SVM_model_500_rbf_win.pkl
output: ./data/HIV_RF_model_1000_win.pkl.z

9) scripts for the prediction of anti-bacterial activity of query compounds 
python step8_antiHIVpre.py
output: anti_HIV_prediction.txt