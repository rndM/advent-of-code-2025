CC = gcc
CFLAGS = -Wall -Wextra -Werror -g
RM = rm -f

SRCS = 	ft_atoi.c ft_printf_functions.c ft_printf.c \
		get_next_line_utils.c get_next_line.c \
		password.c

OBJS = $(SRCS:.c=.o)
TARGET = day01

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(TARGET)

re: fclean all

.PHONY: all clean fclean re
