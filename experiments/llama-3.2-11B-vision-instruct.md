```
MllamaForCausalLM(
  (model): MllamaTextModel(
    (embed_tokens): Embedding(128264, 4096, padding_idx=128004)
    (layers): ModuleList(
      (0-2): 3 x MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (3): MllamaCrossAttentionDecoderLayer(
        (cross_attn): MllamaTextCrossSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_norm): MllamaTextRMSNorm((128,), eps=1e-05)
          (k_norm): MllamaTextRMSNorm((128,), eps=1e-05)
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (4-7): 4 x MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (8): MllamaCrossAttentionDecoderLayer(
        (cross_attn): MllamaTextCrossSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_norm): MllamaTextRMSNorm((128,), eps=1e-05)
          (k_norm): MllamaTextRMSNorm((128,), eps=1e-05)
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (9-12): 4 x MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (13): MllamaCrossAttentionDecoderLayer(
        (cross_attn): MllamaTextCrossSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_norm): MllamaTextRMSNorm((128,), eps=1e-05)
          (k_norm): MllamaTextRMSNorm((128,), eps=1e-05)
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (14-17): 4 x MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (18): MllamaCrossAttentionDecoderLayer(
        (cross_attn): MllamaTextCrossSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_norm): MllamaTextRMSNorm((128,), eps=1e-05)
          (k_norm): MllamaTextRMSNorm((128,), eps=1e-05)
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (19-22): 4 x MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (23): MllamaCrossAttentionDecoderLayer(
        (cross_attn): MllamaTextCrossSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_norm): MllamaTextRMSNorm((128,), eps=1e-05)
          (k_norm): MllamaTextRMSNorm((128,), eps=1e-05)
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (24-27): 4 x MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (28): MllamaCrossAttentionDecoderLayer(
        (cross_attn): MllamaTextCrossSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_norm): MllamaTextRMSNorm((128,), eps=1e-05)
          (k_norm): MllamaTextRMSNorm((128,), eps=1e-05)
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (29-32): 4 x MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (33): MllamaCrossAttentionDecoderLayer(
        (cross_attn): MllamaTextCrossSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_norm): MllamaTextRMSNorm((128,), eps=1e-05)
          (k_norm): MllamaTextRMSNorm((128,), eps=1e-05)
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (34-37): 4 x MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (38): MllamaCrossAttentionDecoderLayer(
        (cross_attn): MllamaTextCrossSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (q_norm): MllamaTextRMSNorm((128,), eps=1e-05)
          (k_norm): MllamaTextRMSNorm((128,), eps=1e-05)
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
      (39): MllamaSelfAttentionDecoderLayer(
        (self_attn): MllamaTextSelfSdpaAttention(
          (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        )
        (mlp): MllamaTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
          (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
          (act_fn): SiLU()
        )
        (input_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): MllamaTextRMSNorm((4096,), eps=1e-05)
      )
    )
    (norm): MllamaTextRMSNorm((4096,), eps=1e-05)
    (rotary_emb): MllamaRotaryEmbedding()
  )
  (lm_head): Linear(in_features=4096, out_features=128256, bias=False)
)
```


# Insights
- You can steer on both self attention decoder layers and cross attention decoder layers
- I was able to make the model prioritize "safer" behavior even across multiple layers