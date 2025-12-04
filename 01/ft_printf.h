#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int	ft_putchar(char c);
int	ft_putstr(char *str);
int	ft_putnbr(int n);
int	ft_putunbr(unsigned int n);
int	ft_putnbr_base(unsigned long n, char *base);
int	ft_printf(const char *str, ...);

#endif // LIBFTPRINF_H
