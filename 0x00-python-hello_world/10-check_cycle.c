#include "lists.h"

/**
 *check_cycle - checks if a singly linked list has a cycle in it
 *list - linked list
 *
 *Return: 0 if cycle, 1 if no cycle
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *mom, *dad;

	mom = list;
	dad = list;

	while (mom && dad)
	{
		if (dad->next == NULL)
			return (0);
		mom = mom->next;
		dad = dad->next;
		if (mom == dad)
			return (1);
	}

	return (0);
}
