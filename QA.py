import pandas as pd
import os
counter_list = []
zstat_list = ["cluster_zstat1.txt", "cluster_zstat2.txt", "cluster_zstat3.txt"]
template = "/home/trevor/mnt/vosslabhpc/Projects/PITCH/Bids/derivatives/flanker_analyses/sub-{sub_id:03d}/ses-{ses_id}/feat_run-{run_id:02d}_shift.feat"
key_file = "/home/trevor/mnt/vosslabhpc/Projects/PITCH/Bids/derivatives/mriqc_analyses/bold_ratings_comments.csv"
key_data = pd.read_csv(key_file)
for row in key_data.itertuples():
    if row.task_id == "flanker":
        sub_id = int(row.subject_id)
        ses_id = row.session_id
        run_id = int(row.run_id)
        zstat_dir = template.format(sub_id=sub_id, ses_id=ses_id, run_id=run_id)
        counter = 0
        for zstat in zstat_list:
            zstat_file = os.path.join(zstat_dir, zstat)
            if not os.path.isfile(zstat_file):
                counter = "non-existant file"
                counter_list.append(counter)
                continue 
            zstat_data = pd.read_csv(zstat_file)
            if zstat_data.empty:
                counter += 1
    else:
        counter = "NA"
    counter_list.append(counter)
    print(counter)