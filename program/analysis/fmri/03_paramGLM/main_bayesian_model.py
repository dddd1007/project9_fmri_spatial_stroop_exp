# 配置基本环境
# %%
import xia_fmri_workflow
from pathlib import Path
import pandas as pd
import os
import re
import scipy.io
from joblib import Parallel, delayed
from nipype.interfaces.spm import Level1Design, EstimateModel, EstimateContrast
from nipype.algorithms.modelgen import SpecifySPMModel

base_path = "/Volumes/Research/all_research_data/project9_fmri_spatial_stroop/data/input"
# 读取被试数据
all_data = pd.read_excel(os.path.join(base_path, "all_data_with_params.xlsx"))

# 被试基本信息
session_num = 6

# 数据位置
root_dir = "/Volumes/Research/all_research_data/project9_fmri_spatial_stroop/data/input/fmri_data/nii"
output_dir = "/Volumes/Research/all_research_data/project9_fmri_spatial_stroop/data/output/param_glm/fmri_add_kl"

# %%
# Set the basic params
params_name = ["congruency_num", "bl_sr_original_kl", "bl_sr_pe"]
# make the contrast matrix
# fmt: off
condition_names = ["run_1", "", "run_1xcongruency_num^1", "", "run_1xbl_sr_original_kl^1", "",
                   "run_1xbl_sr_pe^1", "", "run_error_1", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_2", "", "run_2xcongruency_num^1", "", "run_2xbl_sr_original_kl^1", "",
                   "run_2xbl_sr_pe^1", "", "run_error_2", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_3", "", "run_3xcongruency_num^1", "", "run_3xbl_sr_original_kl^1", "",
                   "run_3xbl_sr_pe^1", "", "run_error_3", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_4", "", "run_4xcongruency_num^1", "", "run_4xbl_sr_original_kl^1", "",
                   "run_4xbl_sr_pe^1", "", "run_error_4", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_5", "", "run_5xcongruency_num^1", "", "run_5xbl_sr_original_kl^1", "",
                   "run_5xbl_sr_pe^1", "", "run_error_5", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_6", "", "run_6xcongruency_num^1", "", "run_6xbl_sr_original_kl^1", "",
                   "run_6xbl_sr_pe^1", "", "run_error_6", "", "X", "Y", "Z", "x_r", "y_r", "z_r"]  # noqa: E501
cont1 = ["V", 'T', condition_names,    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cont2 = ["PE", 'T', condition_names,   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cont3 = ["PE_neg", 'T', condition_names,   [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                            0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                            0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                            0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                            0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                            0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# fmt: on
contrast_list = [cont1, cont2]
# batch analysis
sub_num_list = all_data["sub_num"].unique()
inputs = sub_num_list[(sub_num_list != 41) & (sub_num_list > 10)]


def bl_processInput(sub_num):
    if not isinstance(sub_num, int):
        sub_num = int(sub_num)
    try:
        estimate_result = xia_fmri_workflow.workflow_param_glm_1stlevel(
            root_dir,
            sub_num,
            session_num,
            params_name,
            all_data,
            output_dir,
            "bl",
        )
        contrast_result = xia_fmri_workflow.workflow_contrast(
            estimate_result, contrast_list
        )
        return contrast_result
    except SystemExit:
        print(f"在处理 sub_num {sub_num} 时出错，错误信息为：旧文件仍存在！")
        return None
    except Exception as e:
        print(f"在处理 sub_num {sub_num} 时出错，错误信息为：{str(e)}")
        return None


results = Parallel(n_jobs=3)(
    delayed(bl_processInput)(sub_num) for sub_num in inputs
)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# %%
# The sub 41 don't have the session 1, so we treat it specially

# Set the basic params
# fmt: off
params_name = ['congruency_num', 'bl_sr_original_kl', 'bl_sr_pe']
# make the contrast matrix
condition_names = ["run_2", "", "run_2xcongruency_num^1", "", "run_2xbl_sr_original_kl^1", "",
                   "run_2xbl_sr_pe^1", "", "run_error_2", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_3", "", "run_3xcongruency_num^1", "", "run_3xbl_sr_original_kl^1", "",
                   "run_3xbl_sr_pe^1", "", "run_error_3", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_4", "", "run_4xcongruency_num^1", "", "run_4xbl_sr_original_kl^1", "",
                   "run_4xbl_sr_pe^1", "", "run_error_4", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_5", "", "run_5xcongruency_num^1", "", "run_5xbl_sr_original_kl^1", "",
                   "run_5xbl_sr_pe^1", "", "run_error_5", "", "X", "Y", "Z", "x_r", "y_r", "z_r",  # noqa: E501
                   "run_6", "", "run_6xcongruency_num^1", "", "run_6xbl_sr_original_kl^1", "",
                   "run_6xbl_sr_pe^1", "", "run_error_6", "", "X", "Y", "Z", "x_r", "y_r", "z_r"]  # noqa: E501
cont1 = ["-V", 'T', condition_names,   [
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
cont2 = ["PE", 'T', condition_names,   [
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
contrast_list = [cont1, cont2]
# fmt: on

# Modified the function in the workflow


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
                realignment_para_file_list[int(i) - 1]
            ),
        )
        subject_info.append(tmp_Bunch)
    return subject_info


def parametric_condition_generator(
    single_sub_data,
    params_name,
    realignment_para_file_list,
    duration=0,
    centering=True,
):
    from nipype.interfaces.base import Bunch
    import numpy as np

    run_num = set(single_sub_data.run_num)
    print(run_num)
    subject_info = []
    for i in run_num:
        tmp_table = single_sub_data[single_sub_data.run == i]

        tmp_table_right = tmp_table[tmp_table["stim_resp.corr"] == 1]
        tmp_table_wrong = tmp_table[tmp_table["stim_resp.corr"] == 0]

        pmod_names = []
        pmod_params = []
        pmod_poly = []
        for param in params_name:
            param_value = tmp_table_right[param].values.tolist()
            demean_value = param_value - np.mean(param_value)
            centered_value = demean_value / np.max(demean_value)
            if centering == True:
                # Doing the mean centering
                pmod_params.append(centered_value.tolist())
            elif centering == False:
                pmod_params.append(param_value)
            pmod_names.append(param)
            pmod_poly.append(1)

        error_onsets = tmp_table_wrong.onset.values.tolist()
        if len(error_onsets) == 0:
            error_onsets = [510]

        tmp_Bunch = Bunch(
            conditions=["run_" + str(i), "run_error_" + str(i)],
            onsets=[tmp_table_right.onset.values.tolist(), error_onsets],
            durations=[[duration], [duration]],
            pmod=[
                Bunch(name=pmod_names, poly=pmod_poly, param=pmod_params),
                None,
            ],
            regressor_names=["X", "Y", "Z", "x_r", "y_r", "z_r"],
            regressors=head_movement_regressor_generator(
                realignment_para_file_list[int(i) - 2]
            ),
        )
        subject_info.append(tmp_Bunch)

    return subject_info


def generate_spm_conditions(matfile):
    spm = scipy.io.loadmat(matfile)
    all_conditions_list = spm["SPM"][0][0]["xX"]["name"][0][0][0].tolist()
    all_conditions = [
        x.tolist()[0] for x in spm["SPM"][0][0]["xX"]["name"][0][0][0].tolist()
    ]
    condition_names = [re.sub("Sn\(.\) ", "", i) for i in all_conditions]
    conditions_count = len(all_conditions) / 6
    single_run_conditions = [
        all_conditions_list[x][0] for x in range(int(conditions_count - 1))
    ]

    return condition_names, single_run_conditions


output_dir = "/Users/dddd1007/Library/CloudStorage/Dropbox/Work/Research/project9_fmri_spatial_stroop/data/output/fmri/paramGLM/new_bl/1stLevel/sub41"
Path(output_dir).mkdir(parents=True, exist_ok=True)
os.chdir(output_dir)
root_dir = "/Volumes/research/backup/project9_fmri_spatial_stroop/data/input/fmri_data/nii"
sub_num = 41
session_num = 6

print("Generating SPM model for subject " + str(sub_num) + "...")

nii_list, realignment_para_file_list, single_sub_data, sub_name = nii_selector(
    root_dir, sub_num, session_num, all_data
)
single_sub_data = single_sub_data[single_sub_data.run_num >= 2]
print(realignment_para_file_list)
subject_info = parametric_condition_generator(
    single_sub_data, params_name, realignment_para_file_list, centering=False
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

print("Contrast SPM model for subject " + str(sub_num) + " (2/2)...")
estimator = EstimateModel(
    estimation_method={"Classical": 1},
    spm_mat_file=firstLevelModel.outputs.spm_mat_file,
)
estimateResult = estimator.run()
print("Contrast SPM model")
level1conest = EstimateContrast(
    beta_images=estimateResult.outputs.beta_images,
    residual_image=estimateResult.outputs.residual_image,
    spm_mat_file=estimateResult.outputs.spm_mat_file,
    contrasts=contrast_list,
)
contrastResult = level1conest.run()

# %%
