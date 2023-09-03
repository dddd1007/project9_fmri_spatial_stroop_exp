% List of open inputs
nrun = 1; % enter the number of runs here
jobfile = {'/Volumes/Research/project9_fmri_spatial_stroop/program/analysis/fmri/02_condGLM/2ndLevel/condGLM_2ndLevel_analysis_job.m'};
jobs = repmat(jobfile, 1, nrun);
inputs = cell(0, nrun);
for crun = 1:nrun
end
spm('defaults', 'FMRI');
spm_jobman('run', jobs, inputs{:});
