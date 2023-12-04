#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	long long len = 0;
	int *arr = NULL;

	if (!head || !*head)
		return (1);
	while (curr)
	{
		curr = curr->next;
		len++;
	}
	while (!arr)
		arr = malloc(sizeof(int) * len);
	curr = *head;
	for (int i = 0; i < len; i++)
	{
		arr[i] = curr->n;
		curr = curr->next;
	}
	for (int i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
			return (0);
	}
	return (1);
}
