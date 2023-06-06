#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if the linked list contains a cycle or not
 * @list: the head of the list
 * Return: 0 if there's no cyle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	ptr1 = list;
	ptr2 = list;
	if (list == NULL)
		return (0);
	while (ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr2 == NULL)
			return (0);
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
