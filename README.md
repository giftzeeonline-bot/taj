# Smartnode customer support POC

This repository contains:

- [Smartnode_customer_support_use_cases.pptx](./Smartnode_customer_support_use_cases.pptx): a one-slide use-case and benefits overview.
- [smartnode_customer_support_poc.ipynb](./smartnode_customer_support_poc.ipynb): an end-to-end speech-to-text and Closed/Open/Urgent triage demonstration.
- [generate_slide.py](./generate_slide.py): source used to generate the PowerPoint.

## Run the notebook

Open the notebook in Google Colab and run all cells, or run it in a local Jupyter environment. The notebook installs its Python dependencies, fetches three English audio samples from the public MInDS-14 dataset, downloads the small `tiny.en` Whisper model, transcribes the audio locally with `faster-whisper`, and classifies the resulting text with auditable keyword rules. The first run needs internet access and downloads the model; CPU inference may take a few minutes.

Local setup:

```bash
python -m pip install -r requirements.txt
jupyter notebook smartnode_customer_support_poc.ipynb
```

The notebook writes `poc_outputs/transcribed_calls.csv`. It also runs example checks covering all three categories.

## Scope and assumptions

- “Smartnode” is treated as a customer/dealer support organization for connected or installed products; no Smartnode-specific product, policy, or operating data was supplied or assumed as fact.
- **Closed** means the customer explicitly confirms resolution; **Open** means action or resolution is still pending; **Urgent** is a safety risk or critical service interruption. Urgent takes precedence over other signals.
- Triage is a transparent rules-based baseline, not a trained classifier. Keyword matches can miss context, negation, sarcasm, or unfamiliar wording. Keep a human in the loop, validate against Smartnode-labelled calls, and define escalation policy with operations/safety teams before production.
- MInDS-14 is an English/other-language banking-intent speech dataset, not Smartnode calls. It is used only to exercise the audio-download/transcription pipeline. Its dataset card states CC-BY-4.0; give attribution and check the card for license terms before redistribution.
- Benefits in the slide are directional pilot targets, not measured outcomes or guarantees. Validate them against a baseline and monitor quality, fairness, privacy, and safety.
- The notebook fetches audio and transcribes it locally. Do not upload customer recordings to this public demo; production use requires consent, access controls, retention limits, and approved data handling.

## Regenerate the slide

```bash
python -m pip install python-pptx
python generate_slide.py
```

Source: [PolyAI/MInDS-14 dataset card](https://huggingface.co/datasets/PolyAI/minds14).
