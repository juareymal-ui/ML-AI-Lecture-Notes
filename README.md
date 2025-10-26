## Contenido y advertencia

este proyecto contiene:

1. Un directorio/carpeta llamado:
 ```Introduction```
1. Un directorio/carpeta llamado: 
```ml_project```
1. un script de python llamdo:
```create_ml_project.py```

[!WARNING]

No ejecute el script ```create_ml_project.py``` mientras se crea el proyecto, este script crea la estructura del proyecto.

```
├── data/              # Data directory
│   ├── raw/           # Original, immutable data
│   ├── processed/     # Cleaned, transformed data
│   ├── interim/       # Intermediate transformations
│   └── external/      # Third-party data
├── notebooks/         # Jupyter notebooks for exploration
├── src/               # Source code
│   ├── data/          # Data loading and preprocessing
│   ├── features/      # Feature engineering
│   ├── models/        # Model training and evaluation
│   ├── visualization/ # Visualization utilities
│   └── utils/         # Helper functions
├── models/            # Trained models
├── reports/           # Generated reports and figures
├── tests/             # Unit tests
└── config/            # Configuration files
```
En la carpeta ```ml_project```, el script también da instrucciones después de crear la estructura del proyecto y todos sus directorios y archivos, como instalar el entorno virtual, dependencias, etc.