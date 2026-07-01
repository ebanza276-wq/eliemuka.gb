import flet as ft


def main(page: ft.Page):
    page.title = "ACTUALITÉ DU MONDE"
    page.bgcolor = ft.Colors.BLACK
    page.theme_mode = ft.ThemeMode.DARK

    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False
    page.window.center()

    page.padding = 0
    page.spacing = 0
    states = {"explore_tab": "Tous"}

    produits = [
        {"image": "https://picsum.photos/400?1", "titre": "iPhone 13 Pro 256 Go", "prix": "650 €", "ville": "Paris"},
        {"image": "https://picsum.photos/400?2", "titre": "MacBook Air M2", "prix": "980 €", "ville": "Lyon"},
        {"image": "https://picsum.photos/400?3", "titre": "PlayStation 5", "prix": "420 €", "ville": "Marseille"},
        {"image": "https://picsum.photos/400?4", "titre": "Canapé moderne", "prix": "300 €", "ville": "Bordeaux"},
        {"image": "https://picsum.photos/400?5", "titre": "Samsung Galaxy S24", "prix": "720 €", "ville": "Nice"},
        {"image": "https://picsum.photos/400?6", "titre": "Vélo électrique", "prix": "850 €", "ville": "Lille"},
    ]

    produits_filtrés = produits.copy()
    search_value = ""

    # ---------------- CARTES ----------------
    def carte_produit(item):
        return ft.Container(
            bgcolor="#1c1c1c",
            border_radius=10,
            padding=5,
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Image(
                        src=item["image"],
                        height=190,
                        width=float("inf"),
                        fit="cover",
                        border_radius=10,
                    ),
                    ft.Text(item["titre"], size=14, weight=ft.FontWeight.BOLD, color="white", max_lines=2),
                    ft.Text(item["prix"], color="lime", weight=ft.FontWeight.BOLD),
                    ft.Text(item["ville"], color="grey", size=12),
                ],
            ),
        )

    # ---------------- GRILLE (IMPORTANTE : UNE SEULE FOIS) ----------------
    grille = ft.GridView(
        expand=True,
        runs_count=2,
        max_extent=180,
        spacing=8,
        run_spacing=8,
        child_aspect_ratio=0.68,
        controls=[carte_produit(p) for p in produits_filtrés],
    )
    
    def build_explore_tabs(states):
        def set_tab(tab_name):
            states["explore_tab"] = tab_name
            contenu.content = page_accueil(states)
            page.update()

        return ft.Container(
        padding=ft.Padding.only(top=15, bottom=15, left=10, right=10),
        bgcolor="#000000",
        content=ft.Row(
            controls=[
                ft.TextButton(
                    "Tous",
                    on_click=lambda e: set_tab("Tous"),
                ),
                ft.TextButton(
                    "Voiture",
                    on_click=lambda e: set_tab("Voiture"),
                ),
                ft.TextButton(
                    "Immobilier",
                    on_click=lambda e: set_tab("Immobilier"),
                ),
            ]
        ),
    )
    # ---------------- FILTRE (SANS REBUILD PAGE) ----------------
    def filtrer(e):
        nonlocal produits_filtrés, search_value

        search_value = e.control.value.lower()

        produits_filtrés = [
            p for p in produits
            if search_value in p["titre"].lower()
            or search_value in p["ville"].lower()
            or search_value in p["prix"].lower()
        ]

        # update seulement la grille (PAS la page entière)
        grille.controls = [carte_produit(p) for p in produits_filtrés]
        page.update()
    def page_resultat(data):
        return ft.Container(
        expand=True,
        alignment=ft.Alignment.TOP_CENTER,
        content=data,
    )
    def page_voiture():
        return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        content=ft.Text("Page Voiture", size=30, color="white"),
    )

    def page_immobilier():
        return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        content=ft.Text("Page Immobilier", size=30, color="white"),
    )
    # ---------------- HOME ----------------
    def page_accueil(states):
        if states["explore_tab"] == "Tous":
            resultat = page_resultat(grille)
        elif states["explore_tab"] == "Voiture":
            resultat = page_voiture()
        elif states["explore_tab"] == "Immobilier":
            resultat = page_immobilier()
        return ft.Column(
        expand=True,
        spacing=0,
        controls=[
            ft.Container(
                bgcolor="#121212",
                padding=10,
                content=ft.Text(
                    "AFROCOMMERCE",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
            ),

            ft.Container(
                padding=10,
                content=ft.TextField(
                    hint_text="Rechercher un produit...",
                    prefix_icon=ft.Icons.SEARCH,
                    border_radius=20,
                    filled=True,
                    on_change=filtrer,
                    value=search_value,
                ),
            ),

            build_explore_tabs(states),

            resultat,
        ],
    )

    # ---------------- NAVIGATION ----------------
    contenu = ft.Container(expand=True)
    selected_index = 0

    def set_index(i):
        nonlocal selected_index
        selected_index = i

        if selected_index == 0:
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
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Accueil"),
            ft.NavigationBarDestination(icon=ft.Icons.FAVORITE_BORDER, label="Explorer"),
            ft.NavigationBarDestination(icon=ft.Icons.CHAT_BUBBLE, label="Message"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON_OUTLINE, label="Profil"),
        ],
    )

    # init
    contenu.content = page_accueil(states)
    page.add(contenu)


ft.app(target=main)
