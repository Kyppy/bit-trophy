# Generated by Django 2.1.7 on 2019-03-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_auto_20190320_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='genre',
            field=models.CharField(choices=[('Platformer', 'Platformer'), ('First-person shooter', 'First-person shooter'), ('Looter-shooter', 'Looter-shooter'), ('Fighting', 'Fighting'), ('Stealth', 'Stealth'), ('Survival', 'Survival'), ('Rhythm', 'Rhythm'), ('Survival horror', 'Survival horror'), ('Visual novel', 'Visual novel'), ('Adventure', 'Adventure'), ('Text adventure', 'Text adventure'), ('Role-playing', 'Role-playing'), ('Action RPG', 'Action RPG'), ('MMORPG', 'MMORPG'), ('Simulator', 'Simulator'), ('Strategy', 'Strategy'), ('Sports', 'Sports')], help_text='Select the game genre.', max_length=30),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='platform',
            field=models.CharField(choices=[('PS4', 'PS4'), ('Xbox One', 'Xbox One'), ('Nintendo Switch', 'Nintendo Switch'), ('PC', 'PC'), ('Wii U', 'Wii U'), ('PS3', 'PS3'), ('Xbox 360', 'Xbox 360'), ('Wii', 'Wii'), ('Nintendo 3DS', 'Nintendo 3DS'), ('Playstation Vita', 'Playstation Vita'), ('Nintendo DS', 'Nintendo DS'), ('Playstation Portable', 'Playstation Portable'), ('PS2', 'PS2'), ('Xbox', 'Xbox'), ('Gamecube', 'Gamecube'), ('Gameboy Advance', 'Gameboy Advance'), ('Playstation', 'Playstation'), ('Nintendo 64', 'Nintendo 64'), ('Gameboy', 'Gameboy')], help_text='Select the console that you play the game on.', max_length=30),
        ),
    ]