# 🌾 Shamba AI — Kenya Farmer Advisory in Swahili

> *Shamba* (Swahili) = farm, field, agricultural land

AI-powered farming assistant that helps Kenyan farmers with crop disease diagnosis, weather alerts, market prices, and agricultural advice — all in natural Swahili.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shambaai.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What it does

| Feature | Description |
|---------|-------------|
| 🔍 Crop Disease | Describe symptoms in Swahili, get diagnosis and treatment |
| 🌤 Weather | Daily weather advisory for your county |
| 💰 Market Prices | Current maize, beans, tomato prices by county |
| 🌱 Planting Calendar | Optimal planting windows by crop and region |
| 💊 Inputs Guide | Fertilizer and pesticide recommendations |
| 📱 SMS Export | Send summary to your phone via Africa's Talking |

## Research Basis

Built on the cross-lingual RAG methodology validated for agricultural advisory in low-resource languages (arXiv:2601.02065). Native Swahili reasoning produces ~4× fewer errors than translation-based approaches (arXiv:2509.04516).

## Architecture

```
User (Swahili) → Gemini REST API → Domain-grounded response (Swahili)
                      ↓
              Kenya crop knowledge base
              County weather API
              WFP market price data
```

## Quickstart

```bash
git clone https://github.com/gabrielmahia/shamba-ai
cd shamba-ai
pip install -r requirements.txt
# Add GOOGLE_API_KEY to .streamlit/secrets.toml
streamlit run app.py
```

## Data Sources

- Kenya Meteorological Department (public API)
- WFP Market Monitor Kenya (public data)
- KARI/KALRO crop disease documentation
- Kenya Plant Health Inspectorate Service (KEPHIS)

## Part of the East Africa Civic Tech Portfolio

This app is part of a portfolio of 25+ open-source AI tools for East Africa.
See also: [mpesa-mcp](https://github.com/gabrielmahia/mpesa-mcp) | [DarajaAI](https://github.com/gabrielmahia/daraja-ai) | [ShuleAI](https://github.com/gabrielmahia/shule-ai)

## Disclaimer

This tool provides AI-generated agricultural guidance for educational purposes only.
Always verify with certified agricultural extension officers. Not liable for crop losses.

---

*Built with ❤️ for East African farmers | gabrielmahia.ai*

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).
