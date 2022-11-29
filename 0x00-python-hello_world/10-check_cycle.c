#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow_pointer = list;
	listint_t *fast_pointer = list;

	while (fast_poiner && fast_pointer->next && fast_poiner->next->next)
	{
		slow_pointer = slow_pointer->next;
		fast_pointer = fast_pointer->next->next;

		if(fast_pointer == slow_pointer)
			return (1);
	}

	return (0);
}
