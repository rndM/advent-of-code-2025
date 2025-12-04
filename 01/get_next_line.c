#include "get_next_line.h"

char	*get_next_line(int fd)
{
	t_list		*lst;
	char		*line;
	static char	buffer[BUFFER_SIZE + 1];

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	if (!ft_lst_create(&lst, fd, buffer))
		return (NULL);
	line = ft_str_create(lst);
	ft_lst_free(&lst);
	return (line);
}

int	ft_lst_create(t_list **lst, int fd, char *buffer)
{
	ssize_t	car_read;
	int		has_newline;

	*lst = NULL;
	has_newline = 0;
	if (buffer[0])
		has_newline = ft_process_buffer(lst, buffer);
	if (has_newline)
		return (1);
	while (!has_newline)
	{
		car_read = read(fd, buffer, BUFFER_SIZE);
		if (car_read < 0)
			return (ft_lst_free(lst), 0);
		if (car_read == 0)
			return (*lst != NULL);
		buffer[car_read] = '\0';
		has_newline = ft_process_buffer(lst, buffer);
	}
	return (1);
}

int	ft_process_buffer(t_list **lst, char *buffer)
{
	size_t	len;
	int		has_newline;

	len = ft_buffer_len(buffer, NEWLINE);
	has_newline = (buffer[len] == NEWLINE);
	if (has_newline)
		len++;
	if (!ft_lst_add_node(lst, ft_substr(buffer, 0, len)))
		return (ft_lst_free(lst), 0);
	if (has_newline)
		ft_move_buffer(buffer, len);
	else
		buffer[0] = '\0';
	return (has_newline);
}

char	*ft_str_create(t_list *lst)
{
	char	*line;
	size_t	total_len;
	size_t	pos;
	size_t	i;

	if (!lst)
		return (NULL);
	total_len = ft_get_line_len(lst);
	line = malloc((total_len + 1) * sizeof(char));
	if (!line)
		return (NULL);
	pos = 0;
	while (lst)
	{
		i = 0;
		while (lst->content[i])
			line[pos++] = lst->content[i++];
		lst = lst->next;
	}
	line[pos] = '\0';
	return (line);
}

void	ft_move_buffer(char *buffer, size_t start)
{
	size_t	i;

	i = 0;
	while (buffer[start + i])
	{
		buffer[i] = buffer[start + i];
		i++;
	}
	buffer[i] = '\0';
}
