from django import template

global uniqe
uniqe = []
register = template.Library()

# @register.filter(name='bar')
# def foo_test(value):
# 	return str(value) + " bar"

@register.filter(name='unique_list')
def uniqe_list(value):
	if value not in uniqe:
		uniqe.append(value)
		return True
	else:
		return False

""" This feels hacky, but it works..."""
@register.filter(name='cleanup')
def cleanup_list(value):
	global uniqe
	uniqe = []
	return ""