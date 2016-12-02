__author__ = 'dustinlee'


from pico2d import *

def test_font():
    open_canvas()
    font = load_font('ConsolaMalgun.TTF', 40)
    font.draw(20, 50, "정말 ABC 이대현")
    update_canvas()
    delay(1)
    close_canvas()

def test_rotate():
    image = load_image('character.png')
    for i in range(628):
        rad = i / 100
        clear_canvas()
        image.rotate_draw(rad, 100, 200)
        update_canvas()
        delay(0.01)
    delay(1)

def test_flip():
    image = load_image('character.png')
    for i in range(314):
        rad = i*2 / 100
        clear_canvas()
        image.composite_draw(rad, 'hv', 100, 200)
        update_canvas()
        delay(0.01)
    delay(1)


def test_draw():
    open_canvas()
    test_flip()
    close_canvas()


if __name__ == "__main__":
    test_draw()