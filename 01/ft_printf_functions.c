/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_functions.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmouren <rmouren@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 19:12:28 by rmouren           #+#    #+#             */
/*   Updated: 2025/11/12 21:02:15 by rmouren          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar(char c)
{
	return (write(1, &c, 1));
}

int	ft_putstr(char *str)
{
	size_t	len;

	if (str == NULL)
		str = "(null)";
	len = 0;
	while (str[len])
		len++;
	return (write(1, str, len));
}

int	ft_putnbr(int n)
{
	long	nb;
	int		len;

	len = 0;
	nb = n;
	if (nb < 0)
	{
		len += ft_putchar('-');
		nb = -nb;
	}
	if (nb >= 10)
		len += ft_putnbr(nb / 10);
	len += ft_putchar((nb % 10) + '0');
	return (len);
}

int	ft_putunbr(unsigned int n)
{
	unsigned long	nb;
	int				len;

	len = 0;
	nb = n;
	if (nb >= 10)
		len += ft_putunbr(nb / 10);
	len += ft_putchar((nb % 10) + '0');
	return (len);
}

int	ft_putnbr_base(unsigned long n, char *base)
{
	unsigned long	baselen;
	int				len;

	baselen = 0;
	len = 0;
	while (base[baselen])
		baselen++;
	if (n >= baselen)
		len += ft_putnbr_base(n / baselen, base);
	len += ft_putchar(base[n % baselen]);
	return (len);
}
