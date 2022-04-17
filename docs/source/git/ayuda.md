# Ayuda, tengo que usar GIT

Algunos comandos de utilidad para GIT:

## Ver el estado actual de mi rama

``git status``

Da información sobre el estado de mi rama actual, como cambios sin confirmar, cambios sin subir, en qué rama estoy, etc.

## Alguien hizo cambios en el repo principal, ¿Cómo actualizo mi trabajo?

``git fetch upstream && git rebase upstream/devel``

Va a buscar cambios en el repo principal y los va a aplicar en tu rama de trabajo. Los commits que has hecho desde que
ocurrió la divergencia con devel quedarán encima de los cambios que traes desde el repo principal, como si recién hubieses
empezado a trabajar.

Es posible que encuentres conflictos en este paso, tendrás que resolverlos manualmente utilizando las herramientas de tu
IDE.

## Volver en el tiempo

Casi cualquier acción que hagas con git queda registrada y es posible usarla como referencia para volver en el tiempo. 
Si te mandaste un cagazo y necesitas volver a un punto en que sí funcionaba todo puedes hacer lo siguiente:

``git reflog``

Te devolverá un registro en orden cronológico, desde lo más nuevo a lo más viejo y cada una con una id al principio. 
Una vez encontraste la acción, puedes hacer: 

``git reset --hard <id>`` 

para volver en el tiempo a ese punto. 

## Solución nuclear

``git fetch upstream && git reset upstream/devel --hard``

Vuelve a la versión más reciente de la rama ``devel`` en el repo principal, destruye cualquier cambio que se haya realizado en la rama actual.