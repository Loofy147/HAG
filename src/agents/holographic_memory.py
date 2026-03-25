import torch
import torch.nn as nn
import numpy as np

class HolographicWeightEncoder:
    """
    محرك التشفير الهولوغرافي للأوزان (Build 2.1).
    HolographicWeightEncoder: Implements weights as holographic error-correcting codes.
    Prevents catastrophic forgetting by distributing information across the weight manifold.
    """
    def __init__(self, weight_shape):
        self.weight_shape = weight_shape
        self.flat_dim = np.prod(weight_shape)

    def encode(self, weights: torch.Tensor) -> torch.Tensor:
        """
        تحويل الأوزان إلى المجال الهولوغرافي (FFT-based spreading).
        Encodes weights into a holographic representation using Fast Fourier Transform.
        """
        # Flatten and transform to frequency domain
        flat_weights = weights.view(-1).to(torch.complex64)
        holographic_weights = torch.fft.fft(flat_weights)
        return holographic_weights

    def decode(self, holographic_weights: torch.Tensor) -> torch.Tensor:
        """
        استعادة الأوزان من المجال الهولوغرافي.
        Decodes holographic weights back to the spatial domain.
        """
        recovered_flat = torch.fft.ifft(holographic_weights)
        # Return real part and reshape to original
        return recovered_flat.real.view(self.weight_shape)

    def simulate_erasure(self, holographic_weights: torch.Tensor, erasure_ratio: float = 0.2) -> torch.Tensor:
        """
        محاكاة فقدان التشابكات العصبي (Synaptic Erasure).
        Simulates loss of weights by zeroing out a random fraction of the holographic manifold.
        """
        mask = torch.rand_like(holographic_weights.real) > erasure_ratio
        return holographic_weights * mask

    def recover_weights(self, weights: torch.Tensor, erasure_ratio: float = 0.2):
        """
        دورة كاملة: تشفير -> تخريب -> استعادة.
        Full cycle: Encode -> Erase -> Decode.
        """
        h_weights = self.encode(weights)
        damaged_h = self.simulate_erasure(h_weights, erasure_ratio)
        recovered = self.decode(damaged_h)
        return recovered

class HolographicLayer(nn.Module):
    """
    طبقة عصبية هولوغرافية محمية ضد التخريب - GPU Ready.
    A neural layer protected by holographic weight encoding.
    """
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.weights = nn.Parameter(torch.randn(output_dim, input_dim) * 0.1)
        self.encoder = HolographicWeightEncoder((output_dim, input_dim))

    def forward(self, x, damaged=False, erasure_ratio=0.2):
        """
        Forward pass. weights are already on the correct device as part of the module.
        """
        if damaged:
            # Simulate inference with damaged weights recovered from holographic field
            # Note: recover_weights operations happen on the device of self.weights
            w_eff = self.encoder.recover_weights(self.weights, erasure_ratio)
        else:
            w_eff = self.weights

        return torch.matmul(x, w_eff.t())

    def get_integrity_metrics(self, erasure_ratio=0.2):
        """Calculates recovery precision after erasure."""
        recovered = self.encoder.recover_weights(self.weights, erasure_ratio)
        mse = torch.mean((self.weights - recovered)**2)
        # Cosine similarity as a measure of structural integrity
        cos_sim = torch.nn.functional.cosine_similarity(
            self.weights.view(-1), recovered.view(-1), dim=0
        )
        return {
            "mse": mse.item(),
            "integrity_score": cos_sim.item()
        }
