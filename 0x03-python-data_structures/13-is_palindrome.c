#include "lists.h"

/**
 * reversed - Reverses a listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */

listint_t *reversed(listint_t *head)
{
	listint_t *node = head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a listint_t list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 1 or 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (!(*head) || !((*head)->next))
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if (!(size & 2) && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reversed(tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reversed(mid);
	return (1);
}
