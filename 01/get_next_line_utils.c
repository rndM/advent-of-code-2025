#include "get_next_line.h"

size_t	ft_buffer_len(char *str, char term)
{
	size_t	len;

	len = 0;
	while (str[len] && (str[len] != term))
		len++;
	return (len);
}

size_t	ft_get_line_len(t_list *lst)
{
	size_t	len;
	size_t	i;

	len = 0;
	while (lst)
	{
		i = 0;
		while (lst->content[i])
		{
			len++;
			if (lst->content[i] == NEWLINE)
				return (len);
			i++;
		}
		lst = lst->next;
	}
	return (len);
}

char	*ft_substr(char *s, unsigned int start, size_t len)
{
	size_t	i;
	char	*res;
	size_t	max_len;

	if (!s)
		return (NULL);
	if (start > ft_buffer_len(s, 0))
	{
		res = malloc(1);
		if (!res)
			return (NULL);
		res[0] = '\0';
		return (res);
	}
	max_len = ft_buffer_len(s + start, 0);
	if (len > max_len)
		len = max_len;
	res = malloc((len + 1) * sizeof(char));
	if (!res)
		return (NULL);
	i = -1;
	while (++i < len)
		res[i] = s[start + i];
	res[i] = '\0';
	return (res);
}

int	ft_lst_add_node(t_list **lst, char *content)
{
	t_list	*new;
	t_list	*current;

	new = malloc(sizeof(t_list));
	if (!new)
		return (0);
	new->content = content;
	new->next = NULL;
	if (!*lst)
	{
		*lst = new;
		return (1);
	}
	current = *lst;
	while (current->next)
		current = current->next;
	current->next = new;
	return (1);
}

void	ft_lst_free(t_list **lst)
{
	t_list	*tmp;

	if (!lst || !*lst)
		return ;
	while (*lst)
	{
		tmp = (*lst)->next;
		free((*lst)->content);
		free(*lst);
		*lst = tmp;
	}
	*lst = NULL;
}
