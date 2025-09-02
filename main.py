# import dari modul image
import game.image.open
import game.image.close
import game.image.change

print(game.image.open.buka_gambar())
print(game.image.close.tutup_gambar())
print(game.image.change.ubah_gambar())


# import dari modul level
import game.level.load
import game.level.over
import game.level.start

print(game.level.load.muat_level())
print(game.level.over.game_over())
print(game.level.start.mulai_level())


# import dari modul game
import game.sound.load
import game.sound.pause
import game.sound.play

print(game.sound.load.muat_suara())
print(game.sound.pause.jeda_suara())
print(game.sound.play.putar_suara())

#----
import game.image
import game.level
import game.sound