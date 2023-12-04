#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */
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
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);
	curr = *head;
	for (int i = 0; i < len; i++)
	{
		arr[i] = curr->n;
		curr = curr->next;
	}
	for (int i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
