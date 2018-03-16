# Play With Me
Quick script to check what games your Steam friends have. Useful for LAN parties to see who has what.

## Usage:
```
pwm.py <steamAPIkey> [username] [friendsFilterList] [minimumWhoHaveGame]
pwm.py <steamAPIkey> [username] -listfriends
```

## Example:
Below we set the 'username' as "BossMan" (that's us, and output will be our friends), and the minimjum number of games to have in common to be 4.
```
➜  PlayWithMe python pwm.py QBAGFGRNYZLXRLOEBGUNAXFROT13 BossMan  "BossMan","Ava.Love.Lace","Harry","Bart","Breaker","Smithy","Just Some Guy" 4
+----------------------------------+---------+----------------+---------------+---------------+---------------+----------+----------+
|               Game               | Gamer_1 |    Gamer_2     |    Gamer_3    |    Gamer_4    |    Gamer_5    | Gamer_6  | Gamer_7  |
+----------------------------------+---------+----------------+---------------+---------------+---------------+----------+----------+
|           Garry's Mod            |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
| Counter-Strike: Global Offensive |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|          Rocket League           |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|          Left 4 Dead 2           |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|         Team Fortress 2          |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|     Half-Life 2: Lost Coast      |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|            Half-Life             |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|        Left 4 Dead 2 Beta        |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|     Half-Life 2: Deathmatch      |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|      Counter-Strike: Source      |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|           Half-Life 2            |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | Breaker  | BossMan  |
|  Planetary Annihilation: TITANS  |  Harry  | Ava.Love.Lace  |     Bart      | Just Some Guy |    Breaker    | BossMan  |          |
|     Half-Life 2: Episode One     |  Harry  | Ava.Love.Lace  |     Bart      | Just Some Guy |    Breaker    | BossMan  |          |
|             Portal 2             |  Harry  | Ava.Love.Lace  |     Bart      | Just Some Guy |    Breaker    | BossMan  |          |
|             PAYDAY 2             |  Harry  | Ava.Love.Lace  |    Smithy     |     Bart      | Just Some Guy | BossMan  |          |
|              Portal              |  Harry  | Ava.Love.Lace  |     Bart      | Just Some Guy |    Breaker    | BossMan  |          |
|   Half-Life Deathmatch: Source   |  Harry  | Ava.Love.Lace  |     Bart      | Just Some Guy |    Breaker    | BossMan  |          |
|      Half-Life: Blue Shift       |  Harry  | Ava.Love.Lace  | Just Some Guy |    Breaker    |    BossMan    |          |          |
|    Half-Life: Opposing Force     |  Harry  | Ava.Love.Lace  | Just Some Guy |    Breaker    |    BossMan    |          |          |
|      Team Fortress Classic       |  Harry  | Ava.Love.Lace  | Just Some Guy |    Breaker    |    BossMan    |          |          |
|     Half-Life 2: Episode Two     |  Harry  |     Bart       | Just Some Guy |    Breaker    |    BossMan    |          |          |
|    Chivalry: Medieval Warfare    |  Harry  | Ava.Love.Lace  |     Bart      | Just Some Guy |    BossMan    |          |          |
|          Counter-Strike          |  Harry  | Ava.Love.Lace  |    Smithy     |    Breaker    |    BossMan    |          |          |
+----------------------------------+---------+----------------+---------------+---------------+---------------+----------+----------+
```

## To check the names of your friends:
```
➜  PlayWithMepython pwm.py QBAGFGRNYZLXRLOEBGUNAXFROT13 BossMan -listfriends
BossMan,Ava.Love.Lace,Harry,Bart,Breaker,Smithy,Just Some Guy,AnotherFrenForMe
```



## ToDo:
 * Rather have names has column headers and mark Yes or No in columns.
 * Flask it
 * Use Neo4J or Linkurious to graph output (there are @SensePost Maltego transforms to do all this that I wrote years ago, but I don't have access to that any more.)
