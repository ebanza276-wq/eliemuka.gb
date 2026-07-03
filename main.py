import flet as ft

def main(page: ft.Page):
    page.title = "Annonces App"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False
    page.window.center()

    # Header
    header = ft.Container(
        content=ft.Row(
            [
                ft.Text(
                    "Annonces",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#6200EE",
                ),
                ft.Icon(ft.Icons.NOTIFICATIONS_OUTLINED),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.Padding.only(top=10, bottom=5, left=20, right=20),
        #padding=20,
    )

    # Hero Banner
    hero = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Trouvez ce dont\nvous avez besoin",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
                ft.ElevatedButton(
                    "Explorer",
                    bgcolor="white",
                    color="#6200EE",
                ),
            ]
        ),
        bgcolor="#6200EE",
        padding=20,
        border_radius=15,
        width=float("inf"),
        margin=10,
    )
    def page_immobilier(nom):
        def retour(e):
           contenu.content = page_accueil()
           page.update()
        contenu.content = ft.Column(
        [
            ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    on_click=retour,
                ),
                title=ft.Text(nom),
                bgcolor="#6200EE",
            ),
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=ft.Text(
                    f"Catégorie : {nom}",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
        ],
        expand=True,
    )

        page.update()
    def page_vehicules(nom):
        def retour(e):
           contenu.content = page_accueil()
           page.update()
        contenu.content = ft.Column(
        [
            ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    on_click=retour,
                ),
                title=ft.Text(nom),
                bgcolor="#6200EE",
            ),
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=ft.Text(
                    f"Catégorie : {nom}",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
        ],
        expand=True,
    )

        page.update()
    def page_electronique(nom):
        def retour(e):
           contenu.content = page_accueil()
           page.update()
        contenu.content = ft.Column(
        [
            ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    on_click=retour,
                ),
                title=ft.Text(nom),
                bgcolor="#6200EE",
            ),
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=ft.Text(
                    f"Catégorie : {nom}",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
        ],
        expand=True,
    )

        page.update()
    def page_maison(nom):
        def retour(e):
           contenu.content = page_accueil()
           page.update()
        contenu.content = ft.Column(
        [
            ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    on_click=retour,
                ),
                title=ft.Text(nom),
                bgcolor="#6200EE",
            ),
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=ft.Text(
                    f"Catégorie : {nom}",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
        ],
        expand=True,
    )

        page.update()
    def ouvrir_categorie(nom):
        if nom == "Immobilier":
            page_immobilier(nom)
        elif nom == "Véhicules":
            page_vehicules(nom)
        elif nom == "Électronique":
            page_electronique(nom)
        elif nom == "Maison":
            page_maison(nom)

        page.update()
    # Categories
    def create_cat(icon, label):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Icon(
                            icon,
                            size=30,
                            color="black",
                        ),
                        bgcolor="#F5F5F5",
                        padding=15,
                        border_radius=50,
                    ),
                    ft.Text(label, size=12),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            on_click=lambda e, cat=label: ouvrir_categorie(cat),
        )

    categories = ft.Container(
        margin=ft.Margin.symmetric(vertical=10),
        content=ft.Row(
            [
                create_cat(
                    ft.Icons.HOME_OUTLINED,
                    "Immobilier",
                ),
                create_cat(
                    ft.Icons.DIRECTIONS_CAR_OUTLINED,
                    "Véhicules",
                ),
                create_cat(
                    ft.Icons.TV,
                    "Électronique",
                ),
                create_cat(
                    ft.Icons.CHAIR_OUTLINED,
                    "Maison",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
    )

    # Cartes annonces
    def create_card(image_url, title, price, location, ville):
        return ft.Card(
            content=ft.Container(
                padding=0,
                width=190,
                content=ft.Column(
                    [
                        ft.Image(
                            src=image_url,
                            height=130,
                            fit="cover",
                            border_radius=10,
                            width=float("inf")
                        ),
                        ft.Text(
                            title,
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            max_lines=2,
                        ),
                        ft.Text(
                            price,
                            color="lime",
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(ville, color="grey", size=12),
                        ft.Text(location, size=10, color="grey"),
                    ]
                ),
            )
        )

    annonces = ft.GridView(
        runs_count=2,
        child_aspect_ratio=0.67,
        #spacing=6,
        padding=6,
        expand=True,
        controls=[
            create_card(
                "https://picsum.photos/200/200",
                "Canapé 3 places",
                "250 €",
                "Paris, 75011",
                "Paris",
            ),
            create_card(
                "https://picsum.photos/201/201",
                "Peugeot 208",
                "8 500 €",
                "Lyon, 69003",
                "Lyon",
            ),
            create_card(
                "https://picsum.photos/202/202",
                "Mercedes Classe C",
                "18 500 €",
                "Marseille",
                "Marseille",
            ),
            create_card(
                "https://picsum.photos/203/203",
                "iPhone 15",
                "900 €",
                "Bordeaux",
                "Bordeaux",
            ),
            create_card(
                "https://picsum.photos/204/204",
                "Samsung S24",
                "850 €",
                "Nice",
                "Nice",
            ),
            create_card(
                "https://picsum.photos/205/205",
                "TV LG 55 pouces",
                "450 €",
                "Lille",
                "Lille",
            ),
        ],
    )

    def page_accueil():
        return ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                header,
                ft.Container(
                    padding=10,
                    content=ft.TextField(
                        hint_text="Rechercher un produit...",
                        prefix_icon=ft.Icons.SEARCH,
                        border_radius=20,
                        filled=True,
                        expand=True,
                    ),
                ),
                hero,
                ft.Container(
                    padding=ft.Padding.only(top=0, bottom=5, left=20, right=20),
                    #padding=10,
                    content=ft.Text(
                        "Catégories",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
                categories,
                ft.Container(
                    padding=10,
                    content=ft.Text(
                        "Annonces récentes",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
                ft.Container(
                    expand=True,
                    content=annonces,
                ),
            ],
        )

    contenu = ft.Container(expand=True)

    def set_index(i):
        if i == 0:
            contenu.content = page_accueil()
        else:
            contenu.content = ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=ft.Text("Page vide", size=30),
            )

        page.update()

    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=lambda e: set_index(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="Accueil",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SEARCH,
                label="Rechercher",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                label="Publier",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.MESSAGE_OUTLINED,
                label="Messages",
            ),
        ],
    )
    
    contenu.content = page_accueil()
    page.add(contenu)

ft.app(target=main)
