function changeMap() {
    const mapSelect = document.getElementById('mapSelect');
    const selectedOption = mapSelect.options[mapSelect.selectedIndex];
    const mapImageUrl = selectedOption.getAttribute('data-image-url');
    const mapImage = document.getElementById('mapImage');
    const mapId = selectedOption.value;

    // Changer l'image de la carte
    mapImage.src = mapImageUrl;

    // Générer la grille
    const mapWidth = selectedOption.getAttribute('data-width');
    const mapHeight = selectedOption.getAttribute('data-height');
    const gridContainer = document.getElementById('grid-container');
    gridContainer.innerHTML = ''; // Clear previous grid cells
    gridContainer.style.gridTemplateColumns = `repeat(${mapWidth}, 1fr)`;
    gridContainer.style.gridTemplateRows = `repeat(${mapHeight}, 1fr)`;
    
    for (let i = 0; i < mapWidth * mapHeight; i++) {
        const gridCell = document.createElement('div');
        gridCell.className = 'grid-cell';
        gridContainer.appendChild(gridCell);
    }

    // Filtrer les locations par carte sélectionnée
    const locations = document.querySelectorAll('.location');
    locations.forEach(location => {
        if (location.getAttribute('data-map-id') === mapId) {
            location.style.display = 'block';
        } else {
            location.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    // Initialiser avec la première carte sélectionnée
    changeMap();
});