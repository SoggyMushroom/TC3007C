# TC3007C

## Linear Traits Estimation - Pipeline

```mermaid
flowchart TD
    A([Start]) --> B[Data Collection Phase]

    subgraph C[Data Preparation]
        C1[Capture cow images]
        C2[Manual annotation'\n'(COCO format)]
        C3[Annotate anatomical keypoints\n(hooks, pins, withers, etc.)]
        C4[Create sample dataset]
        C5[Validate label quality]
    end

    B --> C

    subgraph D[Model Development]
        D1[Data exploration & analysis]
        D2[Train DeepLabCut model]
        D3[Validate model performance]
        D4[Save model checkpoints]
    end

    C --> D

    subgraph E[Inference & Evaluation]
        E1[Run inference on new images]
        E2[Compute pose keypoints]
        E3[Convert keypoints → linear measurements\nand trait scores]
        E4[Calculate evaluation metrics]
        E5[Generate visualizations]
    end

    D --> E

    subgraph F[Deployment]
        F1[Build CLI tool]
        F2[Create Streamlit demo]
        F3[Test end-to-end pipeline]
    end

    E --> F
    F --> Z([End])


    %% ==============================
    %% CONNECTIONS
    %% ==============================
    B --> C --> D --> E --> F --> Z([End])
