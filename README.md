# MotorMinder

This project proposes the development of a car maintenance tracking and recommendation application designed to help vehicle owners better understand, manage, and maintain their vehicles' health. A lot of drivers have a hard time keeping track of routine maintenance, like oil changes, tire rotations, inspections, etc. This can lead to unnecessary repairs, wasted money, and reduced vehicle lifespan. This application aims to consolidate vehicle information to give the user valuable maintenance recommendations based on vehicle condition data.

The focal point of our minimum viable product (MVP) will be tracking basic vehicle information and simulating maintenance needs using sample data. Users will be able to view one or more vehicles that will have associated attributes like current mileage, service history, and overall health indicators. With this information, the application will recommend when maintenance is due at appropriate times, like oil changes, brake inspections and replacement, or tire replacements. In the initial release, the application will not connect to real vehicles, and all data will be generated and managed internally using predefined or simulated vehicle records. Using this approach will allow the core logic and system design to be developed without having to rely on any external hardware or third-party integrations.

On top of maintenance recommendations, the application will also include functionality to track regular checkups and services. Users will be able to record when a maintenance task was performed, update mileage, and view upcoming or even overdue services. A third, and important, feature of the system is the ability to find nearby mechanics. The application will provide a list of local mechanic options (using sample data in the initial release), to allow users to connect service visits with specific repair shops or providers.

This project is well-suited for object-oriented design and development. The main entities of vehicle, maintenance task, service record, mechanic, and user can be modeled as classes with well-defined responsibilities and interactions. The recommendation logic that will be designed can be encapsulated within a dedicated maintenance engine that evaluates vehicle data and determines which service, or services, are required. This kind of modular design supports maintainability, testing, and scalability.

The project is designed to support an iterative development process so we can work on it consistently throughout the semester. The first iteration will focus on modeling vehicles, simulating health data, and generating basic maintenance recommendations. Later iterations can introduce more complex rules, expanded service tracking, improved mechanic search functionality, and integrate with real vehicle data sources to replace the simulated data with real-life information.

The car maintenance tracking and recommendation application addresses a practical, real-world problem and provides plenty of opportunities to demonstrate object-oriented programming principles and sound software engineering practices.

## Contributers
Ethan Hess, Ethan Kidd, Preston Little, Ryan Carbine
