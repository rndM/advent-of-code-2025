/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmouren <rmouren@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 11:53:03 by rmouren           #+#    #+#             */
/*   Updated: 2025/11/19 22:41:30 by rmouren          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <stdlib.h>
# include <unistd.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 8
# endif

# ifndef NEWLINE
#  define NEWLINE 10
# endif

typedef struct s_list
{
	char			*content;
	struct s_list	*next;
}					t_list;

size_t				ft_buffer_len(char *str, char term);
size_t				ft_get_line_len(t_list *lst);
char				*ft_substr(char *s, unsigned int start, size_t len);
int					ft_lst_add_node(t_list **lst, char *content);
void				ft_lst_free(t_list **lst);

char				*get_next_line(int fd);
int					ft_lst_create(t_list **lst, int fd, char *buffer);
void				ft_move_buffer(char *buffer, size_t start);
int					ft_process_buffer(t_list **lst, char *buffer);
char				*ft_str_create(t_list *lst);
#endif
