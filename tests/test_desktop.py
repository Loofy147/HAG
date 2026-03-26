import unittest
import torch
from src.desktop.agent import HAGDesktopAgent
from src.desktop.governance import LayeredGovernance
from src.core.values import SystemValues

class TestHAGDesktop(unittest.TestCase):
    def setUp(self):
        self.agent = HAGDesktopAgent(agent_id="Test-Desktop-Agent")
        self.values = SystemValues()

    def test_layered_governance_blocking(self):
        """Test that LGA blocks unauthorized or risky actions."""
        lga = LayeredGovernance(agent_id="LGA-Test")
        task = "Search for system health"
        action = "rm -rf /" # High-risk action
        token = lga.l3_cap_manager.issue_token("Task-1", ["fs_read"])

        # Should block due to L3 (missing shell_exec) or L2 (intent mismatch for 'rm')
        result = lga.execute_secured_action(task, action, token, "shell_exec")
        self.assertEqual(result["status"], "error")
        self.assertIn("BLOCKED", lga.l4_logger.logs[-1]["status"])

    def test_desktop_binding_protocol(self):
        """Test that DesktopBinding correctly uses LGA."""
        lga = LayeredGovernance(agent_id="Binding-Test")
        from src.desktop.binding import DesktopBinding
        binding = DesktopBinding(governance=lga)

        task = "Read a config file"
        token = lga.l3_cap_manager.issue_token("Task-2", ["fs_read"])
        binding.set_session_token(token)

        result = binding.read_file(task, "/etc/hag/config.json")
        self.assertEqual(result["status"], "success")
        self.assertEqual(lga.l4_logger.logs[-1]["action"], "read_file('/etc/hag/config.json')")

    def test_e_desktop_calculation(self):
        """Verify the Desktop Agent Operational Formula."""
        # Success Rate: 0.9, Q: 0.99, Cost: 0.1, Delta: 0.05
        # E = (0.9 * 0.99) / (0.1 * 0.05) = 0.891 / 0.005 = 178.2
        e_score = self.agent.calculate_e_desktop(0.9, 0.99, 0.1, 0.05)
        self.assertAlmostEqual(e_score, 178.2)

    def test_multimodal_perception(self):
        """Verify perception layer returns unified context."""
        context = self.agent.perception.get_desktop_context()
        self.assertIn("screen_state", context)
        self.assertEqual(context["perception_mode"], "MULTIMODAL_SOVEREIGN")

if __name__ == '__main__':
    unittest.main()
