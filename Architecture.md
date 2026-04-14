The project follows a decoupled, modular architecture.

1. **Configuration Layer (GlitchConfig)**: Centralizes style constants (ANSI codes, character sets). This allows for easy skinning or localization without touching business logic.
2. **Engine Layer (GlitchEngine)**: Pure logic component responsible for the transformation algorithm. It is initialized with a configuration object, following the Dependency Injection pattern, making it unit-testable in headless environments.
3. **Interface Layer (main)**: A robust CLI wrapper using `argparse`. It handles both direct arguments and UNIX pipes (stdin), providing a professional tool-chain experience.
4. **Error Handling**: Implements graceful exits for KeyboardInterrupts and stream errors, ensuring the utility behaves predictably in shell pipelines.