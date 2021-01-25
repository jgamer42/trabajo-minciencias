#!/bin/bash
printf "paz: "$(grep -wr "etiqueta exploracion: paz" --include='*.txt*' . | wc -l )
printf "\nconflicto armado: "$(grep -wr "etiqueta exploracion: conflicto armado" --include='*.txt*' . | wc -l )
printf "\nmemoria: "$(grep -wr "etiqueta exploracion: memoria" --include='*.txt*' . | wc -l )
printf "\nvictimas: "$(grep -wr "etiqueta exploracion: victimas" --include='*.txt*' . | wc -l )
printf "\nproceso de paz: "$(grep -wr "etiqueta exploracion: proceso de paz" --include='*.txt*' . | wc -l )