import os

base_dir = './'  #dir to the acl paper data
proj_dir = './' #dir to the project

cat_NLP_TDM_path = os.path.join(base_dir,'data/NLP-TDMS')
kb_dir = os.path.join(base_dir,'data/NLP-TDMS/kb')
datasetKB_path = os.path.join(kb_dir,'datasetKB.tsv')
metricKB_path = os.path.join(kb_dir,'evaMatrixKB.tsv')
taskKB_path = os.path.join(kb_dir,'taskKB.tsv')

NLP_TDM_path = os.path.join(base_dir,'data','NLP-TDMS')
onto_dir = os.path.join(proj_dir,'data/sdo/')
onto_fname = 'mleo.owx'

#output
vote_rs_path = os.path.join(proj_dir,'data/sdo/voteResult.tsv')
paper_entity_path = os.path.join(proj_dir,'data/paper_entity.pl')
top_tag_path = os.path.join(proj_dir,'data/top_tags.pickle')

BERT_TD_path = os.path.join(proj_dir,'data/BERT_TD.pl')
ESIM_TD_path = os.path.join(proj_dir,'data/ESIM_TD.pl')
