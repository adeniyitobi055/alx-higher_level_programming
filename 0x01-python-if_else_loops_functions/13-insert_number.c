#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 * insert_node - Insert node into listint_t
 * @head: pointer to the first node
 * @number: number to insert in the new node
 * Return: address of new node, or NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL;
	listint_t *current = *head;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if (!*head || (*head)->n > number)
	{
		newnode->next = *head;
		return (*head = newnode);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = newnode;
		newnode->next = current;
	}
	return (newnode);
}
