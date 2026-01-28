# MotorMinder Architecture Documentation

## Level 1: System Context Diagram (MVP)

This diagram follows the **C4 Model** for software architecture, representing the highest level of abstraction. It illustrates how the **MotorMinder** application interacts with the user and the local environment.

### Project Scope
For the Minimum Viable Product (MVP), the system is implemented as a **Console-Based Python Application**. To ensure simplicity and portability during initial development, the system relies on local JSON persistence rather than external database servers or cloud APIs.

```mermaid
graph TD
    %% Actor
    User((Vehicle Owner))

    subgraph SystemBoundary [MotorMinder Python Script]
        CLI[Console Interface]
        Engine[Maintenance Logic]
        DataHandler[JSON Parser/Handler]
    end

    %% Storage
    File[(vehicles.json)]

    %% Interactions
    User -->|Inputs car details/services| CLI
    CLI -->|Displays history/recommendations| User
    
    CLI <--> Engine
    Engine <--> DataHandler
    
    DataHandler -->|Writes car records| File
    File -->|Loads records on startup| DataHandler

    %% Styling
    style SystemBoundary fill:#fdfdfd,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
    style CLI fill:#3776ab,color:#fff
    style Engine fill:#3776ab,color:#fff
    style DataHandler fill:#3776ab,color:#fff
    style File fill:#ffd43b,color:#000
```
