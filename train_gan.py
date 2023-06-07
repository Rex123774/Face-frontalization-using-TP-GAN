from tpgan import TPGAN, multipie_gen,CloudableModel
from keras.optimizers import SGD 
from keras.optimizers import Adam
import time
import multiprocessing  
from numba import prange
import tensorflow as tf



time_total =[]
time1=time.time()


if __name__ == '__main__':
         
    op = 'Adam'
    
    gan = TPGAN(base_filters=64, gpus=1,
                
                lcnn_extractor_weights='C:/Users/RONIX/latest_tpgan_19April23/lcnn_weights/extract29v2_lr0.00010_loss0.997_valacc1.000_epoch1110.hdf5',
                generator_weights='E:/BE_PROJECTNO_9/latest_tpgan/out_data/weights/generator/epoch1880_loss0.269.hdf5',
                classifier_weights='E:/BE_PROJECTNO_9/latest_tpgan/out_data/weights/classifier/epoch1880_loss0.269.hdf5',
                discriminator_weights='E:/BE_PROJECTNO_9/latest_tpgan/out_data/weights/discriminator/epoch1880_loss0.797.hdf5')
                # generator_weights='E:/BE_PROJECTNO_9/latest_tpgan/out_data/weights/generator/epoch1786_loss0.261.hdf5',
                # classifier_weights='E:/BE_PROJECTNO_9/latest_tpgan/out_data/weights/classifier/epoch1786_loss0.261.hdf5',   
                # discriminator_weights='E:/BE_PROJECTNO_9/latest_tpgan/out_data/weights/discriminator/epoch1785_loss0.797.hdf5')
                
    
    datagen = multipie_gen.Datagen(dataset_dir='C:/Users/RONIX/latest_tpgan_19April23/dataset/', landmarks_dict_file='E:/BE_PROJECTNO_9/latest_tpgan/landmark/landmarks_file.pkl', 
                                   datalist_dir='E:/BE_PROJECTNO_9/latest_tpgan/datalist_side_face.pkl', min_angle=-90, max_angle=90, valid_count=120)
   
    if op == 'Adam':
        optimizer = Adam(lr=0.0001, beta_1=0.9)
    elif op == 'SGD':
        optimizer = SGD(lr=0.001, momentum=0.9, nesterov=True)
                  
    gan.train_gan(gen_datagen_creator=datagen.get_generator, 
                  gen_train_batch_size=2,#4
                  gen_valid_batch_size=2,#4
                  disc_datagen_creator=datagen.get_discriminator_generator, 
                  disc_batch_size=5,#10
                  disc_gt_shape=gan.discriminator().output_shape[1:3],
                  #disc_gt_shape=gan.discriminator(),
                  optimizer=optimizer,
                  gen_steps_per_epoch=200, disc_steps_per_epoch=200,  #100 #100
                  epochs=3200, out_dir='E:/BE_PROJECTNO_9/latest_tpgan/out_data/', out_period=1, is_output_img=True,
                  lr=0.0001, decay=0, lambda_128=1, lambda_64=1, lambda_32=1,
                  lambda_sym=1e-1, lambda_ip=1e-3, lambda_adv=5e-3, lambda_tv=1e-5,
                  lambda_class=0, lambda_parts=0)

    print ('Time')
    time111 = time.time()-time1
    print (('Time', time111))
    time_total.append (time111)

#    if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(1, range(0,10000))
    pool.close()
