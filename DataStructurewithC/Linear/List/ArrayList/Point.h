#ifndef __POINT_H__
#define __POINT_H__

typedef struct _point
{
	int xpos;
	int ypos;
}Point;

// Set xpot, ypos of Piont Structure
void SetPointPos(Point *ppos, int xpos, int ypos);

// Print xpos, ypos of Point Structure
void ShowPointPos(Point *ppos);

// Compare two Point Structure
int PointComp(Point *pos1, Point *pos2)

#endif
