import torch
import tenseal as ts

class EncryptedLogisticRegression():
    
    def __init__(self, n_features, ctx, epoch=5):        
        self.epoch = epoch
        lr = torch.nn.Linear(n_features, 1)
        self.weight = ts.ckks_vector(ctx, lr.weight.data.tolist()[0])
        self.bias = ts.ckks_vector(ctx, lr.bias.data.tolist()) 
        self._delta_w = 0
        self._delta_b = 0
        self._count = 0
        
    def encrypt(self, context):
        self.weight = ts.ckks_vector(context, self.weight)
        self.bias = ts.ckks_vector(context, self.bias)

    def forward(self, enc_x):
        enc_out = enc_x.dot(self.weight) + self.bias
        enc_out = EncryptedLogisticRegression.sigmoid(enc_out)
        return enc_out
    
    def backward(self, enc_x, enc_out, enc_y):
        out_minus_y = (enc_out - enc_y)
        self._delta_w += enc_x * out_minus_y
        self._delta_b += out_minus_y
        self._count += 1
        
    def update_parameters(self):
        if self._count == 0:
            raise RuntimeError("You should at least run one forward iteration")
        # update weights
        # We use a small regularization term to keep the output
        # of the linear layer in the range of the sigmoid approximation
        self.weight -= self._delta_w * (1 / self._count) + self.weight * 0.05
        self.bias -= self._delta_b * (1 / self._count)
        # reset gradient accumulators and iterations count
        self._delta_w = 0
        self._delta_b = 0
        self._count = 0
    
    @staticmethod
    def sigmoid(enc_x):
        # Polynomial approximation of degree 3, fits the function pretty well in the range [-5,5]
        return enc_x.polyval([0.5, 0.197, 0, -0.004])
         
    def train(self, logEpoch, enc_x_train, enc_y_train):
        for epoch in range(self.epoch):
            logEpoch(epoch-1)
            for enc_x, enc_y in zip(enc_x_train, enc_y_train):
                enc_out = self.forward(enc_x)
                self.backward(enc_x, enc_out, enc_y)
            self.update_parameters()
        logEpoch(epoch)

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
    
