# -*- coding: utf-8 -*-



def uninstall_hook(cr, registry):
    cr.execute(
        "DELETE FROM ir_model_data WHERE module = 'l10n_generic_coa'"
    )
