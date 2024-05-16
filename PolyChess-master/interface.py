import pygame
import sys

class Case:
    def __init__(self, couleur, position):
        self.couleur = couleur
        self.position = position

class Piece:
    def __init__(self, couleur, image, position):
        self.couleur = couleur
        self.image = image
        self.position = position

class Plateau:
    def __init__(self, taille_case):
        self.taille_case = taille_case
        self.cases = []
        self.initialiser_cases()

    def initialiser_cases(self):
        BLANCHE = (205, 72, 44)
        NOIR = (46, 46, 46)
        for i in range(8):
            for j in range(8):
                couleur_case = BLANCHE if (i + j) % 2 == 0 else NOIR
                self.cases.append(Case(couleur_case, (i, j)))

class JeuEchecs:
    def __init__(self):
        pygame.init()
        self.taille_fenetre = (560, 560)
        self.fenetre = pygame.display.set_mode(self.taille_fenetre)
        pygame.display.set_caption('Échecs')
        self.pieces_capturees = []

        self.plateau = Plateau(70)
        self.charger_images_pieces()

        self.piece_selectionnee = None
        self.position_clic_precedent = None

    def charger_images_pieces(self):
        self.images_pieces = {}
        for piece in ['Pion', 'Reine', 'Cavalier', 'Fou', 'Tour', 'Roi']:
            self.images_pieces[piece + '_blanche'] = pygame.image.load(f'PolyChess-master/Screenshots/{piece}_blanche.png')
            self.images_pieces[piece + '_noir'] = pygame.image.load(f'PolyChess-master/Screenshots/{piece}_noir.png')

    def dessiner_plateau(self):
        for case in self.plateau.cases:
            pygame.draw.rect(self.fenetre, case.couleur, (case.position[0]*self.plateau.taille_case, case.position[1]*self.plateau.taille_case, self.plateau.taille_case, self.plateau.taille_case))

    def dessiner_pieces(self, positions_pieces):
        for position, piece in positions_pieces.items():
            x, y = position
            image = self.images_pieces[piece]
            self.fenetre.blit(image, (x*self.plateau.taille_case, y*self.plateau.taille_case))

    def bouger_piece(self, position_clic, positions_pieces):
        if self.piece_selectionnee:
            if position_clic in positions_pieces:
                self.pieces_capturees.append(positions_pieces[position_clic])
                del positions_pieces[position_clic]
            positions_pieces[position_clic] = self.piece_selectionnee
            del positions_pieces[self.position_clic_precedent]
            self.piece_selectionnee = None
            self.position_clic_precedent = None
        else:
            if position_clic in positions_pieces:
                self.piece_selectionnee = positions_pieces[position_clic]
                self.position_clic_precedent = position_clic

    def jouer(self):
        BLANCHE = (205, 72, 44)
        NOIR = (46, 46, 46)
        positions_pieces = {
            (0, 0): 'Tour_blanche',
            (1, 0): 'Cavalier_blanche',
            (2, 0): 'Fou_blanche',
            (3, 0): 'Roi_blanche',
            (4, 0): 'Reine_blanche',
            (5, 0): 'Fou_blanche',
            (6, 0): 'Cavalier_blanche',
            (7, 0): 'Tour_blanche',
            (0, 1): 'Pion_blanche',
            (1, 1): 'Pion_blanche',
            (2, 1): 'Pion_blanche',
            (3, 1): 'Pion_blanche',
            (4, 1): 'Pion_blanche',
            (5, 1): 'Pion_blanche',
            (6, 1): 'Pion_blanche',
            (7, 1): 'Pion_blanche',

            (0, 7): 'Tour_noir',
            (1, 7): 'Cavalier_noir',
            (2, 7): 'Fou_noir',
            (3, 7): 'Roi_noir',
            (4, 7): 'Reine_noir',
            (5, 7): 'Fou_noir',
            (6, 7): 'Cavalier_noir',
            (7, 7): 'Tour_noir',
            (0, 6): 'Pion_noir',
            (1, 6): 'Pion_noir',
            (2, 6): 'Pion_noir',
            (3, 6): 'Pion_noir',
            (4, 6): 'Pion_noir',
            (5, 6): 'Pion_noir',
            (6, 6): 'Pion_noir',
            (7, 6): 'Pion_noir',
        }

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    colonne = x // self.plateau.taille_case
                    ligne = y // self.plateau.taille_case
                    position_clic = (colonne, ligne)
                    self.bouger_piece(position_clic, positions_pieces)

            self.fenetre.fill(BLANCHE)
            self.dessiner_plateau()
            self.dessiner_pieces(positions_pieces)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    jeu = JeuEchecs()
    jeu.jouer()

