import frappe

def get_context(context):
	items = frappe.get_all('Item', fields=['name', 'standard_rate', 'description', 'item_group'])
	item_group_wise_dict = {}
	for item in items:
		item_group = item.item_group
		if item_group not in item_group_wise_dict:
			item_group_wise_dict[item_group] = []

		item_group_wise_dict[item_group].append(item)

	print(item_group_wise_dict)
	context.item_group_wise_dict = item_group_wise_dict