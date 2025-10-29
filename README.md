# TC3007C

## 🧠 Estimación de Características de Conformación Lineal - Workflow Completo

```mermaid
flowchart TD
    %% ==============================
    %% TITLE
    %% ==============================
    A([Start]) --> B([Data Collection Phase])

    %% ==============================
    %% DATA PREPARATION
    %% ==============================
    subgraph C [Data Preparation]
        C1([Capture cow images])
        C2([Manual annotation (COCO format)])
        C3([Annotate anatomical keypoints<br/>(hooks, pins, withers, etc.)])
        C4([Create sample dataset])
        C5([Validate label quality])
        C1 --> C2 --> C3 --> C4 --> C5
    end

    %% ==============================
    %% MODEL DEVELOPMENT
    %% ==============================
    subgraph D [Model Development]
        D1([Data exploration & analysis])
        D2([Train DeepLabCut model])
        D3([Validate model performance])
        D4([Save model checkpoints])
        D1 --> D2 --> D3 --> D4
    end

    %% ==============================
    %% INFERENCE & EVALUATION
    %% ==============================
    subgraph E [Inference & Evaluation]
        E1([Run inference on new images])
        E2([Compute pose keypoints])
        E3([Convert keypoints to linear measurements<br/>and trait scores])
        E4([Calculate evaluation metrics])
        E5([Generate visualizations])
        E1 --> E2 --> E3 --> E4 --> E5
    end

    %% ==============================
    %% DEPLOYMENT
    %% ==============================
    subgraph F [Deployment]
        F1([Build CLI tool])
        F2([Create Streamlit demo])
        F3([Test end-to-end pipeline])
        F1 --> F2 --> F3
    end

    %% ==============================
    %% CONNECTIONS
    %% ==============================
    B --> C --> D --> E --> F --> Z([End])
