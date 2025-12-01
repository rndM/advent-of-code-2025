/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmouren <rmouren@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 12:18:18 by rmouren           #+#    #+#             */
/*   Updated: 2025/11/13 08:16:07 by rmouren          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *str, ...)
{
	va_list			args;
	int				result;
	int				i;
	unsigned long	p;

	if (!str)
		return (0);
	result = 0;
	va_start(args, str);
	i = 0;
	while (str[i])
	{
		if (str[i] == '%' && str[i + 1])
		{
			if (str[i + 1] == 'c')
				result += ft_putchar(va_arg(args, int));
			else if (str[i + 1] == 's')
				result += ft_putstr(va_arg(args, char *));
			else if (str[i + 1] == 'i' || str[i + 1] == 'd')
				result += ft_putnbr(va_arg(args, int));
			else if (str[i + 1] == 'u')
				result += ft_putunbr(va_arg(args, unsigned int));
			else if (str[i + 1] == 'x')
				result += ft_putnbr_base(va_arg(args, unsigned int),
						"0123456789abcdef");
			else if (str[i + 1] == 'X')
				result += ft_putnbr_base(va_arg(args, unsigned int),
						"0123456789ABCDEF");
			else if (str[i + 1] == 'p')
			{
				p = va_arg(args, unsigned long);
				if (p)
				{
					result += ft_putstr("0x");
					result += ft_putnbr_base(p, "0123456789abcdef");
				}
				else
					result += ft_putstr("(nil)");
			}
			else if (str[i + 1] == '%')
				result += ft_putchar('%');
			i++;
		}
		else
			result += ft_putchar(str[i]);
		i++;
	}
	va_end(args);
	return (result);
}
