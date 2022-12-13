from daidepp import create_daide_grammar, daide_visitor

grammar = create_daide_grammar(level=130, string_type='all')
message = 'PRP (DMZ (FRA ITA) (PIE LYO WES TYS))'
parse_tree = grammar.parse(message)
output = daide_visitor.visit(parse_tree)
print(output)

'''
Not validated annotations:
PRP ((ITA SUP ((FRA AMY RUH) MTO MUN)) (FRA SUP (ITA AMY TYR)))
missing AND

PRP (PRP (NOT (RUS SUP MUN)))
double PRP

PRP (ALY (GER AUS))
arrangement = ALY (power power ...) VSS (power power ...)

PRP (GER SUP ((AUS AMY VIE) MTO TYR))
( unit_with_location ) SUP ( unit_with_location )

YES (ALY (GER FRA) VSS (ENG))
missing PRP: YES (PRP (ALY (GER FRA) VSS (ENG)))

NOT (ALY (GER) VSS (ENG))
not considered as a message in daide++

PRP ((TUR AMY SER) MTO TRI)
not an arrangement: PRP (XDO ((TUR AMY SER) MTO TRI))

ADDITIONAL PROBLEMS:
USE SCD on non supply centers
daide++ cannot handle single country as arguments of ALY/VSS
daide++ uses GOB while some players use BOT to represent Gulf of Bothnia
'''