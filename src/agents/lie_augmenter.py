import torch
import torch.nn as nn

class LieAugmenter(nn.Module):
    """
    محرك اكتشاف التناظرات المستمرة عبر جبر لي (Build 2.0).
    LieAugmenter: Continuous symmetry discovery via Lie Algebra (Build 2.0).
    """
    def __init__(self, input_dim, num_generators=3, hidden_dim=64):
        super().__init__()
        # Learnable Lie Algebra Generators: Lie Algebra basis elements
        self.generators = nn.Parameter(torch.randn(num_generators, input_dim, input_dim) * 0.1)

        # Base Prediction Network
        self.prediction_net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1) # Assuming a scalar output for simplicity
        )

    def forward(self, x):
        """
        تطبيق التحولات المكتشفة لتعزيز كفاءة التعلم.
        Applies discovered transformations for sample-efficient learning.
        """
        # 1. Sample transformation coefficients alpha (infinitesimal steps)
        # In practice, these could be learned or sampled from a distribution
        batch_size = x.shape[0]
        num_gens = self.generators.shape[0]
        alphas = torch.randn(batch_size, num_gens, 1, 1).to(x.device)

        # 2. Compute transformation matrix G via Exponential Map
        # G = exp(sum(alpha_l * g_l))
        # Expand generators to batch size
        gens_expanded = self.generators.unsqueeze(0).expand(batch_size, -1, -1, -1)
        lie_algebra_element = torch.sum(alphas * gens_expanded, dim=1)

        # Use Pade Approximation / Scaling and Squaring via torch.matrix_exp
        transformation_matrix = torch.matrix_exp(lie_algebra_element)

        # 3. Apply transformation to inputs (Augmented View)
        # x shape: (batch_size, input_dim)
        # transformation_matrix shape: (batch_size, input_dim, input_dim)
        augmented_x = torch.bmm(x.unsqueeze(1), transformation_matrix).squeeze(1)

        # 4. Symmetry-aware prediction
        return self.prediction_net(augmented_x)

    def get_invariance_loss(self, x):
        """
        Calculates how invariant the model is to the learned symmetries.
        loss = ||f(x) - f(exp(g)x)||
        """
        y_orig = self.prediction_net(x)
        y_aug = self.forward(x)
        return torch.mean((y_orig - y_aug)**2)
