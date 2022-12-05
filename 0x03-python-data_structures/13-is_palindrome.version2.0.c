#include "lists.h"
#include <stddef.h>


/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{

	listint_t *leftside = *head;
	listint_t *endpointer = *head;
	listint_t *midpointer = *head;
	int jumppoint = 0;
	int i = 0;

	if (head == NULL || *head == NULL)
		return (1);

	while (endpointer && endpointer->next && endpointer->next->next)
	{
		midpointer = midpointer->next;
		endpointer = endpointer->next->next;
		jumppoint++;
	}

	if (endpointer->next != NULL && endpointer->next->next == NULL)
		jumppoint++;

	while (jumppoint != 0)
	{
		/*note: i used endpointer for the right hand side*/
		endpointer = midpointer;
		for (i = 0; i < jumppoint; i++)
			endpointer = endpointer->next;

		if (leftside->n != endpointer->n)
			return (0);

		leftside = leftside->next;
		jumppoint--;

	}
	return (1);
}
