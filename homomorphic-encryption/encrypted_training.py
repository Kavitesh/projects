import random
import torch
import tenseal as ts
from encrypted_logistic_regression import EncryptedLogisticRegression 
import logging

poly_mod_degree = 8192
coeff_mod_bit_sizes = [40, 21, 21, 21, 21, 21, 21, 40]
ctx = ts.context(ts.SCHEME_TYPE.CKKS, poly_mod_degree, -1, coeff_mod_bit_sizes)
ctx.global_scale = 2 ** 21
ctx.generate_galois_keys()
torch.random.manual_seed(45)
random.seed(45)
x_test = torch.randn(100, 6)
y_test = (x_test[:, 3] >= x_test[:, 4]).float().unsqueeze(0).t()
enc_x_train = [ts.ckks_vector(ctx, x.tolist()) for x in x_test]
enc_y_train = [ts.ckks_vector(ctx, y.tolist()) for y in y_test]

model = EncryptedLogisticRegression(x_test.shape[1], ctx, 1)

def get_logger(model, x_test, y_test):
    def accuracy(epoch):     
        model.weight = model.weight.decrypt(ctx.secret_key())
        model.bias = model.bias.decrypt(ctx.secret_key())  
        # evaluate accuracy of the model on
        # the plain (x_test, y_test) dataset
        w = torch.tensor(model.weight)
        b = torch.tensor(model.bias)
        out = torch.sigmoid(x_test.matmul(w) + b).reshape(-1, 1)
        correct = torch.abs(y_test - out) < 0.5
        mean = correct.float().mean()            
        logging.info(f"Accuracy at epoch #{epoch+1} is {mean}")
        model.weight = ts.ckks_vector(ctx, model.weight)
        model.bias = ts.ckks_vector(ctx, model.bias) 
    return accuracy

model.train(get_logger(model,x_test, y_test), enc_x_train, enc_y_train)

