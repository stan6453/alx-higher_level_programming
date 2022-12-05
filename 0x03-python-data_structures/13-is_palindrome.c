#include "lists.h"
#include <stddef.h>

listint_t *divide_the_middle(listint_t *midpoint);
int comparelists(listint_t *head, listint_t *list2);

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *endpointer = *head;
	listint_t *midpointer = *head;

	if (head == NULL || *head == NULL)
		return (1);

	while (endpointer && endpointer->next && endpointer->next->next)
	{
		midpointer = midpointer->next;
		endpointer = endpointer->next->next;
	}

	endpointer = divide_the_middle(midpointer);
	return (comparelists(*head, endpointer));
}

/**
 * comparelists - compare two list to see if they are equal
 * (use specifically for this palindrome question)
 * @head: head of te first list
 * @list2: head of the second list
 * Return: 1 if equal, 0 otherwise
 */
int comparelists(listint_t *head, listint_t *list2)
{
	while (head && list2)
	{
		if (head->n != list2->n)
			return (0);
		head = head->next;
		list2 = list2->next;
	}
	return (1);
}


/**
 * divide_the_middle - reverse the second half of a linked list
 * from the middle.
 * @midpoint: the point where the second half of the list
 * shuold be reversed from
 * Return: head of the reversed linked list
 */
listint_t *divide_the_middle(listint_t *midpoint)
{
	listint_t *temp;
	listint_t *temp2;

	if (midpoint->next == NULL)
		return (midpoint);

	temp = midpoint->next;
	temp2 = midpoint->next->next;
	midpoint->next = NULL;
	while (temp2 != NULL)
	{
		temp->next = midpoint;
		midpoint = temp;
		temp = temp2;
		temp2 = temp2->next;
	}
	temp->next = midpoint;
	return (temp);
}
