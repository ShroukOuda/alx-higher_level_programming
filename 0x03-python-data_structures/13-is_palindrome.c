#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * len_list - check the code for
 * @head: it's a head
 * Return: Always 0.
 */
int len_list(listint_t *head)
{
	listint_t *temp = head;
	int cnt = 0;

	while (temp != NULL)
	{
		temp = temp->next;
		cnt++;
	}
	return (cnt);
}
/**
 * reverse - check the code for
 * @head: it's a head.
 * Return: Always 0.
 */
void reverse(listint_t *head)
{
	listint_t *cur = head, *prev = NULL, *nex;

	while (cur != NULL)
	{
		nex = cur->next;
		cur->next = prev;
		prev = cur;
		cur = nex;
	}
	head = prev;
}
/**
 * is_plaindrom - check the code for
 * @head: it's a head.
 * Return: Always 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev = *head, *t1, *t2 = *head;
	int i;

	if (*head == NULL)
		return (1);
	reverse(rev);
	t1 = rev;
	for (i = 0; i < len_list(*head); i++)
	{
		if (t1->n != t2->n)
			return (0);
		t1 = t1->next;
		t2 = t2->next;
	}
	return (1);
}
