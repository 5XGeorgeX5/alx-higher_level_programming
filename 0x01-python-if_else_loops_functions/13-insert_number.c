#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	prev = *head;
	if (!prev || prev.n >= number)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	while (prev->next && prev->next->n < number)
		prev = prev->next;
	new->next = prev->next;
	prev->next = new;
	return (new);
}
