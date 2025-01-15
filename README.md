# Social Media Analysis

This repository contains tools and scripts for analyzing social media data, focusing on sentiment analysis, named entity recognition (NER), and information extraction.

## Features

- **Sentiment Analysis**: Classify social media posts as positive, negative, or neutral using models like TextBlob, VADER, and advanced deep learning models.
- **Named Entity Recognition (NER)**: Identify and categorize entities (e.g., names, organizations, locations) within the text.
- **Information Extraction**: Extract meaningful insights from unstructured text data to support decision-making.
- **Integrated Website**: Access a Streamlit-based web interface for live analysis at [jugado.streamlit.app](https://jugadoo.streamlit.app/).

## Installation

### Prerequisites

- Python 3.7 or higher
- Git installed on your system

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/NYT03/jugadoo.git
   cd jugadoo
   ```
   
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Collection**:
   - Use the provided scripts to collect social media data via APIs (e.g., Twitter API, Facebook Graph API) or by scraping.

2. **Run Analysis**:
   - Execute analysis scripts to perform sentiment analysis, NER, and extract key information.

3. **Web Interface**:
   - Visit the [Streamlit web app](https://jugadoo.streamlit.app/) to perform live analysis directly on your browser.

## Parameters
```
FLOW_ID = "777b93bd-8284-4c3d-9645-4ab43b948b6a"
ASTRA_DB_API_ENDPOINT="https://df161d8b-2706-4ed5-a12a-40c755beb98a-us-east-2.apps.astra.datastax.com"
LANGFLOW_ID = "da6a9de9-e025-4aee-a12f-8b75a4790d4f"
ASTRA_DB_APPLICATION_TOKEN="AstraCS:LqLZHplznKuUDQpyvtahuXbN:66a68fe17b11035c075e89668a50848350184cfb9c320d3a753b27da9b03249d"

```

## Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

For live analysis, visit the [Streamlit App](https://jugadoo.streamlit.app/).
