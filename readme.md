# Coamndos

## Build
    
    buildah bud --layers=true -t uploads:latest .

## Run
    
    mkdir {uploads,upload}

    podman run -it --rm --name uploads \
        -v ${PWD}/upload:/upload \
        -v ${PWD}/uploads:/uploads \
        -p8000:8000 uploads:latest
