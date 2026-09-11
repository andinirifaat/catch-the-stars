import pygame
import random

pygame.init()

# VARIABLES: menyimpan setting dan data game.
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Stars")
clock = pygame.time.Clock()

player = pygame.Rect(350, 520, 100, 30)
speed = 7
stars = []                 # LIST: menyimpan semua bintang -> diisi oleh function new_star().
score, lives = 0, 3
game_over = False

font = pygame.font.Font(None, 40)
big_font = pygame.font.Font(None, 70)


# FUNCTION: membuat satu bintang baru.
def new_star():
    return {
        "x": random.randint(15, WIDTH - 15),
        "y": -15,
        "speed": random.randint(3, 6)
    }


# FUNCTION: mengembalikan game ke kondisi awal.
def reset_game():
    global score, lives, game_over, stars
    player.x = WIDTH // 2 - player.width // 2
    score, lives, game_over = 0, 3, False
    stars = [new_star()]


# FUNCTION: menggambar bintang.
def draw_star(star):
    pygame.draw.circle(
        screen, "yellow", (star["x"], star["y"]), 12
    )


reset_game()
running = True

# LOOP: game terus berjalan selama running = True.
while running:
    clock.tick(60)

    # LOOP: mengecek tindakan dari pemain.
    for event in pygame.event.get():

        # CONDITIONAL: jika pemain menutup window.
        if event.type == pygame.QUIT:
            running = False

        # CONDITIONAL: jika pemain menekan keyboard.
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if game_over and event.key == pygame.K_r:
                reset_game()

    # CONDITIONAL: game hanya bergerak jika belum selesai.
    if not game_over:

        keys = pygame.key.get_pressed()

        # CONDITIONAL: tombol kiri → pemain bergerak ke kiri.
        if keys[pygame.K_LEFT]:
            player.x -= speed

        # CONDITIONAL: tombol kanan → pemain bergerak ke kanan.
        if keys[pygame.K_RIGHT]:
            player.x += speed

        # Membatasi pemain agar tidak keluar layar.
        player.x = max(0, min(player.x, WIDTH - player.width))

        # LOOP: memeriksa setiap bintang di dalam LIST.
        for star in stars[:]:

            star["y"] += star["speed"]

            # Membuat area untuk mengecek tabrakan.
            star_rect = pygame.Rect(
                star["x"] - 12,
                star["y"] - 12,
                24,
                24
            )

            # CONDITIONAL: jika pemain menyentuh bintang.
            if player.colliderect(star_rect):
                score += 1
                stars.remove(star)

            # CONDITIONAL: jika bintang terlewat.
            elif star["y"] > HEIGHT:
                lives -= 1
                stars.remove(star)

        # CONDITIONAL: buat bintang baru jika tidak ada bintang.
        if not stars:
            stars.append(new_star())

        # CONDITIONAL: jika nyawa habis → Game Over.
        if lives <= 0:
            game_over = True

    # DRAW: menggambar kondisi game saat ini.
    screen.fill((20, 25, 60))
    pygame.draw.rect(screen, (70, 140, 200), player)

    # LOOP: menggambar setiap bintang.
    for star in stars:
        draw_star(star)

    screen.blit(
        font.render(f"Score: {score}", True, "white"),
        (20, 20)
    )
    screen.blit(
        font.render(f"Lives: {lives}", True, "white"),
        (680, 20)
    )

    # CONDITIONAL: tampilkan pesan jika game selesai.
    if game_over:
        title = big_font.render("GAME OVER", True, "white")
        msg = font.render("Press R to play again", True, "white")

        screen.blit(
            title, title.get_rect(center=(400, 250))
        )
        screen.blit(
            msg, msg.get_rect(center=(400, 320))
        )

    pygame.display.flip()

pygame.quit()

