##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## Makefile
##

NAME	=	pbrain-gomoku-ai

SRC	=	main.py

all:
	cp $(SRC) $(NAME)

clean:

fclean:	clean
	$(RM) $(NAME)

re:	fclean all

.PHONY: all clean fclean re
