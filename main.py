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
    # Liste des annonces
    annonces_data = [
    {"name":"Marc","image": "https://picsum.photos/500/300?1", "prix": "250 €", "titre": "Canapé 3 places", "ville": "Paris, 75011","details": "Très bon état, peu utilisé.","numero":"+243831234567"},
    {"name":"Micheal","image": "https://picsum.photos/500/300?2", "prix": "8 500 €", "titre": "Peugeot 208 2019", "ville": "Lyon, 69003","details": "45 000 km, révision faite.","numero":"+243831234599"},
    {"name":"Paul","image": "https://picsum.photos/500/300?3", "prix": "320 €", "titre": "iPhone 11 64Go", "ville": "Bordeaux, 33000","details": "45 000 km, révision faite.","numero":"+233831734567"},
    {"name":"Marcus","image": "https://picsum.photos/203/203", "prix": "900 €", "titre": "iPhone 15", "ville": "Bordeaux","details": "45 000 km, révision faite.","numero":"+243831234567"},
    {"name":"Emmanuel","image": "https://picsum.photos/500/300?4", "prix": "120 €", "titre": "Table en bois", "ville": "Nantes, 44000","details": "45 000 km, révision faite.","numero":"+243831234567"},
    {"name":"Simpson","image": "https://picsum.photos/500/300?6", "prix": "120 €", "titre": "Table en bois", "ville": "Nantes, 44000","details": "45 000 km, révision faite.","numero":"+223831234967"},
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
    async def appeler(e, numero):
        await page.launch_url(f"tel:{numero}")
    def page_detail(name,image_url, prix, titre, ville, details,numero):

        def retour(e):
            contenu.content = page_accueil()
            page.update()
        
        image_section = ft.Stack(
    [
        # Image principale (placée en premier dans le Stack pour être en arrière-plan)
        ft.Image(
            src=image_url,
            width=float("inf"),
            height=370,
            fit="cover",
        ),
        # Bouton Retour
        ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color="white",
            top=40,
            left=20,
            bgcolor=ft.Colors.with_opacity(0.4, "black"),
            on_click=retour
        ),
        # Bouton Favoris
        ft.IconButton(
            icon=ft.Icons.FAVORITE_BORDER,
            icon_color="white",
            top=40,
            right=20,
            bgcolor=ft.Colors.with_opacity(0.4, "black")
        ),
        # Indicateur de compteur (1/5)
        ft.Container(
            bottom=15,
            right=15,
            bgcolor=ft.Colors.with_opacity(0.6, "black"), # Utilisation de with_opacity
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
                    on_click=lambda e: page.run_task(appeler, e, numero),
                ),
            ],
            spacing=12,
        ),
        )
        contenu.content = ft.Column(
            [
                
                image_section,
                detaills,
            ],
            spacing=0,
        )
        page.update()
    # Cartes annonces
    def create_card(name,image_url, prix, titre, ville,details,numero):
        return ft.Card(
        content=ft.Container(
            on_click=lambda e: page_detail(
                name,
                image_url,
                prix,
                titre,
                ville,
                details,
                numero
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
        create_card(item["name"],item["image"], item["prix"], item["titre"], item["ville"],item["details"],item["numero"]) 
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
    
    def page_publie():
        return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        spacing=15,
        controls=[
            ft.Container(
                padding=20,
                content=ft.Column(
                    [
                        ft.Text(
                            "Publier une annonce",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Remplissez les informations ci-dessous pour publier votre annonce.",
                            color=ft.Colors.GREY,
                        ),
                    ]
                ),
            ),

            # Photos
            ft.Container(
                width=900,
                margin=10,
                padding=20,
                border=ft.Border.all(2, "#2A2A2A"),
                border_radius=20,
                bgcolor="#1E1E1E",
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            ft.Icons.ADD_PHOTO_ALTERNATE_OUTLINED,
                            size=60,
                            color="#6200EE",
                        ),
                        ft.Text(
                            "Ajouter des photos",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Ajoutez jusqu'à 10 photos de qualité",
                            color=ft.Colors.GREY,
                        ),
                        ft.ElevatedButton(
                            "Choisir des images",
                        ),
                    ],
                ),
            ),

            # Informations générales
            ft.Container(
                width=900,
                margin=10,
                padding=20,
                border_radius=20,
                bgcolor="#1E1E1E",
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Informations générales",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.TextField(
                            label="Titre de l'annonce",
                            hint_text="Ex: iPhone 15 Pro Max 256 Go",
                            prefix_icon=ft.Icons.TITLE,
                            border_radius=12,
                        ),

                        ft.TextField(
                            label="Prix",
                            prefix_icon=ft.Icons.EURO,
                            keyboard_type=ft.KeyboardType.NUMBER,
                            border_radius=12,
                        ),

                        ft.Dropdown(
                            label="Catégorie",
                            border_radius=12,
                            options=[
                                ft.dropdown.Option("Immobilier"),
                                ft.dropdown.Option("Véhicules"),
                                ft.dropdown.Option("Téléphones"),
                                ft.dropdown.Option("Informatique"),
                                ft.dropdown.Option("Mode"),
                                ft.dropdown.Option("Services"),
                                ft.dropdown.Option("Autres"),
                            ],
                        ),

                        ft.TextField(
                            label="Ville",
                            prefix_icon=ft.Icons.LOCATION_ON_OUTLINED,
                            border_radius=12,
                        ),
                    ],
                ),
            ),

            # Description
            ft.Container(
                width=900,
                margin=10,
                padding=20,
                border_radius=20,
                bgcolor="#1E1E1E",
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Description",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.TextField(
                            multiline=True,
                            min_lines=6,
                            max_lines=10,
                            hint_text="Décrivez votre article en détail...",
                            border_radius=12,
                        ),
                    ],
                ),
            ),

            # Conseils
            ft.Container(
                margin=10,
                padding=15,
                border_radius=15,
                bgcolor="#0D47A1",
                content=ft.Row(
                    [
                        ft.Icon(
                            ft.Icons.LIGHTBULB_OUTLINE,
                            color="white",
                        ),
                        ft.Text(
                            "Ajoutez plusieurs photos et une description détaillée pour vendre plus rapidement.",
                            color="white",
                            expand=True,
                        ),
                    ]
                ),
            ),

        ],
    )
    def page_profil():
        return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        controls=[
            # Header profil
            ft.Container(
                padding=20,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.CircleAvatar(
                            radius=55,
                            foreground_image_src="https://picsum.photos/200",
                        ),
                        ft.Text(
                            "Elie Banza",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Membre depuis 2026",
                            color=ft.Colors.GREY,
                        ),
                    ],
                ),
            ),

            # Statistiques
            ft.Container(
                margin=10,
                padding=20,
                bgcolor="#1E1E1E",
                border_radius=20,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "12",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text("Annonces"),
                            ],
                        ),
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "48",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text("Favoris"),
                            ],
                        ),
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "4.8",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text("Note"),
                            ],
                        ),
                    ],
                ),
            ),

            # Boutons rapides
            ft.Container(
                margin=10,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton(
                            "Modifier le profil",
                            icon=ft.Icons.EDIT,
                        ),
                        ft.OutlinedButton(
                            "Partager",
                            icon=ft.Icons.SHARE,
                        ),
                    ],
                ),
            ),

            # Menu
            ft.Container(
                margin=10,
                padding=15,
                bgcolor="#1E1E1E",
                border_radius=20,
                content=ft.Column(
                    spacing=5,
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.LIST_ALT),
                            title=ft.Text("Mes annonces"),
                            trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT),
                        ),
                        ft.Divider(),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.FAVORITE_BORDER),
                            title=ft.Text("Mes favoris"),
                            trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT),
                        ),
                        ft.Divider(),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.CHAT_OUTLINED),
                            title=ft.Text("Mes messages"),
                            trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT),
                        ),
                        ft.Divider(),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.NOTIFICATIONS_OUTLINED),
                            title=ft.Text("Notifications"),
                            trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT),
                        ),
                        ft.Divider(),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.SETTINGS_OUTLINED),
                            title=ft.Text("Paramètres"),
                            trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT),
                        ),
                    ],
                ),
            ),

            # Déconnexion
            ft.Container(
                margin=10,
                content=ft.ElevatedButton(
                    "Déconnexion",
                    icon=ft.Icons.LOGOUT,
                    bgcolor="#D32F2F",
                    color="white",
                    width=float("inf"),
                    height=50,
                ),
            ),
        ],
    )
    contenu = ft.Container(expand=True)

    def set_index(i):
        if i == 0:
            contenu.content = page_accueil()
        elif i == 2:
            contenu.content = page_publie()
        elif i == 4:
            contenu.content = page_profil()
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
                icon=ft.Icons.FAVORITE,
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
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON,
                label="Profil",
            ),
        ],
    )
    
    contenu.content = page_accueil()
    page.add(contenu)

ft.app(target=main)#, view="web_browser")
