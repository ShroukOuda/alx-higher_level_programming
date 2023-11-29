#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - check the code for
 * @head: it's a head
 * @number: it's a number
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = (*head), *newnode, *prev = NULL;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL || *head == NULL)
		return (NULL);
	newnode->n = number;
	while (temp->n < number)
	{
		prev = temp;
		temp = temp->next;
	}
	if (prev == NULL)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
	prev->next = newnode;
	newnode->next = temp;
	}
	return (newnode);
}
