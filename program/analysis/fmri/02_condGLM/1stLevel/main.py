# %% [markdown]
# # fMRI 分析
# ## 0. 环境配置

# %%
# 配置基本环境
import os
import xia_fmri_workflow
from pathlib import Path
import pandas as pd

# 读取被试数据
all_data = pd.read_csv(
    "/Volumes/Research/project9_fmri_spatial_stroop/data/input/all_data_with_params.csv"
)
# 被试基本信息
sub_num_list = pd.unique(all_data["sub_num"])
session_num = 6

# 数据位置
root_dir = "/Volumes/Research/project9_fmri_spatial_stroop/data/input/fmri_data/new_nii"
output_dir = (
    "/Volumes/Research/project9_fmri_spatial_stroop/data/output/new_fmri/"
)

all_data.columns
all_data["PC_factor"] = all_data[["volatile", "prop", "congruency"]].apply(
    lambda row: "_".join(row.astype(str)), axis=1
)
all_data.head()

factors_name = ["PC_factor"]
sub_num_list = sub_num_list[(sub_num_list > 8) & (sub_num_list != 41)]
for sub_num in sub_num_list:
    try:
        estimate_result = xia_fmri_workflow.workflow_condition_glm_1stlevel(
            root_dir, sub_num, session_num, factors_name, all_data, output_dir
        )
    except SystemExit:
        print(f"在处理 sub_num {sub_num} 时出错，错误信息为：旧文件仍存在！")
        continue
    except Exception as e:
        print(f"在处理 sub_num {sub_num} 时出错，错误信息为：{str(e)}")
        continue


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# %%
# The sub 41 don't have the session 1, so we treat it specially
def nii_selector(
    root_dir, sub_num, session_num, all_sub_dataframe, data_type="Smooth_8mm"
):
    import os
    import glob

    session_list = ["session" + str(i) for i in range(2, session_num + 1)]
    sub_name = "sub" + str(sub_num)
    # print(file_path)
    nii_list = []
    realignment_para_file_list = []
    for s in session_list:
        file_path = os.path.join(root_dir, sub_name, data_type, s)
        Orig_path = os.path.join(root_dir, sub_name, "Orig", s)
        nii_list.append(sorted(glob.glob(file_path + "/*.nii")))
        realignment_para_file_list.append(glob.glob(Orig_path + "/rp_*.txt"))

    single_sub_data = all_sub_dataframe[all_sub_dataframe.sub_num == sub_num]
    return (nii_list, realignment_para_file_list, single_sub_data, sub_name)


def head_movement_regressor_generator(single_realignment_para_file):
    import numpy as np

    if type(single_realignment_para_file) is list:
        single_realignment_para_file = single_realignment_para_file[0]
    relignment_params = np.loadtxt(single_realignment_para_file)
    head_movement_regressor = relignment_params.T.tolist()
    return head_movement_regressor


# Build the relationship between onsets and parameters


def factor_condition_generator(
    single_sub_data, factors_name, realignment_para_file_list, duration=0
):
    """Build a bunch to show the relationship between each onset and parameter

    Build a bunch for make a design matrix for next analysis. This bunch is for describing the relationship
    between each onset and parameter.

    Args:
        single_sub_data: A pandas DataFrame which contains data for one subject.
                        It must contains the information about run, onsets, and parameters.
        factors_name: A list of names of conditions which you want to analysis.
        duration: The duration of a TR.

    Returns:
        subject_info: A list of bunch type which can be resolve by SpecifySPMModel interface in nipype.
    """
    from nipype.interfaces.base import Bunch

    run_num = set(single_sub_data.run)
    subject_info = []
    for i in run_num:
        single_run_table = single_sub_data[single_sub_data.run == i]

        tmp_table_right = single_run_table[
            single_run_table["stim_resp.corr"] == 1
        ]
        tmp_table_wrong = single_run_table[
            single_run_table["stim_resp.corr"] == 0
        ]

        condition_table = pd.DataFrame()
        condition_table[factors_name] = tmp_table_right[factors_name].astype(
            "category"
        )
        condition_table["onset"] = tmp_table_right.onset
        onset_condition_table = condition_table.pivot(
            values="onset", columns=factors_name
        )

        bunch_condition = []
        bunch_onsets = []
        bunch_duration = []

        error_onsets = tmp_table_wrong.onset.values.tolist()
        if len(error_onsets) == 0:
            error_onsets = [510]

        for j in range(len(onset_condition_table.columns)):
            bunch_condition.append(
                "run_" + str(i) + "_" + str(onset_condition_table.columns[j])
            )
            bunch_onsets.append(
                onset_condition_table[onset_condition_table.columns[j]]
                .dropna(how="all")
                .tolist()
            )
            bunch_duration.append([duration])
        bunch_condition.append("run_error_" + str(i))
        bunch_onsets.append(error_onsets)
        bunch_duration.append([duration])
        tmp_Bunch = Bunch(
            conditions=bunch_condition,
            onsets=bunch_onsets,
            durations=bunch_duration,
            regressor_names=["X", "Y", "Z", "x_r", "y_r", "z_r"],
            regressors=head_movement_regressor_generator(
                realignment_para_file_list[i - 2]
            ),
        )
        subject_info.append(tmp_Bunch)
    return subject_info


output_dir = "/Volumes/Research/project9_fmri_spatial_stroop/output/fmri/condGLM/reverse_control/1stLevel/sub41"
Path(output_dir).mkdir(parents=True, exist_ok=True)
os.chdir(output_dir)
root_dir = "/Volumes/Research/project9_fmri_spatial_stroop/input/fmri_data/nii/"
sub_num = 41
session_num = 6

print("Generating SPM model for subject " + str(sub_num) + "...")

from nipype.interfaces.spm import Level1Design, EstimateModel, EstimateContrast
from nipype.algorithms.modelgen import SpecifySPMModel
from numpy import single

factors_name = ["PC_factor"]
nii_list, realignment_para_file_list, single_sub_data, sub_name = nii_selector(
    root_dir, sub_num, session_num, all_data
)
single_sub_data = single_sub_data[single_sub_data["run_num"] >= 2]

# %%
subject_info = factor_condition_generator(
    single_sub_data, factors_name, realignment_para_file_list
)
gen_model = SpecifySPMModel(
    concatenate_runs=False,
    input_units="scans",
    output_units="scans",
    time_repetition=1.5,
    high_pass_filter_cutoff=128,
    subject_info=subject_info,
    functional_runs=nii_list,
)
spmModel = gen_model.run()

print("Estimating SPM model for subject " + str(sub_num) + " (1/2)...")
design_model = Level1Design(
    bases={"hrf": {"derivs": [1, 0]}},
    timing_units="scans",
    interscan_interval=1.5,
    microtime_resolution=32,
    microtime_onset=1,
    session_info=spmModel.outputs.session_info,
    spm_mat_dir=output_dir,
)

firstLevelModel = design_model.run()

print("Estimating SPM model for subject " + str(sub_num) + " (2/2)...")
estimator = EstimateModel(
    estimation_method={"Classical": 1},
    spm_mat_file=firstLevelModel.outputs.spm_mat_file,
)
estimateResult = estimator.run()
