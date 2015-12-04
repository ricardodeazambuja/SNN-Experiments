# Generate the points to the 3D Scatter plot

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def show_3d_connections(output, show_index=False, show_coord=False, show_blocked=True, return_figure=False, plot_title=''):
		'''
		Prints the neurons and the connections between them using the output from lsm_connections_probability module.
		output->is the output from the generate_liquid_connections function (from lsm_connections_probability.py)
		show_number=True->shows the index number of each neuron according to the Neurongroup
		show_blocked=True->makes the show() command block the execution of the rest of the code
		'''

		if output['3Dplot_a']==output['3Dplot_b']: # It means population 'a' and 'b' are the same!
			Neuron3DMatrix=output['3Dplot_a']
		else:
			Neuron3DMatrix=output['3Dplot_a']+output['3Dplot_b'] # This works here because they are two LISTS and "NOT" NUMPY ARRAYS.

		# Position of the neurons in the 3D space
		x=[i[0] for i in Neuron3DMatrix] 
		y=[i[1] for i in Neuron3DMatrix]
		z=[i[2] for i in Neuron3DMatrix]


		# List of tuples with (pre synaptic, post synaptic) EXCITATORY->ANYTHING neurons connections indexes
		exc_connect_positions=[output['exc'][i][0] for i in range(len(output['exc']))]

		exc_connect_positions_pre=[output['3Dplot_a'][i[0]] for i in exc_connect_positions]
		exc_connect_positions_post=[output['3Dplot_b'][i[1]] for i in exc_connect_positions]

		# List of tuples with (pre synaptic, post synaptic) INHIBITORY->ANYTHING neurons connections indexes
		inh_connect_positions=[output['inh'][i][0] for i in range(len(output['inh']))]
		inh_connect_positions_pre=[output['3Dplot_a'][i[0]] for i in inh_connect_positions]
		inh_connect_positions_post=[output['3Dplot_b'][i[1]] for i in inh_connect_positions]


		fig = plt.figure() # creates the figure for the following plots
		ax = fig.add_subplot(111, projection='3d') # setup to only one

		ax.scatter(x, y, z) # plots the points correnponding to the neurons

		# Insert a label with the position of each neuron according to the positions_list (NeuronGroup)
		if show_index:
			n=0
			for t in Neuron3DMatrix:
				ax.text(t[0], t[1], t[2], "["+str(n)+"]")
				n+=1	

		# Insert a label with the 3D coordinate used to calculate the connection probabilities
		if show_coord:
			n=0
			for t in Neuron3DMatrix:
				ax.text(t[0], t[1], t[2], str(t)+"="+str(n)) # to insert also the coordinates of the point
				n+=1

		#
		# Draw a 3D vector (arrow)
		# from matplotlib.patches import FancyArrowPatch
		# from mpl_toolkits.mplot3d import proj3d

		# class Arrow3D(FancyArrowPatch):
		#     def __init__(self, xs, ys, zs, *args, **kwargs):
		#         FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
		#         self._verts3d = xs, ys, zs

		#     def draw(self, renderer):
		#         xs3d, ys3d, zs3d = self._verts3d
		#         xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
		#         self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
		#         FancyArrowPatch.draw(self, renderer)


		# # Plot the EXCITATORY connections
		# for i in range(len(exc_connect_positions)):
		# 	a = Arrow3D(
		# 		[ exc_connect_positions_pre[i][0], exc_connect_positions_post[i][0] ], 
		# 		[ exc_connect_positions_pre[i][1], exc_connect_positions_post[i][1] ], 
		# 		[ exc_connect_positions_pre[i][2], exc_connect_positions_post[i][2] ], 
		# 		label='excitatory connections', mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
		# 	ax.add_artist(a)

		# Plot the EXCITATORY connections - FAST VERSION WITHOUT ARROWS
		for i in range(len(exc_connect_positions)):
			ax.plot(
				[ exc_connect_positions_pre[i][0], exc_connect_positions_post[i][0] ], 
				[ exc_connect_positions_pre[i][1], exc_connect_positions_post[i][1] ], 
				[ exc_connect_positions_pre[i][2], exc_connect_positions_post[i][2] ], 
				label='excitatory connections', color='#FF0000')

		# # Plot the INHIBITORY connections
		# for i in range(len(inh_connect_positions)):
		# 	a = Arrow3D(
		# 		[ inh_connect_positions_pre[i][0], inh_connect_positions_post[i][0] ], 
		# 		[ inh_connect_positions_pre[i][1], inh_connect_positions_post[i][1] ], 
		# 		[ inh_connect_positions_pre[i][2], inh_connect_positions_post[i][2] ], 
		# 		label='inhibitory connections', mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
		# 	ax.add_artist(a)

		# Plot the INHIBITORY connections - FAST VERSION WITHOUT ARROWS
		for i in range(len(inh_connect_positions)):
			ax.plot(
				[ inh_connect_positions_pre[i][0], inh_connect_positions_post[i][0] ], 
				[ inh_connect_positions_pre[i][1], inh_connect_positions_post[i][1] ], 
				[ inh_connect_positions_pre[i][2], inh_connect_positions_post[i][2] ], 
				label='inhibitory connections', color='#0000FF')



		ax.set_xlabel('X Axis')
		ax.set_ylabel('Y Axis')
		ax.set_zlabel('Z Axis')

		plt.title(plot_title)
        
		if return_figure:
			print "Sending back the figure object..."
			return plt,fig,ax
		else:
			print "Showing the figure!"
			if show_blocked:
				plt.show(block=show_blocked)
			else:
				plt.show()
