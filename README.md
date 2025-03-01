#### Name: Patsachon Pattakulpong st124952
### Task 1: Dataset link: https://huggingface.co/datasets/Anthropic/hh-rlhf
### Task 2: Training a Model with DPOTrainer
#### Base Model Selection
I implemented Direct Preference Optimization (DPO) using the specialized `DPOTrainer` framework. This approach fine-tunes the model by learning from paired examples of preferred and non-preferred responses, effectively teaching it to distinguish between desirable and undesirable outputs.  

For this homework, I used `Anthropic/hh-rlhf` as the pre-trained language model, available through Hugging Face's model hub, as the foundation for preference optimization. This model architecture provides a strong balance between performance and computational efficiency.

#### Training Configuration
The training process was configured with the following parameters:

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Learning Rate | 1e-3 | Controls step size during optimization |
| Batch Size | 4 | Number of samples processed in each forward pass |
| Gradient Accumulation | 1 | Updates weights after each batch |
| Max Sequence Length | 256 | Limits context window for processing |
| Training Steps | 1000 | Total iterations for optimization |

#### Monitoring and Evaluation
I use Wandb (Weights & Biases) to track these metrics in real-time. The platform provides interactive visualizations that helped identify training patterns and potential issues. With Wandb's logging capabilities, I could observe how the model gradually learned to distinguish between preferred and non-preferred responses over the 1000 training steps.

### Training Results
The table below shows the metrics tracked during model training at steps 500 and 1000:

| Step | Training Loss | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|------|---------------|-----------------|----------------|------------------|-------------------|----------------|-----------------|--------------|-----------------|---------------|
| 500  | 2.041600      | 3.162900        | -11.313297     | -14.325815       | 0.597000          | 3.012520       | -283.884094     | -230.698654  | -9.234812       | -9.627277     |
| 1000 | 0.100600      | 4.512190        | -23.955256     | -28.742985       | 0.597000          | 4.787728       | -428.055786     | -357.118225  | -40.360313      | -40.775414    |

- from training result, it shows a significant decrease on training loss while the reward margin between chosen and rejected responses increased. The consistent accuracy measurement of 59.7% indicates room for improvement in the model's ability to discriminate between preferred and non-preferred responses.

### Task 3: Huggingface link: https://huggingface.co/PattycherryAnker/optimize-human-preference

### Task4: Web Application: 

https://github.com/user-attachments/assets/136fa33e-0663-4cf3-bfa2-a259916b7f22


<img width="614" alt="Screenshot 2568-03-02 at 4 41 08 AM" src="https://github.com/user-attachments/assets/047d2ae7-0b50-4125-9866-72d25e6fa3c1" />

- FYI: model file is too big too push to Github, you can access via this Google Drive link and if you want to run my web application, you can use **"python app.py"** but all you have to do is download model folder. This is link to model file: https://drive.google.com/drive/folders/1FyAWvfTPtbkBGAuY_WBMAA4Jvp1UfW6y?usp=sharing
