# Limitations

While the results of this case study are promising, the following limitations must be noted:

- **Benchmark Specificity:** Performance was evaluated only on the Neural-Scalpel SQL-50 suite.
- **Out-of-Distribution Behavior:** The adapter has not been validated on general-purpose SQL benchmarks like Spider or BIRD.
- **Improvement Scale:** The accuracy improvement (+4.0%) is modest and task-dependent. It should be viewed as a "proof of concept" for non-retraining transplantation rather than a production-ready SQL solution.
- **Architecture Sensitivity:** This specific success (7B to 0.5B) is within the same model family (Qwen2.5). Cross-family projection (e.g., Llama to Qwen) may be significantly more challenging.
- **No Logical Guarantee:** The adapter preserves the target model's "style" of generation. It may still produce logically incorrect SQL if the underlying base model lacks the necessary reasoning capacity for a specific query.
- **Source Adapter Quality Matters:** Structural Projection may transfer both beneficial and harmful components of the source adapter. If the source adapter degrades its own base model, the projected adapter may also introduce interference.
- **Not Monotonic with Model Size:** Larger target models do not necessarily benefit more. Improvements depend on whether the adapter complements the target model's existing capabilities.
- **Interference Risk:** On stronger target models, the projected adapter can act as noise and reduce accuracy.
- **Positive Source Required:** The strongest results were observed when the source adapter first improved its own base model. Source adapters that degrade their base model may also project harmful components.
- **Family-Specific Evidence:** The strongest positive transfer results were observed within the Qwen2.5-Coder family. Cross-family transfer remains unverified.
- **Benchmark-Specific Result:** The positive-teacher experiment was evaluated on SQL-50. Broader benchmarks such as Spider and BIRD remain future work.
