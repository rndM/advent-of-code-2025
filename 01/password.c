#include "password.h"

int	pass_1(char *filename)
{
	int		fd;
	char	*line;
	int		pos;
	int		count;
	int		val;

	pos = 50;
	count = 0;
	fd = open(filename, O_RDONLY);
	if (fd < 0)
		return (-1);
	while ((line = get_next_line(fd)) != NULL)
	{
		val = ft_atoi(line + 1);
		if (line[0] == 'R')
			pos = (pos + val) % 100;
		else if (line[0] == 'L')
		{
			pos = (pos - val) % 100;
			if (pos < 0)
				pos += 100;
		}
		if (pos == 0)
			count++;
		free(line);
	}
	close(fd);
	return (count);
}

int	pass_2(char *filename)
{
	int		fd;
	char	*line;
	int		pos;
	int		count;
	int		val;
	int		i;

	pos = 50;
	count = 0;
	fd = open(filename, O_RDONLY);
	if (fd < 0)
		return (-1);
	while ((line = get_next_line(fd)) != NULL)
	{
		val = ft_atoi(line + 1);
		i = 0;
		while (i < val)
		{
			if (line[0] == 'R')
			{
				pos++;
				if (pos == 100)
					pos = 0;
			}
			else if (line[0] == 'L')
			{
				pos--;
				if (pos < 0)
					pos = 99;
			}
			if (pos == 0)
				count++;
			i++;
		}
		free(line);
	}
	close(fd);
	return (count);
}

int	main(void)
{
	int	res1;
	int	res2;

	res1 = pass_1("./input.txt");
	ft_printf("Pass 1  : %d\n", res1);
	res2 = pass_2("./input.txt");
	ft_printf("Pass 2  : %d\n", res2);
	return (0);
}
