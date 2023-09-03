% Load the participant information from the CSV file
T = readtable('/Volumes/Research/project9_fmri_spatial_stroop/program/analysis/fmri/02_condGLM/1stLevel/sub_type.csv', 'Delimiter', ',');  % Use '\t' as the delimiter

% Loop over each row in the table
for i = 27:28
    % Get the participant ID and the corresponding value
    participant_id = T.sub_num(i);  % Use 'sub_num' as the participant ID column
    value = T.volatile(i);  % Use 'volatile' as the value column
    
    fprintf(['Begin analysis sub ' num2str(participant_id) '\n']);

    % Determine which template script to execute based on the value
    if strcmp(value, 's')
        % Load the content of the 's' template script
        s_template = fileread('/Volumes/Research/project9_fmri_spatial_stroop/program/analysis/fmri/02_condGLM/1stLevel/condGLM_1stLevel_contrast_job_s_v_template.m');
        
        % Modify the 'spmmat' variable in the 's' template script
        s_template = strrep(s_template, 'spm_path/SPM.mat', ['/Volumes/Research/project9_fmri_spatial_stroop/data/output/fmri/condGLM/reverse_control/1stLevel/sub' num2str(participant_id) '/SPM.mat']);
        
        % Write the modified 's' template script back to the file
        fid = fopen('/Volumes/Research/project9_fmri_spatial_stroop/program/analysis/fmri/02_condGLM/1stLevel/tmp.m', 'w');
        fprintf(fid, '%s', s_template);
        fclose(fid);
        
        % Run the 's' template script
        nrun = 1; % enter the number of runs here
        jobfile = {'/Volumes/Research/project9_fmri_spatial_stroop/program/analysis/fmri/02_condGLM/1stLevel/tmp.m'};
        jobs = repmat(jobfile, 1, nrun);
        inputs = cell(0, nrun);
        for crun = 1:nrun
        end
        spm('defaults', 'FMRI');
        spm_jobman('run', jobs, inputs{:});
        
    elseif strcmp(value, 'v')
        % Load the content of the 'v' template script
        v_template = fileread('/Volumes/Research/project9_fmri_spatial_stroop/program/analysis/fmri/02_condGLM/1stLevel/condGLM_1stLevel_contrast_job_v_s_template.m');
        
        % Modify the 'spmmat' variable in the 'v' template script
        v_template = strrep(v_template, 'spm_path/SPM.mat', ['/Volumes/Research/project9_fmri_spatial_stroop/data/output/new_fmri/condGLM/reverse_control/1stLevel/sub' num2str(participant_id) '/SPM.mat']);
        
        % Write the modified 'v' template script back to the file
        fid = fopen('/Volumes/Research/project9_fmri_spatial_stroop/program/analysis/fmri/02_condGLM/1stLevel/condGLM_1stLevel_contrast_mod.m', 'w');
        fprintf(fid, '%s', v_template);
        fclose(fid);
        
        % Run the 'v' template script
        nrun = 1; % enter the number of runs here
        jobfile = {'/Volumes/Research/project9_fmri_spatial_stroop/program/analysis/fmri/02_condGLM/1stLevel/condGLM_1stLevel_contrast_mod.m'};
        jobs = repmat(jobfile, 1, nrun);
        inputs = cell(0, nrun);
        for crun = 1:nrun
        end
        spm('defaults', 'FMRI');
        spm_jobman('run', jobs, inputs{:});
    end
end
