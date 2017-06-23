# UbicaBot - [HackForGood 2017](http://hackforgood.net)
*Scroll down to [English Version](#english-version) for the English README.*
>Chatbot desarrollado durante la [HackForGood 2017](https://hackforgood.net/premios-hackforgood-globales-2017/). Muchas gracias a [LUCA](https://www.luca-d3.com/) por galardonar este proyecto con su 3er premio! :trophy:

__Bot de Telegram que informa de la cantidad de turistas en los municipios de Colombia.__
Dado un municipio colombiano, UbicaBot ofrece el número de personas que han estado en dicho municipio junto con un análisis: si hay más o menos gente respecto la media de los dos meses anteriores (dado un dataset con las fechas determinadas).
Pruébalo! Abre a `@ubica_bot` en [Telegram](http://telegram.me/ubica_bot).

__El bot no está en funcionamiento 24/7. Puedes hablar con él, pero puede no contestar al momento.__
## Cómo está hecho?
Con Python y SQLite3. El bot busca en los datasets de LUCA el número de personas que han visitado el municipio seleccionado.
## Ejemplos de funcionamento
![screenshot1](http://ignasioliver.com/public/screenshotsubicabot.png)
## Puedo usarlo?
Sí. Para ello sigue los siguientes pasos:

1. [Crea un bot de Telegram](https://core.telegram.org/bots). Ten el token que BotFather te da a mano.

2. Importa (o [fork](https://help.github.com/articles/fork-a-repo/)) este repositorio (bajo ninguna condición, siguiendo la [UNLICENSE](https://github.com/ignasioliver/UbicaBot/blob/master/UNLICENSE)).

3. En la línea 18 de `CO_ids_nombres.csv`, cambia `insertTokenHere` por el token dado por BotFather.

4. Añade los datasets. Los usados por `@ubica_bot` no se encuentran en este repositorio puesto que son confidenciales y propiedad de LUCA. Sin embargo, puedes crearlos tú mismo dada la immensa cantidad de datos disponibles en Internet al respecto. Por ejemplo, puedes encontrar información de ciudades de [Estados Unidos](https://catalog.data.gov/dataset?res_format=CSV) y [Colombia](https://data.humdata.org/group/col). Una vez descargados debes modificarlos puesto que deben seguir la estructura que se puede observar en los siguientes ejemplos:

Referente a `CO_ids_nombres.csv`, que contiene la identificación de los municipios con su respectivo departamento:
  ```
  id_mpio;  nombre_mpio;    id_dpto;    nombre_dpto
  1083;     EL ENCANTO;     91;         AMAZONAS
  1081;     LA CHORRERA;    91;         AMAZONAS
  1082;     LA PEDRERA;     91;         AMAZONAS
  ...
  ```
  Referente a `hack4good_dwells.csv`, que contiene el número de habitantes de un municipio (`dwells`) y de personas que se encuentran en la respectiva fecha (`people`):
  ```
  date_dt,     cod_dpto,  cod_mpio,  dwells,  people
  2017-01-06,  5,         151,       753,     437
  2017-02-06,  5,         159,       821,     229
  2017-03-06,  5,         164,       132,     1129
  ...
  ```
5. Ejecuta `ubica_bot.py` (en Python). Si deseas que el funcionamento del bot no dependa de tu conexión a Internet ni de tu sistema local, puedes desplegar el proyecto a sevicios como [Heroku](https://www.heroku.com/) o [DigitalOcean](https://www.digitalocean.com/).

6. Busca en Telegram el nombre del chatbot que escogiste al principio. Si al abrir el chat no dice nada, escribe `/start` y diviértete!

Dado que el proyecto se desarrolló durante una hackathon, el código no está suficientemente bien documentado para producción. Si hay cualquier duda puedes contactar conmigo a través del email `ignasi@ignasioliver.com`.

O bien si deseas probar el bot con los datos originales, envíame un correo y me aseguraré de activarlo.

## Otros
[Presentación](https://docs.google.com/presentation/d/1sVjwLXz6nrE1H2lDqJSlNI_CAeD6x7pREMocrnkKtTs/edit#slide=id.g1d1e834f47_0_0) del proyecto en la hackathon y [vídeo](https://www.youtube.com/watch?v=HnY0G-zhQIc&t=45s).
## Autor
[Ignasi Oliver](http://www.ignasioliver.com/).

<hr>

# English Version
# UbicaBot - [HackForGood 2017](http://hackforgood.net)
>Chatbot developed at [HackForGood 2017](https://hackforgood.net/premios-hackforgood-globales-2017/). Thanks to [LUCA](https://www.luca-d3.com/) to award this project with their 3rd prize! :trophy:

__Telegram bot that informs the amount of current tourists in any city of Colombia.__
Given a Colombian town, UbicaBot offers the number of people who have been there along with an analysis: if there are more or less people regarding the mean of the previous two months -given a dataset with the specified dates.
Test it! Chat with `@ubica_bot` on [Telegram](http://telegram.me/ubica_bot).

__The bot is not running 24/7. You can chat with it anytime, but it may not respond at the moment.__
## How is it done?
With Python and SQLite3. It searches on the LUCA datasets the number of people in the selected city.
## Usage examples
![screenshot1](http://ignasioliver.com/public/screenshotsubicabot.png)
## Can I use it?
Yes. Follow the steps:

1. [Create a Telegram bot](https://core.telegram.org/bots). Have the token that BotFather gives you handy.

2. Import (or [fork](https://help.github.com/articles/fork-a-repo/)) this repo - without conditions, following the [UNLICENSE](https://github.com/ignasioliver/UbicaBot/blob/master/UNLICENSE).

3. On line 18 of `CO_ids_nombres.csv`, change `insertTokenHere` to the token given by BotFather.

4. Add the datasets. The ones used by `@ubica_bot` are not in this repo since they are classified and property of LUCA. Nonetheless, you can create them given all the publicly available data on the Internet. For example, you can find info from cities of the [USA](https://catalog.data.gov/dataset?res_format=CSV) and [Colombia](https://data.humdata.org/group/col). Once downloaded the datasets should be modified in order to achieve the structure shown in the following examples:

Regarding `CO_ids_nombres.csv`, which links the cities (`nombre_mpio`) and cities IDs (`id_mpio`) with their respective government department (`nombre_dpto`) and government department IDs (`id_dpto`):
  ```
  id_mpio;  nombre_mpio;    id_dpto;    nombre_dpto
  1083;     EL ENCANTO;     91;         AMAZONAS
  1081;     LA CHORRERA;    91;         AMAZONAS
  1082;     LA PEDRERA;     91;         AMAZONAS
  ...
  ```
  Regarding `hack4good_dwells.csv`, which contains the number of inhabitants of a city (`dwells`) and the number of people currently in that same city (`people`):
  ```
  date_dt,     cod_dpto,  cod_mpio,  dwells,  people
  2017-01-06,  5,         151,       753,     437
  2017-02-06,  5,         159,       821,     229
  2017-03-06,  5,         164,       132,     1129
  ...
  ```
5. Run `ubica_bot.py`. If you want to make it run independently from your computer you can deploy your project to services such as [Heroku](https://www.heroku.com/) or [DigitalOcean](https://www.digitalocean.com/).

6. Search on Telegram for the bot name you chose earlier. If it doesn't text anything, text `/start` and have fun!

Considering that the project was developed in a hackathon, the code is not well enough documented for production. If any question arises, I am available at `ignasi@ignasioliver.com`.

Also, contact me if you would like to see the bot running with the original data and I will make sure it does.
## Others
[Presentation](https://docs.google.com/presentation/d/1sVjwLXz6nrE1H2lDqJSlNI_CAeD6x7pREMocrnkKtTs/edit#slide=id.g1d1e834f47_0_0) of the project for the hackathon and [video](https://www.youtube.com/watch?v=HnY0G-zhQIc&t=45s).
## Author
[Ignasi Oliver](http://www.ignasioliver.com/).
