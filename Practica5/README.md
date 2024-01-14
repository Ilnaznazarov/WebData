Практика 5. Сбор аудио- и видеоданных
Написать функцию, которая принимает на вход список URL, выгружает по заданным URL весь видеоконтент, найденный по этому адресу, вместе с метаданными и сохраняет его в отдельную папку, названную по URL.

Какая сложность может быть:

Видео может быть многочастным (в формате .m3u8-плейлиста) — нужно разобрать плейлист и скачать каждую из частей видео, а потом склеить
Адрес прямого видеофайла может быть скрыт — для этого можно воспользоваться специализированными средствами, например, youtube-dl GitHub - ytdl-org/youtube-dl: Command-line program to download videos from YouTube.com and other video sites youtube_dl · PyPI
Метаданные к видео могут быть разбросаны по странице — в этом случае стоит предполагать, что адрес содержит только 1 видео и пытаться извлекать их из title, description и т.п.
Какие сайты можно пробовать парсить:

[Imgur: The magic of the Internet] [rBxB9ih.mp4](например How to wake up at 5am every day - GIF - Imgur -> https://i.imgur.com/rBxB9ih.mp4)
Reddit (например, https://packaged-media.redd.it/9kr7fm5k16eb1/pb/m2-res_480p.mp4?m=DASHPlaylist.mpd&v=1&e=1690448400&s=a56139280f0853d7bf356fe10e02cf0da081ba56#t=0)
YouTube
GIPHY - Be Animated
https://tenor.com/
TikTok*
RuTube*
Twitch*
Vimeo*
