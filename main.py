import flet as ft

def main(page: ft.Page):
    page.title = "Annonces App"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO
    #page.window.width = 390
    #page.window.height = 844
    page.window.resizable = False
    page.window.center()
    # Liste des annonces
    annonces_data = [
    {"name":"Marc","image": "https://picsum.photos/500/300?1", "prix": "250 €", "titre": "Canapé 3 places", "ville": "Paris, 75011","details": "Très bon état, peu utilisé."},
    {"name":"Micheal","image": "https://picsum.photos/500/300?2", "prix": "8 500 €", "titre": "Peugeot 208 2019", "ville": "Lyon, 69003","details": "45 000 km, révision faite."},
    {"name":"Paul","image": "https://picsum.photos/500/300?3", "prix": "320 €", "titre": "iPhone 11 64Go", "ville": "Bordeaux, 33000","details": "45 000 km, révision faite."},
    {"name":"Marcus","image": "https://picsum.photos/203/203", "prix": "900 €", "titre": "iPhone 15", "ville": "Bordeaux","details": "45 000 km, révision faite."},
    {"name":"Emmanuel","image": "https://picsum.photos/500/300?4", "prix": "120 €", "titre": "Table en bois", "ville": "Nantes, 44000","details": "45 000 km, révision faite."},
    {"name":"Simpson","image": "https://picsum.photos/500/300?6", "prix": "120 €", "titre": "Table en bois", "ville": "Nantes, 44000","details": "45 000 km, révision faite."},
    ]
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
    def page_detail(name,image_url, prix, titre, ville, details):

        def retour(e):
            contenu.content = page_accueil()
            page.update()
        header = ft.Container(
        padding=15,
        content=ft.Row(
            [
                ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=retour),
                ft.Text(
                    "Détails de l’annonce",
                    expand=True,
                    text_align=ft.TextAlign.CENTER,
                    size=22,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Icon(ft.Icons.SHARE_OUTLINED, size=28),
                ft.Icon(ft.Icons.FAVORITE_BORDER, size=28),
            ]
        ),
    )
        image_section = ft.Stack(
        [
            ft.Image(
                src=image_url,
                width=float("inf"),
                height=370,
                fit="cover",
            ),
            ft.Container(
                bottom=15,
                right=15,
                bgcolor="#00000099",
                border_radius=8,
                padding=8,
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.PHOTO_CAMERA, color="white", size=18),
                        ft.Text("1/5", color="white"),
                    ],
                    tight=True,
                ),
            ),
        ]
        )
        detaills = ft.Container(
        padding=20,
        content=ft.Column(
            [
                ft.Text(
                    titre,
                    size=26,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    prix,
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#1565C0",
                ),

                ft.Row(
                    [
                        ft.Icon(ft.Icons.ACCESS_TIME, size=18, color="grey"),
                        ft.Text("Publiée il y a 2 jours", color="grey"),

                        ft.Container(width=20),

                        ft.Icon(ft.Icons.LOCATION_ON_OUTLINED,
                                size=18,
                                color="grey"),
                        ft.Text(ville, color="grey"),
                    ]
                ),

                ft.Divider(),

                ft.Text(
                    "Description",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    details,
                    size=16,
                ),

                ft.Divider(height=30),

                ft.Text(
                    "Contacter l'annonceur",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Row(
                    [
                        ft.CircleAvatar(
                            radius=25,
                            content=ft.Icon(ft.Icons.PERSON),
                        ),

                        ft.Column(
                            [
                                ft.Text(
                                    name,
                                    weight=ft.FontWeight.BOLD,
                                    size=18,
                                ),
                                ft.Text(
                                    "Membre depuis mars 2022",
                                    color="grey",
                                ),
                            ],
                            spacing=2,
                            expand=True,
                        ),

                        ft.ElevatedButton(
                            "Écrire",
                            icon=ft.Icons.CHAT_BUBBLE_OUTLINE,
                            style=ft.ButtonStyle(
                                bgcolor="#1565C0",
                                color="white",
                            ),
                            height=50,
                            width=150,
                        ),
                    ]
                ),

                ft.Container(height=15),

                ft.ElevatedButton(
                    "Appeler",
                    icon=ft.Icons.CALL,
                    style=ft.ButtonStyle(
                        bgcolor="#16A34A",
                        color="white",
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    width=float("inf"),
                    height=55,
                ),
            ],
            spacing=12,
        ),
        )
        contenu.content = ft.Column(
            [
                header,
                image_section,
                detaills,
            ],
            spacing=0,
        )
        page.update()
    # Cartes annonces
    def create_card(name,image_url, prix, titre, ville,details):
        return ft.Card(
        content=ft.Container(
            on_click=lambda e: page_detail(
                name,
                image_url,
                prix,
                titre,
                ville,
                details,
            ),
            #on_click=lambda e: print(f"Action pour {titre}"),
            padding=0,
        content=ft.Column(
                spacing=0,
                controls=[
                    ft.Stack(
                        controls=[
                            ft.Image(
                                src=image_url,
                                height=170,
                                width=250,
                                fit="cover",
                                border_radius=10,
                            ),

                            ft.Container(
                                top=10,
                                right=10,
                                width=35,
                                height=35,
                                bgcolor="white",
                                border_radius=20,
                                alignment=ft.Alignment.CENTER,
                                content=ft.Icon(
                                    ft.Icons.FAVORITE_BORDER,
                                    color="#B05A6E",
                                ),
                            ),
                        ]
                    ),

                    ft.Container(
                        padding=15,
                        content=ft.Column(
                            spacing=5,
                            controls=[
                                ft.Text(
                                    prix,
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    titre,
                                    size=16,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.LOCATION_ON_OUTLINED,
                                            size=16,
                                            color="grey",
                                        ),
                                        ft.Text(
                                            ville,
                                            color="grey",
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ),
                ],
            )
    )
        )

    annonces = ft.GridView(
        runs_count=2,
        child_aspect_ratio=0.56,
        padding=6,
        expand=True,
        controls=[
        create_card(item["name"],item["image"], item["prix"], item["titre"], item["ville"],item["details"]) 
        for item in annonces_data
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
