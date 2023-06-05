#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *prev = list;
	listint_t *next = list;

	if (!list)
		return (0);

	while (next && next->next)
	{
		prev = prev->next;
		next = next->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
