from django import template

register = template.Library()

# version for localised langs - declension for FEW (2-4) and OTHER (5<)


@register.filter
def declension(number, forms):
    """
    Usage:
      {{ count|declension:"one,few,other" }}

    Example:
      1 game
      2 games
      5 games
    """
    try:
        number = int(number)
    except (TypeError, ValueError):
        return ""

    one, few, other = forms.split(",")

    # 11–14 are special → counts as OTHER
    if 11 <= (number % 100) <= 14:
        return other

    # Last digit rules to define numeration sorting
    last_digit = number % 10
    # if it ends with 1 (but not 11 due to rule above) it is ONE
    if last_digit == 1:
        return one
    # if it is between 2 and 4 (not 11-14 due to rule above) FEW
    elif 2 <= last_digit <= 4:
        return few
    # everything else is OTHER (5<)
    else:
        return other
