/************************** 
 * Pc_Spatial_Stroop Test *
 **************************/


// store info about the experiment session:
let expName = 'PC_spatial_stroop';  // from the Builder filename that created this script
let expInfo = {
    'name': 'Xia Xiaokai',
    'sub_num': '01',
    'group': ["A", "B", "C", "D"],
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from init_val
totalaccuracy = 0;
errorsset = 0;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([-1.0000, -1.0000, -1.0000]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(introRoutineBegin());
flowScheduler.add(introRoutineEachFrame());
flowScheduler.add(introRoutineEnd());
const practice_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_trialsLoopBegin(practice_trialsLoopScheduler));
flowScheduler.add(practice_trialsLoopScheduler);
flowScheduler.add(practice_trialsLoopEnd);
flowScheduler.add(judgeRoutineBegin());
flowScheduler.add(judgeRoutineEachFrame());
flowScheduler.add(judgeRoutineEnd());
const runsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(runsLoopBegin(runsLoopScheduler));
flowScheduler.add(runsLoopScheduler);
flowScheduler.add(runsLoopEnd);
flowScheduler.add(end_expRoutineBegin());
flowScheduler.add(end_expRoutineEachFrame());
flowScheduler.add(end_expRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'material/fixation.png', 'path': 'material/fixation.png'},
    {'name': 'material/top-xia.png', 'path': 'material/top-xia.png'},
    {'name': 'material/short_rest.png', 'path': 'material/short_rest.png'},
    {'name': 'material/end_rest.jpg', 'path': 'material/end_rest.jpg'},
    {'name': 'material/bottom-shang.png', 'path': 'material/bottom-shang.png'},
    {'name': 'material/long_rest.png', 'path': 'material/long_rest.png'},
    {'name': 'material/top-shang.png', 'path': 'material/top-shang.png'},
    {'name': 'material/end_exp.png', 'path': 'material/end_exp.png'},
    {'name': 'seq/trial/exercise.csv', 'path': 'seq/trial/exercise.csv'},
    {'name': 'material/bottom-xia.png', 'path': 'material/bottom-xia.png'},
    {'name': 'material/intro.png', 'path': 'material/intro.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.3';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/sub_${expInfo["sub_num"]}_${expInfo["name"]}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var introClock;
var intro_image;
var intro_key_resp;
var fixationClock;
var fixation_image;
var stimClock;
var stim_image;
var stim_resp;
var ITIClock;
var black_text;
var jitter_practiceClock;
var jitter_practice_text;
var judgeClock;
var judge_message;
var judge_resp;
var wait_fmriClock;
var wait_fmri_text;
var wait_fmri_key_resp;
var threeClock;
var three_text;
var three_key_resp;
var twoClock;
var two_text;
var two_key_resp;
var oneClock;
var one_text;
var one_key_resp;
var jitterClock;
var jitter_text;
var short_restClock;
var short_rest_image;
var rest_endClock;
var rest_end_image;
var rest_end_key_resp;
var long_restClock;
var long_rest_image;
var long_rest_endClock;
var long_rest_end_image;
var long_rest_end_resp;
var end_expClock;
var end_exp_image;
var end_resp;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  intro_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_image', units : undefined, 
    image : 'material/intro.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  intro_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fixation_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixation_image', units : undefined, 
    image : 'material/fixation.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "stim"
  stimClock = new util.Clock();
  stim_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  stim_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  black_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'black_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1,1,1]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "jitter_practice"
  jitter_practiceClock = new util.Clock();
  jitter_practice_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'jitter_practice_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "judge"
  judgeClock = new util.Clock();
  judge_message = new visual.TextStim({
    win: psychoJS.window,
    name: 'judge_message',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  judge_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wait_fmri"
  wait_fmriClock = new util.Clock();
  wait_fmri_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'wait_fmri_text',
    text: 'Wating for begin...',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  wait_fmri_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "three"
  threeClock = new util.Clock();
  three_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'three_text',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  three_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "two"
  twoClock = new util.Clock();
  two_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'two_text',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  two_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "one"
  oneClock = new util.Clock();
  one_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'one_text',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  one_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "jitter"
  jitterClock = new util.Clock();
  jitter_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'jitter_text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "short_rest"
  short_restClock = new util.Clock();
  short_rest_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'short_rest_image', units : undefined, 
    image : 'material/short_rest.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "rest_end"
  rest_endClock = new util.Clock();
  rest_end_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rest_end_image', units : undefined, 
    image : 'material/end_rest.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  rest_end_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "long_rest"
  long_restClock = new util.Clock();
  long_rest_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'long_rest_image', units : undefined, 
    image : 'material/long_rest.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "long_rest_end"
  long_rest_endClock = new util.Clock();
  long_rest_end_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'long_rest_end_image', units : undefined, 
    image : 'material/end_rest.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  long_rest_end_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end_exp"
  end_expClock = new util.Clock();
  end_exp_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'end_exp_image', units : undefined, 
    image : 'material/end_exp.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  end_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _intro_key_resp_allKeys;
var introComponents;
function introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro' ---
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    intro_key_resp.keys = undefined;
    intro_key_resp.rt = undefined;
    _intro_key_resp_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(intro_image);
    introComponents.push(intro_key_resp);
    
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro' ---
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro_image* updates
    if (t >= 0.0 && intro_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_image.tStart = t;  // (not accounting for frame time here)
      intro_image.frameNStart = frameN;  // exact frame index
      
      intro_image.setAutoDraw(true);
    }

    
    // *intro_key_resp* updates
    if (t >= 0.0 && intro_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_key_resp.tStart = t;  // (not accounting for frame time here)
      intro_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { intro_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { intro_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { intro_key_resp.clearEvents(); });
    }

    if (intro_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = intro_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _intro_key_resp_allKeys = _intro_key_resp_allKeys.concat(theseKeys);
      if (_intro_key_resp_allKeys.length > 0) {
        intro_key_resp.keys = _intro_key_resp_allKeys[_intro_key_resp_allKeys.length - 1].name;  // just the last key pressed
        intro_key_resp.rt = _intro_key_resp_allKeys[_intro_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro' ---
    introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(intro_key_resp.corr, level);
    }
    psychoJS.experiment.addData('intro_key_resp.keys', intro_key_resp.keys);
    if (typeof intro_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('intro_key_resp.rt', intro_key_resp.rt);
        routineTimer.reset();
        }
    
    intro_key_resp.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_trials;
function practice_trialsLoopBegin(practice_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'seq/trial/exercise.csv',
      seed: undefined, name: 'practice_trials'
    });
    psychoJS.experiment.addLoop(practice_trials); // add the loop to the experiment
    currentLoop = practice_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practice_trials.forEach(function() {
      snapshot = practice_trials.getSnapshot();
    
      practice_trialsLoopScheduler.add(importConditions(snapshot));
      practice_trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(fixationRoutineEachFrame());
      practice_trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(stimRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(stimRoutineEachFrame());
      practice_trialsLoopScheduler.add(stimRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(ITIRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(ITIRoutineEachFrame());
      practice_trialsLoopScheduler.add(ITIRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(jitter_practiceRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(jitter_practiceRoutineEachFrame());
      practice_trialsLoopScheduler.add(jitter_practiceRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(practice_trialsLoopEndIteration(practice_trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practice_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var runs;
function runsLoopBegin(runsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    runs = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("seq/run/run_" + expInfo["group"].toString()) + ".csv"),
      seed: undefined, name: 'runs'
    });
    psychoJS.experiment.addLoop(runs); // add the loop to the experiment
    currentLoop = runs;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    runs.forEach(function() {
      snapshot = runs.getSnapshot();
    
      runsLoopScheduler.add(importConditions(snapshot));
      runsLoopScheduler.add(wait_fmriRoutineBegin(snapshot));
      runsLoopScheduler.add(wait_fmriRoutineEachFrame());
      runsLoopScheduler.add(wait_fmriRoutineEnd(snapshot));
      runsLoopScheduler.add(threeRoutineBegin(snapshot));
      runsLoopScheduler.add(threeRoutineEachFrame());
      runsLoopScheduler.add(threeRoutineEnd(snapshot));
      runsLoopScheduler.add(twoRoutineBegin(snapshot));
      runsLoopScheduler.add(twoRoutineEachFrame());
      runsLoopScheduler.add(twoRoutineEnd(snapshot));
      runsLoopScheduler.add(oneRoutineBegin(snapshot));
      runsLoopScheduler.add(oneRoutineEachFrame());
      runsLoopScheduler.add(oneRoutineEnd(snapshot));
      const blocksLoopScheduler = new Scheduler(psychoJS);
      runsLoopScheduler.add(blocksLoopBegin(blocksLoopScheduler, snapshot));
      runsLoopScheduler.add(blocksLoopScheduler);
      runsLoopScheduler.add(blocksLoopEnd);
      runsLoopScheduler.add(long_restRoutineBegin(snapshot));
      runsLoopScheduler.add(long_restRoutineEachFrame());
      runsLoopScheduler.add(long_restRoutineEnd(snapshot));
      runsLoopScheduler.add(long_rest_endRoutineBegin(snapshot));
      runsLoopScheduler.add(long_rest_endRoutineEachFrame());
      runsLoopScheduler.add(long_rest_endRoutineEnd(snapshot));
      runsLoopScheduler.add(runsLoopEndIteration(runsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var blocks;
function blocksLoopBegin(blocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    blocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: block_seq,
      seed: undefined, name: 'blocks'
    });
    psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
    currentLoop = blocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    blocks.forEach(function() {
      snapshot = blocks.getSnapshot();
    
      blocksLoopScheduler.add(importConditions(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      blocksLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      blocksLoopScheduler.add(trialsLoopScheduler);
      blocksLoopScheduler.add(trialsLoopEnd);
      blocksLoopScheduler.add(short_restRoutineBegin(snapshot));
      blocksLoopScheduler.add(short_restRoutineEachFrame());
      blocksLoopScheduler.add(short_restRoutineEnd(snapshot));
      blocksLoopScheduler.add(rest_endRoutineBegin(snapshot));
      blocksLoopScheduler.add(rest_endRoutineEachFrame());
      blocksLoopScheduler.add(rest_endRoutineEnd(snapshot));
      blocksLoopScheduler.add(blocksLoopEndIteration(blocksLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: seqfile,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixationRoutineEachFrame());
      trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(stimRoutineBegin(snapshot));
      trialsLoopScheduler.add(stimRoutineEachFrame());
      trialsLoopScheduler.add(stimRoutineEnd(snapshot));
      trialsLoopScheduler.add(ITIRoutineBegin(snapshot));
      trialsLoopScheduler.add(ITIRoutineEachFrame());
      trialsLoopScheduler.add(ITIRoutineEnd(snapshot));
      trialsLoopScheduler.add(jitterRoutineBegin(snapshot));
      trialsLoopScheduler.add(jitterRoutineEachFrame());
      trialsLoopScheduler.add(jitterRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function blocksLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(blocks);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function blocksLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function runsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(runs);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function runsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.400000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(fixation_image);
    
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_image* updates
    if (t >= 0.0 && fixation_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_image.tStart = t;  // (not accounting for frame time here)
      fixation_image.frameNStart = frameN;  // exact frame index
      
      fixation_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var target_clock;
var target_begin;
var _stim_resp_allKeys;
var stimComponents;
function stimRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stim' ---
    t = 0;
    stimClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.200000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from response_code
    target_clock = new util.Clock();
    target_begin = target_clock.getTime();
    
    stim_image.setImage(stim_image_loc);
    stim_resp.keys = undefined;
    stim_resp.rt = undefined;
    _stim_resp_allKeys = [];
    // keep track of which components have finished
    stimComponents = [];
    stimComponents.push(stim_image);
    stimComponents.push(stim_resp);
    
    stimComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stimRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stim' ---
    // get current time
    t = stimClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stim_image* updates
    if (t >= 0.0 && stim_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim_image.tStart = t;  // (not accounting for frame time here)
      stim_image.frameNStart = frameN;  // exact frame index
      
      stim_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stim_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stim_image.setAutoDraw(false);
    }
    
    // *stim_resp* updates
    if (t >= 0.0 && stim_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim_resp.tStart = t;  // (not accounting for frame time here)
      stim_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { stim_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { stim_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { stim_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 1.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stim_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stim_resp.status = PsychoJS.Status.FINISHED;
  }

    if (stim_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = stim_resp.getKeys({keyList: ['q', 'p'], waitRelease: false});
      _stim_resp_allKeys = _stim_resp_allKeys.concat(theseKeys);
      if (_stim_resp_allKeys.length > 0) {
        stim_resp.keys = _stim_resp_allKeys[0].name;  // just the first key pressed
        stim_resp.rt = _stim_resp_allKeys[0].rt;
        // was this correct?
        if (stim_resp.keys == corr_resp) {
            stim_resp.corr = 1;
        } else {
            stim_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stimComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var totalaccuracy;
function stimRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stim' ---
    stimComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from response_code
    if (stim_resp.corr) {
        totalaccuracy = (totalaccuracy + 1);
    } else {
        errorsset = (errorsset + 1);
    }
    psychoJS.experiment.addData("errorsset", errorsset);
    psychoJS.experiment.addData("totalaccuracy", totalaccuracy);
    
    // was no response the correct answer?!
    if (stim_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp)) {
         stim_resp.corr = 1;  // correct non-response
      } else {
         stim_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(stim_resp.corr, level);
    }
    psychoJS.experiment.addData('stim_resp.keys', stim_resp.keys);
    psychoJS.experiment.addData('stim_resp.corr', stim_resp.corr);
    if (typeof stim_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('stim_resp.rt', stim_resp.rt);
        routineTimer.reset();
        }
    
    stim_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var iti_duration;
var ITIComponents;
function ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI' ---
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from iti_code
    iti_duration = (1.6 - (target_clock.getTime() - target_begin));
    
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(black_text);
    
    ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI' ---
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *black_text* updates
    if (t >= 0.0 && black_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      black_text.tStart = t;  // (not accounting for frame time here)
      black_text.frameNStart = frameN;  // exact frame index
      
      black_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + iti_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (black_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      black_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI' ---
    ITIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var jitter_practiceComponents;
function jitter_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'jitter_practice' ---
    t = 0;
    jitter_practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    jitter_practiceComponents = [];
    jitter_practiceComponents.push(jitter_practice_text);
    
    jitter_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function jitter_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'jitter_practice' ---
    // get current time
    t = jitter_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *jitter_practice_text* updates
    if (t >= 0.0 && jitter_practice_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jitter_practice_text.tStart = t;  // (not accounting for frame time here)
      jitter_practice_text.frameNStart = frameN;  // exact frame index
      
      jitter_practice_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jitter_practice_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jitter_practice_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    jitter_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function jitter_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'jitter_practice' ---
    jitter_practiceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var msg;
var _judge_resp_allKeys;
var judgeComponents;
function judgeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'judge' ---
    t = 0;
    judgeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from judege_code
    msg = ((("\u7ec3\u4e60\u7ed3\u675f, \n\u4f60\u7684\u6b63\u786e\u7387\u4e3a" + ((totalaccuracy / 16) * 100).toString()) + "%") + "\n\u8bf7\u6309\u7a7a\u683c\u952e\u5f00\u59cb\u5b9e\u9a8c!");
    
    judge_message.setText(msg);
    judge_resp.keys = undefined;
    judge_resp.rt = undefined;
    _judge_resp_allKeys = [];
    // keep track of which components have finished
    judgeComponents = [];
    judgeComponents.push(judge_message);
    judgeComponents.push(judge_resp);
    
    judgeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function judgeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'judge' ---
    // get current time
    t = judgeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *judge_message* updates
    if (t >= 0.0 && judge_message.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      judge_message.tStart = t;  // (not accounting for frame time here)
      judge_message.frameNStart = frameN;  // exact frame index
      
      judge_message.setAutoDraw(true);
    }

    
    // *judge_resp* updates
    if (t >= 0.0 && judge_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      judge_resp.tStart = t;  // (not accounting for frame time here)
      judge_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { judge_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { judge_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { judge_resp.clearEvents(); });
    }

    if (judge_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = judge_resp.getKeys({keyList: ['space'], waitRelease: false});
      _judge_resp_allKeys = _judge_resp_allKeys.concat(theseKeys);
      if (_judge_resp_allKeys.length > 0) {
        judge_resp.keys = _judge_resp_allKeys[_judge_resp_allKeys.length - 1].name;  // just the last key pressed
        judge_resp.rt = _judge_resp_allKeys[_judge_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    judgeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var errorsset;
function judgeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'judge' ---
    judgeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from judege_code
    totalaccuracy = 0;
    errorsset = 0;
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(judge_resp.corr, level);
    }
    psychoJS.experiment.addData('judge_resp.keys', judge_resp.keys);
    if (typeof judge_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('judge_resp.rt', judge_resp.rt);
        routineTimer.reset();
        }
    
    judge_resp.stop();
    // the Routine "judge" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _wait_fmri_key_resp_allKeys;
var wait_fmriComponents;
function wait_fmriRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'wait_fmri' ---
    t = 0;
    wait_fmriClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    wait_fmri_key_resp.keys = undefined;
    wait_fmri_key_resp.rt = undefined;
    _wait_fmri_key_resp_allKeys = [];
    // keep track of which components have finished
    wait_fmriComponents = [];
    wait_fmriComponents.push(wait_fmri_text);
    wait_fmriComponents.push(wait_fmri_key_resp);
    
    wait_fmriComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function wait_fmriRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'wait_fmri' ---
    // get current time
    t = wait_fmriClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *wait_fmri_text* updates
    if (t >= 0.0 && wait_fmri_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wait_fmri_text.tStart = t;  // (not accounting for frame time here)
      wait_fmri_text.frameNStart = frameN;  // exact frame index
      
      wait_fmri_text.setAutoDraw(true);
    }

    
    // *wait_fmri_key_resp* updates
    if (t >= 0.0 && wait_fmri_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wait_fmri_key_resp.tStart = t;  // (not accounting for frame time here)
      wait_fmri_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { wait_fmri_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { wait_fmri_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { wait_fmri_key_resp.clearEvents(); });
    }

    if (wait_fmri_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = wait_fmri_key_resp.getKeys({keyList: ['s'], waitRelease: false});
      _wait_fmri_key_resp_allKeys = _wait_fmri_key_resp_allKeys.concat(theseKeys);
      if (_wait_fmri_key_resp_allKeys.length > 0) {
        wait_fmri_key_resp.keys = _wait_fmri_key_resp_allKeys[_wait_fmri_key_resp_allKeys.length - 1].name;  // just the last key pressed
        wait_fmri_key_resp.rt = _wait_fmri_key_resp_allKeys[_wait_fmri_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    wait_fmriComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wait_fmriRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'wait_fmri' ---
    wait_fmriComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(wait_fmri_key_resp.corr, level);
    }
    psychoJS.experiment.addData('wait_fmri_key_resp.keys', wait_fmri_key_resp.keys);
    if (typeof wait_fmri_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('wait_fmri_key_resp.rt', wait_fmri_key_resp.rt);
        routineTimer.reset();
        }
    
    wait_fmri_key_resp.stop();
    // the Routine "wait_fmri" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _three_key_resp_allKeys;
var threeComponents;
function threeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'three' ---
    t = 0;
    threeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    three_key_resp.keys = undefined;
    three_key_resp.rt = undefined;
    _three_key_resp_allKeys = [];
    // keep track of which components have finished
    threeComponents = [];
    threeComponents.push(three_text);
    threeComponents.push(three_key_resp);
    
    threeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function threeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'three' ---
    // get current time
    t = threeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *three_text* updates
    if (t >= 0.0 && three_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      three_text.tStart = t;  // (not accounting for frame time here)
      three_text.frameNStart = frameN;  // exact frame index
      
      three_text.setAutoDraw(true);
    }

    
    // *three_key_resp* updates
    if (t >= 0.0 && three_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      three_key_resp.tStart = t;  // (not accounting for frame time here)
      three_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { three_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { three_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { three_key_resp.clearEvents(); });
    }

    if (three_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = three_key_resp.getKeys({keyList: ['s'], waitRelease: false});
      _three_key_resp_allKeys = _three_key_resp_allKeys.concat(theseKeys);
      if (_three_key_resp_allKeys.length > 0) {
        three_key_resp.keys = _three_key_resp_allKeys[_three_key_resp_allKeys.length - 1].name;  // just the last key pressed
        three_key_resp.rt = _three_key_resp_allKeys[_three_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    threeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function threeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'three' ---
    threeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(three_key_resp.corr, level);
    }
    psychoJS.experiment.addData('three_key_resp.keys', three_key_resp.keys);
    if (typeof three_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('three_key_resp.rt', three_key_resp.rt);
        routineTimer.reset();
        }
    
    three_key_resp.stop();
    // the Routine "three" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _two_key_resp_allKeys;
var twoComponents;
function twoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'two' ---
    t = 0;
    twoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    two_key_resp.keys = undefined;
    two_key_resp.rt = undefined;
    _two_key_resp_allKeys = [];
    // keep track of which components have finished
    twoComponents = [];
    twoComponents.push(two_text);
    twoComponents.push(two_key_resp);
    
    twoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function twoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'two' ---
    // get current time
    t = twoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *two_text* updates
    if (t >= 0.0 && two_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_text.tStart = t;  // (not accounting for frame time here)
      two_text.frameNStart = frameN;  // exact frame index
      
      two_text.setAutoDraw(true);
    }

    
    // *two_key_resp* updates
    if (t >= 0.0 && two_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      two_key_resp.tStart = t;  // (not accounting for frame time here)
      two_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { two_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { two_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { two_key_resp.clearEvents(); });
    }

    if (two_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = two_key_resp.getKeys({keyList: ['s'], waitRelease: false});
      _two_key_resp_allKeys = _two_key_resp_allKeys.concat(theseKeys);
      if (_two_key_resp_allKeys.length > 0) {
        two_key_resp.keys = _two_key_resp_allKeys[_two_key_resp_allKeys.length - 1].name;  // just the last key pressed
        two_key_resp.rt = _two_key_resp_allKeys[_two_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    twoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function twoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'two' ---
    twoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(two_key_resp.corr, level);
    }
    psychoJS.experiment.addData('two_key_resp.keys', two_key_resp.keys);
    if (typeof two_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('two_key_resp.rt', two_key_resp.rt);
        routineTimer.reset();
        }
    
    two_key_resp.stop();
    // the Routine "two" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _one_key_resp_allKeys;
var jitter_list;
var count_num;
var oneComponents;
function oneRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'one' ---
    t = 0;
    oneClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    one_key_resp.keys = undefined;
    one_key_resp.rt = undefined;
    _one_key_resp_allKeys = [];
    // Run 'Begin Routine' code from before_roution_code
    jitter_list = [1.8, 1.8, 2.05, 2.05, 2.3, 2.3, 2.3, 2.3, 2.3, 2.55, 2.55, 2.55, 2.55, 2.55, 2.55, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05];
    util.shuffle(jitter_list);
    count_num = 0;
    
    // keep track of which components have finished
    oneComponents = [];
    oneComponents.push(one_text);
    oneComponents.push(one_key_resp);
    
    oneComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function oneRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'one' ---
    // get current time
    t = oneClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *one_text* updates
    if (t >= 0.0 && one_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      one_text.tStart = t;  // (not accounting for frame time here)
      one_text.frameNStart = frameN;  // exact frame index
      
      one_text.setAutoDraw(true);
    }

    
    // *one_key_resp* updates
    if (t >= 0.0 && one_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      one_key_resp.tStart = t;  // (not accounting for frame time here)
      one_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { one_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { one_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { one_key_resp.clearEvents(); });
    }

    if (one_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = one_key_resp.getKeys({keyList: ['s'], waitRelease: false});
      _one_key_resp_allKeys = _one_key_resp_allKeys.concat(theseKeys);
      if (_one_key_resp_allKeys.length > 0) {
        one_key_resp.keys = _one_key_resp_allKeys[_one_key_resp_allKeys.length - 1].name;  // just the last key pressed
        one_key_resp.rt = _one_key_resp_allKeys[_one_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    oneComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function oneRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'one' ---
    oneComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(one_key_resp.corr, level);
    }
    psychoJS.experiment.addData('one_key_resp.keys', one_key_resp.keys);
    if (typeof one_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('one_key_resp.rt', one_key_resp.rt);
        routineTimer.reset();
        }
    
    one_key_resp.stop();
    // the Routine "one" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var jitter_duration;
var jitterComponents;
function jitterRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'jitter' ---
    t = 0;
    jitterClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from jitter_code
    jitter_duration = jitter_list[count_num];
    count_num = (count_num + 1);
    psychoJS.experiment.addData("jitter", jitter_duration);
    
    // keep track of which components have finished
    jitterComponents = [];
    jitterComponents.push(jitter_text);
    
    jitterComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function jitterRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'jitter' ---
    // get current time
    t = jitterClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *jitter_text* updates
    if (t >= 0.0 && jitter_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jitter_text.tStart = t;  // (not accounting for frame time here)
      jitter_text.frameNStart = frameN;  // exact frame index
      
      jitter_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + jitter_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jitter_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jitter_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    jitterComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function jitterRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'jitter' ---
    jitterComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "jitter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var short_restComponents;
function short_restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'short_rest' ---
    t = 0;
    short_restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    short_restComponents = [];
    short_restComponents.push(short_rest_image);
    
    short_restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function short_restRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'short_rest' ---
    // get current time
    t = short_restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *short_rest_image* updates
    if (t >= 0.0 && short_rest_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      short_rest_image.tStart = t;  // (not accounting for frame time here)
      short_rest_image.frameNStart = frameN;  // exact frame index
      
      short_rest_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + short_rest_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (short_rest_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      short_rest_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    short_restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function short_restRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'short_rest' ---
    short_restComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "short_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _rest_end_key_resp_allKeys;
var rest_endComponents;
function rest_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rest_end' ---
    t = 0;
    rest_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    rest_end_key_resp.keys = undefined;
    rest_end_key_resp.rt = undefined;
    _rest_end_key_resp_allKeys = [];
    // Run 'Begin Routine' code from reset_jitter_code
    util.shuffle(jitter_list);
    count_num = 0;
    
    // keep track of which components have finished
    rest_endComponents = [];
    rest_endComponents.push(rest_end_image);
    rest_endComponents.push(rest_end_key_resp);
    
    rest_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function rest_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rest_end' ---
    // get current time
    t = rest_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rest_end_image* updates
    if (t >= 0.0 && rest_end_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_end_image.tStart = t;  // (not accounting for frame time here)
      rest_end_image.frameNStart = frameN;  // exact frame index
      
      rest_end_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + stop_rest_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rest_end_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rest_end_image.setAutoDraw(false);
    }
    
    // *rest_end_key_resp* updates
    if (t >= 0.0 && rest_end_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_end_key_resp.tStart = t;  // (not accounting for frame time here)
      rest_end_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rest_end_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rest_end_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rest_end_key_resp.clearEvents(); });
    }

    frameRemains = 0.0 + stop_rest_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rest_end_key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rest_end_key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (rest_end_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rest_end_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rest_end_key_resp_allKeys = _rest_end_key_resp_allKeys.concat(theseKeys);
      if (_rest_end_key_resp_allKeys.length > 0) {
        rest_end_key_resp.keys = _rest_end_key_resp_allKeys[_rest_end_key_resp_allKeys.length - 1].name;  // just the last key pressed
        rest_end_key_resp.rt = _rest_end_key_resp_allKeys[_rest_end_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    rest_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rest_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rest_end' ---
    rest_endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rest_end_key_resp.corr, level);
    }
    psychoJS.experiment.addData('rest_end_key_resp.keys', rest_end_key_resp.keys);
    if (typeof rest_end_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rest_end_key_resp.rt', rest_end_key_resp.rt);
        routineTimer.reset();
        }
    
    rest_end_key_resp.stop();
    // the Routine "rest_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var long_restComponents;
function long_restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'long_rest' ---
    t = 0;
    long_restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    long_restComponents = [];
    long_restComponents.push(long_rest_image);
    
    long_restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function long_restRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'long_rest' ---
    // get current time
    t = long_restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *long_rest_image* updates
    if (t >= 0.0 && long_rest_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      long_rest_image.tStart = t;  // (not accounting for frame time here)
      long_rest_image.frameNStart = frameN;  // exact frame index
      
      long_rest_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + long_rest_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (long_rest_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      long_rest_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    long_restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function long_restRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'long_rest' ---
    long_restComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "long_rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _long_rest_end_resp_allKeys;
var long_rest_endComponents;
function long_rest_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'long_rest_end' ---
    t = 0;
    long_rest_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    long_rest_end_resp.keys = undefined;
    long_rest_end_resp.rt = undefined;
    _long_rest_end_resp_allKeys = [];
    // keep track of which components have finished
    long_rest_endComponents = [];
    long_rest_endComponents.push(long_rest_end_image);
    long_rest_endComponents.push(long_rest_end_resp);
    
    long_rest_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function long_rest_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'long_rest_end' ---
    // get current time
    t = long_rest_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *long_rest_end_image* updates
    if (t >= 0.0 && long_rest_end_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      long_rest_end_image.tStart = t;  // (not accounting for frame time here)
      long_rest_end_image.frameNStart = frameN;  // exact frame index
      
      long_rest_end_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + stop_long_rest_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (long_rest_end_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      long_rest_end_image.setAutoDraw(false);
    }
    
    // *long_rest_end_resp* updates
    if (t >= 0.0 && long_rest_end_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      long_rest_end_resp.tStart = t;  // (not accounting for frame time here)
      long_rest_end_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { long_rest_end_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { long_rest_end_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { long_rest_end_resp.clearEvents(); });
    }

    frameRemains = 0.0 + stop_long_rest_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (long_rest_end_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      long_rest_end_resp.status = PsychoJS.Status.FINISHED;
  }

    if (long_rest_end_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = long_rest_end_resp.getKeys({keyList: ['space'], waitRelease: false});
      _long_rest_end_resp_allKeys = _long_rest_end_resp_allKeys.concat(theseKeys);
      if (_long_rest_end_resp_allKeys.length > 0) {
        long_rest_end_resp.keys = _long_rest_end_resp_allKeys[_long_rest_end_resp_allKeys.length - 1].name;  // just the last key pressed
        long_rest_end_resp.rt = _long_rest_end_resp_allKeys[_long_rest_end_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    long_rest_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function long_rest_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'long_rest_end' ---
    long_rest_endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(long_rest_end_resp.corr, level);
    }
    psychoJS.experiment.addData('long_rest_end_resp.keys', long_rest_end_resp.keys);
    if (typeof long_rest_end_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('long_rest_end_resp.rt', long_rest_end_resp.rt);
        routineTimer.reset();
        }
    
    long_rest_end_resp.stop();
    // the Routine "long_rest_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _end_resp_allKeys;
var end_expComponents;
function end_expRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_exp' ---
    t = 0;
    end_expClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    end_resp.keys = undefined;
    end_resp.rt = undefined;
    _end_resp_allKeys = [];
    // keep track of which components have finished
    end_expComponents = [];
    end_expComponents.push(end_exp_image);
    end_expComponents.push(end_resp);
    
    end_expComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function end_expRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_exp' ---
    // get current time
    t = end_expClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_exp_image* updates
    if (t >= 0.0 && end_exp_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_exp_image.tStart = t;  // (not accounting for frame time here)
      end_exp_image.frameNStart = frameN;  // exact frame index
      
      end_exp_image.setAutoDraw(true);
    }

    
    // *end_resp* updates
    if (t >= 0.0 && end_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_resp.tStart = t;  // (not accounting for frame time here)
      end_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_resp.clearEvents(); });
    }

    if (end_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_resp.getKeys({keyList: ['space'], waitRelease: false});
      _end_resp_allKeys = _end_resp_allKeys.concat(theseKeys);
      if (_end_resp_allKeys.length > 0) {
        end_resp.keys = _end_resp_allKeys[_end_resp_allKeys.length - 1].name;  // just the last key pressed
        end_resp.rt = _end_resp_allKeys[_end_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    end_expComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_expRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_exp' ---
    end_expComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(end_resp.corr, level);
    }
    psychoJS.experiment.addData('end_resp.keys', end_resp.keys);
    if (typeof end_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_resp.rt', end_resp.rt);
        routineTimer.reset();
        }
    
    end_resp.stop();
    // the Routine "end_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
