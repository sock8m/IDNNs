"""
Train % plot networks in the information plane
"""

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


from idnns.networks import information_network as inet
def main():
    #Build the network
    print ('Building the network')
    net = inet.informationNetwork()
    net.print_information()
    print ('Start running the network')
    net.run_network()
    print ('Saving data')
    net.save_data()
    print ('Ploting figures')
    #Plot the newtork
    net.plot_network()
if __name__ == '__main__':
    main()

