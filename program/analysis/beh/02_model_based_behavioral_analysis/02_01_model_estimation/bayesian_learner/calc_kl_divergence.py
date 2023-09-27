import pandas as pd
import sys
import os
import tqdm

sys.path.append('/Users/dddd1007/Research/developing_lib/xia_cog_model')
import xia_cog_model

bl_path = "/Volumes/Research/all_research_data/project9_fmri_spatial_stroop/data/output/model_estimation/bayesian_learner/single_sub"
model_types = ['ab', 'sr']
sub_num = range(9, 44)

results = []
for model_types_i in model_types:
    print("Calc the KL divergence for model type: ", model_types_i)
    for sub_num_i in tqdm.tqdm(sub_num):
        try:
            file_path = os.path.join(bl_path, model_types_i,f"sub_{sub_num_i}")
            df = xia_cog_model.load_dataframes(file_path)
            kl_df = pd.DataFrame(xia_cog_model.param_kl(df, 'r', debug=False))
            kl_df['type'] = model_types_i
            kl_df['sub'] = sub_num_i
            results.append(kl_df)
        except Exception as e:
            print(f"Error occurred with sub_num {sub_num_i}: {e}")
            continue

results_df = pd.concat(results, ignore_index=True)
results_df.to_csv('/Volumes/Research/all_research_data/project9_fmri_spatial_stroop/data/output/model_estimation/bayesian_learner/kl_divergence.csv')
