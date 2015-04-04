import sys
import Oger
import vectorize

filename = sys.argv[1]
x,y = vectorize.get_vectorized_data(filename)
train_data = [None, zip(x,y)]

reservoir = Oger.nodes.ReservoirNode(output_dim = 100)
readout = Oger.nodes.RidgeRegressionNode()

flow = reservoir + readout
flow.train(train_data)