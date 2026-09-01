REPORT zcrm_customer_report.

*---------------------------------------------------------------------*
* SAP CRM Customer Analytics Demonstration
*
* Purpose:
* Demonstrates an ABAP Objects-style customer reporting component
* for a CRM analytics workflow.
*
* This is a portfolio/learning implementation and was not developed
* against a production SAP system.
*---------------------------------------------------------------------*

TYPES: BEGIN OF ty_customer,
         customer_id       TYPE string,
         customer_name     TYPE string,
         revenue           TYPE p DECIMALS 2,
         purchase_frequency TYPE i,
         recency_days      TYPE i,
         segment            TYPE string,
       END OF ty_customer.

CLASS lcl_customer_analysis DEFINITION.

  PUBLIC SECTION.

    METHODS:
      calculate_segment
        IMPORTING
          iv_revenue TYPE p
          iv_frequency TYPE i
          iv_recency TYPE i
        RETURNING
          VALUE(rv_segment) TYPE string,

      display_customer
        IMPORTING
          is_customer TYPE ty_customer.

ENDCLASS.


CLASS lcl_customer_analysis IMPLEMENTATION.

  METHOD calculate_segment.

    IF iv_revenue >= 10000
       AND iv_frequency >= 10
       AND iv_recency <= 60.

      rv_segment = 'CHAMPION'.

    ELSEIF iv_frequency >= 5
       AND iv_recency <= 120.

      rv_segment = 'LOYAL'.

    ELSEIF iv_recency > 180.

      rv_segment = 'AT RISK'.

    ELSE.

      rv_segment = 'POTENTIAL'.

    ENDIF.

  ENDMETHOD.


  METHOD display_customer.

    WRITE: / 'Customer:', is_customer-customer_id.
    WRITE: / 'Name:', is_customer-customer_name.
    WRITE: / 'Revenue:', is_customer-revenue.
    WRITE: / 'Frequency:', is_customer-purchase_frequency.
    WRITE: / 'Recency:', is_customer-recency_days.
    WRITE: / 'Segment:', is_customer-segment.
    ULINE.

  ENDMETHOD.

ENDCLASS.
