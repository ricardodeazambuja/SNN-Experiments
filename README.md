<img src="DSC_0040-ANIMATION.gif" alt="Random experiment using BAXTER" width="800"/>  

# SNN-Experiments
Here I'm sharing some of the **initial and/or unpublished** experiments I did with spiking neural networks (SNN). As I don't have time to expand them, I hope they are going to be useful to someone else. Probably there are some (or lots of?) bugs, so feel free to correct them :)   
## Everything I'm sharing here is TOTALLY FREE to be (re)used, but be a nice person and: 1)share any work derived from here; 2)cite my papers :D

Biased Unsupervised Learning Method: a novel(???) way to use STDP  
https://github.com/ricardodeazambuja/SNN-Experiments/blob/master/Biased%20Unsupervised%20Learning%20Method/Biased%20Unsupervised%20Learning%20Method.ipynb  

Feedback in complex spiking neural networks   
https://github.com/ricardodeazambuja/SNN-Experiments/blob/master/Feedback%20in%20complex%20neural%20system/Feedback_Experiment_1.2_V_and_I_WITHOUT_saturation.ipynb   

Implementing a Liquid State Machine using Brian Simulator   
https://github.com/ricardodeazambuja/SNN-Experiments/blob/master/Implementing%20a%20Liquid%20State%20Machine%20using%20Brian%20Simulator/Implementing%20a%20Liquid%20State%20Machine%20using%20Brian%20Simulator.ipynb  

Improving the resolution of population coding by the use of multiple layers  
https://github.com/ricardodeazambuja/SNN-Experiments/blob/master/Multilayer%20population%20code/Improving%20the%20resolution%20of%20population%20coding%20by%20the%20use%20of%20multiple%20layers.ipynb

In case you are working with neuromorphic computers, I've developed some code that translates LSM models from [Bee](https://github.com/ricardodeazambuja/Bee) to [SpiNNaker](http://spinnakermanchester.github.io/) and, as the other stuff available here, I never had the time to publish about it:  
https://github.com/ricardodeazambuja/sPLYnnaker  
https://github.com/ricardodeazambuja/SpiNNakerWorkshop2016  


## Crazy ideas
### 1. Stochastic Resonance
The idea is to study better the effects of noise.

"In order to exhibit stochastic resonance (SR), a system should possess three basic properties: a non-linearity in terms of threshold, sub-threshold signals like signals with small amplitude and a source of additive noise. This phenomenon occurs frequently in bistable systems or in systems with threshold-like behavior [18]. The general behavior of SR mechanism shows that at lower noise intensities the weak signal is unable to cross the threshold, thus giving a very low SNR. For large noise intensities the output is dominated by the noise, also leading to a low SNR. But, for moderate noise intensities, the noise allows the signal to cross the threshold giving maximum SNR at some optimum additive noise level"

From:
Chouhan, Rajlaxmi, C. Pradeep Kumar, Rawnak Kumar, and Rajib Kumar Jha. “Contrast Enhancement of Dark Images Using Stochastic Resonance in Wavelet Domain.” International Journal of Machine Learning and Computing, 2012, 711–15. doi:10.7763/IJMLC.2012.V2.220.

### 2. Importance of input code
The idea here is to do the same experiments testing how good random liquids are when doing the drawing task, but in this case I would like to test what happens when the input code changes.

Here they say a body needs to change in order to do a different morphological computation:
https://www.researchgate.net/publication/308500845_Morphosis_Taking_Morphological_Computation_to_the_Next_Level

But my guess is that changing only the input code is going to make a huge difference already because I had problems with my old input codes.

### 3. Ensembles and Evolutionary Algorithms
For [my IJCNN2016 paper](https://github.com/ricardodeazambuja/IJCNN2016), I had multiple 'liquids' working in parallel generating better results than individuals ones. Below it's a figure (unpublished results) that shows random generated liquids are hardly good (or bad!) in all tasks:  
<img src="DTW_100_individual_liquids_square_triangle_circle.png" alt="Scores for individual liquids" width="800"/>  
However, when you test them for only one task, even randomly mixing them generates a better result:  
<img src="DTW_100_different_liquids_parallel_avr.png" alt="Scores for parallel liquids  - drawing a circle task" width="800"/>  
<img src="DTW_100_different_liquids_parallel.png" alt="Scores for parallel liquids  - drawing a circle task" width="800"/>  
Another interesting (quite obvious) fact is that random generated liquids are... not great in general, but some generate much better results than others:
<img src="DTW_100_individual_liquids_circle.png" alt="Scores for individual liquids - drawing a circle task" width="800"/>  
Maybe, it's not possible to have 'one neural circuit to rule them all'. Also, evolutionary algorithms could be useful to iterate based on the best random generated ones creating better invidual liquids. That's it, food for thought!

### 4. Different shapes
I finally found in an old email some plots from my experiments teaching an LSM to control BAXTER to draw:
#### Multiple Squares:
I'm not sure, but I think it would manipulate the bias variables (check my [IJCNN2016 paper](https://github.com/ricardodeazambuja/IJCNN2016) if you don't know what I'm talking about).

<img src="multiple_squares_experiment_1.png" alt="Drawing the system was taught to reproduce" width="400"/>  
<img src="multiple_squares_experiment_2.png" alt="Results teaching all four squares" width="400"/>  
<img src="multiple_squares_experiment_3.png" alt="Results teaching only one square" width="400"/>  

#### Trefoil:
The trefoil is a very interesting shape because the system passes more than once over the same place. I think it's a very nice example of the power of LSMs when you need to take into account events that happened in the past.
<img src="Trefoil.png" alt="Random experiment using BAXTER" width="400"/>
## If you liked the stuff above, you may want to check [BEE - The Spiking Reservoir (LSM) Simulator](https://github.com/ricardodeazambuja/Bee) and/or [my papers](https://ricardodeazambuja.com/publications/).


## Other projects you may like to check:
* [colab_utils](https://github.com/ricardodeazambuja/colab_utils/): Some useful (or not so much) Python stuff for Google Colab notebooks
* [ExecThatCell](https://github.com/ricardodeazambuja/ExecThatCell): (Re)Execute a Jupyter (colab) notebook cell programmatically by searching for its label.
* [Maple-Syrup-Pi-Camera](https://github.com/ricardodeazambuja/Maple-Syrup-Pi-Camera): Low power('ish) AIoT smart camera (3D printed) based on the Raspberry Pi Zero W and Google Coral EdgeTPU
* [The CogniFly Project](https://github.com/thecognifly): Open-source autonomous flying robots robust to collisions and smart enough to do something interesting!
* [Bee](https://github.com/ricardodeazambuja/Bee): The Bee simulator is an open source Spiking Neural Network (SNN) simulator, freely available, specialised in Liquid State Machine (LSM) systems with its core functions fully implemented in C.

https://ricardodeazambuja.com/
