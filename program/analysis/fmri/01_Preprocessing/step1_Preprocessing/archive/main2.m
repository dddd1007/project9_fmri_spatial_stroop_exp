% 定义所需资源
spm8_param_path = '/home/dddd1007/Research/project9_fmri_spatial_stroop/program/analysis/fmri/Preprocessing/step1_Preprocessing/SPM8_Parameters.mat';
home_folder = '/home/dddd1007/Research/project9_fmri_spatial_stroop/data/input/fmri_data/';
subject_folder = cell(1, 8); % 预分配内存
for i = 1:8
    subject_folder{i} = sprintf('sub%.2d', i + 16); % sprintf 创建一个格式化字符串。'%.2d' 意味着打印两位数，前面用0填充。
end

% 批量预处理
for i = 1:length(subject_folder)
    try
        func_preprocess(home_folder, subject_folder{i}, spm8_param_path)
    catch ME
        fprintf('Error while processing %s: %s\n', subject_folder{i}, ME.message);
        % 这行代码将打印出出错的主题和错误信息
        continue % 跳过当前循环的剩余部分并开始下一次循环
    end
end