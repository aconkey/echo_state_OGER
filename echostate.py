import sys
import Oger
import vectorize
import random
import numpy as np

#filename = sys.argv[1]
filename = "data/semeval_combined.txt"
x,y = vectorize.get_vectorized_data(filename) # x = sentence, y = classification

# for now just do simple hack splitting of train/test sets
# TODO more advanced cross validation
ziplist = zip(x,y)
#random.shuffle(ziplist)
data = [x, ziplist]
#train_data = [None, ziplist[:1800]]
#test_data = ziplist[1800:]
#test_inputs, test_targets = zip(*test_data) # get the input/output separation back
#test_inputs = np.asarray(test_inputs)
#test_targets = np.asarray(test_targets)

reservoir = Oger.nodes.ReservoirNode(output_dim = 100)
readout = Oger.nodes.RidgeRegressionNode()
    
flow = reservoir + readout

test_errors = Oger.evaluation.validate(
    data, flow, Oger.utils.nmse, cross_validate_function=Oger.evaluation.train_test_only, training_fraction=0.5)
        
#flow.train(train_data)

#test_outputs = flow.execute([None, test_inputs])
#confmat = Oger.utils.ConfusionMatrix.from_data(2, test_outputs, test_targets)


# TODO getting divide by zero error, try comparing with privided datasets to 
# see why it is not behaving like theirs