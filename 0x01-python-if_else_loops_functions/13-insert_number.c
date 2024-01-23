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
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (temp == NULL  || temp->n >= number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	while (temp != NULL && temp->n < number)
	{
		prev = temp;
		temp = temp->next;
	}
	prev->next = newnode;
	newnode->next = temp;
	return (newnode);
}
