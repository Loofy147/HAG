import torch
import torch.nn as nn

class LieAugmenter(nn.Module):
    """
    محرك اكتشاف التناظرات المستمرة عبر جبر لي (Build 2.0).
    LieAugmenter: Continuous symmetry discovery via Lie Algebra (Build 2.0).
    """
    def __init__(self, input_dim, num_generators=3, hidden_dim=64):
        super().__init__()
        # Learnable Lie Algebra Generators: Lie Algebra basis elements (input_dim x input_dim)
        self.generators = nn.Parameter(torch.randn(num_generators, input_dim, input_dim) * 0.1)

    def forward(self, x):
        """
        تطبيق التحولات المكتشفة لتعزيز كفاءة التعلم.
        Applies discovered transformations.
        Input: (batch, input_dim) -> Output: (batch, input_dim)
        """
        batch_size = x.shape[0]
        num_gens = self.generators.shape[0]
        # Alphas: coefficients for the infinitesimal transformation
        alphas = torch.randn(batch_size, num_gens, 1, 1).to(x.device)

        # 2. Compute transformation matrix G via Exponential Map
        gens_expanded = self.generators.unsqueeze(0).expand(batch_size, -1, -1, -1)
        lie_algebra_element = torch.sum(alphas * gens_expanded, dim=1)

        # G = exp(A)
        transformation_matrix = torch.matrix_exp(lie_algebra_element)

        # 3. Apply transformation: (batch, 1, input_dim) @ (batch, input_dim, input_dim)
        augmented_x = torch.bmm(x.unsqueeze(1), transformation_matrix).squeeze(1)

        return augmented_x

    def get_invariance_loss(self, x):
        """
        Calculates how invariant a dummy prediction (magnitude) is to the learned symmetries.
        In a real scenario, this would compare model(x) and model(aug_x).
        """
        # For simplicity in this base class, we measure how much the transformation changes the norm
        x_aug = self.forward(x)
        return torch.mean((torch.norm(x, dim=1) - torch.norm(x_aug, dim=1))**2)
