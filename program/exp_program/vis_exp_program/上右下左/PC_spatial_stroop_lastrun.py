#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.3),
    on Thu Jan  5 22:20:03 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('latest')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from init_val
totalaccuracy = 0
errorsset = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.3'
expName = 'PC_spatial_stroop'  # from the Builder filename that created this script
expInfo = {
    'name': 'Xia Xiaokai',
    'sub_num': '01',
    'group': ['A','B','C','D'],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/sub_%s_%s_%s' % (expInfo['sub_num'], expInfo['name'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/dddd1007/ResearchData/project9_fmri_spatial_stroop/program/上右下左/PC_spatial_stroop_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "intro" ---
intro_image = visual.ImageStim(
    win=win,
    name='intro_image', 
    image='material/intro.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "fixation" ---
fixation_image = visual.ImageStim(
    win=win,
    name='fixation_image', 
    image='material/fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "stim" ---
stim_image = visual.ImageStim(
    win=win,
    name='stim_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
stim_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ITI" ---
ITI_text = visual.TextStim(win=win, name='ITI_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1,1,1], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "jitter_practice" ---
jitter_practice_text = visual.TextStim(win=win, name='jitter_practice_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "judge" ---
judge_message = visual.TextStim(win=win, name='judge_message',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
judge_resp = keyboard.Keyboard()

# --- Initialize components for Routine "wait_fmri" ---
wait_fmri_text = visual.TextStim(win=win, name='wait_fmri_text',
    text='Wating for begin...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
wait_fmri_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "three" ---
three_text = visual.TextStim(win=win, name='three_text',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
three_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "two" ---
two_text = visual.TextStim(win=win, name='two_text',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
two_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "one" ---
one_text = visual.TextStim(win=win, name='one_text',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
one_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "reset_jitter" ---

# --- Initialize components for Routine "fixation" ---
fixation_image = visual.ImageStim(
    win=win,
    name='fixation_image', 
    image='material/fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "stim" ---
stim_image = visual.ImageStim(
    win=win,
    name='stim_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
stim_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ITI" ---
ITI_text = visual.TextStim(win=win, name='ITI_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1,1,1], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "jitter" ---
jitter_text = visual.TextStim(win=win, name='jitter_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
recieve_trigger_jitter = keyboard.Keyboard()

# --- Initialize components for Routine "long_rest" ---
long_rest_image = visual.ImageStim(
    win=win,
    name='long_rest_image', 
    image='material/long_rest.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
recieve_trigger_long_rest = keyboard.Keyboard()

# --- Initialize components for Routine "long_rest_end" ---
long_rest_end_image = visual.ImageStim(
    win=win,
    name='long_rest_end_image', 
    image='material/end_rest.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
long_rest_end_resp = keyboard.Keyboard()

# --- Initialize components for Routine "end_exp" ---
end_exp_image = visual.ImageStim(
    win=win,
    name='end_exp_image', 
    image='material/end_exp.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
end_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_key_resp.keys = []
intro_key_resp.rt = []
_intro_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [intro_image, intro_key_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_image* updates
    if intro_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_image.frameNStart = frameN  # exact frame index
        intro_image.tStart = t  # local t and not account for scr refresh
        intro_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_image.started')
        intro_image.setAutoDraw(True)
    
    # *intro_key_resp* updates
    waitOnFlip = False
    if intro_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp.frameNStart = frameN  # exact frame index
        intro_key_resp.tStart = t  # local t and not account for scr refresh
        intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_key_resp.started')
        intro_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro_key_resp_allKeys.extend(theseKeys)
        if len(_intro_key_resp_allKeys):
            intro_key_resp.keys = _intro_key_resp_allKeys[-1].name  # just the last key pressed
            intro_key_resp.rt = _intro_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key_resp.keys in ['', [], None]:  # No response was made
    intro_key_resp.keys = None
thisExp.addData('intro_key_resp.keys',intro_key_resp.keys)
if intro_key_resp.keys != None:  # we had a response
    thisExp.addData('intro_key_resp.rt', intro_key_resp.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=4.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('seq/trial/exercise.csv'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_image]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 0.4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_image* updates
        if fixation_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_image.frameNStart = frameN  # exact frame index
            fixation_image.tStart = t  # local t and not account for scr refresh
            fixation_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_image.started')
            fixation_image.setAutoDraw(True)
        if fixation_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_image.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                fixation_image.tStop = t  # not accounting for scr refresh
                fixation_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_image.stopped')
                fixation_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.400000)
    
    # --- Prepare to start Routine "stim" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from response_code
    target_clock = core.Clock()
    target_begin = target_clock.getTime()
    stim_image.setImage(stim_image_loc)
    stim_resp.keys = []
    stim_resp.rt = []
    _stim_resp_allKeys = []
    # keep track of which components have finished
    stimComponents = [stim_image, stim_resp]
    for thisComponent in stimComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "stim" ---
    while continueRoutine and routineTimer.getTime() < 1.2:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_image* updates
        if stim_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_image.frameNStart = frameN  # exact frame index
            stim_image.tStart = t  # local t and not account for scr refresh
            stim_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim_image.started')
            stim_image.setAutoDraw(True)
        if stim_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_image.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                stim_image.tStop = t  # not accounting for scr refresh
                stim_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_image.stopped')
                stim_image.setAutoDraw(False)
        
        # *stim_resp* updates
        waitOnFlip = False
        if stim_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_resp.frameNStart = frameN  # exact frame index
            stim_resp.tStart = t  # local t and not account for scr refresh
            stim_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim_resp.started')
            stim_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(stim_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(stim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if stim_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_resp.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                stim_resp.tStop = t  # not accounting for scr refresh
                stim_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_resp.stopped')
                stim_resp.status = FINISHED
        if stim_resp.status == STARTED and not waitOnFlip:
            theseKeys = stim_resp.getKeys(keyList=['1','4'], waitRelease=False)
            _stim_resp_allKeys.extend(theseKeys)
            if len(_stim_resp_allKeys):
                stim_resp.keys = _stim_resp_allKeys[0].name  # just the first key pressed
                stim_resp.rt = _stim_resp_allKeys[0].rt
                # was this correct?
                if (stim_resp.keys == str(corr_resp)) or (stim_resp.keys == corr_resp):
                    stim_resp.corr = 1
                else:
                    stim_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stim" ---
    for thisComponent in stimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from response_code
    if stim_resp.corr:
        totalaccuracy=totalaccuracy+1
    else:
        errorsset=errorsset+1
    thisExp.addData('errorsset', errorsset)
    thisExp.addData('totalaccuracy', totalaccuracy)
    # check responses
    if stim_resp.keys in ['', [], None]:  # No response was made
        stim_resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp).lower() == 'none':
           stim_resp.corr = 1;  # correct non-response
        else:
           stim_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('stim_resp.keys',stim_resp.keys)
    practice_trials.addData('stim_resp.corr', stim_resp.corr)
    if stim_resp.keys != None:  # we had a response
        practice_trials.addData('stim_resp.rt', stim_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.200000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from iti_code
    iti_duration = 1.6 - (target_clock.getTime() - target_begin)
    # keep track of which components have finished
    ITIComponents = [ITI_text]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_text* updates
        if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_text.frameNStart = frameN  # exact frame index
            ITI_text.tStart = t  # local t and not account for scr refresh
            ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_text.started')
            ITI_text.setAutoDraw(True)
        if ITI_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_text.tStartRefresh + iti_duration-frameTolerance:
                # keep track of stop time/frame for later
                ITI_text.tStop = t  # not accounting for scr refresh
                ITI_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                ITI_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "jitter_practice" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    jitter_practiceComponents = [jitter_practice_text]
    for thisComponent in jitter_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "jitter_practice" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitter_practice_text* updates
        if jitter_practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jitter_practice_text.frameNStart = frameN  # exact frame index
            jitter_practice_text.tStart = t  # local t and not account for scr refresh
            jitter_practice_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jitter_practice_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'jitter_practice_text.started')
            jitter_practice_text.setAutoDraw(True)
        if jitter_practice_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jitter_practice_text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                jitter_practice_text.tStop = t  # not accounting for scr refresh
                jitter_practice_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'jitter_practice_text.stopped')
                jitter_practice_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitter_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "jitter_practice" ---
    for thisComponent in jitter_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'practice_trials'


# --- Prepare to start Routine "judge" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from judege_code
msg = "练习结束, \n你的正确率为" + str((totalaccuracy / 16) * 100) + "%" + "\n请按空格键开始实验!"
judge_message.setText(msg)
judge_resp.keys = []
judge_resp.rt = []
_judge_resp_allKeys = []
# keep track of which components have finished
judgeComponents = [judge_message, judge_resp]
for thisComponent in judgeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "judge" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *judge_message* updates
    if judge_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        judge_message.frameNStart = frameN  # exact frame index
        judge_message.tStart = t  # local t and not account for scr refresh
        judge_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(judge_message, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'judge_message.started')
        judge_message.setAutoDraw(True)
    
    # *judge_resp* updates
    waitOnFlip = False
    if judge_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        judge_resp.frameNStart = frameN  # exact frame index
        judge_resp.tStart = t  # local t and not account for scr refresh
        judge_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(judge_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'judge_resp.started')
        judge_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(judge_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(judge_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if judge_resp.status == STARTED and not waitOnFlip:
        theseKeys = judge_resp.getKeys(keyList=['space'], waitRelease=False)
        _judge_resp_allKeys.extend(theseKeys)
        if len(_judge_resp_allKeys):
            judge_resp.keys = _judge_resp_allKeys[-1].name  # just the last key pressed
            judge_resp.rt = _judge_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in judgeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "judge" ---
for thisComponent in judgeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from judege_code
totalaccuracy = 0
errorsset = 0

# check responses
if judge_resp.keys in ['', [], None]:  # No response was made
    judge_resp.keys = None
thisExp.addData('judge_resp.keys',judge_resp.keys)
if judge_resp.keys != None:  # we had a response
    thisExp.addData('judge_resp.rt', judge_resp.rt)
thisExp.nextEntry()
# the Routine "judge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('seq/run/run_'+str(expInfo['group'])+'.csv'),
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "wait_fmri" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wait_fmri_key_resp.keys = []
    wait_fmri_key_resp.rt = []
    _wait_fmri_key_resp_allKeys = []
    # keep track of which components have finished
    wait_fmriComponents = [wait_fmri_text, wait_fmri_key_resp]
    for thisComponent in wait_fmriComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wait_fmri" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wait_fmri_text* updates
        if wait_fmri_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_fmri_text.frameNStart = frameN  # exact frame index
            wait_fmri_text.tStart = t  # local t and not account for scr refresh
            wait_fmri_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_fmri_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wait_fmri_text.started')
            wait_fmri_text.setAutoDraw(True)
        
        # *wait_fmri_key_resp* updates
        waitOnFlip = False
        if wait_fmri_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wait_fmri_key_resp.frameNStart = frameN  # exact frame index
            wait_fmri_key_resp.tStart = t  # local t and not account for scr refresh
            wait_fmri_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wait_fmri_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wait_fmri_key_resp.started')
            wait_fmri_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wait_fmri_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wait_fmri_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wait_fmri_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = wait_fmri_key_resp.getKeys(keyList=['s'], waitRelease=False)
            _wait_fmri_key_resp_allKeys.extend(theseKeys)
            if len(_wait_fmri_key_resp_allKeys):
                wait_fmri_key_resp.keys = _wait_fmri_key_resp_allKeys[-1].name  # just the last key pressed
                wait_fmri_key_resp.rt = _wait_fmri_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wait_fmriComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wait_fmri" ---
    for thisComponent in wait_fmriComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if wait_fmri_key_resp.keys in ['', [], None]:  # No response was made
        wait_fmri_key_resp.keys = None
    runs.addData('wait_fmri_key_resp.keys',wait_fmri_key_resp.keys)
    if wait_fmri_key_resp.keys != None:  # we had a response
        runs.addData('wait_fmri_key_resp.rt', wait_fmri_key_resp.rt)
    # the Routine "wait_fmri" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "three" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    three_key_resp.keys = []
    three_key_resp.rt = []
    _three_key_resp_allKeys = []
    # keep track of which components have finished
    threeComponents = [three_text, three_key_resp]
    for thisComponent in threeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "three" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *three_text* updates
        if three_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            three_text.frameNStart = frameN  # exact frame index
            three_text.tStart = t  # local t and not account for scr refresh
            three_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'three_text.started')
            three_text.setAutoDraw(True)
        
        # *three_key_resp* updates
        waitOnFlip = False
        if three_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            three_key_resp.frameNStart = frameN  # exact frame index
            three_key_resp.tStart = t  # local t and not account for scr refresh
            three_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'three_key_resp.started')
            three_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(three_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(three_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if three_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = three_key_resp.getKeys(keyList=['s'], waitRelease=False)
            _three_key_resp_allKeys.extend(theseKeys)
            if len(_three_key_resp_allKeys):
                three_key_resp.keys = _three_key_resp_allKeys[-1].name  # just the last key pressed
                three_key_resp.rt = _three_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in threeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "three" ---
    for thisComponent in threeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if three_key_resp.keys in ['', [], None]:  # No response was made
        three_key_resp.keys = None
    runs.addData('three_key_resp.keys',three_key_resp.keys)
    if three_key_resp.keys != None:  # we had a response
        runs.addData('three_key_resp.rt', three_key_resp.rt)
    # the Routine "three" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "two" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    two_key_resp.keys = []
    two_key_resp.rt = []
    _two_key_resp_allKeys = []
    # keep track of which components have finished
    twoComponents = [two_text, two_key_resp]
    for thisComponent in twoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "two" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *two_text* updates
        if two_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            two_text.frameNStart = frameN  # exact frame index
            two_text.tStart = t  # local t and not account for scr refresh
            two_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two_text.started')
            two_text.setAutoDraw(True)
        
        # *two_key_resp* updates
        waitOnFlip = False
        if two_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            two_key_resp.frameNStart = frameN  # exact frame index
            two_key_resp.tStart = t  # local t and not account for scr refresh
            two_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two_key_resp.started')
            two_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(two_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(two_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if two_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = two_key_resp.getKeys(keyList=['s'], waitRelease=False)
            _two_key_resp_allKeys.extend(theseKeys)
            if len(_two_key_resp_allKeys):
                two_key_resp.keys = _two_key_resp_allKeys[-1].name  # just the last key pressed
                two_key_resp.rt = _two_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in twoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "two" ---
    for thisComponent in twoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if two_key_resp.keys in ['', [], None]:  # No response was made
        two_key_resp.keys = None
    runs.addData('two_key_resp.keys',two_key_resp.keys)
    if two_key_resp.keys != None:  # we had a response
        runs.addData('two_key_resp.rt', two_key_resp.rt)
    # the Routine "two" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "one" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    one_key_resp.keys = []
    one_key_resp.rt = []
    _one_key_resp_allKeys = []
    # keep track of which components have finished
    oneComponents = [one_text, one_key_resp]
    for thisComponent in oneComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "one" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *one_text* updates
        if one_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one_text.frameNStart = frameN  # exact frame index
            one_text.tStart = t  # local t and not account for scr refresh
            one_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'one_text.started')
            one_text.setAutoDraw(True)
        
        # *one_key_resp* updates
        waitOnFlip = False
        if one_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one_key_resp.frameNStart = frameN  # exact frame index
            one_key_resp.tStart = t  # local t and not account for scr refresh
            one_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'one_key_resp.started')
            one_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(one_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(one_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if one_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = one_key_resp.getKeys(keyList=['s'], waitRelease=False)
            _one_key_resp_allKeys.extend(theseKeys)
            if len(_one_key_resp_allKeys):
                one_key_resp.keys = _one_key_resp_allKeys[-1].name  # just the last key pressed
                one_key_resp.rt = _one_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in oneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "one" ---
    for thisComponent in oneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if one_key_resp.keys in ['', [], None]:  # No response was made
        one_key_resp.keys = None
    runs.addData('one_key_resp.keys',one_key_resp.keys)
    if one_key_resp.keys != None:  # we had a response
        runs.addData('one_key_resp.rt', one_key_resp.rt)
    # the Routine "one" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(block_seq),
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "reset_jitter" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from reset_jitter_code_2
        jitter_list = [1.8,1.8,2.05,2.05,2.3,2.3,2.3,2.3,2.3,2.55,2.55,2.55,2.55,2.55,2.55,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,3.05,3.05,3.05,3.05,3.05,3.05,3.05,3.05,3.05,3.05,3.05,3.05,3.05,3.05,3.05]
        shuffle(jitter_list)
        thisExp.addData('jitter_list', jitter_list)
        count_num = 0
        # keep track of which components have finished
        reset_jitterComponents = []
        for thisComponent in reset_jitterComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reset_jitter" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reset_jitterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reset_jitter" ---
        for thisComponent in reset_jitterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "reset_jitter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=4.0, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(seqfile),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "fixation" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            fixationComponents = [fixation_image]
            for thisComponent in fixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            while continueRoutine and routineTimer.getTime() < 0.4:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_image* updates
                if fixation_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_image.frameNStart = frameN  # exact frame index
                    fixation_image.tStart = t  # local t and not account for scr refresh
                    fixation_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_image.started')
                    fixation_image.setAutoDraw(True)
                if fixation_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_image.tStartRefresh + 0.4-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_image.tStop = t  # not accounting for scr refresh
                        fixation_image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_image.stopped')
                        fixation_image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.400000)
            
            # --- Prepare to start Routine "stim" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from response_code
            target_clock = core.Clock()
            target_begin = target_clock.getTime()
            stim_image.setImage(stim_image_loc)
            stim_resp.keys = []
            stim_resp.rt = []
            _stim_resp_allKeys = []
            # keep track of which components have finished
            stimComponents = [stim_image, stim_resp]
            for thisComponent in stimComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stim" ---
            while continueRoutine and routineTimer.getTime() < 1.2:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stim_image* updates
                if stim_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stim_image.frameNStart = frameN  # exact frame index
                    stim_image.tStart = t  # local t and not account for scr refresh
                    stim_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_image.started')
                    stim_image.setAutoDraw(True)
                if stim_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim_image.tStartRefresh + 0.4-frameTolerance:
                        # keep track of stop time/frame for later
                        stim_image.tStop = t  # not accounting for scr refresh
                        stim_image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim_image.stopped')
                        stim_image.setAutoDraw(False)
                
                # *stim_resp* updates
                waitOnFlip = False
                if stim_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stim_resp.frameNStart = frameN  # exact frame index
                    stim_resp.tStart = t  # local t and not account for scr refresh
                    stim_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_resp.started')
                    stim_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(stim_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(stim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if stim_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stim_resp.tStartRefresh + 1.2-frameTolerance:
                        # keep track of stop time/frame for later
                        stim_resp.tStop = t  # not accounting for scr refresh
                        stim_resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim_resp.stopped')
                        stim_resp.status = FINISHED
                if stim_resp.status == STARTED and not waitOnFlip:
                    theseKeys = stim_resp.getKeys(keyList=['1','4'], waitRelease=False)
                    _stim_resp_allKeys.extend(theseKeys)
                    if len(_stim_resp_allKeys):
                        stim_resp.keys = _stim_resp_allKeys[0].name  # just the first key pressed
                        stim_resp.rt = _stim_resp_allKeys[0].rt
                        # was this correct?
                        if (stim_resp.keys == str(corr_resp)) or (stim_resp.keys == corr_resp):
                            stim_resp.corr = 1
                        else:
                            stim_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stimComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stim" ---
            for thisComponent in stimComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from response_code
            if stim_resp.corr:
                totalaccuracy=totalaccuracy+1
            else:
                errorsset=errorsset+1
            thisExp.addData('errorsset', errorsset)
            thisExp.addData('totalaccuracy', totalaccuracy)
            # check responses
            if stim_resp.keys in ['', [], None]:  # No response was made
                stim_resp.keys = None
                # was no response the correct answer?!
                if str(corr_resp).lower() == 'none':
                   stim_resp.corr = 1;  # correct non-response
                else:
                   stim_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('stim_resp.keys',stim_resp.keys)
            trials.addData('stim_resp.corr', stim_resp.corr)
            if stim_resp.keys != None:  # we had a response
                trials.addData('stim_resp.rt', stim_resp.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.200000)
            
            # --- Prepare to start Routine "ITI" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from iti_code
            iti_duration = 1.6 - (target_clock.getTime() - target_begin)
            # keep track of which components have finished
            ITIComponents = [ITI_text]
            for thisComponent in ITIComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ITI_text* updates
                if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI_text.frameNStart = frameN  # exact frame index
                    ITI_text.tStart = t  # local t and not account for scr refresh
                    ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_text.started')
                    ITI_text.setAutoDraw(True)
                if ITI_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ITI_text.tStartRefresh + iti_duration-frameTolerance:
                        # keep track of stop time/frame for later
                        ITI_text.tStop = t  # not accounting for scr refresh
                        ITI_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                        ITI_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "jitter" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from jitter_code
            jitter_duration = jitter_list[count_num]
            thisExp.addData('count_num', count_num)
            count_num = count_num + 1
            thisExp.addData('jitter', jitter_duration)
            recieve_trigger_jitter.keys = []
            recieve_trigger_jitter.rt = []
            _recieve_trigger_jitter_allKeys = []
            # keep track of which components have finished
            jitterComponents = [jitter_text, recieve_trigger_jitter]
            for thisComponent in jitterComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "jitter" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *jitter_text* updates
                if jitter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    jitter_text.frameNStart = frameN  # exact frame index
                    jitter_text.tStart = t  # local t and not account for scr refresh
                    jitter_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(jitter_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'jitter_text.started')
                    jitter_text.setAutoDraw(True)
                if jitter_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > jitter_text.tStartRefresh + jitter_duration-frameTolerance:
                        # keep track of stop time/frame for later
                        jitter_text.tStop = t  # not accounting for scr refresh
                        jitter_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'jitter_text.stopped')
                        jitter_text.setAutoDraw(False)
                
                # *recieve_trigger_jitter* updates
                waitOnFlip = False
                if recieve_trigger_jitter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    recieve_trigger_jitter.frameNStart = frameN  # exact frame index
                    recieve_trigger_jitter.tStart = t  # local t and not account for scr refresh
                    recieve_trigger_jitter.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(recieve_trigger_jitter, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recieve_trigger_jitter.started')
                    recieve_trigger_jitter.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(recieve_trigger_jitter.clock.reset)  # t=0 on next screen flip
                if recieve_trigger_jitter.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > recieve_trigger_jitter.tStartRefresh + jitter_duration-frameTolerance:
                        # keep track of stop time/frame for later
                        recieve_trigger_jitter.tStop = t  # not accounting for scr refresh
                        recieve_trigger_jitter.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'recieve_trigger_jitter.stopped')
                        recieve_trigger_jitter.status = FINISHED
                if recieve_trigger_jitter.status == STARTED and not waitOnFlip:
                    theseKeys = recieve_trigger_jitter.getKeys(keyList=['s'], waitRelease=False)
                    _recieve_trigger_jitter_allKeys.extend(theseKeys)
                    if len(_recieve_trigger_jitter_allKeys):
                        recieve_trigger_jitter.keys = [key.name for key in _recieve_trigger_jitter_allKeys]  # storing all keys
                        recieve_trigger_jitter.rt = [key.rt for key in _recieve_trigger_jitter_allKeys]
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in jitterComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "jitter" ---
            for thisComponent in jitterComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if recieve_trigger_jitter.keys in ['', [], None]:  # No response was made
                recieve_trigger_jitter.keys = None
            trials.addData('recieve_trigger_jitter.keys',recieve_trigger_jitter.keys)
            if recieve_trigger_jitter.keys != None:  # we had a response
                trials.addData('recieve_trigger_jitter.rt', recieve_trigger_jitter.rt)
            # the Routine "jitter" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'trials'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'blocks'
    
    
    # --- Prepare to start Routine "long_rest" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    recieve_trigger_long_rest.keys = []
    recieve_trigger_long_rest.rt = []
    _recieve_trigger_long_rest_allKeys = []
    # keep track of which components have finished
    long_restComponents = [long_rest_image, recieve_trigger_long_rest]
    for thisComponent in long_restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "long_rest" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *long_rest_image* updates
        if long_rest_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            long_rest_image.frameNStart = frameN  # exact frame index
            long_rest_image.tStart = t  # local t and not account for scr refresh
            long_rest_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(long_rest_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'long_rest_image.started')
            long_rest_image.setAutoDraw(True)
        if long_rest_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > long_rest_image.tStartRefresh + long_rest_duration-frameTolerance:
                # keep track of stop time/frame for later
                long_rest_image.tStop = t  # not accounting for scr refresh
                long_rest_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'long_rest_image.stopped')
                long_rest_image.setAutoDraw(False)
        
        # *recieve_trigger_long_rest* updates
        waitOnFlip = False
        if recieve_trigger_long_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recieve_trigger_long_rest.frameNStart = frameN  # exact frame index
            recieve_trigger_long_rest.tStart = t  # local t and not account for scr refresh
            recieve_trigger_long_rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recieve_trigger_long_rest, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recieve_trigger_long_rest.started')
            recieve_trigger_long_rest.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(recieve_trigger_long_rest.clock.reset)  # t=0 on next screen flip
        if recieve_trigger_long_rest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > recieve_trigger_long_rest.tStartRefresh + long_rest_duration-frameTolerance:
                # keep track of stop time/frame for later
                recieve_trigger_long_rest.tStop = t  # not accounting for scr refresh
                recieve_trigger_long_rest.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recieve_trigger_long_rest.stopped')
                recieve_trigger_long_rest.status = FINISHED
        if recieve_trigger_long_rest.status == STARTED and not waitOnFlip:
            theseKeys = recieve_trigger_long_rest.getKeys(keyList=['s'], waitRelease=False)
            _recieve_trigger_long_rest_allKeys.extend(theseKeys)
            if len(_recieve_trigger_long_rest_allKeys):
                recieve_trigger_long_rest.keys = [key.name for key in _recieve_trigger_long_rest_allKeys]  # storing all keys
                recieve_trigger_long_rest.rt = [key.rt for key in _recieve_trigger_long_rest_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in long_restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "long_rest" ---
    for thisComponent in long_restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if recieve_trigger_long_rest.keys in ['', [], None]:  # No response was made
        recieve_trigger_long_rest.keys = None
    runs.addData('recieve_trigger_long_rest.keys',recieve_trigger_long_rest.keys)
    if recieve_trigger_long_rest.keys != None:  # we had a response
        runs.addData('recieve_trigger_long_rest.rt', recieve_trigger_long_rest.rt)
    # the Routine "long_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "long_rest_end" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    long_rest_end_resp.keys = []
    long_rest_end_resp.rt = []
    _long_rest_end_resp_allKeys = []
    # keep track of which components have finished
    long_rest_endComponents = [long_rest_end_image, long_rest_end_resp]
    for thisComponent in long_rest_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "long_rest_end" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *long_rest_end_image* updates
        if long_rest_end_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            long_rest_end_image.frameNStart = frameN  # exact frame index
            long_rest_end_image.tStart = t  # local t and not account for scr refresh
            long_rest_end_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(long_rest_end_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'long_rest_end_image.started')
            long_rest_end_image.setAutoDraw(True)
        
        # *long_rest_end_resp* updates
        waitOnFlip = False
        if long_rest_end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            long_rest_end_resp.frameNStart = frameN  # exact frame index
            long_rest_end_resp.tStart = t  # local t and not account for scr refresh
            long_rest_end_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(long_rest_end_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'long_rest_end_resp.started')
            long_rest_end_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(long_rest_end_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(long_rest_end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if long_rest_end_resp.status == STARTED and not waitOnFlip:
            theseKeys = long_rest_end_resp.getKeys(keyList=['space'], waitRelease=False)
            _long_rest_end_resp_allKeys.extend(theseKeys)
            if len(_long_rest_end_resp_allKeys):
                long_rest_end_resp.keys = _long_rest_end_resp_allKeys[-1].name  # just the last key pressed
                long_rest_end_resp.rt = _long_rest_end_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in long_rest_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "long_rest_end" ---
    for thisComponent in long_rest_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if long_rest_end_resp.keys in ['', [], None]:  # No response was made
        long_rest_end_resp.keys = None
    runs.addData('long_rest_end_resp.keys',long_rest_end_resp.keys)
    if long_rest_end_resp.keys != None:  # we had a response
        runs.addData('long_rest_end_resp.rt', long_rest_end_resp.rt)
    # the Routine "long_rest_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'runs'


# --- Prepare to start Routine "end_exp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
# keep track of which components have finished
end_expComponents = [end_exp_image, end_resp]
for thisComponent in end_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end_exp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_exp_image* updates
    if end_exp_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_exp_image.frameNStart = frameN  # exact frame index
        end_exp_image.tStart = t  # local t and not account for scr refresh
        end_exp_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_exp_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_exp_image.started')
        end_exp_image.setAutoDraw(True)
    
    # *end_resp* updates
    waitOnFlip = False
    if end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_resp.started')
        end_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_resp.getKeys(keyList=['space'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_exp" ---
for thisComponent in end_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_resp.keys in ['', [], None]:  # No response was made
    end_resp.keys = None
thisExp.addData('end_resp.keys',end_resp.keys)
if end_resp.keys != None:  # we had a response
    thisExp.addData('end_resp.rt', end_resp.rt)
thisExp.nextEntry()
# the Routine "end_exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
