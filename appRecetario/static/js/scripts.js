document.addEventListener("DOMContentLoaded", () => {
    // Cargar más tipos de plato
    const cargarMasTiposPlatoBtn = document.getElementById("cargar-mas-tipos-plato");
    const categoriesContainer = document.getElementById("categories-container");

    if (cargarMasTiposPlatoBtn) {
        cargarMasTiposPlatoBtn.addEventListener("click", () => {
            const offset = parseInt(cargarMasTiposPlatoBtn.getAttribute("data-offset"));

            fetch(`/tipos-plato/cargar-mas/?offset=${offset}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Error en la respuesta del servidor");
                    }
                    return response.json();
                })
                .then(data => {
                    data.tipos_plato.forEach(item => {
                        const cardId = `tipo-plato-${item.id}`;
                        if (!document.getElementById(cardId)) {
                            const card = `
                                <a href="/tipos-plato/${item.id}" id="${cardId}" class="category-card-rectangular">
                                    <div class="category-image-rectangular">
                                        <img src="${item.imagen || '/static/images/default.png'}" alt="${item.nombre}">
                                    </div>
                                    <div class="category-text-rectangular">
                                        <h4>${item.nombre}</h4>
                                        <p>${item.descripcion}</p>
                                    </div>
                                </a>
                            `;
                            categoriesContainer.insertAdjacentHTML("beforeend", card);
                        }
                    });

                    cargarMasTiposPlatoBtn.setAttribute("data-offset", offset + data.tipos_plato.length);

                    if (data.tipos_plato.length < 10) {
                        cargarMasTiposPlatoBtn.style.display = "none";
                    }
                })
                .catch(error => console.error("Error al cargar más tipos de plato:", error));
        });
    }

    // Cargar más recetas
    const cargarMasRecetasBtn = document.getElementById("cargar-mas-recetas");
    const recipesContainer = document.getElementById("recipes-container");

    if (cargarMasRecetasBtn) {
        cargarMasRecetasBtn.addEventListener("click", () => {
            const offset = parseInt(cargarMasRecetasBtn.getAttribute("data-offset"));

            fetch(`/recetas/cargar-mas/?offset=${offset}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Error en la respuesta del servidor");
                    }
                    return response.json();
                })
                .then(data => {
                    data.recetas.forEach(item => {
                        const cardId = `recipe-${item.id}`;
                        if (!document.getElementById(cardId)) {
                            const card = `
                                <div id="recipe-${item.id}" class="recipe-card">
                                    <img src="${item.imagen || '/static/media/default_image.png'}" alt="${item.nombre}" class="recipe-image">
                                    <div class="recipe-info">
                                        <h3 class="recipe-title">${item.nombre}</h3>
                                        <p>Tipo de Plato: ${item.tipo_plato}</p>
                                    </div>
                                    <a href="/recetas/${item.id}" class="btn-recipe">Ver Detalles</a>
                                </div>
                            `;
                            recipesContainer.insertAdjacentHTML("beforeend", card);
                        }
                    });

                    cargarMasRecetasBtn.setAttribute("data-offset", offset + data.recetas.length);

                    if (data.recetas.length < 10) {
                        cargarMasRecetasBtn.style.display = "none";
                    }
                })
                .catch(error => console.error("Error al cargar más recetas:", error));
        });
    }

    // Cargar más ingredientes
    const cargarMasIngredientesBtn = document.getElementById("cargar-mas-ingredientes");
    const ingredientsContainer = document.getElementById("ingredients-container");

    if (cargarMasIngredientesBtn) {
        cargarMasIngredientesBtn.addEventListener("click", () => {
            const offset = parseInt(cargarMasIngredientesBtn.getAttribute("data-offset"));

            fetch(`/ingredientes/cargar-mas/?offset=${offset}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Error en la respuesta del servidor");
                    }
                    return response.json();
                })
                .then(data => {
                    data.ingredientes.forEach(item => {
                        const cardId = `ingredient-${item.id}`;
                        if (!document.getElementById(cardId)) {
                            const card = `
                                <div id="ingredient-${item.id}" class="ingredient-card">
                                    <img src="${item.imagen || '/static/images/default.png'}" alt="${item.nombre}" class="ingredient-image">
                                    <div class="ingredient-text">
                                        <h3 class="ingredient-title">${item.nombre}</h3>
                                        <p class="ingredient-category">Categoría: ${item.categoria}</p>
                                        <a href="/ingredientes/${item.id}/recetas/" class="btn-ingrediente">Ver Recetas</a>
                                    </div>
                                </div>
                            `;
                            ingredientsContainer.insertAdjacentHTML("beforeend", card);
                        }
                    });

                    // Actualiza el offset en el botón
                    cargarMasIngredientesBtn.setAttribute("data-offset", offset + data.ingredientes.length);

                    // Oculta el botón si no hay más ingredientes
                    if (data.ingredientes.length < 10) {
                        cargarMasIngredientesBtn.style.display = "none";
                    }
                })
                .catch(error => console.error("Error al cargar más ingredientes:", error));
        });
    }
});
