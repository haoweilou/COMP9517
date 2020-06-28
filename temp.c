// COMP2521 20T2 Assignment 1
// Dict.c ... implementsation of Dictionary ADT

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "Dict.h"
#include "WFreq.h"

typedef struct _DictNode *Link;

typedef struct _DictNode
{
   int height;
   WFreq data;
   Link left;
   Link right;
} DictNode;

struct _DictRep
{
   Link tree;
};

static Link rotateLeft(Link old);
static Link rotateRight(Link old);

// return how depth the node is
static int height(Link n)
{
   if (n == NULL)
   {
      return -1;
   }
   else
   {
      return n->height;
   }
}

static int max(int a, int b)
{
   return a > b ? a : b;
}

// create new empty Dictionary
Dict newDict()
{
   Dict new = malloc(sizeof(Dict));
   if (new == NULL)
   {
      fprintf(stderr, "Insufficient memory!\n");
      exit(EXIT_FAILURE);
   }
   new->tree = NULL;
   return new;
}

// create new node containing a word
Link newDictnode(char *w)
{
   Link new = malloc(sizeof *new);
   if (new == NULL)
   {
      fprintf(stderr, "Insufficient memory!\n");
      exit(EXIT_FAILURE);
   }
   new->data.word = w;
   new->data.freq = 0;
   new->height = 0;
   new->left = new->right = NULL;
   return new;
}

// insert new word into Dictionary
// return pointer to the (word,freq) pair for that word
WFreq *DictInsert(Dict d, char *w)
{
   Link new = newDictnode(w);
   WFreq *output = &new->data;
   if (d->tree == NULL)
   {
      d->tree = new;
      return output;
   }
   else
   {
      Link curr = d->tree;
      while (curr != NULL)
      {
         int cmp = strcmp(w, curr->data.word);
         if (cmp < 0)
         {
            curr = curr->left;
         }
         else if (cmp > 0)
         {
            curr = curr->right;
         }
         else
         {
            return &curr->data;
         }
      }
      curr = new;
   }
   // insertion done
   // correct the height of the current subtree
   Link head = d->tree;
   head->height = 1 + max(height(head->left), height(head->right));

   // rebalance the tree
   int LH = height(head->left);
   int RH = height(head->right);

   if ((LH - RH) > 1)
   {
      if (strcmp(w, head->left->data.word) > 0)
      {
         head->left = rotateLeft(head->left);
      }
      head = rotateRight(head);
   }

   if ((RH - LH) > 1)
   {
      if (strcmp(w, head->right->data.word) < 0)
      {
         head->right = rotateRight(head->right);
      }
      head = rotateLeft(head);
   }

   return output;
}

// find Word in Dictionary
// return pointer to (word,freq) pair, if found
// otherwise return NULL
WFreq *DictFind(Dict d, char *w)
{
   if(d->tree == NULL){
      return NULL;
   }
   Link curr = d->tree;
   while(curr != NULL){
      WFreq *output = &curr->data;
      int cmp = strcmp(w, curr->data.word);
      if(cmp == 0){
         return output;
      } else if(cmp > 0){
         curr = curr->right;
      } else {
         curr = curr->left;
      }
   }
   return NULL;
}

int BSTreeNumNodes (Link t)
{
	if (t == NULL)
		return 0;
	else
		return 1 + BSTreeNumNodes (t->left) + BSTreeNumNodes (t->right);
}


int* insertEnd (Link t, int *topN)
{
   int i = 0;
   while(topN[i] != 0){
      i++;
   }
   topN[i] = t->data.freq;
   return topN;
}

int *findAll(Link t,int *topN){
   if(t != NULL){
      insertEnd(t,topN);
      findAll(t->left,topN);
      findAll(t->right,topN);
   }
   return topN;
}


void bucketSort(int *arr, int size, int max)
{
    int i,j;
    int buckets[max];
    memset(buckets, 0, max * sizeof(int));
    for (i = 0; i < size; i++) {
        buckets[arr[i]]++; 
    }
    for (i = 0, j = 0; i < max; i++) {
        while((buckets[i]--) >0)
            arr[j++] = i;
    }
}

// find top N frequently occurring words in Dict
// input: Dictionary, array of WFreqs, size of array
// returns: #WFreqs in array, modified array
int findTopN(Dict d, WFreq *wfs, int n)
{
   int counter = BSTreeNumNodes(d->tree);
   int *topN = calloc(counter, sizeof *topN);
   int i = 0;
   Link head = d->tree;
   topN = findAll(head,topN);
   bucketSort(topN,counter,counter);
   while(i < n && topN[i] != 0){
      i++;
   }
   if(i == n){
      return n;
   }
   return i;
}

void printDict(Link t){
   if(t != NULL){
      printf("%s\n",t->data.word);
      printDict(t->left);
      printDict(t->right);
   }
}


// print a dictionary
void showDict(Dict d)
{
   Link head = d->tree;
   printDict(head);
}

// rotate tree to the left based on a node
// o = old father node (defore rotate)
// n = new father node (after rotate)
Link rotateLeft(Link old)
{
   // empty node case
   if (old == NULL)
      return NULL;
   // no right node, cannot rotate
   if (old->right == NULL)
      return old;

   Link new = old->right;
   old->right = new->left;
   new->left = old;

   // update height from llow to hight
   //left node is not NULL
   if (old->left != NULL)
   {
      //only have left node
      if (old->right == NULL)
      {
         old->height = old->left->height + 1;
      }
      else
      { // compare with left and right
         if (old->left->height > old->right->height)
         {
            old->height = old->left->height + 1;
         }
         else
         {
            old->height = old->right->height + 1;
         }
      }
      //left node is NULL
   }
   else
   {
      // both right and left are NULL
      if (old->right == NULL)
      {
         old->height = 0;
         // only have right node
      }
      else
      {
         old->height = old->right->height + 1;
      }
   }
   //updata root node hight
   // only have left node, it must have.
   if (new->right == NULL)
   {
      new->height = new->left->height + 1;
   }
   else
   { // compare with left and right
      if (new->left->height > new->right->height)
      {
         new->height = new->left->height + 1;
      }
      else
      {
         new->height = new->right->height + 1;
      }
   }
   return new;
}

// rotate tree to the right based on a node
// o = old father node (defore rotate)
// n = new father node (after rotate)
Link rotateRight(Link old)
{
   // empty node case
   if (old == NULL)
      return NULL;
   // no right node, cannot rotate
   if (old->left == NULL)
      return old;

   Link new = old->left;
   old->left = new->right;
   new->right = old;

   // update height from llow to hight
   //left node is not NULL
   if (old->left != NULL)
   {
      //only have left node
      if (old->right == NULL)
      {
         old->height = old->left->height + 1;
      }
      else
      { // compare with left and right
         if (old->left->height > old->right->height)
         {
            old->height = old->left->height + 1;
         }
         else
         {
            old->height = old->right->height + 1;
         }
      }
      //left node is NULL
   }
   else
   {
      // both right and left are NULL
      if (old->right == NULL)
      {
         old->height = 0;
         // only have right node
      }
      else
      {
         old->height = old->right->height + 1;
      }
   }
   //updata root node hight
   // only have right node, it must have.
   if (new->left == NULL)
   {
      new->height = new->right->height + 1;
   }
   else
   { // compare with left and right
      if (new->left->height > new->right->height)
      {
         new->height = new->left->height + 1;
      }
      else
      {
         new->height = new->right->height + 1;
      }
   }
   return new;
}
