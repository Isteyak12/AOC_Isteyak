#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char grid[150][150];
int minx, maxy;
void printsquare(int start, int range);

int find(int x, int y);
int next(int x, int y, int dir);

int main (int argc, char * argv[])
{
    char *filename = "input";
    long result=0, steps=0;
    int part=1;
    char buf[150];
    int dir, x=0, y, check=0;
    int start,old;
    FILE * fp;
    if(argc > 1)
        part=atoi(argv[1]);
    if(argc > 2)
        filename=argv[2];
    if((fp = fopen (filename, "r"))==NULL)
    {
        printf("error opening file %s\n", filename);
        return 1;
    }
    while(fgets(buf, 150, fp) != NULL)
    {
        memcpy(grid[x++],buf,sizeof(buf));
    }
    for(x=0;x<150;x++)
    {
        for(y=0;y<150;y++)
            if(grid[x][y]=='S')
            {
                dir=start=find(x,y);
                check=1;
                break;
            }
        if(check)
            break;
    }
    minx=60000;
    maxy=0;
    while(dir)
    {
        steps++;
        old=dir;
        switch(dir)
        {
          case 1:
            dir=next(--x,y,1);
            break;
          case 2:
            dir=next(x,++y,2);
            break;
          case 3:
            dir=next(++x,y,3);
            break;
          case 4:
            dir=next(x,--y,4);
            break;
        }
    }
    dir=old;
    if(dir==start)
    {
        if(dir%2)
            grid[x][y]='|';
        else
            grid[x][y]='-';
    }
    else
    {
        if(dir==1)
        {
            if(start==2)
                grid[x][y]='F';
            else
                grid[x][y]='7';
        }
        if(dir==2)
        {
            if(start==1)
                grid[x][y]='J';
            else
                grid[x][y]='7';
        }
        else if(dir==3)
        {
            if(start==2)
                grid[x][y]='L';
            else
                grid[x][y]='J';
        }
        if(dir==4)
        {
            if(start==1)
                grid[x][y]='L';
            else
                grid[x][y]='F';
        }
    }
    grid[x][y]|=128;
    if(part==1)
        result=steps/2;
    else
    {
        for(x=0;x<150;x++)
            for(y=0;y<150;y++)
                if(grid[x][y]& 128)
                    grid[x][y]^=128;
                else
                    grid[x][y]=0;
        x=minx;
        y=maxy;
        dir=3;
        while(dir)
        {
            switch(dir)
            {
              case 1:
                if(!grid[x][y+1])
                    grid[x][y+1]=1;
                dir=next(--x,y,1);
                if(dir==4&&!grid[x][y+1])
                    grid[x][y+1]=1;
                break;
              case 2:
                if(!grid[x+1][y])
                    grid[x+1][y]=1;
                dir=next(x,++y,2);
                break;
              case 3:
                if(!grid[x][y-1])
                    grid[x][y-1]=1;
                dir=next(++x,y,3);
                break;
              case 4:
                if(!grid[x-1][y])
                    grid[x-1][y]=1;
                dir=next(x,--y,4);
                break;
            }
        }
        for(int check=1;check;)
        {
            check=0;
            for(x=1;x<149;x++)
                for(y=1;y<149;y++)
                    if(!grid[x][y] && ((grid[x+1][y]==1)||(grid[x-1][y]==1)||(grid[x][y+1]==1)||(grid[x][y-1]==1)))
                        grid[x][y]=check=1;
        }
        for(x=0;x<150;x++)
            for(y=0;y<150;y++)
                if(grid[x][y]==1)
                    result++;
    }
    printf("%ld\n",result);END
    return 0;
}
int find(int x, int y)
{
    if((x>1)&& (grid[x-1][y]=='|')||(grid[x-1][y]=='7')||(grid[x-1][y]=='F'))
        return 1;
    if( (grid[x][y+1]=='-')||(grid[x][y+1]=='7')||(grid[x][y+1]=='J'))
        return 2;
    if( (grid[x+1][y]=='|')||(grid[x+1][y]=='L')||(grid[x+1][y]=='J'))
        return 3;
}

int next(int x, int y, int dir)
{
    if(x<=minx)
    {
        if(x<minx)
            maxy=0;
        minx=x;
        if(y>maxy)
            maxy=y;
    }
    int pipe=grid[x][y];
    grid[x][y]|=128;
    if(dir==1)
    {
        if(pipe=='|')
            return 1;
        if(pipe=='F')
            return 2;
        if(pipe=='7')
            return 4;
    }
    else if(dir==2)
    {
        if(pipe=='-')
            return 2;
        if(pipe=='J')
            return 1;
        if(pipe=='7')
            return 3;
    }
    else if(dir==3)
    {
        if(pipe=='|')
            return 3;
        if(pipe=='J')
            return 4;
        if(pipe=='L')
            return 2;
    }
    else
    {
        if(pipe=='-')
            return 4;
        if(pipe=='F')
            return 3;
        if(pipe=='L')
            return 1;
    }
    return 0;
}