# %% [markdown]
# # fMRI 分析
# ## 0. 环境配置

# %%
# 配置基本环境
import os
import pandas as pd
import subprocess
import xia_fmri_workflow

# 读取被试数据
all_data = pd.read_csv(
    "/Volumes/Research/project9_fmri_spatial_stroop/data/input/all_data_with_params.csv"
)
# 被试基本信息
sub_num_list = pd.unique(all_data["sub_num"])
session_num = 6

# 数据位置
root_dir = (
    "/Volumes/Research/project9_fmri_spatial_stroop/data/input/fmri_data/nii"
)
output_dir = "/Volumes/Research/project9_fmri_spatial_stroop/data/output/fmri/"

all_data.columns
all_data["PC_factor"] = all_data[["volatile", "prop", "congruency"]].apply(
    lambda row: "_".join(row.astype(str)), axis=1
)
all_data.head()

factors_name = ["PC_factor"]


# Begin the batch subject analysis
sub_num_list = sub_num_list[(sub_num_list > 34) & (sub_num_list < 37)]
for sub_num in sub_num_list:
    try:
        estimate_result = xia_fmri_workflow.workflow_condition_glm_1stlevel(
            root_dir, sub_num, session_num, factors_name, all_data, output_dir
        )
    except SystemExit:
        print(f"在处理 sub_num {sub_num} 时出错，旧文件仍存在，跳过该被试！")
        continue
    except Exception as e:
        print(f"在处理 sub_num {sub_num} 时出错，错误信息为：{str(e)}")
        continue


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# %%
# The sub 41 don't have the session 1, so please treat it specially

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# %%
# Contrast
matlab_script_path = os.path.join(
    "/Volumes/Research/project9_fmri_spatial_stroop/",
    "program/analysis/fmri/02_condGLM/1stLevel/contrast.m",
)
# Create the command to run the MATLAB script
command = (
    f"matlab -nodisplay -nosplash -nodesktop "
    f"-r \"run('{matlab_script_path}'); exit;\""
)
# Run the command
subprocess.check_output(command, shell=True)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# %%
output_dir = (
    "/Volumes/Research/project9_fmri_spatial_stroop/data/output/concate_fmri/"
)

all_data.columns
all_data["PC_factor"] = all_data[["volatile", "prop", "congruency"]].apply(
    lambda row: "_".join(row.astype(str)), axis=1
)
all_data.head()

factors_name = ["PC_factor"]


# Begin the batch subject analysis
sub_num_list = sub_num_list[(sub_num_list > 34) & (sub_num_list < 37)]
for sub_num in sub_num_list:
    try:
        estimate_result = xia_fmri_workflow.workflow_condition_glm_1stlevel(
            root_dir, sub_num, session_num, factors_name, all_data, output_dir
        )
    except SystemExit:
        print(f"在处理 sub_num {sub_num} 时出错，旧文件仍存在，跳过该被试！")
        continue
    except Exception as e:
        print(f"在处理 sub_num {sub_num} 时出错，错误信息为：{str(e)}")
        continue

# %%
