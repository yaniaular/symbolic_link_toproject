import os
private = "/home/yanina/vauxoo/private_addons/"
public = "/home/yanina/vauxoo/public_addons/"

links = [
    "%sodoo" % public,
    "%spartner-contact" % public,
    "%shr" % public,
    "%sodoo-panama" % public,
    "%sstock-logistics-workflow" % public,
    "%spanama-dv" % public,
    "%swebsite_multi_image" % public,
    "%sproduct-attribute" % public,
    "%sodoo-themes" % private,
    "%sodoo-snippets" % private,
    "%sSerpentCS_Contributions-v8" % private,
    "%sserver-tools" % public,
    "%spartner-contact" % private,
    "%svauxoo_crm" % public,
    "%srma" % public,
    "%syoytec_rebase" % private,
]

for link in links:
    os.system('ln -s %s .' % link)
