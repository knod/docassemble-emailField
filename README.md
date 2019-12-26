Creates one email field that will send an attachement with
customizations possible, such as email subject line and
email contents. Includes a 'Send' button on the same line
as the email field. Should remain so for various device widths.

Arrangement remains the same for

``` yaml
---
features:
  labels above fields: True
---
```

Should this be optional? Choice of css files?

## Example

See email_labels_above_fields_test.yml and
email_default_label_position_test.yml for example use.

## TODO
- Create separate css files for different label placement style choices?

## Stretch Goals
- Test multiple email fields
