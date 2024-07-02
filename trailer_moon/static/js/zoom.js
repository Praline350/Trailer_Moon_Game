document.addEventListener('DOMContentLoaded', (event) => {
    let scale = 1;
    let clickCount = 0;
    const map = document.getElementById('map');
    const mapContainer = document.querySelector('.map-container');

    function zoomIn() {
        if (clickCount < 5) {
            clickCount += 1;
            scale = 1 + (clickCount * 0.1);
            applyZoom();
        }
    }

    function zoomOut() {
        if (clickCount > 0) {
            clickCount -= 1;
            scale = 1 + (clickCount * 0.1);
            applyZoom();
        }
    }

    function applyZoom() {
        map.style.transform = `scale(${scale})`;
        updateMapPosition();
    }

    function updateMapPosition() {
        const mapRect = map.getBoundingClientRect();
        const containerRect = mapContainer.getBoundingClientRect();

        // Vérifiez les limites horizontales
        if (mapRect.left > containerRect.left) {
            map.style.left = '0px';
        } else if (mapRect.right < containerRect.right) {
            map.style.left = `${containerRect.width - mapRect.width}px`;
        }

        // Vérifiez les limites verticales
        if (mapRect.top > containerRect.top) {
            map.style.top = '0px';
        } else if (mapRect.bottom < containerRect.bottom) {
            map.style.top = `${containerRect.height - mapRect.height}px`;
        }
    }

    function moveMap(direction) {
        const step = 100; // Nombre de pixels pour chaque mouvement
        const mapRect = map.getBoundingClientRect();
        const containerRect = mapContainer.getBoundingClientRect();

        switch (direction) {
            case 'up':
                if (mapRect.top + step < containerRect.top) {
                    map.style.top = `${map.offsetTop + step}px`;
                } else {
                    map.style.top = '0px';
                }
                break;
            case 'down':
                if (mapRect.bottom - step > containerRect.bottom) {
                    map.style.top = `${map.offsetTop - step}px`;
                } else {
                    map.style.top = `${containerRect.height - mapRect.height}px`;
                }
                break;
            case 'left':
                if (mapRect.left + step < containerRect.left) {
                    map.style.left = `${map.offsetLeft + step}px`;
                } else {
                    map.style.left = '0px';
                }
                break;
            case 'right':
                if (mapRect.right - step > containerRect.right) {
                    map.style.left = `${map.offsetLeft - step}px`;
                } else {
                    map.style.left = `${containerRect.width - mapRect.width}px`;
                }
                break;
        }
    }

    // Expose the functions to the global scope
    window.zoomIn = zoomIn;
    window.zoomOut = zoomOut;
    window.moveMap = moveMap;
});
