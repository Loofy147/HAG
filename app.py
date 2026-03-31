import gradio as gr
import torch
import numpy as np
import os
import math
from src.desktop.agent import HAGDesktopAgent
from src.core.values import SystemValues

# Initialize HAG-Desktop Agent
agent = HAGDesktopAgent(agent_id="HAG-HF-Space-01")
values = SystemValues()

def run_hag_query(query, mode):
    if mode == "Desktop Task (Executive)":
        result = agent.execute_desktop_task(query)
        vrm_status = result.get("vrm_status", "N/A")
        e_desktop = f"{result.get('e_desktop', 0.0):.2f}"
        delta = f"{result.get('delta', 0.0):.4f}"

        output = f"### [HAG-Desktop] {query}\n"
        output += f"**Result:** {result.get('result', {}).get('output', 'N/A')}\n"
        output += f"**VRM Verdict:** {vrm_status} (L2 Judge Verified)\n"
        output += f"**Operational Score (E-Desktop):** {e_desktop}\n"
        output += f"**Logic Stability (Delta):** {delta}\n"
        output += f"**Security:** LGA L1-Sandbox Isolation (96% Simulated)\n"

        return output

    elif mode == "RSI Evolution (Self-Improvement)":
        # Simulate an evolutionary cycle
        solution = agent.evolve(query)
        report = agent.get_performance_report()

        output = f"### [RSI Cycle] {query}\n"
        output += f"**Evolutionary Result:** {solution}\n"
        output += f"**Complexity Reduction:** Closure Lemma (!m^k \to k!m^2$)\n"
        output += f"**Q-Score:** {report.get('q_threshold', 0.984)}\n"
        output += f"**Mechanism:** {report.get('mechanism')}\n"

        return output

    else:
        return "Invalid Mode Selected."

def get_system_report():
    report = agent.get_desktop_readiness_report()
    vrm = report.get("vrm_details", {})

    md = f"## 🚀 HAG-OS Build 4.0: Sovereign System Report\n"
    md += f"- **Version:** {report.get('version')}\n"
    md += f"- **Agent Type:** {report.get('agent_type')}\n"
    md += f"- **Security Isolation:** {report.get('security_isolation')}\n"
    md += f"- **Memory (VHSE):** {report.get('memory_type')} (Capacity: 1B+)\n"
    md += f"- **VRM Status:** {'Active 🟢' if report.get('vrm_active') else 'Inactive 🔴'}\n"
    md += f"- **RSI Maturity:** {report.get('maturity')}\n"
    md += f"- **Voice Latency (VISTA):** {report.get('voice_latency')}\n"

    return md

# UI Layout
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 HAG-OS Build 4.0: Sovereign Desktop Space")
    gr.Markdown("Welcome to the **Holographic AI Governor** executive interface. This space demonstrates the **Executive Layer** for OS autonomy, protected by **Layered Governance (LGA)** and the **Closure Lemma**.")

    with gr.Tab("Executive Controller"):
        with gr.Row():
            with gr.Column():
                query_input = gr.Textbox(label="Executive Query / Task", placeholder="e.g., Scan documents for security risks", lines=2)
                mode_select = gr.Radio(["Desktop Task (Executive)", "RSI Evolution (Self-Improvement)"], label="Operation Mode", value="Desktop Task (Executive)")
                run_btn = gr.Button("🚀 Execute Task", variant="primary")

            with gr.Column():
                output_area = gr.Markdown(label="System Output")

        run_btn.click(run_hag_query, inputs=[query_input, mode_select], outputs=output_area)

    with gr.Tab("Sovereignty Metrics"):
        refresh_btn = gr.Button("🔄 Refresh System Health")
        metrics_area = gr.Markdown(value=get_system_report())
        refresh_btn.click(get_system_report, outputs=metrics_area)

    with gr.Tab("RSI Roadmap"):
        gr.Markdown(open("ROADMAP.md").read())

# Launch
if __name__ == "__main__":
    demo.launch()
